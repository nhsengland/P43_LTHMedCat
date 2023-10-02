def common_imports():

    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv())
    import json
    import logging
    import os
    import pickle
    import statistics
    import seaborn as sns
    from spacy import displacy
    from pathlib import Path
    from tqdm import tqdm
    from matplotlib import pyplot as plt

    import numpy as np
    import pandas as pd
    from medcat.cat import CAT
    from medcat.cdb import CDB
    from medcat.cdb_maker import CDBMaker
    from medcat.meta_cat import MetaCAT
    from medcat.vocab import Vocab
    from negspacy.negation import Negex
    from negspacy.termsets import termset
    from medcat.utils.preprocess_snomed import Snomed
    import medcat

    medcat.__version__

def common_setupConfig(cdb,MEDCAT_MODEL_PATH):
    cdb.config.general["spacy_model"] = str(
        MEDCAT_MODEL_PATH.joinpath(cdb.config.general["spacy_model"])
    )
    
    #TODO review config
    
    cdb.config.general["spacy_disabled_components"] = [
        "ner",
        # 'parser',
        "vectors",
        # 'textcat',
        "entity_linker",
        # 'sentencizer',
        "senter",
        "entity_ruler",
        "merge_noun_chunks",
        "merge_entities",
        "merge_subtokens",
    ]

    cdb.config.general["spacy_disabled_components"] = []
    
    return cdb, len(cdb.config.linking.filters.cuis)

def common_initialiseCAT(cdb, vocab, meta_cats):
    # https://github.com/CogStack/MedCAT/issues/293
    cdb.config.linking.filters.cuis = set()
    cat = CAT(cdb=cdb, vocab=vocab, meta_cats=meta_cats)
    
    # Add negspacy - https://github.com/jenojp/negspacy
    # Next line avoids accidentally removing 'unused import' in vscode
    logging.debug(f"Setting up {Negex.__name__}")
    # ts = termset("en_clinical_sensitive") # for additional history related stuff

    ts = termset("en_clinical")
    cat.pipe.spacy_nlp.add_pipe(
        "negex",
        config={
            "neg_termset": ts.get_patterns(),
            "chunk_prefix": ["no"],
        },
    )

    return cat, ts

# Create function to output entities for a single document
def annotate_single(docid: str, doctext: str):  # -> ParsedDocSchema:
    try:
        doc = cat(doctext)

        out = cat._doc_to_out(
            doc, only_cui=False, addl_info=["cui2icd10", "cui2ontologies", "cui2snomed"]
        )

        negations = {e._.id: e._.negex for e in doc._.ents}

        for ent_id, ent in out["entities"].items():
            out["entities"][ent_id]["is_negated"] = negations[ent_id]

        out = {
            "docid": docid,
            # "doctext": doctext,
            "entities": out["entities"],
        }
    except Exception as e:
        out = {
            "docid": docid,
            # "doctext": doctext,
            "entities": {},
        }
        logging.error(e)
    return out
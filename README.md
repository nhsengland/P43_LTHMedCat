# Enriching Neurology Patient Information using MedCAT
## NHS England Digitial Analytics and Research Team - PhD Internship Project

### About the Project

[![status: experimental](https://github.com/GIScience/badges/raw/master/status/experimental.svg)](https://github.com/GIScience/badges#experimental)

This repository holds code for the Enriching Neurology Patient Information using MedCAT - An investigation of how to evaulate the embedding space generated for automated clinical coding tasks.

Neurology and other clinical specialities are awash with clinical data. However, these are generally not structured and lack the characteristics to allow straightforward automatic extraction of clinically relevant concepts. Software tools do exist that can recognise clinical terms in unstructured clinical data (e.g. clinic letters) and link them to other concepts. These are called ‘named entity recognition and linking’ (NER+L) tools. But many such tools require prior ‘labelling’ by a domain expert (i.e. person with specialty knowledge) of the relevant clinical concepts. MedCAT is a NER+L tool that can work without this prior labelling as it contains an algorithm that is aligned with a customisable knowledge database (ontology). This works in two stages: 1) linking unambiguous portions of texts (entities) to unique terms in the ontology then 2) linking ambiguous entities to terms in the ontology with the most similar contexts. However, evaluation of the MedCAT models which inform the NER+L process has only been performed on labelled data, and the learned numerical representations of concepts (embeddings) has not been assessed before. Additionally, to the best of our knowledge, in the UK, only organisations related to the home institution (King’s College) have evaluated MedCAT. We are the first NHS organisation, independent of King’s College, to have evaluated MedCAT models and its usability. The contributions of this report are: 1) evaluation of three separate MedCAT models, 2) comparison of three different clustering techniques as evaluation methods in the absence of la- 32
belled data, 3) evaluation of MedCAT’s learned concept embeddings, 4) comparison of intrinsic and extrinsic evaluation metrics and 5) comparison of qualitative and quantitative evaluation approaches. We found that all three models produced NER+L results which are not consistent with clinical understanding. Clustering can enable deeper examination of learned embeddings, but further work needs to be done on finding the best input data and clustering approach. Intrinsic evaluation metrics are only meaningful in the presence of extrinsic measures and further research needs to be done to identify the most informative set of metrics. Quantitative assessment must be supplemented by qualitative inspection. The work performed here forms the first phase in evaluation of MedCAT models’ performance. Once optimal evaluation strategies have been identified, the next phase can be focused on improving MedCAT models. This will ultimately enable extraction of clinical terms that can be used for multiple downstream tasks such as automated clinical coding, research, monitoring of interventions, audits as well as service improvements.

[Link to original project propsoal](https://nhsx.github.io/nhsx-internship-projects/enriching-neurology-information-medcat/)

_**Note:** Only public or fake data are shared in this repository._

### Project Stucture

- The main code for this work is specific to LTHTR and maintained within their trusted research environment LANDER.  
- This repo contains some non-sensitive notebooks used to investigate the different models applied in this work 
- The accompanying [report](./report/Redacted_MedCAT_Neurology_Report.pdf) is also available in the `reports` folder - this is currently a redacted version whilst awaiting publication of the methods used.

### Built With

[![Python v3.8](https://img.shields.io/badge/python-v3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
- {LIST OF MAIN PACKAGE VERSIONS}

### Getting Started

#### Installation

To get a local copy up and running follow these simple steps.

To clone the repo:

`git clone https://github.com/nhsx/p43_lthmedcat`

To create a suitable environment, use Python 3.8:
- ```python -m venv _env```
- `source _env/bin/activate`
- `pip install -r requirements.txt`

The publicly-available model (available from https://github.com/CogStack/MedCAT) was pretrained unsupervised by KCH on the MIMIC-III dataset (predominantly consisting of Intensive Care health records), using the SNOMED International ontology enriched with concepts from UMLS.   For details of the two non-public models used see the [report](./report/Redacted_MedCAT_Neurology_Report.pdf)

### Usage
The code is not in a state for reuse but published here as a transparent record of the work done and to support the project report. 

#### Datasets
Restricted data set of clinical letters held on [LANDER](http://northwest-lsc-tre.surge.sh/#/)

### Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

_See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidance._

### License

Unless stated otherwise, the codebase is released under [the MIT Licence][mit].
This covers both the codebase and any sample code in the documentation.

_See [LICENSE](./LICENSE) for more information._

The documentation is [© Crown copyright][copyright] and available under the terms
of the [Open Government 3.0][ogl] licence.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

### Contact

To find out more about the [Digitial Analytics and Research Team](https://www.nhsx.nhs.uk/key-tools-and-info/nhsx-analytics-unit/) visit our [project website](https://nhsx.github.io/nhsx-internship-projects/) or get in touch at [datascience@nhs.uk](mailto:analytics-unit@nhsx.nhs.uk).

<!-- ### Acknowledgements -->


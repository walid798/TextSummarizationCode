# An Evaluation of Large Language Models on Text Summarization Tasks using Prompt Engineering Techniques
This repository contains the code, datasets, and results used in the paper "An Evaluation of Large Language Models on Text Summarization Tasks using Prompt Engineering Techniques,".
- [An Evaluation of Large Language Models on Text Summarization Tasks using Prompt Engineering Techniques]
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Repository Structure](#Repository_Structure)
  - [Datasets](#Datasets)
  - [Prompts](#Prompts)
  - [Results](#Results)
  - [Evaluation Metrics](#Evaluation_Metrics)
  - [Contributions](#Contributions)
  - [Acknowledgments](#Acknowledgments)
 
## Overview
In this study, we systematically evaluate large language models (LLMs) on four text summarization tasks across different domains, including:

News Summarization: CNN/Daily Mail and NewsRoom datasets
Dialogue Summarization: SAMSum dataset
Scientific Papers Summarization: ArXiv dataset
The study explores the performance of LLMs using multiple prompt engineering techniques, such as zero-shot and in-context learning. Evaluation metrics include ROUGE and BERTScore, among others.
 
## Repository_Structure
|-- code/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;                     source code for experiments<br />
|&nbsp;   |-- data_processing/ &nbsp;&nbsp; &nbsp; &nbsp;     Scripts for preprocessing datasets<br />
|&nbsp;   |-- evaluation/&nbsp; &nbsp; &nbsp; &nbsp;          Scripts for calculating evaluation metrics<br />
|-- prompts/&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;                 Different prompts used in each dataset<br />
|-- data/&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;                    Utilized dataset<br />
|-- results/&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;                 Contains generated summaries and results files<br />
|-- figures/&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;                 Plots and figures for analysis<br />
|-- README.md&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;                Project README file<br />
 

## Datasets
 
The datasets used in this study are:

CNN/Daily Mail and NewsRoom (for news summarization)
SAMSum (for dialogue summarization)
ArXiv (for scientific paper summarization)
### Accessing the Datasets
Due to size constraints, the datasets are not included in this repository. Download each dataset from its respective source as follows:<br/>
|-- cnn_dailymail&nbsp;&nbsp; &nbsp;            >> https://github.com/abisee/cnn-dailymail <br />
|-- newsroom&nbsp; &nbsp;&nbsp; &nbsp;          >> https://lil.nlp.cornell.edu/newsroom/<br/>
|-- samsum&nbsp; &nbsp;&nbsp; &nbsp;            >> https://arxiv.org/src/1911.12237v2/anc<br/>
|-- arxiv&nbsp; &nbsp;&nbsp; &nbsp;             >> https://github.com/armancohan/long-summarization<br/>

## Prompts
Due to the difference nature of the used datasets we used different prompts for each dataset in ZSL and FSL.
## Results
The results of each experiment are stored in the results/ directory. This includes:

Generated summaries for each dataset
Evaluation metrics (e.g., ROUGE, BERTScore)
We also include a sample table from the paper displaying reference summaries and generated summaries for qualitative comparison.

## Evaluation_Metrics
The following evaluation metrics were used to assess the model performance:

ROUGE: Measures overlap between generated and reference summaries.
BERTScore: Computes similarity using contextual embeddings.
For details on how each metric is calculated, see code/evaluation/.

## Contributions
Walid Mohamed Ali: Corresponding Researcher, developed code, conducted experiments, and wrote the paper.
Taysir Hassan A Soliman: Supervision, review, and editing.
Amr Mohamed AbdelAziz: Supervision, review, and editing.

## Acknowledgments

We acknowledge the datasets’ authors and sources, as well as the contributors of open-source tools that supported this research.







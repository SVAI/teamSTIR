# teamSTIR

# Automated segmentation of whole body MRI using deep learning segmentation algorithms

## Please cite our work -- here is the ICMJE Standard Citation:

### ...and a link to the DOI: *You can make a free DOI with zenodo, synapse, figshare, or other resources <link>*

## Abstract 
Neurofibromatosis is a rare, debilitating genetic predisposition to cancer that results in tumors of the nervous system all over the body. Noninvasive monitoring of disease progress and response to therapy can be achieved through whole body MRI using a STIR acquisition sequence. Segmentation of tumor tissue is required to track tumor burden. Manual segmentation of lesions is painstaking and time consuming, requires trained specialists and often has high intra-rater variability. A fast and accurate automated method would facilitate volumetric analysis, time series tracking and reduce burden on radiologists. Using a synapse dataset of 48 manually segmented NF patient MRIs, we utilize a PyTorch implementation of Unet for pixel-wise segmentation of whole body MRI images. We query whether a T1 sequence can improve accuracy over segmentation using the STIR sequence alone.

## Introduction *: What's the problem? Why should we solve it?*

## Methods *: How did we go about solving it?*

## Results *: What did we observe? Figures are great!*

## Conclusion/Discussion: 

### Please make sure you address ALL of the following:

#### *1. What additional data would you like to have*

#### *2. What are the next rational steps?* 

#### *3. What additional tools or pipelines will be needed for those steps?*

#### *4. What skills would additional collaborators ideally have?*

## Reproduction: *How to reproduce the findings!*

### Docker

*The Docker image contains <R/jupyter> notebooks of all analyses and the dependencies to run them. *Be sure to note if you need any special credentials to access data for these analyses, **don't package restricted data** in your containers!*

Instructions for running the following notebooks: *be sure to adjust these instructions as necessary! check out https://github.com/Sage-Bionetworks/nf-hackathon-2019 for example containers and instructions*

1. `docker pull <your dockerhub repo>/<this container>` command to pull the image from the DockerHub
2. `docker run <your dockerhub repo>/<this container>` Run the docker image from the master shell script

### Important Resources *: primary data, github repository, Synapse project, dockerfile link etc.*



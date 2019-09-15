# teamSTIR

# Automated segmentation of whole body MRI using deep learning segmentation algorithms

## Please cite our work -- here is the ICMJE Standard Citation:

### ...and a link to the DOI: *You can make a free DOI with zenodo, synapse, figshare, or other resources <link>*

## Abstract 
We have evaluated techniques for an automated assay of tumor volume in neurofibromatosis patients through a machine learning algorithm trained on a set of clinical, whole body MRI images. A fast and accurate automated method would facilitate volumetric analysis, time series tracking and reduce burden on radiologists. Using a synapse dataset of 48 manually segmented NF patient MRIs, we utilize a PyTorch implementation of Unet for pixel-wise segmentation of whole body MRI images. We query whether a T1 sequence can improve accuracy over segmentation using the STIR sequence alone.

## Introduction
Neurofibromatosis is a rare, debilitating genetic predisposition to benign tumors of the nervous system throughout the body which may progress and metasticize into malignant lesions. While no therapy presently exists, the decision for surgical resection of the tumors requires accuratly measuring tumor involvement and monitoring of disease progress. In addition, a clinician evaluating potential therapies requires accurate assessment to determine efficacy of treatment. Magnetic Resonance Imaging (MRI) with its sensitivity to soft-tissue tumors is the current gold-standard for non-invasive evaluation. The preferred protocol for tumors of this nature is a short tau inversion recovery (STIR) acquisition sequence with the high contrast given to soft tissue tumors.

After tumor involvement is determined, a technician must manually determine the tumor area on a set of images and compile the results into a volumetric estimate. However, this process is painstaking, time consuming, and expensive. There are often discrepancies in ground truth segmentations among different raters, institutions and MRI sequences. An automated segmentation method would reduce costs and time required for analysis as well as facilitate an analysis pipeline.

## Methods
Our goal was to do binary classification of each pixel as 'tumor' or 'not tumor'. We used a training dataset of 36 patients' MRIs from a single institution with corresponding segmentation masks as ground truth. Preprocessing of DICOMS included masking out label annotations on images and normalizing data from (-1 to 1) (ignoring outliers).

We augmented the data by creating 64 x 64 pixel patches using a 1 pixel stride. There was a drastic class imbalance between tumor and not tumor - tumor pixels comprised only ~0.5% of all the pixels. To address this imbalances, we defined a patch with at least 1 tumor pixel as a 'tumor' class patch and then randomly selected an equal number of non-tumor patches. Because of overlapping augmentation, we had 250 million patches of each class. We randomly subsetted this data for ease of use for 50,000 patches of each type.

Using PyTorch, we trained a Unet architecture from @milesial with a batch size of 32 images for 100,000 batches per epoch for 10 epochs. We used an ADAM optimizer to set the learning rate. We used a logistic loss function which was averaged over each pixel.

## Results *: What did we observe? Figures are great!*
Figure 1.

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



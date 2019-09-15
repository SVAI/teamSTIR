"""
docker tutorial: reproducible code

install/run containers: https://github.com/Sage-Bionetworks/nf-hackathon-2019

how to make a container:

in github folder: any files and notebooks plus a dockerfile

dockerfile tells docker where to find all dependencies and packages to create a VM

1) load base docker image with python or R
2) install packages / dependencies
3) make a directory inside your docker image
4) copy all the notebooks / code into docker container

to run: in this directory that contains the dockerfile, run 'docker build .'

DockerHub is a good repository for dockers
"""

##Start from base jupyter notebook docker container
FROM jupyter/base-notebook:6c3390a9292e
     ##this is a specific build so updates don't screw you up

##jupyter does not have root user as default, so switch to root to use apt-get and pip3
USER root 

RUN apt-get update
RUN apt-get -y install gcc

#upgrade pip and get synapseclient
RUN pip install --upgrade pip
RUN pip install synapseclient[pandas] pickle 
RUN mkdir /home/akp/work/output

COPY 0-0-download data from synapse.ipynb /home/akp/work/0-0-download data from synapse.ipynb
COPY nf_dataset.py /home/akp/work/nf_dataset.py
COPY patch_dataset.py /home/akp/work/patch_dataset.py
COPY train_unet.py /home/akp/work/train_unet.py


#building dockerfile:

#save as 'dockerfile' no extension
#terminal:
#move to folder with files and dockerfile
# docker build -t dockerhubloc/nameofdockerimage:version . #. signifies local file
 

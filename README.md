# Example flask wrapper for textual classifications.

An example repository of how to create an wrapper using flask and docker to deploy the predictions of a textual classifier created in sklearn. (As described in https://github.com/maartensukel/example-textual-classification-citizen-reports).

An online version of the demo can be found at http://ec2-54-171-141-211.eu-west-1.compute.amazonaws.com/.

## 1) Download the dataset
Create pickles as described in https://github.com/maartensukel/example-textual-classification-citizen-reports and place them in the folder 'flask_demo'.

## 2) Install docker
Make sure docker is installed, or install docker https://docs.docker.com/install/.

##3) 
To build the containers run: 'docker-compose build'

## 4)
To run the application execute: 'docker-compose up'

## 5)
To see the demo open /web_pages/index.html or post {'text':'example text'} to http://localhost:8140/signals_mltool/predict
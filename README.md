# Configuration-Space-Reduction
An explainable framework using deep learning and XAI for configuration space reduction and human-in-the-loop interaction

Simulation of the Explainable framework

## Project name:

explainable_ai

## Project description:

The implementation of adaptation option double selection process. It
contains a learning module and an explainable module.

## Project environment:

-   Python 3

-   Tensorflow 2.2.0

-   Pip

-   Numpy

-   Pandas

-   Scikit-learn

-   Matplotlib

-   Flask

-   requests

-   Sublime text and Terminal

## Instructions on how to build the Explainable framework

-   Build the learning module

    -   Find the best hyperparameters for the CNN learning models

    -   Create and train the CNN learning models

    -   Create a classification mechanism for the adaptation options

-   Build the explainable module

    -   Create a gradient calculator for input features

    -   Create an integrated gradients calculator

    -   Build the feature attribution mechanism

## The Docker file:

It is created on the root folder of the project. The docker
file
helps to create a container image for the final simulation of the
interaction between the XAI framework and the self-adaptive IoT system.


![image](https://user-images.githubusercontent.com/57788241/131268319-b70e9811-ed16-4ad9-be3c-3f54a12fc97e.png)


Finding the best hyperparameters for the learning model

Navigate to the root folder 'explainable_ai' and type the following
command

python LearningModule/ HyperparameterTuning.py

Please choose the version of the system in the file as showed below


![image](https://user-images.githubusercontent.com/57788241/131268398-e6190aff-c1eb-434d-85f3-4cd1f0b84e55.png)


Building and training the learning models

Navigate to the root folder and type the following command

python LearningModule/ ModelTraining.py

Please configure the version of the system and the sample of the dataset
as well as the test size


![image](https://user-images.githubusercontent.com/57788241/131268457-26660044-24ac-4836-a64e-0e9f35b79ea8.png)



classification mechanism for the adaptation options: classification.py




<img src="https://user-images.githubusercontent.com/57788241/131268466-ea308c75-e3f1-4317-af88-3adc4e914e74.png" width="200">

Create a gradient calculator for the input features:
calculate_outputs_and gradients.py


![image](https://user-images.githubusercontent.com/57788241/131268475-2e298b30-18c8-40fb-b519-d1f57d3fbf08.png)



Create an integrated gradients calculator: integrated_gradients.py



![image](https://user-images.githubusercontent.com/57788241/131268482-cd69273e-cdd2-47c5-9759-699d86432297.png)



Build the feature attribution selection mechanism: attributions.py



![image](https://user-images.githubusercontent.com/57788241/131268485-db7cde1a-7475-423e-b77d-be94d45f6005.png)



client that sends and receives messages from the simulation service:
app.py



![image](https://user-images.githubusercontent.com/57788241/131268498-609bcf5f-ae83-4a18-b41c-b30229e55de9.png)



Simulation of self-adaptive IoT system

## Project name:

Simulation

## Project description:

This program simulates the self-adaptive IoT system. It contains two
modules: Activforms module and Simulator module.

The Activforms module contains the code that simulates the MAPE-K
feedback loop, while the Simulator module contains the code that
simulates the DeltaIoT system.

The simulation code can be downloaded from
[here](https://drops.dagstuhl.de/opus/volltexte/2017/7142/artifact/DARTS-3-1-4-artifact-6798858c9a89c871093d9a095a029b64.tgz)

Related research paper: [Applying Machine Learning to Reduce the
Adaptation Space in Self-Adaptive Systems: an exploratory
work](http://lnu.diva-portal.org/smash/record.jsf?pid=diva2%3A1240014&dswid=-7780)

## Project environment:

-   Java

-   Maven

-   Eclipse IDE

## Instructions on how to edit and use the Simulation code

The Simulation package is a multi-module maven project with a packaging
of type pom. The Activforms and Simulator modules of packaging type jar,
is a child of Simulation.

-   To use the code in eclipse, just go to File Open projects from File
    System

-   Next to 'Import source', choose 'Directory' or 'Archive'

-   Navigate to the directory where the folder or compressed file of the
    Simulation code is and click 'Next' and 'Finish'

## The Docker file:

It is created on the root folder of the project. The docker
file
helps to create a container image for the final simulation of the
interaction between the XAI framework and the self-adaptive IoT system.



![image](https://user-images.githubusercontent.com/57788241/131268511-f377d690-1a3a-4a63-a16f-3474fb10daf6.png)



## The Config file:

The Simulation project contains a configuration file named
***SMCConfig.properties***


Basically, the file is used by the Activforms module in order to get the
information about which version of system's simulation to run.



![image](https://user-images.githubusercontent.com/57788241/131268523-9f5ee825-59e3-4217-8a4e-0e4ec9f5b035.png)



To change the quality models depending on
the version of the system, just add or remove the '\#' before the
property name



![image](https://user-images.githubusercontent.com/57788241/131268536-585781c2-1c9d-4b64-adb4-85c5df6e2fdb.png)




Below are the general settings that are common for all the versions of
the DeltaIoT system



![image](https://user-images.githubusercontent.com/57788241/131268545-b9fc662c-aa20-41d8-b67a-4a47c69a7a7d.png)




Below are the descriptions of the two child modules of the Simulation

## Module name:

Activforms

## Module description:

This module is a simulation of the MAPE-K feedback loop. It contains all
the code of the different components of the MAPE-K loop. When the 'Main'
is launched, it loads the version of the DeltaIoT to simulate from the
configuration file and initializes the monitored system which is
'Simulator' as shown below: Main.java



![image](https://user-images.githubusercontent.com/57788241/131268554-aea58c85-7749-4f50-baba-007183696c9b.png)



Then the feedback loop starts based on the initialized monitoring
values. The feedback loop checks whether adaptation is required:
FeedbackLoop.java



![image](https://user-images.githubusercontent.com/57788241/131268558-4900d1f3-61e2-4996-a21b-ff5bf94ece1f.png)



Below is the code that makes the simulation receive the selected options
from the XAI program, and sends the verified options for training:
SMCConnector.java



![image](https://user-images.githubusercontent.com/57788241/131268563-9e9faddc-8431-4aad-a7a6-5df9e3751c83.png)



## Module name:

Simulator

## Module description:

This is a simulation of the DeltaIoT platform. It has the code to create
DeltaIoTv1 and DeltaIoTv2 as shown below:
deltaiot/client/SimulationClient.java



![image](https://user-images.githubusercontent.com/57788241/131268578-41c94f5d-4a8a-4410-9e0a-a21c738bda4f.png)



The main method of the 'simulator'
package, simulates a continual operation of the system by applying
adaptation based on the network QoS: simulator/Main.java



![image](https://user-images.githubusercontent.com/57788241/131268586-04c86d10-cd84-4f80-98a5-20f40d598766.png)




# Overview of Configuration Space Reduction project

## Project name:

Adaptation Space Reduction

## Content:

Simulation

Explainable AI (XAI)

## Project description:

This project simulates the overall operations of the self-adaptive IoT
system with the explainable framework. The project uses docker to
creates a virtual environment in which the application's services are
interacting.

There is a YAML file at the root folder that is used to configure the application
services. The Simulation container image behaves like a web server. It
requests or sends messages in json format to the XAI container image
which behaves like a client of a web server.

## Project environment:

Docker 3.3

## How to run the project

-   Download and install docker

-   With command prompt, navigate to the project root folder

-   Type the following command to build the docker containers for the
    simulation

docker compose build

-   then type the following command to run the simulation

docker compose up

## Example:

Building the containers



![image](https://user-images.githubusercontent.com/57788241/131268609-7907adf0-0db0-4992-9f16-cde0428787e3.png)



launching the simulation



![image](https://user-images.githubusercontent.com/57788241/131268613-85de3720-3033-4826-8a85-8bce29c842e2.png)



Feedback loop starting



![image](https://user-images.githubusercontent.com/57788241/131268617-e74603da-fc3d-4b7c-8ba2-873a507279d4.png)



System running



![image](https://user-images.githubusercontent.com/57788241/131268621-ae0a2ee4-7f5a-495c-b979-68972ff4a989.png)




The first value '1' is the cycle counter meaning this is cycle 1

The second value '1629616829181' is the beginning timestamp of the cycle

The third value '216' is the number of analyzed adaptation options

The fourth value '70460' is the analysis time

The sixth value '6.419559999999' is the packet loss

The seventh value '0.0' is the latency

The eight value '12.7398' is the energy consumption

The ninth value '1629616907634' is the ending timestamp of the cycle


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

It is created on the root folder of the project. The [docker
file](file:///Users/boner/Desktop/untitled%20folder/temp/temp2/Adaptation%20Space%20Reduction/explainable_ai/Dockerfile)
helps to create a container image for the final simulation of the
interaction between the XAI framework and the self-adaptive IoT system.

![](media/image1.png){width="4.763888888888889in"
height="1.9861111111111112in"}

Finding the best hyperparameters for the learning model

Navigate to the root folder 'explainable_ai' and type the following
command

python LearningModule/ HyperparameterTuning.py

Please choose the version of the system in the file as showed below

![](media/image2.png){width="6.5in" height="1.1652777777777779in"}

Building and training the learning models

Navigate to the root folder and type the following command

python LearningModule/ ModelTraining.py

Please configure the version of the system and the sample of the dataset
as well as the test size

![](media/image3.png){width="6.5in" height="1.4388888888888889in"}

classification mechanism for the adaptation options: classification.py

![](media/image4.png){width="6.5in" height="3.515277777777778in"}

Create a gradient calculator for the input features:
calculate_outputs_and gradients.py

![](media/image5.png){width="6.5in" height="2.5701388888888888in"}

Create an integrated gradients calculator: integrated_gradients.py

![](media/image6.png){width="6.5in" height="1.9083333333333334in"}

Build the feature attribution selection mechanism: attributions.py

![](media/image7.png){width="6.5in" height="2.7993055555555557in"}

client that sends and receives messages from the simulation service:
app.py

![](media/image8.png){width="6.5in" height="2.8020833333333335in"}

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

It is created on the root folder of the project. The [docker
file](file:///Users/boner/Desktop/untitled%20folder/temp/temp2/Adaptation%20Space%20Reduction/simulation/Dockerfile)
helps to create a container image for the final simulation of the
interaction between the XAI framework and the self-adaptive IoT system.

![](media/image9.png){width="6.5in" height="1.6965277777777779in"}

## The Config file:

The Simulation project contains a configuration file named
***[SMCConfig.properties](file:///Users/boner/Desktop/untitled%20folder/temp/temp2/Adaptation%20Space%20Reduction/simulation/SMCConfig.properties)***
.

Basically, the file is used by the Activforms module in order to get the
information about which version of system's simulation to run.

![](media/image10.png){width="5.2125in" height="1.948611111111111in"}

![](media/image11.png){width="5.886111111111111in"
height="4.2868055555555555in"}To change the quality models depending on
the version of the system, just add or remove the '\#' before the
property name

Below are the general settings that are common for all the versions of
the DeltaIoT system

![](media/image12.png){width="4.333333333333333in" height="5.375in"}

Below are the descriptions of the two child modules of the Simulation

## Module name:

Activforms

## Module description:

This module is a simulation of the MAPE-K feedback loop. It contains all
the code of the different components of the MAPE-K loop. When the 'Main'
is launched, it loads the version of the DeltaIoT to simulate from the
configuration file and initializes the monitored system which is
'Simulator' as shown below: Main.java

![](media/image13.png){width="6.5in" height="2.0083333333333333in"}

Then the feedback loop starts based on the initialized monitoring
values. The feedback loop checks whether adaptation is required:
FeedbackLoop.java

![](media/image14.png){width="5.027777777777778in"
height="1.3194444444444444in"}

Below is the code that makes the simulation receive the selected options
from the XAI program, and sends the verified options for training:
SMCConnector.java

![](media/image15.png){width="6.5in" height="2.1083333333333334in"}

## Module name:

Simulator

## Module description:

This is a simulation of the DeltaIoT platform. It has the code to create
DeltaIoTv1 and DeltaIoTv2 as shown below:
deltaiot/client/SimulationClient.java

![](media/image16.png){width="6.5in" height="1.395138888888889in"}

![](media/image17.png){width="5.823611111111111in"
height="2.0076388888888888in"}The main method of the 'simulator'
package, simulates a continual operation of the system by applying
adaptation based on the network QoS: simulator/Main.java

Overview of Configuration Space Reduction project

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

There is a
[YAML](file:///Users/boner/Desktop/untitled%20folder/temp/temp2/Adaptation%20Space%20Reduction/docker-compose.yml)
file at the root folder that is used to configure the application
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

![](media/image18.png){width="7.073611111111111in"
height="3.5805555555555557in"}

launching the simulation

![](media/image19.png){width="7.354861111111111in"
height="3.323611111111111in"}

Feedback loop starting

![](media/image20.png){width="6.5in" height="3.8583333333333334in"}

System running

![](media/image25.png){width="6.5in" height="3.7305555555555556in"}

The first value '1' is the cycle counter meaning this is cycle 1

The second value '1629616829181' is the beginning timestamp of the cycle

The third value '216' is the number of analyzed adaptation options

The fourth value '70460' is the analysis time

The sixth value '6.419559999999' is the packet loss

The seventh value '0.0' is the latency

The eight value '12.7398' is the energy consumption

The ninth value '1629616907634' is the ending timestamp of the cycle


# Lab-Project

The major task of this project is to gather historical energy data collected from data loggers that are situated around the University of the Witwatersrand (WITS), manipulate the data to create an interactive web portal to visualize said data. The web portal allows for analysis of the data. The data is stored in a time series database (TSD), in this case OpenTSDB, and a web portal is created using the Flask micro web framework to create and display the visuals. The visuals allow for analysis of energy usage on the campus, as well as other important characteristics of the dataset and data loggers.

# Overview of System

The system is designed to reproduce the energy data from the dataloggers, however, this system can be used to visualize data from any source.
The following visualizations are catered for:

* Dygraphs - Line Graphs
* Choropleth Map
* Data Outage Heat Map
* Heat Map
* Sankey Diagram
* Treemap

Examples of these are illustrated below.

## Dygraphs - Line Graphs


![Sunniside Residence](https://github.com/tintin305/Lab-Project/blob/master/Administration_Documents/Poster_Template/Feathergraphics/DygraphsSunisideResidence.png?raw=true "Sunniside Residence")

## Choropleth Map

![Choropleth Map](https://github.com/tintin305/Lab-Project/blob/master\Administration_Documents\Poster_Template\FeatherGraphics\ChoroplethMap.png?raw=true "Choropleth Map of West Campus")

## Data Outage Heat Map

![Data Outage Heat Map](https://github.com/tintin305/Lab-Project/blob/master\Administration_Documents\Poster_Template\FeatherGraphics\DataOutageDavidWebster.png?raw=true "Data Outage Heat Map")

## Heat Map

![Heat Map](https://github.com/tintin305/Lab-Project/blob/master\Administration_Documents\Poster_Template\FeatherGraphics\HeatMapCollegeHouse.png?raw=true "Heat Map")

## Sankey Diagram

![Sankey Diagram](https://github.com/tintin305/Lab-Project/blob/master\Administration_Documents\Poster_Template\FeatherGraphics\SankeyMatrix.png?raw=true "Sankey Diagram")

## Treemap

![Sunniside Residence](https://github.com/tintin305/Lab-Project/blob/master\Administration_Documents\Poster_Template\FeatherGraphics\Treemap.png?raw=true "Tree Map")

## Backend

The system makes use of the flask web server. The system is designed to make use of OpenTSDB for the data source.

## Running the Application

### Network Connection

In order to run the application, you need to be connected to the University of the Witwatersrand (WITS) network. This provides access to the opentsdb server that houses the data.
If you are not on the campus (i.e. connected to any of the wits networks), then you can make use of the WITS VPN [application](https://www.wits.ac.za/access/). 
You will need to sign in with your credentials that you would usually sign into when using the WITS proxy.
Alternatively, if you have your own data warehouse, alter the connection to the server in this codebase.

### Required Applications

In order to run the application you will also need a number of applications to be installed on your system:

* Python (v3.7)
* Putty (this is used to run the SSH connection to the server)

Once these are installed, you are required to have the following Python packages installed:

  * Pandas
  * Flask
  * Requests
  * JSON
  * Numpy
  * Seaborn
  * Matplotlib
  * Datetime
  * sshtunnel
  * subprocess
  * platform
  * socket

The socket package can be installed with the use of:

    python -m pip install requests[socks]

### Launching the Application

To run the application, navigate to /Database/Flask and from there run the "Launch.sh" shell script:

    ./Launch.sh

This will launch the SSH connection to the server and host the web site locally.
Access to the website is found on "localhost:3000"

## Markdown files and Documentation

    This project makes use of Markdown to create documentation. In order to generate the html documentation, [pandoc](https://pandoc.org) is required to be installed. In each of the documentation folders, there is a batch file that allows the generation of the html files from the *.md files.
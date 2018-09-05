# Lab-Project

## Running the Application

### Network Connection

In order to run the application, you need to be connected to the University of the Witwatersrand (WITS) network.
If you are not on the campus (i.e. connected to any of the wits networks), then you can make use of the WITS VPN [application](https://www.wits.ac.za/access/). 
You will need to sign in with your credentials that you would usually sign into when using the WITS proxy.

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
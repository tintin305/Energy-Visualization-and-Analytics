---
title: Poster
---

# Poster Notes

## Introduction

The project involves the use of multiple energy data loggers placed on the university campuses which record periodical energy use of buildings, transformers, residences, stadiums & sports fields, main incomers, generators, and other general loads. These data loggers provide historical usage for the university going back as far as 2013. The data is transferred from the ecWIN system, manipulated and then imported into a time series database (TSD). A web framework is developed with the use of Flask.
The web framework allows for the visualization of the data in a number of methods.
The visualizations include:

    * Time Series Line Charts (Dygraphs)
    * Heat Maps
        * Colour Heat Map
        * Data Outage
        * Three Dimensional Heat Map
    * Sankey Diagram
    * Tree Map
    * Map

These visualizations allow for the unique interpretation of the day in multiple ways. Different visualization methods highlight different characteristics of the energy usage.

## OpenTSDB

Time series database (TSDB) is inherently useful for this type of data as it makes use of key-value pairs. These key value pairs are made up of a timestamp and a corresponding, associated value, which in this case represents energy usage for a specific time period.
The database has a convenient set of utilities that allow for importing, managing, and querying any data required. OpenTSDB is made up of a Time Series Daemon (TSD) which allow for users to interact with the underlying data. The underlying data is stored using Apache HBase or Google Bigtable.
The current installation uses Apache HBase as the underlying Hadoop database; it provides a distributed and  highly scalable data storage solution.
Interaction with the data is done using number of supported methods: a telnet-style protocol, an HTTP API, or the built in user interface.

## Flask Server

This web framework is used in order to provide processing for the visuals, as well as provide a front end for the system.
The flask framework, in conjunction with the Python requests package allows for easily querying the OpenTSDB database.
Flask makes use of the Jinja templating engine (within Python), this allows for the use of static web pages to be reused while creating dynamic content.
This web server allows for short feedback cycles (testing) on the developers local machine. The web server can easily be ported to a more permanent solution on a dedicated server.

## Writing Data to Database

Writing data to the database can be done using three methods: Telnet, an HTTP API, or internel OpenTSDB importing tools.
Each time series point is imported into the database and each component of the data specification is important for querying ability further down the line. Metrics have been used as the major identifiers of the different data loggers and their readings, tags are important to identify cases where data outages occurred. The use of tags is highly relevant when extra information can be affixed to specific data points in time. This can be in cases where a unique data outage occurred or an abnormal reading was taken and an explanation is required.

## Dataloggers and IST

IST's product, ecWIN, is employed on the universities campuses such that there is a central point where the energy readings can be accumulated and managed. This system allows for the monitoring of energy usage from the data loggers installed throughout the campuses.
This web portal has been used to draw the historical data from the data loggers, some of which go back to 2013.

## Dygraphs

Highly useful for examining, at a simple level, the normal magnitudes of energy usage/flow for the load/source in question. This form of visual highlights the trend of energy over time periods. It can highlight patterns, and anomalies within the data. This is highly relevant in cases where the validity of the data is in question.

## Heat Maps

Colour representation of relative magnitudes of energy is created with the use of block corresponding to hours in the day. This is particularly useful for illustrating trends over regions of time. 

# Sankey Diagram

The width of the pipes in these diagrams represent the magnitude of the energy usage over a specified time period. The ability to visually compare the widths with reference to eachother provides reference points of magnitudes. The widths of each of the bands are proportional to the energy incoming, and consumption through the system.
This can effectively highlight unnaccounted for energy within the system, which can be cases where portions of the system are unmetered.

## Tree Map


## Map


## Three Dimensional Heat Map


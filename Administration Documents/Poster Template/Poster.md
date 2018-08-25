---
title: Poster
---

# Poster Notes

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

## 
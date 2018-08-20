---
title: Database
---

# Different Types of Databases

## Wiki

### Common logical data models

* Navigational databases
  * Hierarchical database model
  * Network model
  * Graph database
* Relational model
* Entity-relationship model
  * Enhanced entity-relationship model
* Object model
* Document model
* Entity-attribute-value model
* Star schema

### An object-relational database combines the two related structures

Physical data models include:

* Inverted index
* Flat file

Other models include:

* Associative model
* Multidimensional model
* Array model
* Multivalue model

Specialized models are optimize for particular types of data:

* XML database
* Semantic model
* Content store
* Event store
* Time series model

### OML

This is a technique of accessing a relational database from an object-oriented language ([site](https://www.yegor256.com/2014/12/01/orm-offensive-anti-pattern.html). Yegor speaks about how the standard use of ORM is, instead of encapsulating database interaction inside an object, it extracts it away, literally tearing a solid and cohesive living organism apart.

## NoSQL

Commonly very fast, do not require fixed table schemas, avoid join operations by storing denormalized data, and are designed to scale horizontally.

Examples of NoSQL:

* MongoDB
* Couchbase
* Riak
* Memcached
* Redis
* CouchDB
* Hazelcast
* Apache Cassandra
* HBase

## RBDMS

Relational database management system

Examples:

* Ingres
* MySQL
* Oracle
* PostgreSQL
* SAP
* SQL Azure
* SQLBase

# Choice of database

This should be determined chosen from a number of factors:

* Requirements of tools
* Size
* Speed
* Start with the end in mind
* Choose the right data model (choose the data model which things about the end goal)
* Disks are fast, memory is faster
* Consider both reads and writes

## [Short guide](https://reflect.io/blog/analytics-101-choosing-the-right-database/)

The following section illustrates the different databases and what they are useful for and where they fall short:

### General purpose databases

* Postgres
* MySQL
* MongoDB
* MSSQL

Mostly relational, work well serving small to large size data sets in a high throughput environment. It can be problematic for large data sets, or for workloads distributed across multiple machines.

### Distributed table-oriented databases

* Cassandra
* DynamoDB
* HBase
* BigTable

Similar to the general purpose databases, however, they reduce their feature set in order to scale across a cluster.

### Key-value databases

* Redis (highly consistent, can't handle very large data sets)
* Riak (can scale out to whatever your ops team can handle, but sometimes it'll take a bit before you can read what you just wrote to it)
* S3
* SimpleDB

Suited for when you know the exact data you need. They should be considered as being key-value only.
The main considerations are level of scale and [read consistency](https://en.wikipedia.org/wiki/Consistency_(database_systems))

### Massively parallel processing databases

* Impala
* SparkSQL
* BigQuery
* Redshift
* Hive
* Presto

Usually used when you need the ability to "slice-and-dice" very large data sets. Concurrent reads are limited.

### Time series database

The reasons for choosing a [time series database](https://www.influxdata.com/time-series-database/)

[Comparisons](https://blog.outlyer.com/top10-open-source-time-series-databases)

[Other Site](https://thenewstack.io/use-time-series-database/)

Top Rankings (according to InfluxDB (based on social media mentions, job postings, tech discussion, etc.)):

1. InfluxDB
2. Kdb+
3. RRDtool
4. Graphite
5. OpenTSDB
6. Prometheus
7. Druid
8. KairosDB
9. eXtremeDB
10. Riak TS

KairosDB appears to make use of Cassandra which is a NoSQL datastore to manage its data

## General Database Guide Links

[Database Blog](https://blog.timescale.com)
https://blog.chartio.com/posts/choosing-the-right-database-for-your-data-strategy

Strengths and Weaknesses: https://www.infoworld.com/article/3268871/database/how-to-choose-the-right-type-of-database-for-your-enterprise.html

https://blog.cloud66.com/3-tips-for-selecting-the-right-database-for-your-app/

https://blog.timescale.com/what-the-heck-is-time-series-data-and-why-do-i-need-a-time-series-database-dcf3b1b18563

https://blog.timescale.com/time-series-data-why-and-how-to-use-a-relational-database-instead-of-nosql-d0cd6975e87c

http://basho.com/resources/time-series-databases/

A curated list of awesome time series databases , benchmarks and papers: https://github.com/xephonhq/awesome-time-series-databas
# General Notes

It appears as if a time series database will work well for the data, or the use of a key-value database.
It may make sense to work with a hybrid solution which allows for an efficient time series database(or key value) and then make use of a standard relational database (MySQL or Postgres) for the other data that needs to use incorporated

# Installing InfluxDB

https://www.youtube.com/watch?v=34oOp1OLOUk

# MongoDB

Installing:

https://www.youtube.com/watch?v=cYj1AJAU_mk

Once mongodb is installed, then you can start a MongoDB database by:
"C:\Project\mongodb\bin\mongod.exe" --dbpath="C:\Project\data\db"

The --dbpath option points to your database directory.

If the MongoDB database is running correctly, then you will see: "[initandlisten] waiting for connections"

Then you can connect to the MongoDB by:

"C:\Project\mongodb\bin\mongo.exe"

You can start MongoDB as a service, not sure if we should do that just yet.

[This](http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/) guy used MongoDB to create a web app that managed the data, his choice for using a database was:
    It is true that you can use the data directly from a JSON file. The main reason for using MongoDB in this tutorial are:
    - In this tutorial, we are only using a few fields (subset of the data). With MongoDB, we can query only the fields that we need. If you use the JSON file directly, you will have to send all the data to the browser before selecting the field that you are interested in. This may cause the browser to crash. 
    - If you want to build a dashboard to visualize data that is constantly changing, then you need a database for managing the records. 
    - In this tutorial, I wanted to introduced all the building blocks for creating interactive visualization. Even though, I could have managed by not using a database, I think that showing how a database can be integrated can be useful for people who want to build dashboards with complex datasets.

# Testing out Graphite

The folks at Graphite have created a system called "[Synthesize](http://graphiteapp.org/quick-start-guides/synthesize.html)" which is a "fully automated installation and configuration script for the Graphite stack".

It appears that the easiest way to test it out is to use Vagrant (sort of like virtualbox).

# Working on the Server

## Server Details

hostname:  tsdb.eie.wits.ac.za
ip address: 146.141.16.82
username: username
password: password

http://146.141.16.82:4242

http://146.141.16.82:4242/api/suggest?type=metrics&max=10&q=

## Checking that Zookeeper is accessible

One of the first steps in setting up OpenTSDB, from their [site](http://opentsdb.net/docs/build/html/installation.html#id1) is to check that Zookeeper is accessible. One can do this with the following commands:
    telnet localhost 2181
    stats

This will tell you if it is set up.

## Install

We have assumed that the installation has been carried out successfully and that we are able to make use of the system.

When searching through the file system, I found Hbase installed in /opt/hbase. This had all kinds of files for its workings. 

I also found a folder with OpenTSDB stuff in the /etc folder. This had some config files.

OpenTSDB files are installed in the following places:

* /etc/opentsdb - Configuration files
* /tmp/opentsdb - Temporary cache files
* /usr/share/opentsdb - Application files
* /usr/share/opentsdb/bin - The "tsdb" startup script that launches a TSD or command line tools
* /usr/share/opentsdb/lib - Java JAR library files
* /usr/share/opentsdb/plugins - Location for plugin files and dependencies
* /usr/share/opentsdb/static - Static files for the GUI
* /usr/share/opentsdb/tools - Scripts and other tools
* /var/log/opentsdb - Logs

The installation includes an init script at /etc/init.d/opentsdb that can start, stop, and restart OpenTSDB

In order to get this to work, simply use:
    service opentsdb start
    service opentsdb stop

In order to edit the configuration file, you need to stop the service. After it is installed, it will not be running, this means that you will be able to edit the configuration file.

## Accessing the Server localhost

In order to access the server, you have to tunnel into the server. I made use of MobaXterm to do this. The MobaSSHTunnel tool allows you to set up forwarding for that port.

This allows one to access: 127.0.0.1:4242 which is the GUI.


/usr/share/opentsdb/bin/tsdb mkmetric mysql.bytes_received mysql.bytes_sent
This now shows up on the GUI when searched for in the metric box.

In order to get the csv data into the database a number of steps need to take place:

Firstly, the csv data needs to be converted into a format read by OpenTSDB, this means that each csv file will be converted so that it has the form:

    put metric timestamp value tags

This should be in an OpenTSDB ASCII format.
This system was found from [here](https://groups.google.com/forum/#!topic/opentsdb/rmx1pU6niY8)

* The metric part will be the identifier of the data logger, which in this case will be the name of the sensor.
* The timestamp is required to be in the form of a unix Epoch timestamp in seconds or milliseconds (ISO 9601 format).
* The value will be the value measured by the data logger at that point in time, which is given by an integer or a floating point value.
* The tags are other unique pieces of information that may relate to that data entry, or to the sensor.

[Another](https://stackoverflow.com/questions/8520612/how-to-insert-data-in-opentsdb-time-series-database) way to import the data to the database.

## Importing into Server

Info found [here](http://opentsdb.net/docs/build/html/user_guide/cli/import.html)

    import path [...paths]

Example

    import /home/hobbes/timeseries1.gz /home/hobbes/timeseries2.gz

## My Experience

The formatting of the files is most important.
The first thing to consider is the naming of the metric, one should be consistent in the use of full stops or underscores. The use of spaces does not work.
The next important point is that of the date formatting, the Unix Epoch Timestamp must not have a ".0" on its tail.

In order to import data into the database, spaces are used to separate the fields.

Tags are mandatory, these should be chosen appropriately, this can include things such as the location, install date, or a number of other chosen parameters.

In order to import into the database use:
    /usr/share/opentsdb/bin/tsdb import filename.gz

This implies that the file should be zipped (the file should not have a file type when doing this (from my experience)).
I did this by using:
    gzip -k filename

While testing out the server, I had issues with importing individual entries, I only had luck with importing a sensors data as a whole.

When testing, there were multiple errors while attempting to input negative numbers or numbers with decimal points, this should be tested out.
An error was given that ".0" would not be accepted. However, this could have been due to the ".0" in the Unix timestamp field.

The following [site](https://www.erol.si/2014/06/opentsdb-the-perfect-database-for-your-internet-of-things-projects/) was highly useful.

Linking the database with D3.js and some other tools. [This](https://gist.github.com/stuart-warren/5354116) has some useful info.

Query from command line:
    /usr/share/opentsdb/bin/tsdb query 1y-ago  sum LoggerName

### List Number of Metrics in Database

Place [this](http://localhost:4242/api/suggest?type=metrics&max=10000s) into your web browser.

### Delete Metric from Database

/usr/share/opentsdb/bin/tsdb uid delete metrics "metricName"

### Floating Point Numbers

The OpenTSDB database is not commonly used for storing measurements that require exact values. The database makes use of IEEE 754 floating point single format with positive and negative value support.
If the value input into the database lacks a ".", then it will import the number as an integer, this will be exported correctly.
When one imports a value that has decimal points, the database will return a different number.

From the [website](http://opentsdb.net/docs/build/html/user_guide/writing.html):
    Note: Because OpenTSDB only supports floating point values, it is not suitable for storing measurements that require exact values like currency. This is why, when storing a value like 15.2 the database may return 15.199999809265137.

Sort of solution:
    https://groups.google.com/forum/#!topic/opentsdb/MOcjjLr3iDw

### Duplicate Data Points

Overwriting old data points will not negatively affect the database, one must just make sure that compactions are disabled.
This is very convenient, as it makes writing the import scripts simplistic. http://opentsdb.net/docs/build/html/user_guide/writing.html

### The Choice of the HTTP API

[Note](http://opentsdb.net/docs/build/html/user_guide/writing.html):
    The Telnet method of writing is discouraged as it doesn't provide a way of determining which data points failed to write due to formatting or storage errors. Instead use the HTTP API.

### Query Limits

It appears that there is a limit to the number of metrics that can possible be queried at any point in time. A number of workarounds were made for this use case. The case of the treemaps, we had to limit the number of metrics per query, and then concatenate the data returned. 

# Linux Commands Used

## Copy Files

pscp -r 'C:\...' username@tsdb.eie.wits.ac.za:'/home/username/.../'

## Count Files in Folder

ls -1 | wc -l

## Zip a File

To make a .gz file simply:
    gzip -k filename

## Size of Folder

du -sh file_path

## Getting a Shell Script to Work

First create the shell script with:
    touch filename.sh

Then edit the file with the contents you want.
You have to allow it to have execution ability, you can do this by using
    chmod +x filename.sh

Then you can run the script with
    ./filename.sh
Where the './' indicates that you are running it from inside the current folder.

## Checking if a Service is Running

To check the status of a specific service:
    service service_name status

To check the status of all services on the system:
    service --status-all

To start, restart, stop, services:
    service service_name stop
    service service_name start
    service service_name restart

## Install Python Packages

I did not manage to get the server to install python packages using the pip command, there seemed to be an issue to do with the proxy, or internet access.
However, it is possible to update linux packages, this can be used to install python packages using the apt-get command:
    apt-get install python3-package_name

## Run command and keep it running even when user logs out

Use the [screen](https://www.ostechnix.com/4-ways-keep-command-running-log-ssh-session/) package.
This will run the command, and the user can leave that session with it will running.
You can launch a screen by the simply comand:
    screen

Once the screen is up and running, you can issue your normal commands.

You can disconnect from the screen by using:
    Ctrl + A followed by d

To go back into your screen:
    screen -r

### Size of files in directory

ls -l *

## Delete all files that do not contain the *** file type

find . ! -name "*.file_fype" | xargs rm

### Bulk Import into Database

sudo find . -name "*.gz" -exec /usr/share/opentsdb/bin/tsdb import {} \;
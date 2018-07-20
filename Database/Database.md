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

This is a technique of accessing a relational database from an object-oriented language (from: https://www.yegor256.com/2014/12/01/orm-offensive-anti-pattern.html). Yegor speaks about how the standard use of ORM is, instead of encapsulating database interaction inside an object, it extracts it away, literally tearing a solid and cohesive living organism apart.

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

https://thenewstack.io/use-time-series-database/

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

KairosDB appears to make use of Cassandra which is a NoSQL datastore to manage its data.
## General Database Guide Links

[Database Blog](https://blog.timescale.com)
https://blog.chartio.com/posts/choosing-the-right-database-for-your-data-strategy

Strengths and Weaknesses: https://www.infoworld.com/article/3268871/database/how-to-choose-the-right-type-of-database-for-your-enterprise.html

https://blog.cloud66.com/3-tips-for-selecting-the-right-database-for-your-app/

https://blog.timescale.com/what-the-heck-is-time-series-data-and-why-do-i-need-a-time-series-database-dcf3b1b18563

https://blog.timescale.com/time-series-data-why-and-how-to-use-a-relational-database-instead-of-nosql-d0cd6975e87c

http://basho.com/resources/time-series-databases/

A curated list of awesome time series databases , benchmarks and papers: https://github.com/xephonhq/awesome-time-series-database
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

The --dbpat option points to your database directory. 

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

### KarosDB

Following the [guide](http://kairosdb.github.io/docs/build/html/GettingStarted.html)

[Link](https://github.com/kairosdb/kairosdb/releases/download/v1.3.0-beta1/kairosdb-1.3.0-0.1beta.tar.gz) for the download of the database.
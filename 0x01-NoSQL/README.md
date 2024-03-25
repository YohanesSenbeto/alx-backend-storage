# NoSQL Project

## Description

This project is part of the curriculum for the NoSQL specialization. It covers various tasks related to MongoDB and Python, aimed at understanding and implementing NoSQL concepts and MongoDB usage.

## Learning Objectives

By completing this project, you will:

- Understand the concept of NoSQL databases and their benefits
- Differentiate between SQL and NoSQL databases
- Gain proficiency in using MongoDB for document storage
- Learn how to perform basic operations like querying, inserting, updating, and deleting information in a MongoDB database
- Develop skills in working with MongoDB using Python and PyMongo library

## Requirements

- MongoDB command files for each task
- Python scripts for tasks involving Python and PyMongo
- Use of Ubuntu 18.04 LTS with MongoDB 4.2
- Proper commenting and documentation in code
- README.md file providing necessary information about the project setup and usage

## Resources

- [NoSQL Databases Explained](#)
- [What is NoSQL?](#)
- [MongoDB with Python Crash Course - Tutorial for Beginners](#)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](#)
- [Introduction to MongoDB and Python](#)
- [mongo Shell Methods](#)
- [Mongosh](#)

## Tasks

1. **List all databases**
   - Description: Write a script to list all databases in MongoDB.
   - File: [0-list_databases](./0-list_databases)

2. **Create a database**
   - Description: Write a script to create or use the database `my_db`.
   - File: [1-use_or_create_database](./1-use_or_create_database)

3. **Insert document**
   - Description: Write a script to insert a document in the collection `school`.
   - File: [2-insert](./2-insert)

...

## Installation

1. Install MongoDB 4.2 in Ubuntu 18.04 using the following commands:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org


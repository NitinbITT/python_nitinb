# Database
* Database is a place where data is stored, which can be in any form

## Relational database:
* It is a DB where there are rows and columns in a table.
* Data is stored in these tables.
* All the tables in the DB have relation among them using foreign key.

### RDBMS vs DBMS:
* RDMS is a software which is used to maintain a relational DB.
* DBMS is a software which is used to maintain a relational DB.

### Keys:
* Keys are used to identify a set of data or a unique data from the tables.
* There are many types of keys
    * Super Keys: Super keys is two or more column which is has unwanted columns among them
    * Primary Key: It is a key which uniquely identofies a row. It is a single coloumn
    * Candidate Key: Candidate key is a key which uniquely identitfies row using 2 or more columns. It does not have unwanted column among them.

```
Super Key (Candidate Key (Primary Key) )
```
## SQL commands:
* DDL : To define the structure
* DQL : To query the tables
* DML : To manipulate the data inside the table
* DCL : To control permission of transactions
* TCL : To control transactions

## Constraints
* Constraints are conditons which are checked during insertion
```
insert into table_name values
(
    val1 type constraint,
    val1 type constraint,
    val1 type constraint
    .....
    .....
)
```

* Primary key constraint : To check whther the inserting value is unique and not null
* Foreign key constraint : To add a given column as a foreign key
* Check constraint : Checks a condition before inserting
* Default constraint : Provides default value during insertion
* Unique constraint : To check whether the inserting value in unique
* NOT NULL constraint : To check whether the inserting value is not null

## ACID Properties
* Atomicity : If a transaction occurs it must  get complete else it stops and rollbacks to previous.
* Consistency : There must be consistency in the data
* Isolation : Each transaction must take place isolated and there must be any dirty data
* Durability : Even if the system fails, the data must be consistent and right.

## Normalization:
* 1NF : the values in each cell must be atomic
* 2NF : Every non primary key is only dependent on the primary key
* 3NF : There must no be nay transistive dependency
* BCNF : Stricter version of 3NF
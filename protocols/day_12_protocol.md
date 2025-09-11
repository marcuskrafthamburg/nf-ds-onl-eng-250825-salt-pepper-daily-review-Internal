# Day 12, 09.09.2025

##   __Basic Overview__ </span>
 
* <span style="color:grey"> [DBeaver](#dbeaver)
* <span style="color:grey"> [Databases](#databases)
* <span style="color:grey"> [SQL](#sql)
* <span style="color:grey"> [Groupwork](#miro-groupwork-results)
* <span style="color:grey"> [Bonus](#bonus)

---
##  __Schedule__
<span style="color:grey">

|Time|Content|
|---|---|
|09:00 - 09:30|Daily Review|
|09:30 - 10:00|Setup DBeaver|
|10:00 - 10:40|Introduction to DatabasesL|
|10:45 - 11.30|Miro Group Practise| 
|12:30 - 13:30|Lunch Break|
|13:30 - 15:00|Introduction to SQL|
|15:00 - |Pair/Group SQL Exercise| 

</span>

# DBeaver <span style="color:grey">
> DBeaver Community is a free cross-platform database tool for developers, database administrators, analysts, and everyone working with data. [Official Site.](https://dbeaver.io/)

### How to connect
1. Open DBeaver
1. Click on New Connection Button (Top Left)
2. Select your Database &mdash; we use PostgreSQL
3. Fill in Connection Settings 
    1. Credentials we used:

        ```
        database = postgres
        user = saltandpepper
        password = mialovesicecream
        host = ds-sql-playground.c8g8r1deus2v.eu-central-1.rds.amazonaws.com
        port = 5432
        ```
4. Test Connection
5. Connect

> [Course Setup](https://ideal-adventure-6vymekm.pages.github.io/sessions/05.1_Intro_to_Databases.html#dbeaver)
</span>



# Databases </span>
<span style="color:grey">

> For more detailed description refer to the provided [Course Material.](https://ideal-adventure-6vymekm.pages.github.io/sessions/05.1_Intro_to_Databases.html)
* Systematic collection of data
* either stored on disk or in-memory (faster)

### Types of Data:
* Unstructured
* Semi-Structured
* Structured

### Types of Databases:
* RDBMS: Relational Database Management Systems
* NoSQL Databases

---

### General Database Structure / Hierachy:
> ### schema(s) <span style="color:green"> > </span> tables <span style="color:green"> > </span> columns and rows <span style="color:green"> > </span> cells

---

### Entity-Relationship types
* One-to-one (1:1)
* One-to-many (1:n) / Many-to-one (n:1)
* Many-to-many (n:n)


### Relational Databases
* Tables connected via **Primary** and **Foreign Key**
* Primary key is unique for each record
* Foreign keys refer to the primary key in another table

</span>


# SQL </span>
<span style="color:grey">

* *Structured Query Language*
* Language for storing, manipulating and retreiving data in databases.


> For more detailed Information refer to the provided [Course Material.](https://ideal-adventure-6vymekm.pages.github.io/sessions/05.2_Intro_to_SQL.html)

</span>





<span style="color:grey">


### Core Syntax
| KEYWORD || FUNCTION|
|---|---|---|
|```SELECT``` |column_name(s)| Returns final data, separated by " , " for multiple columns|
|```FROM``` | table_name|Choose tables to get base data| 
|```WHERE```| condition| Filter the base data &mdash; for multiple conditions: ```AND, OR, NOT, ID (NOT) NULL```|

> Separate each SQL statement with a semicolon **;**  

### Additional Options
| KEYWORD || FUNCTION|
|---|---|---|
|```SELECT * ```| | select all
|```SELECT DISTINCT``` |column_name(s)| Returns only distinct (=different) values|
|```AS```|```SELECT``` column ```AS``` alias_name| assign temporary alias to column/row| 
|```GROUP BY``` |column_name(s)| Aggregates the base data|
|```HAVING```| condition |Filters aggregated data &mdash; comes after GROUP BY instead of WHERE
|```ORDER BY```| column1 , column2 |Sorts the final data|
|```LIMIT```|number |Limits he returned data to a row count|
|```JOIN``` | table2 t2 ```ON``` t1.key1 = t2.key2 | INNER JOIN is default. For more see below


---

### Filter data with WHERE 

| Operator        | Description                              |
|-----------------|------------------------------------------|
| =               | Equal                                    |
| >               | Greater than                             |
| <               | Less than                                |
| >=              | Greater than or equal                    |
| <=              | Less than or equal                       |
| <> or !=        | Not equal                                |
| BETWEEN         | Between a certain range                  |
| LIKE            | Search for a pattern                     |
| IN              | To specify multiple possible values for a column |
| IS NULL /IS NOT NULL | Filter for NULL values|
| AND| displays data if all conditions are TRUE|
|OR| displays data if any conditions are TRUE|
|NOT|displays data if condition(s) is NOT TRUE|


### comment your code with:
``` sql
-- single line comment

/* Mulit line
coments
*/
```
#### Additional Information
AVG() , COUNT() , SUM() , MIN(), MAX()

Arithmetic Operators **+ - * / %**

## Multiple Tables</span>

* Use Aliases to give table / columns a temporary name
* ```JOIN``` tables:
``` sql
    SELECT t1.name, t2.something
    FROM table1 t1
    INNER JOIN table2 t2
    ON t1.key1 = t2.key2;
```
--- 

![Cheatsheet](/cheatsheets/join_cheatsheet.png)

</span>




##   __Helpful References__

* SQL tutorial on [W3School](https://www.w3schools.com/sql/default.asp)
* Introductory NF Course Materials on
    * [Databases](https://ideal-adventure-6vymekm.pages.github.io/sessions/05.1_Intro_to_Databases.html)
    * [SQL](https://ideal-adventure-6vymekm.pages.github.io/sessions/05.2_Intro_to_SQL.html)

* NF SQL Introduction exercises [on GitHub](https://github.com/neuefische/ds-sql-intro/tree/main)

---

# MIRO GROUPWORK RESULTS
> [Miro](miro.com) &mdash; collaborative workspace 

* The task was:
    * create 4 - 8 entities ('tables')
    * add properties (columns)
    * model the dependencies (connect the tables)

![Restaurant](/group_work/miro_airport.png)
![Restaurant](/group_work/miro_chocolate_factory.png)
![Restaurant](/group_work/miro_restaurant.png)
![Restaurant](/group_work/miro_restaurant_dogo_pasta_express.png)
![Restaurant](/group_work/miro_general_example.png)

[RETURN TO TOP](#basic-overview)

## Bonus

Add some whimsy to your VS CODE :D

The pets will appear in a tab on the bottom left

    Name: vscode-pets

    Id: tonybaloney.vscode-pets

    Description: Pets for your VS Code

    Version: 1.33.0

    Publisher: Anthony Shaw

    VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=tonybaloney.vscode-pets
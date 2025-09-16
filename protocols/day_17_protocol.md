# Day 17 — 16.09.2025
## Basic Overview
* [EDA Project](#EDA_Project)
    * [General](#General)
    * [Data Retrieval](#Data_Retrieval)
    * [Data Preparation](#Data_Preparation)
    * [Data Analysis](#Data_Analysis)
    * [Result Presentation](#Result_Presentation)
* [Helpful References](#Helpful_References)
## Schedule
 Time        | Content                                         
 ----------- | ----------------------------------------------- 
09:00 - 11:00 |presentation about EDA project setup
11:00 - 12:00 |technical setup of python environment
12:00 - 14:00 |initial exploration of project data
14:00 - 14:30 |discussion on hypothesis definition
14:30 - end of the day| pair work on EDA project


# EDA Project
## General


__Provided Information:__
* Table of properties in King County (WA) USA
* Table of realised property sales between 2014-05 and 2015-05

__Group Selection:__
* List of different clients was provided
* Each client has specific requirements and goals
* Each pair programming group decided for one client
* Define at least 3 hypothesis you want to test

__Project Target:__
* Do all necessary steps to generate insights for __*your*__ client
* Document your work in a Jupyter notebook
* Present your results as slides focussed on your client

__Schedule:__
 Day |  Task
 -|-
 Tuesday |Introduction to project, initial data exploration and hypothesis definition
 Wednesday | pair work on project (daily review at 1pm)
 Thursday | pair work on project
 Friday | before 1pm: pair work on project / at 1pm: result presentation
 

## Data Retrieval
Data is stored in the EDA schema of the Postgres DB we have used before.
Attribute | Value
-|-
Database | postgres
Schema | eda
Table | king_county_house_details
Table | king_county_house_sales


### Connection Details
~~~prolog
Database = postgres
User = saltandpepper
Password = mialovesicecream
Host = ds-sql-playground.c8g8r1deus2v.eu-central-1.rds.amazonaws.com
Port = 5432 
~~~
### Data Retrieval in Python
Connection based on SQL Alchemy:
~~~python
from sqlalchemy import create_engine

DB_STRING = 'postgresql+psycopg2://saltandpepper:mialovesicecream@ds-sql-playground.c8g8r1deus2v.eu-central-1.rds.amazonaws.com:5432/postgres'

db = create_engine(DB_STRING)
~~~
Example of query execution:
~~~python
import pandas as pd

query_string = "SELECT min(date), max(date) FROM eda.king_county_house_sales"

df = pd.read_sql(query_string, db)
~~~
Query string to combine property data and sales data:
~~~SQL
SELECT kchd.*,kchs."date" ,kchs.price 
FROM king_county_house_details kchd 
LEFT JOIN  king_county_house_sales kchs 
ON kchd.id = kchs.house_id;
~~~
> Note: this will duplicate house data having several entries in sales table!

## Data Preparation
Before analysis of data:
1. retrieve data in python (as described above)
1. (you might want to store retrieved data as csv)
1. prepare dataframe(s): e.g. remove spaces in column names and adopt caps (see day 16)
1. identify and clean entries that don't fit your desired column data type (e.g. string in number column)
1. define appropriate data types for each column (date, int, float, ...)


## Data Analysis
 Analyse the provided data focussing on the **requirements of your client** as well as the **hypothesis** defined by you.

__Remember:__
* Clean the data.
* Decide how you treat outliers.
* Do not just focus on metrics that proves your assumptions.
* Identify patterns and correlations.
* What are your insights?

## Result Presentation

### Time
* Each group has 10 minutes for the result presentation. 
* Use this time but don't exceed it.


### Content

Introduction:
* about dataset
* about client
* about the data quality

Content:
* findings and changes in approach… in context
* generated knowledge: insights
* propose actions
* future work

Focus:
* hypothesis => whys
* methodology => hows



### Style
* Adapt the presentation to your audience (client).
* Keep it simple, stupid! (KISS principle)
* Be concise and accurate, no extra information if not needed
* Join explanation blocks with “whys” and “hows”
* Be clear, don’t be ambiguous - clarity inspires trust in your results



### Charts
* Less is more
* Keep charts as simple as possible and as complex as required
* If you use colors be intentional
* Define / use a color theme and stick to it
* Use axis according to data type (categorical vs numerical)
* Don't truncate axis


#  Helpful References
* EDA project introduction
    * https://ideal-adventure-6vymekm.pages.github.io/sessions/07.2_EDA_process.html
* KISS principle:
    * https://en.wikipedia.org/wiki/KISS_principle
* Colour paletts defined in visualisation library "bokeh"
    * https://docs.bokeh.org/en/latest/docs/reference/palettes.html

# Day 17 — 16.09.2025
## Basic Overview
* [EDA Project](#eda-project)
    * [General](#general)
    * [Data Retrieval](#data-retrieval)
    * [Data Preparation](#data-preparation)
    * [Data Analysis](#data-analysis)
    * [Result Presentation](#result-presentation)
* [References](#references)
## Schedule
Time| Content
-- | -- 
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
* Each group defined at least 3 hypothesis they want to test

__Project Target:__
* Do all necessary steps to generate insights for __*your*__ client
* Document your work in a Jupyter notebook
* Present your results **about** your client **to** an audience of mixed group of company internal stakeholders

__Project Schedule:__
 Day |  Task
 -|-
 Tuesday |Introduction to project / initial data exploration / hypothesis definition
 Wednesday | pair work on project / at 1pm: daily review 
 Thursday | pair work on project / 10am: check-in with attendance picture
 Friday | pair work on project / at 1pm: result presentation
 

## Data Retrieval
Data is stored in the EDA schema of the Postgres DB we have used before.

### Database Information
__Storage location:__
Attribute | Value
-|-
Database | postgres
Schema | eda
Table | king_county_house_details
Table | king_county_house_sales

__Connection Details:__
~~~prolog
Database = postgres
User = saltandpepper
Password = mialovesicecream
Host = ds-sql-playground.c8g8r1deus2v.eu-central-1.rds.amazonaws.com
Port = 5432 
~~~
### Data in Python
__Connection based on SQL Alchemy:__
~~~python
from sqlalchemy import create_engine

#connection string => dialect+driver://username:password@host:port/database

DB_STRING = 'postgresql+psycopg2://saltandpepper:mialovesicecream@ds-sql-playground.c8g8r1deus2v.eu-central-1.rds.amazonaws.com:5432/postgres'

db = create_engine(DB_STRING)
~~~
> __Note:__ The connection string includes the database but not the schema!

__Example of query execution:__
~~~python
import pandas as pd

query_string = "SELECT min(date), max(date) FROM eda.king_county_house_sales"

df = pd.read_sql(query_string, db)
~~~
> __Note:__ The schema is added to the table name in this example "... __eda__.king_county_house_sales ..."!

__Query string to combine property data and sales data:__
~~~SQL
SELECT kchd.*,kchs."date" ,kchs.price 
FROM king_county_house_details kchd 
LEFT JOIN  king_county_house_sales kchs 
ON kchd.id = kchs.house_id;
~~~
> __Note:__ this will duplicate house data having several entries in sales table!

__If you prefer you can store data as csv:__
~~~python
#export the data to a csv-file (locally)
df.to_csv('data/eda.csv',index=False)
   
#import the data from a csv-file
df_import = pd.read_csv('data/eda.csv')
~~~

## Data Preparation
Before analysis of data:
1. retrieve data in python (as described above)
1. you might want to store retrieved data as csv  (as described above)
1. prepare dataframe(s): e.g. remove spaces in column names and adopt caps (see day 16)
1. identify and clean entries that don't fit your desired column data type (e.g. string in number column)
1. define appropriate data types for each column (date, int, float, ...)


## Data Analysis
 Analyse the provided data focussing on the **requirements of your client** as well as the **hypothesis** defined by you.

 You might add other (external) data to your analysis if meaningful for the context - but only after your are done analysing of provided data.

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
* try to identify financial impact
* propose actions
* future work

Focus:
* hypothesis => whys
* methodology => hows



### Style
* Adapt the presentation to your audience (mixed group of company internal stakeholders)
* Keep it simple, stupid! (KISS principle)
* Be concise and accurate, no extra information if not needed
* Join explanation blocks with “whys” and “hows”
* Be clear, don’t be ambiguous - clarity inspires trust in your results



### Charts
* Less is more
* Keep charts as simple as possible and as complex as required
* If you use colours be intentional
* Define a colour palette and stick to it
* Use axis according to data type (categorical vs numerical)
* Don't mislead the audience  (e.g. by truncating axis)


#  References
* EDA project introduction
    * https://ideal-adventure-6vymekm.pages.github.io/sessions/07.2_EDA_process.html
* KISS principle:
    * https://en.wikipedia.org/wiki/KISS_principle
* Colour palettes defined in visualisation library "bokeh"
    * https://docs.bokeh.org/en/latest/docs/reference/palettes.html

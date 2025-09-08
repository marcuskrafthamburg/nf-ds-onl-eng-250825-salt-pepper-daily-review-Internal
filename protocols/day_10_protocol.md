# Day 10, 05.09.2025
<span style="color:grey">
Daily Routine
</span>

--- 

__Basic Overview__
 

* <span style="color:grey"> Daily Protocol
* <span style="color:grey"> Python Day 10


##  __Schedule__

|Time|Content|
|---|---|
|10:00 - 11:00|Introduction to Pandas|
|11:00 - 16:00|Pandas Practice and self study
|Ending|
</span>
---


<img src="https://raw.githubusercontent.com/pydata/pandas/main/web/pandas/static/img/pandas_white.svg" alt="Pandas Logo" width="500"/>



</span>

##  __Objective__

<span style="color:white">

- explain why Pandas is important to Data Scientists
- create Pandas DataFrames from lists or a list of dictionaries
- load data from csv-files to DataFrames
- access data stored in DataFrames
- use the common features of a DataFrame
- Data Visualization, plots and their use
</span>


## <span style="color:white">**Why Pandas needed in Data science**

<span style="color:white">

Pandas is important to Data Scientists because it makes working with data fast, easy, and efficient. It provides powerful tools for cleaning, transforming, and analyzing structured data (like tables in Excel). With Pandas, you can quickly filter rows, group and summarize data, handle missing values, merge datasets, and create basic visualizations.

</span>

## <span style="color:white">0. Creating DataFrames Manually</span>

<span style="color:white">
Build small DataFrames directly inside code using lists or dictionaries.

```python
# From list of dicts (each dict = row, keys = columns)
data = [{'a':1,'b':2,'c':3}, {'a':4,'b':5,'c':6}]
df = pd.DataFrame(data)

# From list of lists with column names
values = [[1,2,3],[4,5,6]]
cols = ['a','b','c']
df = pd.DataFrame(values, columns=cols)
```
To execute this we need to import pandas as pd, which is explained in next section
</span>

## <span style="color:white">**1. Importing Data**</span>

<span style="color:white">
Load datasets into pandas (e.g., read_csv) so you can analyze them.

```
import pandas as pd         #Importing pandas

df = pd.read_csv("D:/DataScience/_pandasbasics/data/abalone.csv")  # reading external data
```
</span> 

## <span style="color:white">2. Peek at Data</span>

<span style="color:white">
Quickly inspect structure, first/last rows, column info, and summary statistics.

```python
df.head()       # first 5 rows
df.tail()       # last 5 rows
df.tail(10)     # last 10 rows
df.shape        # (rows, cols)
df.columns      # list of column names
df.info()       # column info, non-null counts, dtypes
df.describe()   # summary stats: count, mean, std, min, 25%, 50%, 75%, max
```
</span>

## <span style="color:white">3. Accessing Data</span>
<span style="color:white">
Select single/multiple columns or rows using labels (df['col'], df.loc) or positions (df.iloc).

```python
df['sex']              # single column
df.sex                 # single column (alternative)
df[['sex','length']]   # multiple columns
df.iloc[:3]            # first 3 rows (positional)
df.head(3)             # same result as above

# ⚠️ df[0] → ❌ invalid for column access (use df.iloc[:,0])
```

## <span style="color:white">4. Copy & Rename Columns</span>

<span style="color:white">
Make safe copies of your DataFrame and clean/rename column names for easier use.

```python
df2 = df.copy()                                  # copy DataFrame
cols = df2.columns.tolist()                      # list of column names
cols = [col.replace(' ', '_') for col in cols]   # replace spaces with underscores
df2.columns = cols                               # assign cleaned names

df2.rename(columns={'n_rings': 'nr_rings'}, inplace=True)  # rename
```
</span>

## <span style="color:white">5. Row & Column Selection</span>

<span style="color:white">

Extract specific rows and columns by labels (loc) or positions (iloc).
```python
df.loc[0, 'sex']                         # row label 0, column 'sex'
df.loc[0:9, ['sex','length','height']]   # rows 0–9, specific columns
df.iloc[0:10, [0,1,3]]                   # rows 0–9, cols 0,1,3 (by index)

loc vs iloc
loc[] → labels (strings or integers, end inclusive)
iloc[] → integer positions (end exclusive)
```
</span>

## <span style="color:white">6. Filtering Data</span>

<span style="color:white">
Apply conditions to keep only rows that match criteria (e.g., length ≤ 0.4, sex = 'F').

```python
df['length'] <= 0.4                        # boolean mask
df[df['length'] <= 0.4]                    # apply mask
df[(df['length'] <= 0.4) & (df['sex']=='F')]  # multiple conditions

df['length'].between(0.35, 0.4)            # range filter
df[df['sex'].isin(['F','M'])]              # membership filter

# Using query()
df.query('0.35 < length <= 0.4 and 0.25 < weight_whole < 0.3')
```
</span>

## <span style="color:white">7. GroupBy & Aggregation</span>

<span style="color:white">
Group data by categories and compute summaries like mean, max, count, etc.

```python
df['sex'].unique()           # unique values
df['sex'].nunique()          # number of unique values
df['sex'].value_counts()     # frequency counts

g = df.groupby('sex')
g.mean()                     # mean per group
g.max()                      # max per group
g.count()                    # counts per group
df.groupby('sex')['length'].count()

# Multiple groupby
df.groupby(['sex','n_rings'])['weight_whole'].count()

# Modern agg
df.groupby('sex').agg(
    mean_len=('length','mean'), # compute mean of column 'length', name it "mean_len"
    max_len=('length','max'), # compute max of column 'length', name it "max_len"
    n=('length','count') # count non-null values in 'length', name it "n"
).reset_index() # converts that index back into a normal column, so the result looks like a regular DataFrame.
"""
Without reset_index()
       mean_len  max_len  n
sex                          
F        0.523    0.80   500
I        0.350    0.60   400
M        0.600    0.90   600

With reset_index()
  sex  mean_len  max_len    n
0   F     0.523     0.80  500
1   I     0.350     0.60  400
2   M     0.600     0.90  600
"""
```
</span>

## <span style="color:white">8. Sorting</span>

<span style="color:white">
Arrange rows based on column values, in ascending/descending order, single or multiple columns.

```python
df.sort_values('length').head(15)                         # ascending (default)
df.sort_values('length', ascending=False).head(15)        # descending
df.sort_values(['length','diameter'], ascending=[False, False]).head(15)  # multi-column
df['length'].nlargest(5)                                  # top 5 values
```
</span>

## <span style="color:white">9. Creating & Dropping Columns</span>

<span style="color:white">
Add new calculated columns, modify with eval(), or remove columns you don’t need.

```python
# Create new column
df['age'] = df['n_rings'] + 1.5

# With eval (less common, use backticks if spaces in column names)
df.eval('age = n_rings + 1.5', inplace=True)

# Drop columns
df.drop('n_rings', axis=1, inplace=True)   # drop by name

# Why inplace is used
'By default, most pandas methods return a new DataFrame (or Series) and leave the original one unchanged'

'If you add inplace=True, pandas will modify the original DataFrame directly (no copy is returned)'
```
</span>

## <span style="color:white">10. Dealing with Missing Data</span>

<span style="color:white">
Identify, fill, or drop missing values (NaN) to clean the dataset for analysis.

```python
df.isna().sum()              # count NaN per column
df.fillna(-1, inplace=True)  # replace NaNs with -1
df.dropna(inplace=True)      # drop rows with any NaN
```
</span>


## <span style="color:white">11. Visualization</span>

Quick plots from DataFrame using .plot(kind=...).

### <span style="color:white">**Plot Types in Pandas and Their Useage**</span>

### <span style="color:white">Histogram</span>
📌 Shows distribution of a single numeric column (frequency of values).  
✅ Use to understand spread, skewness, or common ranges.  

<span style="color:white">

```python
df['quality'].plot(kind='hist')
```

### <span style="color:white">Scatter Plot</span>

📌 Plots two numeric columns against each other (x vs. y).  
✅ Use to check relationships, correlations, or outliers.  

<span style="color:white">

```python
df.plot(kind='scatter', x='quality', y='alcohol')
```

### <span style="color:white">Box Plot</span>

📌 Shows summary statistics: median, quartiles, outliers.  
✅ Use to compare distributions or detect extreme values.  

<span style="color:white">

```python
df[['fixed acidity','alcohol']].plot(kind='box')
```

### <span style="color:white">Bar Plot</span>

📌 Displays categorical data with bars (heights = values).  
✅ Use for frequency counts or category comparisons.  

<span style="color:white">

```python
df[['fixed acidity','alcohol']].plot(kind='box')
```

</span>

## <span style="color:white">**Plot Types in Pandas and Their Useage**

<span style="color:white">

Pandas is important to Data Scientists because it makes working with data fast, easy, and efficient. It provides powerful tools for cleaning, transforming, and analyzing structured data (like tables in Excel). With Pandas, you can quickly filter rows, group and summarize data, handle missing values, merge datasets, and create basic visualizations.

</span> 





## <span style="color:white">__Helpful References__
* [W3 Schools Panda reference](https://www.w3schools.com/python/pandas/pandas_cleaning.asp)

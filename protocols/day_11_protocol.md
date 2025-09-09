# Day 11, 08.09.2025

<span style="color:white">

##  __Schedule__

|Time|Content|
|---|---|
|10:00 - 11:00|Introduction to combining pandas DataFrames and numpy|
|11:00 - 18:00|Self study and exercises


##  __Objective__

- combining DataFrames with different methods
- learning basic concepts of numpy
- binning data and creating pivot tables
- working with dates and times


## __Combining DataFrames__

Methods to combine two DataFrames:

```
df1.join(df2, how={something})
pd.concat([df1, df2], axis='columns', join={something})
pd.merge(df1, df2, how={something})
```

| {something} | Description |
|---|---|
| left | Use keys from left frame only |
| right | Use keys from right frame only |
| outer | Use union of keys from both frames |
| inner | Use intersection of keys from both frames |


## __Basics of numpy__

Numpy works with arrays, which are list-like objects that contain only one type of data. They are mostly used for numerical operations. Numpy arrays take advantage of vectorization, which makes them perform certain tasks much faster than normal lists.

Here are some examples of useful numpy methods:

```python
import numpy as np

# creating a numpy array
arr1 = np.array([1, 2, 3])                          # create array from list
arr2 = np.array([[2, 3, 4], [3, 4, 5], [4, 5, 6]])  # create array from list of lists for n-d array
arr3 = np.zeros((2, 3), dtype=int)                  # create array filled with 0s
arr4 = np.ones((3, 4), dtype=float)                 # create array filled with 1s
arr5 = np.arange(0, 4.5, 0.5)                       # create array as a range
arr6 = arr5.reshape(3, 3)                           # reshape array into n-d array
```

```python
# numerical operations
print(arr1 + 1)                                     # add a single value to all elements in array
print(arr2 % 2)                                     # modulo single value to all elements in array
print(arr3 - [[2], [3]])                            # substract different values from each row
print(arr4 / [2, 1, 4, 3])                          # divide different values from each column
print(arr5 ** 2)                                    # square every element in n-d array
print(arr6 * arr2)                                  # multiply two arrays of same shape

print(np.sum(arr2, axis=0))                         # compute sum along rows
print(np.min(arr5))                                 # find minimum in entire array
print(np.max(arr6, axis=1))                         # find maximum along columns
```

```python
# indexing arrays
print(arr1[2])                                      # access element at certain position
print(arr2[1:, :2])                                 # slice elements from n-d array
print(np.where(arr5 > 2))                           # find indeces of elements for certain condition
```


## __Binning data__

Continuous values inside a DataFrame can be categorized into bins. The size and number of bins / categories can be adjusted.

An easy way to bin data is to use the "cut" method:

```python
my_bins = np.arange(2, 4, 0.5)                                  # 3 bins, each of size 0.5
binned_column = pd.cut(df['my_favorite_column'], bins=my_bins)  # categorize all elements in 'my_favorite_column' into the bins
binned_column.name = 'nice_bins'                                # name the new Series
df = pd.concat([df, binned_column], axis=1)                     # add Series as column to DataFrame
```


## __Pivot tables__

From [wiki](https://en.wikipedia.org/wiki/Pivot_table): "Among other functions, a pivot table can automatically sort, count total, or give the average of the data stored in one table or spreadsheet, displaying the results in a second table showing the summarized data. Pivot tables are also useful for quickly creating unweighted cross tabulations."

Usage:

```python
pd.pivot_table(df, values='my_worst_column', index='id', columns='nice_bins')   # create table where rows are defined by 'index' and columns are defined by 'columns'
                                                                                # the corresponding values inside this table are defined by 'values'
```


## __Datetime__

The library 'datetime' is a useful tool to work with dates and times in Python. It makes use of the data types 'date', 'time', 'datetime', and 'timedelta'.

```python
from datetime import datetime, date, time, timedelta

d1 = date(2025, 9, 8)                           # create date (year, month, day)
d2 = date.today()                               # create today's date
day = d2.day                                    # access day, month or year of the date
t1 = time(9, 43, 30, 500)                       # create time (hour, minute, second, microsecond)
t2 = time.now()                                 # create now's time
minute = t2.minute                              # access hour, minute, second, microsecond of the time
dt1 = datetime(2025, 9, 8, 9, 43, 30, 500)      # create datetime (year, month, day, hour, minute, second, microsecond)
dt2 = datetime.now()                            # create now's datetime
weekday = datetime.weekday()                    # e.g. weekday of today
```

```python
d0 = '08 September, 2025 9:43:30'
d1 = datetime.strptime(d0, '%d %B, %Y %H:%M:%S')        # convert string to datetime
d2 = datetime.strftime(d1, '%d/%m/%Y %H:%M')            # convert datetime to string
```

Format codes to specify date or time:

| Directive | Meaning | Example |
|---|---|---|
| %a | Abbreviated weekday name. | Sun, Mon, ...|
| %A | Full weekday name. | Sunday, Monday, ... |
| %w |	Weekday as a decimal number. |	0, 1, ..., 6 |
| %d |	Day of the month as a zero-padded decimal. |	01, 02, ..., 31 |
| %-d |	Day of the month as a decimal number.|	1, 2, ..., 30|
| %b |	Abbreviated month name.|	Jan, Feb, ..., Dec|
| %B |	Full month name.|	January, February, ...|
| %m |	Month as a zero-padded decimal number.|	01, 02, ..., 12|
| %-m |	Month as a decimal number.|	1, 2, ..., 12|
| %y |	Year without century as a zero-padded decimal number.|	00, 01, ..., 99|
| %-y |	Year without century as a decimal number.|	0, 1, ..., 99|
| %Y |	Year with century as a decimal number.|	2013, 2019 etc.|
| %H |	Hour (24-hour clock) as a zero-padded decimal number.|	00, 01, ..., 23|
| %-H |	Hour (24-hour clock) as a decimal number.|	0, 1, ..., 23|
| %I |	Hour (12-hour clock) as a zero-padded decimal number.|	01, 02, ..., 12|
| %-I |	Hour (12-hour clock) as a decimal number.|	1, 2, ... 12|
| %p|	Locale’s AM or PM.|	AM, PM|
| %M|	Minute as a zero-padded decimal number.|	00, 01, ..., 59|
| %-M|	Minute as a decimal number.|	0, 1, ..., 59|
| %S|	Second as a zero-padded decimal number.|	00, 01, ..., 59|
| %-S|	Second as a decimal number.|	0, 1, ..., 59|
| %f|	Microsecond as a decimal number, zero-padded on the left.|	000000 - 999999|
| %z|	UTC offset in the form +HHMM or -HHMM.|	| 
| %Z|	Time zone name.|	 |
| %j|	Day of the year as a zero-padded decimal number.|	001, 002, ..., 366|
| %-j|	Day of the year as a decimal number.|	1, 2, ..., 366|
| %U|	Week number of the year (Sunday as the first day of the week). |	00, 01, ..., 53|
| %W|	Week number of the year (Monday as the first day of the week). |	00, 01, ..., 53|
| %c|	Locale’s appropriate date and time representation.|	Mon Sep 30 07:06:05 2013|
| %x|	Locale’s appropriate date representation.|	09/30/13|
| %X|	Locale’s appropriate time representation.|	07:06:05|
| %%|	A literal '%' character.|	%|

```python
# calculating with datetimes
dt1 = datetime(2025, 9, 8, 9, 43, 30, 500)
dt2 = datetime(2025, 9, 9, 10, 43, 30, 500)
duration = dt2 - dt1                            # duration between dt1 and dt2 as a timedelta type
duration.days                                   # access number of days in duration
duration.seconds                                # access number of seconds in duration
```

```python
# datetime in pandas
date = pd.to_datetime('8th of September, 2025')         # create date as pandas timestamp type
pd.date_range(start=date, periods=10, freq='D')         # create range of certain number ('periods') of dates (freq='D' in days)
```


## __Helpful References__

- ds-pandas-numpy/06_combine_dataframes.ipynb
- ds-pandas-numpy/07_numpy.ipynb
- ds-pandas-numpy/08_numpy_pratice.ipynb
- ds-pandas-numpy/09_pandas_practice_4.ipynb
- ds-pandas-numpy/10_datetime.ipynb
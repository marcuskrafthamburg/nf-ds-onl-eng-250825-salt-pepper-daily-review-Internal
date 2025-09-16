# Day 16 — 15.09.2025
---
> **Disclaimer:** Claude AI was used to format the raw classroom notes to a polished format.

## __Basic Overview__
- What is Exploratory Data Analysis (EDA)?  
- What questions should we ask before starting EDA?
- Exercise: How to clean data
---
## __Schedule__
| Time        | Content                                         |
| ----------- | ----------------------------------------------- |
| 09:00–09:45 | Daily Review + Lunchbreak Discussion            |
| 10:00–11:00 | Data Cleaning & Exploratory Data Analysis (EDA) |
| 11:00–11:10 | Coffee Break                                    |
| 11:10–12:00 | Data Cleaning & Exploratory Data Analysis (EDA) |
| 12:00–13:30 | Lunch Break                                     |
| 13:30–14:00 | Exercise Introduction & Group Split             |
| 14:00–16:00 | Exercise Time                                   |
| 16:00–16:30 | Standup                                         |
| 16:30–End   | Exercise Time                                   |
---

# Exploratory Data Analysis (EDA)

## What is EDA?
**Detective work for data** - the process of summarizing and visualizing important characteristics of data to gain insights.

- **Goal**: Understand your data before formal modeling
- **Purpose**: Confirm the expected or show the unexpected
- **Approach**: Any method of looking at data that doesn't include formal statistical modeling

## The EDA Process

### 1. Ask Research Questions as Hypotheses
- Start with business/research questions
- Generate testable hypotheses in "if/then" or "the more the..." format
- Example: "If the sun shines, then ice cream sales increase"

### 2. Talk to Domain Experts
*"The hardest thing is to find a black cat in a dark room, especially if there is no cat"*
- Become a domain expert or consult one
- Essential questions: What do you want to find? Who are your customers? Why do you need analysis?

## Types of EDA

### By Variables
- **Univariate**: Analysis of single variables (distribution, central tendency)
- **Multivariate**: Analysis of relationships between variables

### By Method
- **Graphical**: Visual representations (histograms, scatter plots, box plots)
- **Non-graphical**: Statistical summaries (mean, median, correlations)

### By Data Type
- **Numerical**: Continuous measurements
- **Categorical**: Discrete categories (nominal, ordinal)

## Key Statistical Measures

### Central Tendency
- **Mean**: Sum ÷ count (sensitive to outliers)
- **Median**: Middle value when sorted (robust to outliers)
- **Mode**: Most frequent value (best for categorical data)

### Spread/Dispersion
- **Range**: Max - Min (sensitive to outliers)
- **Interquartile Range (IQR)**: 75th - 25th percentile (robust)
- **Variance**: Average squared difference from mean
- **Standard Deviation**: √variance (same units as data)

### Distribution Shape
- **Skewness**: Degree of asymmetry
- **Kurtosis**: Degree of "pointyness" vs normal distribution
- **Modality**: Number of peaks (unimodal, bimodal, multimodal)

## Data Types & Examples

### Numerical Data
- **Discrete**: Counts of people, events
- **Continuous**: Height, temperature, sales

### Categorical Data
- **Nominal**: Country, color (no order)
- **Ordinal**: Clothing sizes S/M/L (ordered)

## Visualization Tools

### Univariate
- **Histograms**: Show distribution shape (bin width matters!)
- **Box plots**: Show quartiles, median, outliers
- **Bar charts**: For categorical data

### Multivariate
- **Scatter plots**: Relationships between two numerical variables
- **Correlation matrices**: All pairwise correlations
- **Cross-tabulation tables**: Categorical variable relationships

## Correlation Analysis

### Pearson's r
- Measures **linear** relationships (-1 to +1)
- Close to 1: Strong positive linear relationship
- Close to 0: No linear relationship
- Close to -1: Strong negative linear relationship

### Spearman's ρ (rho)
- Measures **monotonic** relationships (based on ranks)
- Better for non-linear but monotonic relationships

### Important Warnings
- Correlation ≠ Causation
- Visual examination cannot be replaced by correlation coefficients
- Zero correlation doesn't mean independence

## Practical Guidelines

### Histogram Bin Selection
**Rule of thumb**: √(sample size) = number of bins
- Too few bins → lose detail
- Too many bins → too much noise

### Outlier Detection
- There is no general definition of an outlier
- Example: Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR ([Tukey's Fences](https://en.wikipedia.org/wiki/Outlier#Tukey's_fences))
- Context matters: outliers might be errors OR valuable insights

### For Categorical Data
- **Frequency tables**: Count occurrences
- **Expected values**: Weighted averages for decision-making
- **Cross-tabulation**: Relationships between categorical variables

## Common Data Distributions
- **Normal**: Bell curve (most continuous variables)
- **Uniform**: All values equally likely (dice roll)
- **Binomial**: Discrete version of normal (coin flips)
- **Poisson**: Events in time/space (website visits)
- **Exponential**: Time between events

## EDA Workflow Summary

1. **Understand the problem** and generate hypotheses
2. **Examine each variable individually** (univariate analysis)
3. **Explore relationships** between variables (multivariate analysis)
4. **Identify patterns, outliers, and anomalies**
5. **Validate or refine hypotheses**
6. **Decide on next steps** for modeling/analysis

## Key Takeaways

- EDA is **exploratory**, not confirmatory
- Always **visualize your data** - numbers alone aren't enough
- **Question everything** - unusual patterns might reveal insights
- **Domain knowledge** is crucial for meaningful interpretation
- EDA informs **data cleaning**, **feature engineering**, and **model selection**  

---

### Useful Resources  
- [Intro to EDA (GeeksforGeeks)](https://www.geeksforgeeks.org/exploratory-data-analysis-in-python/)  
- [Pearson vs Spearman Correlation (YouTube)](https://www.youtube.com/watch?v=6uu4sFl1avE)  
- [Color-blind-friendly plotting library (cblind)](https://pypi.org/project/cblind/)  
- [EDA Case Study – Titanic Dataset (Kaggle Notebook)](https://www.kaggle.com/code/startupsci/titanic-data-science-solutions)  

---

# __Exercise Summary__

## Groups of the Day
- **Room 1**: Irene Polgar, Dizzy Englmaier, Vinayak Betageri, Moritz Jaksch 
- **Room 2**: Maryam Rutner, Marcus Kraft, Timo Wolf, Ya-Chi Hsiao  
- **Room 3**: Pedro Miguel, Atefeh Pflüger, Karl Rackwitz, Chavely Albert Fernandez  
- **Room 4**: Yaxin Tang, Arash Ghandi, Stephanie Behrens, Mert Asaroglu, Gunar Kachel  
- **Room 5**: Diane Tuma, Siri Amanda Natalie Rääf, Tim Dannenfeld, Maria Sokotushchenko, Apostolos Koumparos  

---

## Data Cleaning: Step-by-Step

**Rule of thumb:** Start simple. Fix the obvious (names, types, duplicates) before tackling missing data. Each pass can be more detailed, but avoid overcomplicating.  

1. **Initial inspection**  
   - Load raw data with pandas.  
   - Use `.head()`, `.tail()`, `.info()`, `.describe()`.  
   - Look for: odd column names, missing values, duplicates, inconsistent units/types, outliers.  

2. **Fix column names & formats**  
   - Standardize: lowercase, underscores instead of spaces.  
   - Rename unclear or unnamed columns.  

3. **Remove duplicates**  
   - Detect with `.duplicated().sum()`.  
   - Drop using `.drop_duplicates()` + reset index.  

4. **Correct data types**  
   - Convert strings of dates to `datetime` where relevant.  
   - Clean numeric-like strings (e.g., `74 F`) into `int/float`.  
   - Optional: Standardize fields as `string` instead of `object` where appropriate.

5. **Handle unit inconsistencies**  
   - Detect mismatches (e.g., °F vs °C).  
   - Convert into a consistent unit.  

6. **Clean categorical values**  
   - Map inconsistent labels (e.g., "Rain", "r.", "R").  
   - Decide how to handle ambiguous codes.

7. **Address missing data**  
   - Identify with `df.isna().sum()` or visualizations.  
   - Choose a strategy:  
     - Drop rows/columns (safe if <10% missing).
     - Impute:
       - Flag values (e.g., `"MISSING"`, `-999`).  
       - Mean/median/mode.  
       - Forward/backward fill for time series.  
       - Interpolation for continuous data.  
       - Data Prediction (advanced, not yet implemented).  

8. **Transform & round values**  
   - Round floats where extra precision is irrelevant.  

9.  **Document your steps**  
    - Maintain a cleaning log with actions and justifications.  
    - Helps with reproducibility and collaboration.   

10. **Open Questions**
       - How to decide what is an outlier?
         - especially when it's not an extreme numerical value?
       - How to deal with outliers?

> A different useful tutorial to EDA can be found here: [Intro to EDA)](https://ideal-adventure-6vymekm.pages.github.io/sessions/07_Intro_EDA.html)
___

## Useful links for the Exercises:

1. [fillna Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)
2. [dropna Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
3. [interpolate Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html)
4. [copy Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html)

> Note: for neither of these methods it is actually neccessary to create a copy of the dataframe as described in the exercise. They all return a new instance of the dataframe UNLESS you call them with the `inplace=True` option. (e.g. `df_weather.dropna(inplace=True)` <- this will alter your original data)
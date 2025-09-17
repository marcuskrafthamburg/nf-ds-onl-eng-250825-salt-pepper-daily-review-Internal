# Day 15, 12.09.2025


##  __Basic Overview__
 

*  Visualization Lib Environment setup
*  Introduction to Visualization
*  Tried sketching a plot manually
*  Group exercise on Visualization
*  Supported a question on SQL subqueries

---
##  __Schedule__

|Time|Content|
|---|---|
|09:00 - 10:00|Daily Review|
|10:00 - 12:10|Lecture (Tereza) - Visualization|
|12:10 - 13:10|Lunch Break| 
|13:10 - 16:30|Group Work - Visualization|
|16:30 - 17:30|Extra session (Maxi) - Subqueries (SQL)|

---
##  __Daily Review__ 

* Daily Review of Day_14
* The report should push to the main branch directly. The notes-taker for the following day should be assigned as pull-approver.
* Environment setup: Link to Repo: https://github.com/neuefische/ds-vizualization_libs-intro 

---
##  __Lecture 1.part__ 
* Lecture Repo Link: https://github.com/neuefische/ds-vizualization_libs-intro


* Introduction to plotting with pandas, Matplotlib and Seaborn
    * *Matplotlib* - the core plotting library in Python  
        like a toolbox that lets you draw anything: line charts, scatter plots, bar charts, histograms, but have to specify lots of details yourself  

    * *Seaborn* - built on top of Matplotlib  
    it makes statistical plots easier and prettier  
        
* Warm-up exercise with the penguin dataset

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    # may or may not need this depending on your matplotlib version
    #%matplotlib inline
    import seaborn as sns
    ```
    1. Load data into a notebook in a dataframe

    ```python
    df = pd.read_csv("./data/penguins_clean.csv")
    df
    ```


    2.  Inspect data: 
        * what columns do we have?
        ```python
        df.head()
        ```
        * what types?
        ```python
        df.info()
        ```
        * are there missing values?
        ```python
        df.isna().count()
        ```


    3. Drop all rows with any missing values  
        ```python
        type(df.isna().sum())
        ```


    
* plotting with matplotlib
    * 3.1 create an empty figure
        ```python
        fig, ax = plt.subplots()
            ax.plot([1, 2, 3, 4],'o-r')
            plt.title('Simple example')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
        plt.show()
        ```
    * 3.2 adding data to axes of a figure  
        ```python
        # line plot
        fig, ax = plt.subplots()
        ax.plot(df['body_mass_g'])
        plt.show()
        ```

        - choose one type of plots, which can best answer the question
        ```python
        # Example: Scatter plot for Question: Do bigger penguins have longer flippers?

        fig, ax = plt.subplots(figsize= (10,5))
        ax.scatter(
            x=df.body_mass_g,
            y=df.flipper_length_mm)
        plt.show()
        ```
    * 3.3 configuring a plot  
        ```python
        # create a new plot
        fig, ax = plt.subplots(figsize = (10,5))

        # adding data to axes-x & y
        ax.scatter(
            x=df.body_mass_g,
            y=df.flipper_length_mm)

        # adding a title to the plot
        ax.set_title(
            label="Penguins FLipper Length VS Body Mass",
            fontsize = 24)

        # adding a title to axes-x
        ax.set_xlabel(
            xlabel="Body Mass in grams",
            fontsize = 16)

        # adding a title to axes-y
        ax.set_ylabel(
            ylabel="FLipper Length in mm",
            fontsize=16,
        # rotation=0,
            #loc=
            )

        # check available styles of our figures
        plt.style.available

        # give command to use the chosen style  
        plt.style.use("seaborn-v0_8")
        df
        ```  
  

   
    * 3.4 subplot  
        Q: What is the distribution of body mass for both males and females?  

        -> To visualize this question, we could either create one plot with transparent figures or one subplot.  

  
        * One plot with transparent figures by using the parameter "alpha"  
        alpha - can range from 0.0(completely transparent) to 1.0 (full opaque)
        ```python
        fig, ax = plt.subplots(figsize = (10,6))

        ax.hist(df_female.body_mass_g, bins=10, label='Female',alpha=0.4)
        ax.hist(df_male.body_mass_g, bins=10, label='male', alpha=0.5)


        ax.set_xlabel('Body Mass (g)', fontsize=14)
        ax.set_title('Distribution of Body Mass for Female and Male Penguins', fontsize=16)
        ax.legend(fontsize=15)
        plt.show()
        ```

        * Subplot  
        syntax:  
        fig, ax = plt.subplots(nrows=2,ncols=1, figsize=(8,6))  
        plt.show()
        

        ```python
        # create a subplot
        fig, (ax0,ax1) = plt.subplots(2,1, figsize=(8,8))

        # female axis (color hotpink, label)
        ax0.hist(df_female.body_mass_g, bins=10, label='Female',)
        ax0.legend()

        # male axis (color teal, label)
        ax1.hist(df_male.body_mass_g, bins=10, label='male', color="hotpink")
        ax1.set_xlabel('Body Mass (g)', fontsize=14)
        ax1.legend()


        fig.suptitle('Distribution of Body Mass for Female and Male Penguins', fontsize=15)

        plt.show()
        ````




---
##  __Practice - sketch a plot__
* Datasets link: https://github.com/neuefische/ds-group-work/tree/sketch/sketch-datasets

* Description of the task: every student picks one of table from the datasets and sketch a plot with a pan on a paper without using computer in 15 min. 

* Outputs from students link: https://discord.com/channels/1327196356191981662/1414515344692744295/threads/1415977600970391674

---
##   __Lecture 2.part__

* 3.5 More comparative plots
    * Compared penguin body mass across islands using boxplots.
    * Explored bill length vs. bill depth with scatterplots, split by species.  

* Plotting with Seaborn  
    * Replotted scatterplots with Seaborn (hue, palette, size) and customized style/themes.
    * Created faceted subplots by island/sex with relplot.
    * Used catplot (box/bar) to compare body mass across islands, adding breakdown by sex and error bars.
    * Generated pairplots for multivariate overview by species.






---
##   __Group Work - Visualization__

Repo Link: https://github.com/neuefische/ds-visualisation-group-work/tree/main

Environment Setup Link: https://github.com/neuefische/ds-visualisation-group-work/blob/main/README.md

* Task:   

    * Work in groups to compare four plotting libraries: Matplotlib, Seaborn, Plotly, Altair.

    * Each group produces one notebook that: imports the libraries, uses the assigned plot type and dataset from the table. 

* Group assignments  
Group 1: Scatterplot — Seattle Weather  
Group 2: Lineplot — Seattle Weather  
Group 3: Barchart — Seattle Weather  
Group 4: Geographical maps — Airports (focus on Plotly & Altair first)


---
##   __Helpful References__
* Matplotlib galery - more examples of different kinds of plots with code   
https://matplotlib.org/stable/gallery/index.html  
* Great youtube tutorial on matplotlib:  
https://www.youtube.com/watch?v=wB9C0Mz9gSo

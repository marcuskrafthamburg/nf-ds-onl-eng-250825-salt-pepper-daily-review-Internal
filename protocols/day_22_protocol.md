# Day 22, 22.09.2025

Linear Regression


---
##  __Basic Overview__
 

*  linear regression theoretical intro
*  implementation in pandas
*  first model training

---
##  __Schedule__

|Time|Content|
|---|---|
|10:00 - 11:30|First theoretical inputs|
|11:30 - 12:30|Other theoretical inputs|
|12:30 - 13:30|Lunch Break| 
|13:30 - 15:00|Practical exercises|
|15:00 - 17:00|Exercises and Ending|

---
##  __First Content Notes__ 

✅ Linear regression (βs enter linearly):
y = β0 + β1·x
y = β0 + β1·x + β2·x²
y = β0 + β1·log(x)

❌ Not linear regression (βs enter nonlinearly):
y = β0 + x^β1        (β in exponent)
y = β0 + (β1)²·x     (β squared → nonlinear in β)

So: a quadratic curve in x can still be linear regression. 
In linear regression, "linear" means linear in the coefficients (β).
We treat all functions of x (like x, x², log(x), …) as fixed terms, and only the βs are the free parameters.

So a model like
y = β0 + β1·x + β2·x²
is still linear regression: the βs enter linearly, even though the slope
dy/dx = β1 + 2β2·x
is not constant.

---
## __Markdown Formatting__ 

* you make a heading with \#, one for a level one heading, which is the largest - you can go down to level 6
* starting a new line: use a double space
* use single asterisks or underscores to make words italic (\*words* makes *words*) 
* use double asterisks or underscores to make words bold (\*\*this** makes **this**)
* use both at the same time with three asterisks or hyphens (\_\_\_ x ___ makes ___x___)
* you make a divider with three hyphens (---)
* you can make unordered lists with an asterisk (*) and ordered list with any number, a period and a space: \1.  
(__super useful__: it doesn't matter which number you choose, it will be displayed as 1,2, etc. )

---

## __Links, Quotes, Pictures and GIFs__

* you can use links in your notes by using this formatting:  
[link text](link URL “title”) becomes [neue fische website](https://www.neuefische.de/ "neue fische website")
* you can also use pictures in your notes by using this format:   
![image text](image URL) becomes ![neue fische logo](https://www.neuefische.de/neuefische-gmbh-logo.svg)
* block quotes: you can highlight a quote from someone by using an angle bracket (>), for example: 
    > I think there is a world market for maybe five computers. - Thomas J. Watson Sr.
* use GIFs with the same formatting as links and pictures, the URL you use must end with .gif and if it expires, your gif will not be seen anymore  
example: 
![Another Gif](https://www.crumplab.com/rstatsforpsych/imgs/regression_squares.gif)
![Fish Gif](https://miro.medium.com/v2/resize:fit:640/format:webp/1*nhGPRU12caIw7NK5Rr3p-w.gif)


---
##  __Taking Good Notes__ 

* stick to one style, e.g. links are in italic, keywords are in bold, dividers inbetween topics, etc.  
* don't vary your text style too much, keep it simple
* use bold and italic words rarely so they stand out more

---

##  __Code inside notes__ 
You can insert blocks of code into your notes with Markdown by wrapping the code in backticks (\`)
\`/from x import y\` becomes  
`/from x import y`

---
##  __Helpful References__
* [pre-preppers](https://docs.google.com/presentation/d/1a7cdrUL_-Reg-myKLcfaBgx_ReR2efUf/edit?slide=id.p1#slide=id.p1)
* [Slides](https://ideal-adventure-6vymekm.pages.github.io/sessions/08_Linear_Regression.html#)
* [Markdown Cheatsheet on Github](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 
* [Guide to Markdown for Documentation Writers](https://document360.com/blog/introductory-guide-to-markdown-for-documentation-writers/#p8)
* [Markdown Crash Course by Traversy Media](https://www.youtube.com/watch?v=HUBNt18RFbo)
* [Basic Markdown Introduction and Syntax by Mike Dane](https://www.youtube.com/watch?v=2JE66WFpaII)

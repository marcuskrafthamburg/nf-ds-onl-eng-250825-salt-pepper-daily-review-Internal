# Day 08, 03.09.2025

The day was divided into 2 parts: the career Training in the morning and Python functions lesson in the afternoon.


---
## __Basic Overview__
 

* Career Training
* Python function lesson
* more practice with python

---
##  __Schedule__

|Time|Content|
|---|---|
|09:00 - 11:30|Career Training|
|11:30 - 13:00|Lunch Break| 
|13:00 - 13:40|Python functions lesson|
|13:40 - 17:00|Exercises and Ending|

---
## __Career Training Notes__ 

* The career training is time for the students to work on their CV, prepare for interviews and figure out some job searching strategies 
* coach Renate recommends to define a smart goal for the next 2 hours
* Take one of the 9 targets on the wheel of readiness like LinkedIn Profile, Transferable Skill Awareness, Target Role Clarity, Update CV etc.
* At career compass you can’t skip modules

---

## __Python lesson notes__
### __Organisation__

* W3 School was again mentioned as learning platform, link is in the discord
* [Python tutorial on W3](https://www.w3schools.com/python/) 
* Cohorts were merged so that the students are better able to support each other and for networking reasons
* Questions can always be asked in the ‚ask-the-coaches‘ discord channel so everybody can see and answer the question
*  or can be discussed during the daily review

### __Python list comprehension and functions__
* List comprehension:
    * Comprehension = Compress loop statements
    * for example we can reduce this statement
    ```
    list_were_building = []
    for thing in iterable:
        list_were_building.append(transform(thing))
    ```
    to this statement
    ```
    list_were_building = [transform(thing) for thing in iterable]
    ```
    * can be also applied to dictionaries and tuples


* Functions

    * Declare order of instructions
    * Functions are Reusable
    * More flexible code
    * Reduces number of lines of code
    * basic construction:
    ```
    def my_func():
        pass # This pass just acts as a filler right now.
    ```
    * starts with the 'def' keyword, followed by a space and the name of the function
    * in parenthesis you can add arguments
    * don't forget the colon at the end
    * in the next line indent the block of code that defines the body of the function
    * Explaining the get_evens function example:
    ```
    def get_evens(): 
        evens = []
        for element in range(10): 
            if element % 2 == 0: 
                evens.append(element)                
    ```
    * Functions can have default values or can be called with arguments
    ```
    def get_multiples(n=5, divisor=2): 
    ```

    * There are positional arguments and keyword arguments (can be mixed, but default values always at last positions)
    ```
    positional arguments
    get_multiples(5, 2)

    keyword arguments
    get_multiples(n=5, divisor=2)

    correct mix
    get_multiples(5, divisor=2)
    ```


---

## __Helpful References__
* [Python tutorial on functions](https://www.w3schools.com/python/python_functions.asp) 



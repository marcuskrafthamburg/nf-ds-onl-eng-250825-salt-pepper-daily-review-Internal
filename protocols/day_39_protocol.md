# Day 39, 27.10.2025
On this day we learned about **Unit Testing and Integrationtests**, which helps the developer to build better software with less errors.

---
## __Basic Overview__ 
- Unit tests
- Integrationtests

---
##  __Schedule__

|Time|Content|
|---|---|
|09:30 - 10:00|Daily Review (CNN)|
|10:00 - 10:56|Testing|
|11:00 - 13:00|Lunch Break| 
|13:00 - 17:00|Practical exercises|

---
## __Why do we need to test our Code__
Nobody is perfect. Writing tests for your code helps you to make sure that it works in all cases. Even if you change your code from time to time it helps to find dependencies you may have forgotten. And it prevents you from deploying incorrectly software.

---
## __What types of tests do exist?__

* Unit tests
* Integration tests

## __Unit Tests__
An unit test tests the smallest encapsulated unit of an application: a single method or function. It should tell you the expected behavior of a function. Keep the test simple and only test its functionality.

**Requirements for unit tests**  
   - Must be able to run alone  
   - The order of the tests should not matter
   - Use descriptive names for testing functions

**Unit test example**  
```python
def test_divide():
    assert divide(3,2) == 1.5
    assert divide(5,5) == 1
    assert divide(6,2) == 3
    assert divide(-2,0) == "Can not divide by zero"
    assert divide(10,-2) == -5
```
- the assert keyword tells python to check if the following statement is true


**Unit testing libraries**  
→ unittest: Comes as standard library with python

→ doctest: Comes as standard library with python

→ pytest: The most used testing library

**Running pytest from terminal / console**
```python
python -m pytest -q tests/test_something.py
```

  
## __Integration tests__

To check the overall functionality of an application from the very first input to the end, for user input and frontend to backend communication. It should check if all dependencies inside the application are valid and that all modules / units can communicate with each other. Tests if the application logic is valid.

**Requirements for integration tests**  
- integrating the various modules of an application
- testing their behaviour as a combined, or integrated, unit
- Verifying if the individual units are communicating with each other properly
- dummy programms can be used for missing modules

## __Test driven development - TDD__
Means writing the test first and afterwards the function / unit. This helps you to think about the possible input parameters, edge cases and everything that could go wrong in your unit. Therefore you already have that in mind when you code your unit.

**Phases of TDD**
- **Red Phase** - write the test or tests to validate the functionality
- **Green Phase** - implement the simplest code that will make the failed test pass
- **Refactor Phase** - improve the code without changing the functionality

## __Typical edge cases (in Data Science)__
→ NaN and None as input values

→ 0 values and empty strings

→ Minimum and maximum values

→ numbers that have special meaning in the function (e.g. constants)

→ Invalid inputs (e.g. int vs float, str vs number)

→ Negative numbers

---
## __Helpful References__
* Lecture slides:\
https://ideal-adventure-6vymekm.pages.github.io/sessions/14_Testing.html

# Day 07, 02.09.2025
On this day we continued with the discussion about python basics, specifically about **Looping** and **Data Structures** (lists, tuples, sets and dictionaries). Additionally, we continued working on the exercises.

---
## <span style="color:black"> __Basic Overview__ </span>
- Looping in Python
- Data Structures in Python
  - lists
  - tuples
  - sets
  - dictionaries
- Mutability of python structures

---
##  __Schedule__

|Time|Content|
|---|---|
|09:00 - 10:00|Daily Review|
|10:00 - 11:05|Discussion about Python Basics: Looping, Lists, Sets, Mutability and Dictionaries|
|11:05 - 11:30|Git pull request|
|12:30 - 13:30|Lunch Break| 
|13:30 - 17:00|Practical exercises|

---
## <span style="color:black"> __Looping in Python__ </span>
* **while** loops

  Do a task **while** a condition is met 

  ```python
  while <condition>:
      task
  ```


* **for** loops

  Repeat a task for every element in an iterable (like a list, range, or string)
  ```python
  for <elements> in <iterable>:
      task
  ```


---
## <span style="color:black"> __Data Structures in Python__ </span>

* **lists**: collections of ordered items
  ```python
  my_list = [element1, element2, element3, ...] or 
  my_list = list(element1, element2, element3, ...)
  ```

    * <span style="color:red">! </span>[ ] square brackets are important

    * elements can be of any type (strings, integers, floats, etc)

* **tuples**: immutable collections of ordered items

  ```python
  my_tuples = (item1, item2, item3, ...) or 
  my_tuples = tuple([item1, item2, item3, ...])
  ```

    * <span style="color:red">! </span>( ) parenthesis are important 

    **Ordered**: Items have a defined order.

   **Immutable**: You cannot add or remove items after creation.

* **sets**: unordered, mutable collection of unique items

  **Unordered**: Items do not have a defined order. You cannot access them by index.

  **Unique items**: Duplicate items are automatically removed.

  **Mutable**: You can add or remove items after creation.

  ```python
   my_set = {1, 2, 3} or my_set = set([1, 2, 3])
   ```

    * <span style="color:red">! </span>{ } brackets are important 

* **dictionaries**: store a value associated with a keyword

  ```python
  my_dict = {<key1>: <value1>, <key2>: <value2>, ...}
  ```


---
## <span style="color:black"> __Mutability: mutable and immutable python structures__ </span> 

* Immutable: Cannot be changed after creation. Any modification creates a new object.
  * int, float, complex, str, tuples

* Mutable: can be changed after creation (elements can be added, removed, or modified)
  * lists, sets, dictionaries (keys are immutable)
---

## <span style="color:black"> __Git pull request__ </span> 
After going into the directory where we are working and making changes to a file:

- Create an switch to own branch

`git switch -c <brach_name>`

- Add the file you modified to the git repository

`git  add <file_name>`

- Make a comment about the changes

`git commit -m "<message>"`

- Push current local branch to remote repository (Github)
  - if first time 

  `git push --set-upstream origin <branch_name>`

  or alternatively, in a shorter version:

  `git push -u origin <branch_name>`

  - if not

  `git push`

- Go to your branch in the Github repository and a message like this will appear in green: "See comments and pull request". 

  -Select , add comments about the changes, can add reviewers.  
  -The reviewers receive a notification and can add a review on the file with the options of **comment, approve or request changes**.

- When a final version is agreed, the branch can be deleted remotely and locally to keep only the main branch.  
  - To remove locally:  
  `git branch -d <branch_name>`

  




---
## <span style="color:black"> __Helpful References__
* Basics/4_Loops.ipynb
* Data_Structures_in_Python/1_Lists.ipynb
* Data_Structures_in_Python/2_Sets.ipynb
* Data_Structures_in_Python/3_Mutability.ipynb
* Data_Structures_in_Python/4_Dictionaries.ipynb
* [Git Cheat Sheet](https://discord.com/channels/1327196356191981662/1408355040741167224/1412366569287323728)

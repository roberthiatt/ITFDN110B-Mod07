# Module 7: Pickling and Structured Error Handling
Developer: Robert Hiatt <br/>
Date: 3/2/2021

## Introduction
Hello and welcome to my page where I will review Python concepts such as _pickling_ and _structured error handling_.

## What Is Pickling?
_Pickling_ takes its name from the process of food preservation. The word "pickle" is [Dutch](https://www.etymonline.com/word/pickle#:~:text=pickle%20(n.)%20c.%201400,%20%22spiced%20sauce%20served%20with,which%20are%20of%20uncertain%20origin%20or%20original%20meaning.) and it means "brine," but before I get too carried away with the history of pickling foods, suffice it to say that the concept refers to storing. 

In [technical terms](https://www.geeksforgeeks.org/pickle-python-object-serialization/), _pickling_ means the process whereby a Python object hierarchy is converted into a byte stream.

In less technical terms, pickling is a means by which to store, serialize, and refer to data. The concept works similarly to a _dictionary_. Here's an [example](https://pythonbasics.org/pickle/):

<img src = "https://github.com/roberthiatt/ITFDN110B-Mod07/blob/main/docs/Serialize.PNG" width = "500">

## Structured Error Handling
_Structured Error Handling_ is a formal way to state that your program can obviate certain errors that would normally halt a program, and your program is able to complete its job _despite_ any potential errors.

Here is a nice visual of what I mean:

<img src = "https://files.realpython.com/media/try_except_else_finally.a7fac6c36c55.png" width = "500">

In this image you can see the underpinning logic to _try_ the script, _except_ for certain circumstances, _else_ take a different action, and _finally_ complete your program.

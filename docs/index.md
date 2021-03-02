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

In this image you can see the underpinning logic to search for certain errors, with particular messages to the user in place should an error present itself; otherwise, you'll run the program to its completion.

## Writing a Program with Pickling and Structured Error Handling
To start my program, I have to import the _Pickle_ module. Then I initialize my variables.
<img width="539" alt="ImportPickle" src="https://user-images.githubusercontent.com/60247240/109703552-73786b00-7b4a-11eb-9672-5d48af5b2f61.PNG">

Next, I introduce my program to the user.
<img width="718" alt="Intro" src="https://user-images.githubusercontent.com/60247240/109703747-afabcb80-7b4a-11eb-8e6c-c2ee8cbf073d.PNG">

If the user has already started a file, I want to display the file's contents. Otherwise, I tell the user to start pickling!
<img width="578" alt="ErrorHandling_1" src="https://user-images.githubusercontent.com/60247240/109703975-f13c7680-7b4a-11eb-9ae6-3270e92807cd.PNG">

Now let's let the user create/manage their data. We use a conditional _while_ loop that perpetuates unless the user enters the keyword 'leave.' Note the use of the _try_ stateme<img width="607" alt="Dump" src="https://user-images.githubusercontent.com/60247240/109704612-a66f2e80-7b4b-11eb-9776-be14d4a4087b.PNG">
nt with the _else_ clause. If the user does not adhere to the choices provided, the program provides a sly reminder to stick to the script. 

Next we'll pickle the user entries, utilizing the _dump_ pickle function to save the information to the binary file. Prior to exiting the program, we recapitulate the stored data to the user. 
<img width="631" alt="Loop1" src="https://user-images.githubusercontent.com/60247240/109704268-42e50100-7b4b-11eb-962a-9f6e000dc978.PNG">

## Summary
This exercise provides a great understanding of pickling, how to write structured error handling, and I’ve also created a GitHub page that more fully delves into using the markdown language known as Jekyll. Regarding the GitHub page, I embedded images and also used hyperlinks to cite research sources.


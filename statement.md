Project Statement: Simple Python CLI To-Do List

This document defines the core purpose and boundaries of the Simple Python CLI To-Do List application.

● Problem Statement

Individuals need a lightweight, accessible, and persistent tool to track personal or professional tasks without relying on complex, resource-heavy software or continuous internet connectivity. A simple, file-based command-line interface application is needed to offer core task management functionality quickly and efficiently using standard, portable file types.

● Scope of the Project

The scope of this project is strictly limited to a single-user, local, Command Line Interface (CLI) application.

In Scope

--Core CRUD operations (Create, Read, Update, Delete): specifically Add, View, Mark Done, and Delete tasks.

--Local file persistence using plain text (.txt) for saving and loading data.

--Minimal dependencies: The project uses only the Python standard library.

--Basic error handling: Includes checks for invalid index numbers or choices.

Out of Scope

--Network synchronization or multi-user support.

--Rich Graphical User Interface (GUI).

--Advanced features such as reminders, scheduling, or priority levels.

--Data encryption or complex security features.

● Target Users

The primary target users for this application are:

--Python Beginners: Students and new programmers solidifying their understanding of Python fundamentals (functions, lists, file I/O, control flow).

--CLI Enthusiasts: Users who prefer interacting with tools via the terminal for speed and efficiency.

--Developers/Casual Users: Individuals who require a quick, no-fuss logging tool for local task tracking.

● High-Level Features

These are the primary capabilities the application provides:

--Task Addition: Allow the user to input text that is added to the list as a new "To Do" item.

--Task Viewing: Display the entire list of tasks, clearly showing the index number and current completion status.

--Status Marking: Enable the user to toggle a task's status between "To Do" ([ ]) and "Done" ([x]).

--Task Deletion: Permanently remove a selected task from the list.

--Local Persistence: Automatically save the entire state of the list to the local todo_list.txt file after any modification.

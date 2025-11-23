# ToDoList-Manager
A simple, file-based Command Line Interface (CLI) To-Do List application written in pure Python for Evaluated Course Project. Tasks persist across sessions using a plain text file.
📝 Python To-Do List Manager

🌟 Overview

This is an easy-to-use beginner-oriented Command Line Interface (CLI) tool designed to handle a to-do list. The program is developed entirely in Python. Relies on a simple text file (todo_list.txt), for storage ensuring your tasks remain saved after exiting the application.

This is a project to practice fundamental Python skills such, as functions, loops, working with strings and managing files.

✨ Features

Insert Tasks: Rapidly add entries to your list.

View Tasks: Show every task along, with its index number and current status ([ ] or [x]).

Mark as Done: Easily change a task's status from [ ] (To Do) to [x] (Done).

Delete Tasks: Remove completed or unwanted tasks from the list permanently.

Persistence: Every modification is saved automatically to todo_list.txt.

🛠️ Prerequisites

To execute this program having Python installed on your computer is all that’s required.

Python 3.x (Check your version by running python --version or python3 --version)

🚀 Installation and Setup

Since this is a single-file application, setup is very simple.

Clone the Repository (or Download the File):

git clone [YOUR_REPOSITORY_URL]

cd [YOUR_REPOSITORY_NAME]

Verify the File Presence: Confirm that the todo_cli.py file is located in your working directory.

💻 Usage

To start the application, navigate to the project directory in your terminal or command prompt and run the following command:

python todo_cli.py

Main Menu Options

When the application launches the menu will appear:

===================================

PYTHON SIMPLE TO-DO LIST (CLI)

===================================

1. Add a New Task

2. View All Tasks

3. Mark Task as Done

4. Delete a Task

5. Exit Application

Enter your choice (1-5):

1 (Add): Prompts you for the description of the new task.

3 & 4 (Mark Done / Delete): Initially these choices display the existing list then prompt you to enter the task number (index) you intend to change.

5 (Exit): Terminates the application. Guarantees that all data is preserved.

Data Storage

The program automatically. Handles a file called todo_list.txt within the identical folder where you execute the script. This document keeps your tasks with each task, on its line featuring the [ ] or [x] status indicator.

🤝 Contributing

Feel free to suggest improvements or new features!

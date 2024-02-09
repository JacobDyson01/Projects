# Task Manager

**Task Manager** is a console-based application written in Python that allows users to manage their tasks effectively.

## Features

- **Add tasks** with titles and descriptions.
- **Update existing tasks' descriptions**.
- **Delete tasks**.
- **View all tasks**.

## Installation

1. **Clone the repository**:

git clone https://github.com/yourusername/task-manager.git

markdown


2. **Navigate to the project directory**:

cd task-manager

markdown


3. **Run the application**:

python task_manager.py

markdown


## Usage

1. Upon launching the application, follow the on-screen prompts to perform various actions:
- To **add a new task**, enter `ADD:task_title` and then provide the task description when prompted.
- To **update an existing task's description**, enter `UPDATE:task_title` and then provide the new task description when prompted.
- To **delete a task**, enter `DELETE:task_title`.
- To **view all tasks**, enter `VIEW`.
- To **quit the application**, enter `QUIT`.

2. Task titles and descriptions should not contain colons (`:`).

## Example

Welcome
How can I help?: ADD:Do laundry

Enter task description: Wash clothes and fold them neatly.

Task 'Do laundry' added successfully.

How can I help?: VIEW

Task: Do laundry, Description: Wash clothes and fold them neatly.

How can I help?: UPDATE:Do laundry

Enter new task description: Wash clothes, fold them neatly, and put them away.

Task 'Do laundry' updated successfully.

How can I help?: DELETE:Do laundry

Task 'Do laundry' deleted successfully.

How can I help?: QUIT
GoodBye

## Author

**Jacob Dyson** ((https://github.com/jacobdyson01))

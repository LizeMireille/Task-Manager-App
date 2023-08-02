# Task-Manager-App
 A Python program for a small business to manage tasks assigned to each team member. The program allows users to log in, add tasks, view all tasks, and view tasks assigned to them. The admin user has additional features like user registration and generating reports on task and user statistics. 

## Features
* User Login: The program allows users to log in once they have provided their username and password. Invalid credentials will prompt the user to re-enter until correct ones are provided.
* User Registration (Admin only): New users can be registered by the admin user. Upon registration the password of the newly registered user must be confirmed to ensure accuracy.
* Adding Tasks: Users can add tasks by providing details, including the username of the person the task is assigned to, task title, description, and due date. The current date is automatically used as the task assignment date.
* Viewing All Tasks: All tasks can be viewed including the task numbers, usernames, titles, descriptions, assignment dates, due dates, and completion status.
* Viewing Assigned Tasks: Users can view tasks assigned to them. 
* Editing Tasks: Users can edit a specific task assigned to them, either marking it as complete or modifying the assigned user or due date. 
* Generating Reports (Admin only): The admin user can generate two reports: task_overview.txt and user_overview.txt. These reports provide various statistics on tasks and users, such as the total number of tasks, completed tasks, uncompleted tasks, overdue tasks, and percentages of task completion.

## How to Use
1. Clone the repository to your local computer (with Python installed).
2. Run the Task Manager App.py script in your Python environment.
3. When running the application, the application will prompt you to enter a username and password.
4. Following successful login, the main menu will be displayed, offering various options for user interactions.

#### This application was developed based on the task instructions from HyperionDev, a software training institute. It encompasses one of their capstone tasks from the provided syllabus. 


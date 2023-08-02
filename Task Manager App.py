#=====importing libraries===========
from datetime import datetime
DATETIME_STRING_FORMAT = "%d %b %Y"
import os

#====Functions====
def reg_user():
    if user_username != "admin":
        print("You are not an admin user. Only admin can register new users.")
    else:
        new_username = input("Please enter the new username: \n")
        while new_username in users:
            print("This user is already registered. Please try again!")
            new_username = input("Please enter the new username: \n")

        new_password = input("Please enter the new matching password: \n")
        password_confirm = input("Please confirm the new password: \n")

        while new_password != password_confirm:
            print("Your password does not match the confirmation.")
            new_password = input("Please enter the new matching password: \n")
            password_confirm = input("Please confirm the new password: \n")

        with open("user.txt", 'a') as user_file:
            user_file.write(f"\n{new_username}, {new_password}")

def add_task():
    username_of_assigned = input("Please enter the username of the person the task is assigned to: \n")
    while username_of_assigned not in users:
        print("The username is incorrect.")
        username_of_assigned = input("Please enter a valid username: \n")

    task_title = input("Enter the title of the task: \n")
    task_description = input("Enter a task description: \n")

    while True:
        due_date_str = input("Please enter the due date in the format 'DD MMM YYYY' (e.g. '10 Feb 2023'): ")
        try:
            due_date = datetime.strptime(due_date_str, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Error: the date was not in the correct format. Please try again.")

    today = datetime.today()
    date_string = today.strftime("%d %b %Y")

    with open("tasks.txt", 'a') as task_file:
        task_file.write(f"\n{username_of_assigned}, {task_title}, {task_description}, {due_date}, {date_string}, No")

def view_all():
    num_task = 0
    with open("tasks.txt", 'r') as task:
        for line in task:
            data = line.split(", ")
            num_task += 1
            print(f"""
Task number:        {num_task}
Username:           {data[0]}
Task title:         {data[1]}
Task description:   {data[2]}
Date assigned:      {data[3]}
Due date:           {data[4]}
Task complete?      {data[5].strip()}
""")

def view_mine():
    num_task = 0
    with open("tasks.txt", 'r') as task:
        lines = task.readlines()
        for line in lines:
            data = line.split(", ")
            num_task += 1
            if user_username.strip() == data[0]:
                print(f"""
Task number:        {num_task}
Username:           {data[0]}
Task title:         {data[1]}
Task description:   {data[2]}
Date assigned:      {data[3]}
Due date:           {data[4]}
Task complete?      {data[5].strip()}
""")

def view_stats():
    if user_username != "admin":
        print("You are not an admin user. Only admin can display statistics.")
    else:
        if not os.path.isfile('task_overview.txt') or not os.path.isfile('user_overview.txt'):
            gen_report()

        with open('task_overview.txt', 'r') as task_file:
            task_stats = task_file.read()
            print("Task Overview:\n")
            print(task_stats)

        with open('user_overview.txt', 'r') as user_file:
            user_stats = user_file.read()
            print("User Overview:\n")
            print(user_stats)

def gen_report():
    with open('user.txt', 'r') as user_file:
        users_data = [line.strip().split(',') for line in user_file.readlines()]

    with open('tasks.txt', 'r') as task_file:
        tasks_data = [line.strip().split(',') for line in task_file.readlines()]

    today = datetime.today()
    date_string = today.strftime("%d %b %Y")

    total_tasks = len(tasks_data)
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    for task in tasks_data:
        if task[5].strip().lower() == 'yes':
            completed_tasks += 1
        elif task[5].strip().lower() == 'no':
            uncompleted_tasks += 1
            if datetime.strptime(task[4].strip(), DATETIME_STRING_FORMAT) <= today:
                overdue_tasks += 1

    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100

    with open('task_overview.txt', 'w') as task_file:
        task_file.write(f'''
Task Overview Report ({date_string})

Total tasks:                {total_tasks}
Total completed tasks:      {completed_tasks}
Total uncompleted tasks:    {uncompleted_tasks}
Total overdue tasks:        {overdue_tasks}
Uncompleted tasks (%):      {incomplete_percentage:.2f}%
Overdue tasks (%):          {overdue_percentage:.2f}%
''')

    total_users = len(users_data)
    user_overview_data = []

    for user in users_data:
        total_assigned_tasks = 0
        completed_user_tasks = 0
        uncompleted_user_tasks = 0
        overdue_user_tasks = 0

        for task in tasks_data:
            if task[0] == user[0]:
                total_assigned_tasks += 1
                if task[5].strip().lower() == 'yes':
                    completed_user_tasks += 1
                elif task[5].strip().lower() == 'no':
                    uncompleted_user_tasks += 1
                    if datetime.strptime(task[4].strip(), DATETIME_STRING_FORMAT) <= today:
                        overdue_user_tasks += 1

        assigned_percentage = (total_assigned_tasks / total_tasks) * 100 if total_tasks != 0 else 0
        completed_percentage = (completed_user_tasks / total_assigned_tasks) * 100 if total_assigned_tasks != 0 else 0
        uncompleted_percentage = (uncompleted_user_tasks / total_assigned_tasks) * 100 if total_assigned_tasks != 0 else 0
        overdue_percentage_user = (overdue_user_tasks / total_assigned_tasks) * 100 if total_assigned_tasks != 0 else 0

        user_overview_data.append(f''' 
Total registered tasks for user {user[0]}:   {total_assigned_tasks}
Amount assigned to user of total tasks (%): {assigned_percentage:.2f}%
Completed user tasks (%):                  {completed_percentage:.2f}%
Uncompleted user tasks (%):                {uncompleted_percentage:.2f}%
Overdue user tasks (%):                    {overdue_percentage_user:.2f}%
''')

    with open('user_overview.txt', 'w') as user_file:
        user_file.write(f'''
Total registered users: {total_users}
Total registered tasks: {total_tasks}

User Overview:
{''.join(user_overview_data)}
''')

#====Login Section====
users = {}
with open("user.txt", 'r') as user_file:
    for line in user_file:
        username, password = line.split(", ")
        users[username.strip()] = password.strip()

user_username = input("Please enter your username: \n")
while user_username not in users:
    print("The username is incorrect.")
    user_username = input("Please enter a valid username: \n")

user_password = input("Please enter your password: \n")
while user_password != users[user_username]:
    print("Your username is correct but your password is incorrect.")
    user_password = input("Please enter a valid password: ")

while True:
    menu = input('''Please select one of the following options:
r  - Registering a user 
a  - Adding a task
va - View all tasks
vm - View my tasks
gr - Generate reports
s  - Display statistics
e  - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 's':
        view_stats()

    elif menu == 'gr':
        gen_report()
        print("""The files 'task_overview.txt' and 'user_overview.txt' containing statistical reports of 
        the task_manager users are now available.""")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made an invalid selection. Please Try again!")
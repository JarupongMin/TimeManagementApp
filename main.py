import sys
from os import system

# Function to display the main menu
def display_main_menu():
    print("\nWelcome To Time-Management Application!")
    print("\nMain Menu:")
    print("1. Create Task")
    print("2. Create Long-Term Goal")
    print("3. Display Tasks")
    print("4. Display Long-Term Goals")
    print("5. Exit")

# Function to create a task
def create_task():
    print("\nCreating a new task:")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (DD-MM-YYYY): ")
    priority = input("Enter priority (High, Medium, Low): ")

    # Check if all required information is provided
    if title and description and due_date and priority:
        new_task = Task(title, description, due_date, priority)
        tasks.append(new_task)
        print("Task created successfully!")
    else:
        print("Invalid input. Please provide all required information.")

# Function to create a long-term goal
def create_long_term_goal():
    print("\nCreating a new long-term goal:")
    title = input("Enter goal title: ")
    milestones = input("Enter milestones (comma-separated): ").split(',')
    deadline = input("Enter deadline (DD-MM-YYYY): ")

    # Check if all required information is provided
    if title and milestones and deadline:
        new_goal = LongTermGoal(title, milestones, deadline)
        long_term_goals.append(new_goal)
        print("Long-term goal created successfully!")
    else:
        print("Invalid input. Please provide all required information.")

# Function to display all created tasks
def display_tasks():
    print("\nCurrent Tasks:")
    for task in tasks:
        print(f"- {task.title} (Due: {task.due_date}, Priority: {task.priority})")

# Function to display all created long-term goals
def display_long_term_goals():
    print("\nCurrent Long-Term Goals:")
    for goal in long_term_goals:
        print(f"- {goal.title} (Deadline: {goal.deadline})")
        print(f"  Milestones: {', '.join(goal.milestones)}")

# Function to exit the program
def exit_program():
    system('cls')  # clears stdout
    print("Goodbye")
    sys.exit()

# Class to represent a single Task
class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

# Class to represent a Long-Term Goal
class LongTermGoal:
    def __init__(self, title, milestones, deadline):
        self.title = title
        self.milestones = milestones
        self.deadline = deadline

# Main program logic
tasks = []  # List to store tasks
long_term_goals = []  # List to store long-term goals

while True:
    # Display the main menu
    display_main_menu()

    # Get user selection
    selection = int(input("Please enter your selection number: "))

    # Handle user selection
    if selection == 1:
        create_task()  # Call function to create a task
    elif selection == 2:
        create_long_term_goal()  # Call function to create a long-term goal
    elif selection == 3:
        display_tasks()  # Call function to display tasks
    elif selection == 4:
        display_long_term_goals()  # Call function to display long-term goals
    elif selection == 5:
        exit_program()  # Call function to exit the program
    else:
        print("Invalid selection. Please enter a number between 1 and 5.")

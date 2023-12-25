# Time Management App

## Introduction

Welcome to the Time Management App, a command-line tool designed to help users organize their tasks and set and track long-term goals efficiently.

## Purpose

The purpose of this application is to enable users to manage their daily tasks, set and monitor long-term goals, and maintain a record of completed activities. The app operates entirely in the terminal, providing a straightforward and efficient way to enhance productivity.

## Style Guide

The codebase for this project adheres to the style guide outlined is in python. 

## Project Features

### Task Management
- Users can create tasks with titles, descriptions, due dates, and priorities.
- Individual tasks can be managed, edited, and deleted.
- Collaboration features enable team members to work on tasks together.

### Long-Term Goal Setting
- Users can set and track long-term goals.
- Goals come with milestones and deadlines.
- Progress analysis with visual representations helps users adjust goals as needed.

### Logging Completed Tasks
- Maintain a log of completed tasks and activities for reference.

## Implementation Plan
The implementation plan is divided into key features, each with specific tasks and deadlines. The plan is tracked using a project management platform, ensuring a systematic and organized development process.

## Attribution
This project draws inspiration from discussions within the development community and insights shared by peers on platforms such as Discord. Special thanks to CallumW and Simon for their valuable input during the project approval phase.

---
**Note:** Screenshots and detailed implementation plans are available in the `docs` folder. Please refer to the project documentation for a comprehensive overview

R3 Provide full attribution to referenced sources (where applicable).
<!-- 

edstem.org. (n.d.). Ed Discussion. [online] Available at: https://edstem.org/au/courses/13988/lessons/43347/slides/297106.

Stack Overflow. (n.d.). How to create a menu system for a console, terminal application. [online] Available at: https://stackoverflow.com/questions/71943877/how-to-create-a-menu-system-for-a-console-terminal-application [Accessed 25 Dec. 2023].

Meyer, I. (n.d.). simple-term-menu: A Python package which creates simple interactive menus on the command line. [online] PyPI. Available at: https://pypi.org/project/simple-term-menu/ [Accessed 25 Dec. 2023].

‌www.tutorialsteacher.com. (n.d.). Python - if, else, elif conditions (With Examples). [online] Available at: https://www.tutorialsteacher.com/python/python-if-elif.

‌Stack Overflow. (n.d.). How to increment datetime by custom months in python without using library. [online] Available at: https://stackoverflow.com/questions/4130922/how-to-increment-datetime-by-custom-months-in-python-without-using-library. 

edstem.org. (n.d.). Ed Discussion. [online] Available at: https://edstem.org/au/courses/13988/lessons/43345/slides/297095 [Accessed 25 Dec. 2023].

‌

-->

‌
‌
‌

R4
Provide a link to your source control repository


<!-- 

git@github.com:JarupongMin/TimeManagementApp.git  

-->

R5	
Identify any code style guide or styling conventions that the application will adhere to.

Reference the chosen style guide appropriately.

<!-- 

I will adhere to the PEP 8 style guide for Python. PEP 8 provides a comprehensive set of guidelines for writing clean and readable code in Python. Following this style guide ensures consistency across our codebase, making it easier for team members to collaborate and maintain the code in the long run.

 -->


R6	Develop a list of features that will be included in the application. It must include:
- at least THREE features
- describe each feature

Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:
- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

Consult with your educator to check your features are sufficient .

<!-- 
Task Management:

Description: Users can create tasks with titles, descriptions, due dates, and priorities.
Implementation Details: Utilizes variables to store task information. Uses loops for input validation and conditional control structures to manage task creation. Implements error handling to ensure valid input.
Task Editing and Deletion:

Description: Users can manage, edit, and delete tasks individually.
Implementation Details: Involves variables to identify tasks, loops for user interaction, and conditional control structures for editing or deleting tasks. Incorporates error handling to manage unexpected scenarios.
Long-Term Goal Tracking:

Description: Users can set and track long-term goals with milestones and deadlines.
Implementation Details: Uses variables to store goal details. Implements loops for milestone input and conditional control structures for goal tracking. Incorporates error handling to handle goal-setting errors.
These features encompass the creation, management, and analysis of tasks and long-term goals, demonstrating the use of variables, loops, conditional control structures, and error handling as requested. Additionally, visual representations will be implemented in the terminal as approved, providing a simple yet effective interface for users. 
-->



R7	
Develop an implementation plan which:
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images that demonstrates your usage of a project management platform used to track this implementation plan. 


> Your checklists for each feature should have at least 5 items.

<!-- 

Task Creation:

- Implement function to collect user input for task details.
- Validate input and create a Task object.
- Integrate task creation into the main program logic.
- Add error handling for invalid inputs.
- Test task creation functionality.

Task Editing:

- Implement function to edit existing tasks.
- Identify tasks using a unique identifier.
- Allow users to modify task details.
- Add error handling for non-existent tasks.
- Test task editing functionality.

Task Deletion:

- Implement function to delete tasks.
- Prompt users for task identification.
- Confirm deletion with the user.
- Add error handling for non-existent tasks.
- Test task deletion functionality.

Task Display:

- Implement function to display all created tasks.
- Ensure proper formatting and details.
- Integrate into the main program menu.
- Test task display functionality.

Task Priority Handling:

- Add priority attribute to Task class.
- Implement logic to handle task priorities.
- Test priority handling in different scenarios.
- Update display and other functions to consider priority.

Deadline:

- Task Management Features: 2 weeks
- Feature 2: Long-Term Goal Tracking

Goal Creation:

- Implement function to collect user input for goal details.
- Validate input and create a LongTermGoal object.
- Integrate goal creation into the main program logic.
- Add error handling for invalid inputs.
- Test goal creation functionality.

Goal Tracking:

- Implement function to track progress on long-term goals.
- Include logic for updating milestones.
- Integrate goal tracking into the main program menu.
- Test goal tracking functionality.

Milestone Tracking:

- Implement milestone tracking within long-term goals.
- Allow users to update milestones.
- Consider visual representation of milestones.
- Test milestone tracking functionality.

Deadline Handling:

- Add deadline attribute to LongTermGoal class.
- Implement logic to handle goal deadlines.
- Test deadline handling in different scenarios.
- Update display and other functions to consider deadlines.

Goal Display:

- Implement function to display all created long-term goals.
- Ensure proper formatting and details.
- Integrate into the main program menu.
- Test goal display functionality.

Deadline:

- Long-Term Goal Tracking Features: 2 weeks
- Feature 3: User Interface

Main Menu Design:

- Design a clear and user-friendly main menu.
- Add options for each feature.
- Consider aesthetics and readability.
- Test menu navigation.

Input Validation:

- Implement robust input validation for user inputs.
- Handle edge cases and invalid entries gracefully.
- Test input validation in various scenarios.

Visual Representation:

- Plan and implement a simple visual representation.
- Consider ASCII art or other terminal-friendly graphics.
- Ensure it doesn't compromise the user experience.
- Test visual representation in the terminal.

User-Friendly Interaction:

- Implement features with user-friendly prompts.
- Ensure clear instructions and guidance.
- Test user interaction for each feature.

Error Handling:

- Implement comprehensive error handling mechanisms.
- Capture and manage unexpected scenarios gracefully.
- Test error handling for different user inputs.

 -->


R8	
Design help documentation which includes a set of instructions which accurately describe how to use and install the application.

You must include:
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application

<!-- # Time Management Application Help Documentation

Welcome to the Time Management Application! This guide provides instructions on how to install, configure, and use the application effectively.

## Installation

Users must have python3 installed to run your app and need to be on Mac or linux

In terminal: 
      ```
      chmod +x run.sh
      ```
      ```
      bash run.sh
      ```
           


1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Run the following command to clone the repository:
     ```
     git clone [repository_url]
     ```

2. **Navigate to the Application Directory:**
   - Change your current directory to the application folder:
     ```
     cd time-management-app
     ```

3. **Install Dependencies:**
   - Ensure you have Python installed.
   - Install required dependencies using the following command:
     ```
     pip install -r requirements.txt
     ```

## Application Setup

4. **Run the Application:**
   - Execute the following command to start the application:
     ```
     python main.py
     ```

5. **Main Menu:**
   - The main menu presents options to create tasks, set long-term goals, display tasks and goals, and exit the application.

6. **Creating Tasks:**
   - Choose option 1 and follow the prompts to create a new task, providing the title, description, due date, and priority.

7. **Creating Long-Term Goals:**
   - Select option 2 and enter details for a new long-term goal, including the title, milestones (comma-separated), and deadline.

8. **Displaying Tasks and Goals:**
   - Options 3 and 4 allow you to view existing tasks and long-term goals, respectively.

9. **Exiting the Application:**
   - Choose option 5 to exit the application.

## Command Line Arguments

The application supports the following command line arguments:

- `-h` or `--help`: Display the help message and exit.

## System Requirements

- Python3
- Internet connectivity for cloning the repository and installing dependencies.

Feel free to reach out if you encounter any issues or have questions. Thank you for using the Time Management Application! -->


Slide deck
You must present your Terminal application and its code - which will form the basis of a professional report.

The presentation and associated Slide deck should include,

Present your Terminal application to the class. You must provide a walk-through of the logic of your application and how the application is used.

A walk-through of your Terminal application, its features and how it used
A walk-through of the logic of your Terminal application and code
A review of your development/build process including challenges, ethical issues, favourite parts, etc
Make sure to incorporate the following into your presentation Slide deck,

No.	Slides must include…	You must explain…
R9	An overview of your Terminal application	The main features and overall structure of your app
R10	An overview of your code	An explanation of the important parts of your code, including any crucial application logic
PRESENTATION REQUIREMENTS
Your presentation must:

be no longer than 10 minutes (or the time limit specified by your Educators)
utilise the submitted Slide deck
be recorded and uploaded to a video hosting platform (YouTube, Vimeo, etc.)
CODE REQUIREMENTS
No.	Requirement
R11	Implement features in the software development plan you have designed. You must utilise a range of programming concepts and structures using Python such as:
- variables and variable scope
- loops and conditional control structures
- write and utilise simple functions
- error handling
- input and output
- importing a Python package
- using functions from a Python package
R12	Apply DRY (Don’t Repeat Yourself) coding principles to all code produced.
R13	Apply all style and conventions for the programming language consistently to all code produced.
R14	Creates an application which runs without error and has features that are consistent with the development plan.
R15	Design TWO tests which check that the application is running as expected.

Each test should:
- cover a different feature of the application
- state what is being tested
- provide at least TWO test cases and the expected results for each test case

> An outline of the testing procedure and cases should be included with the source code of the application
R16	Utilise source control throughout the development of the application by:
- making regular commits (at least 20 commits) with a commit message that summarises the changes
- pushing all commits to a remote repository
R17	Utilise developer tools to facilitate the execution of the application:
For example,
- writing a script which turns the application into an executable
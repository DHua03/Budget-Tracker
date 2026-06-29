# Budget Tracking Application
A command-line budget tracking system built with Python and SQLite that allows users to manage financial categories, track transactions, and analyze spending behavior through structured reporting.

## Overview
This application provides a simple but functional budgeting system where users can create categories, record transactions, and track spending over time. It uses a moduar architecture with persistent data storage to simulate a lightweight personal finance manager.

## Features
* Create and manage budget categories
* Record deposits, withdrawals, and transfers between catagories
* Validate funds before transactions
* Persistent transaction storage using SQLite
* Real-time balance calculations per category
* Spending summary reports by category
* Text-based bar chart visualization of spending distribution

## Tech Stack
* Python
* SQLite
* Object-Oriented Programming (OOP)
* Command-Line Interface (CLI)

## Project Structure
Budget_Tracker\
│\
├── main.py              # CLI entry point (user interface)\
├── category.py          # Core business logic (Category class)\
├── database.py          # SQLite database operations\
├── budget.db            # Local database file (excluded from Git)\
├── .gitignore\
└── README.md

## Installations
Make sure Python 3.10+ is installed on system
### 1. Clone Repository
git clone https://github.com/DHua03/Budget-Tracker.git
### Navigate into project directory
cd Budget_Tracker
### Run Application
python main.py

## What I learned
* Object-oriented programming in Python
* Designing modular applications with seperation of concerns
* Working with SQLite for persistent data storage
* Implementing CRUD operations (Create, Read, Update, Delete)
* Building CLI-based user interfaces
* Structuring real-world Python projects

## Inspiration
This project was initially inspired by the FreeCodeCamp "Budget App" python certification project.
It was extended into a fully functional CLI application with SQLite persistence, modular design, and enhanced reporting features.

## Future Improvements
* Load categories dynamically from database on startup
* Add monthly budgeting and spending limits per category
* Add graphical user interface (GUI)

## Author
Dylan Hua\
Computer Science Graduate | Software Engineer\
Github: https://github.com/DHua03

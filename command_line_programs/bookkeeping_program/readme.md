# Bookkeeping Software for Home Services

This project is a comprehensive bookkeeping software solution designed for home service businesses. It allows you to manage users, clients, services, invoices, and expenses effectively. The software is built using Python, SQLAlchemy for ORM (Object-Relational Mapping), and SQLite as the database.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Running the Code from VS Code on Mac](#running-the-code-from-vs-code-on-mac)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Management**: Create, update, and delete users.
- **Client Management**: Manage client information and service history.
- **Service Tracking**: Track and manage services provided to clients.
- **Invoicing**: Create, update, and delete invoices.
- **Expense Management**: Log and manage business expenses.
- **Data Backup and Restore**: Backup and restore system data securely.
- **Security**: Hash passwords and verify user credentials securely.

## Installation

### Prerequisites

1. **Python 3.8+**: Ensure you have Python installed. You can check your Python version by running:

    ```bash
    python3 --version
    ```

2. **pip**: Python package manager should be installed by default with Python. Verify by running:

    ```bash
    pip --version
    ```

3. **VS Code**: Install Visual Studio Code, a popular code editor, from [here](https://code.visualstudio.com/).

### Step-by-Step Installation

1. **Clone the Repository**

    Open the Terminal on your Mac and run the following command to clone the repository:

    ```bash
    git clone https://github.com/yourusername/bookkeeping-software.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd bookkeeping-software
    ```

3. **Create a Virtual Environment**

    It is recommended to use a virtual environment to manage dependencies. Run the following commands:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    This will create and activate a virtual environment named `venv`.

4. **Install Required Dependencies**

    Install the dependencies listed in the `requirements.txt` file using pip:

    ```bash
    pip install -r requirements.txt
    ```

    If the `requirements.txt` file is not provided, install SQLAlchemy manually:

    ```bash
    pip install sqlalchemy
    ```

## Configuration

### Database Configuration

The software uses SQLite as its database. The database file (`home_services.db`) will be created automatically in the project root directory.

### Setting Up the Database

1. **Create Database Tables**

    Run the Python script that initializes the database tables. This script uses SQLAlchemy to create the necessary tables:

    ```bash
    python3 src/models/user.py
    ```

    Repeat this for all other models (`client.py`, `service.py`, `invoice.py`, `expense.py`):

    ```bash
    python3 src/models/client.py
    python3 src/models/service.py
    python3 src/models/invoice.py
    python3 src/models/expense.py
    ```

## Usage

### Running the Program

You can run individual Python scripts to interact with the program:

1. **Start the Application**

    To start the application, run any of the view scripts. For example, to manage users:

    ```bash
    python3 src/views/user_view.py
    ```

2. **Using the Command-Line Interface**

    Follow the on-screen prompts to create, update, delete, or view records for users, clients, services, invoices, and expenses.

### Running Unit Tests

To ensure all components are working correctly, run the unit tests:

```bash
python3 -m unittest discover tests/


bookkeeping-software/
│
├── src/
│   ├── models/
│   │   ├── user.py
│   │   ├── client.py
│   │   ├── service.py
│   │   ├── invoice.py
│   │   └── expense.py
│   │
│   ├── controllers/
│   │   ├── user_controller.py
│   │   ├── client_controller.py
│   │   ├── service_controller.py
│   │   ├── invoice_controller.py
│   │   └── expense_controller.py
│   │
│   ├── views/
│   │   ├── user_view.py
│   │   ├── client_view.py
│   │   ├── service_view.py
│   │   ├── invoice_view.py
│   │   └── expense_view.py
│   │
│   └── utils/
│       ├── data_backup.py
│       ├── data_restore.py
│       └── security.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── tests/
│   ├── test_user.py
│   ├── test_client.py
│   ├── test_service.py
│   ├── test_invoice.py
│   └── test_expense.py
│
└── README.md

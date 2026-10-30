# Python Nexus 🐍

Python Nexus is a comprehensive utility suite designed to demonstrate core Python programming concepts through three essential tools: a Banking System, a Contact Directory, and a Mathematical Engine.

While the project includes a premium Retro-OS frontend, the **primary core of this project is the Python backend logic**, implemented using standard libraries to ensure maximum compatibility and efficiency.

## 🚀 Core Python Modules

The heartbeat of the project resides in three independent Python scripts. Each is designed to be run directly from the CLI.

### 1. ATM Banking System (`atmbank.py`)
A secure ledger implementation for financial transactions.
- **Key Logic**: Global state management for balance, input validation for deposits/withdrawals, and a menu-driven interface.
- **Functions**:
  - `check_balance()`: Retrieves current account state.
  - `deposit(amount)`: Validates and adds funds to the ledger.
  - `withdraw(amount)`: Implements overdraft protection and fund deduction.

### 2. Contact Directory (`contactbook.py`)
A dictionary-backed directory for managing personal contacts.
- **Key Logic**: Utilizes Python dictionaries for $O(1)$ search complexity, implementing full CRUD (Create, Read, Update, Delete) operations.
- **Functions**:
  - `add_contact()`: Validates phone numbers (10-digit constraint) and adds entries.
  - `search_contact()`: Performs key-based lookups in the directory.
  - `update_contact()`: Modifies existing entries with validation.
  - `delete_contact()`: Removes entries from the data structure.
  - `view_contacts()`: Iterates through the dictionary to display all records.

### 3. Precision Calculator (`calculator.py`)
An arithmetic computation engine.
- **Key Logic**: Implements a state-based calculation loop with a zero-division guard to prevent system crashes.
- **Core Capabilities**: Addition, Subtraction, Multiplication, and Division.

---

## 🖥️ Frontend Presentation Layer

To surface the Python logic in a modern way, the project includes a **Retro-OS Frontend** (`frontend/index.html`).

- **Purpose**: This file serves as the **output display**. It mirrors the exact logic, function names, and menu options of the Python scripts using JavaScript.
- **Design**: Minimalist "Total Black & Neon Orange" aesthetic with CRT scanlines, 8-bit typography, and animated technical outlines.
- **Role**: The HTML is a presentation shell; the logic it executes is a direct mirror of the `.py` source files.

## 🛠️ Execution Guide

### Running the Backend (Primary)
To run the core logic, use the Python interpreter:
```bash
python atmbank.py
python contactbook.py
python calculator.py
```

### Viewing the Frontend (Output)
Open the following file in any modern web browser:
`frontend/index.html`

## ⚙️ Technical Stack
- **Language**: Python 3.x (Backend)
- **UI**: HTML5, CSS3 (Tailwind), JavaScript (Frontend Mirror)
- **Fonts**: Press Start 2P, JetBrains Mono

# Python Nexus 🐍

A high-performance utility suite implementing core computational and data-management logic in Python, presented through a premium Retro-OS interface.

**Author:** [Puneeth](https://github.com/SMNpuneeth)
**Repository:** [https://github.com/SMNpuneeth/-PYTHON-PY-Functions.git](https://github.com/SMNpuneeth/-PYTHON-PY-Functions.git)

---

## 🧠 Core Python Architecture (70%)

The primary objective of this project is the implementation of robust, efficient, and scalable Python logic. The system is divided into three specialized modules, each focusing on different aspects of the Python standard library.

### 1. Banking Core (`atmbank.py`)
This module implements a secure financial ledger. It focuses on **state management** and **input validation** to ensure data integrity.
- **Technical Implementation**: Uses global state variables to track account balances across multiple function calls.
- **Key Logic**: 
    - **Validation**: Implements strict checks to prevent negative deposits or overdrafts.
    - **Flow Control**: A `while True` loop manages the session, mirroring a real-world ATM machine's operational state.
    - **Complexity**: $O(1)$ time complexity for all transaction operations.

### 2. Data Book (`contactbook.py`)
A sophisticated contact management system that demonstrates the power of **Python Dictionaries** for high-speed data retrieval.
- **Technical Implementation**: Uses a dictionary `{name: phone}` to store records, ensuring that search and deletion operations are nearly instantaneous.
- **Key Logic**:
    - **CRUD Operations**: Full implementation of Create, Read, Update, and Delete functionality.
    - **String Constraints**: Implements phone number validation using length checks and digit verification.
    - **Data Integrity**: Prevents duplicate entries by checking key existence before adding new contacts.
- **Complexity**: $O(1)$ average case for search, addition, and deletion.

### 3. Math Engine (`calculator.py`)
A precise arithmetic computation tool focusing on **error handling** and **mathematical guards**.
- **Technical Implementation**: Implements a state-based calculation loop.
- **Key Logic**:
    - **Zero-Division Guard**: Includes a critical check to prevent `ZeroDivisionError`, ensuring the system remains stable during invalid operations.
    - **Floating Point Precision**: Handles float conversions for accurate decimal calculations.

---

## 🛠️ Installation & Usage (20%)

To run this project locally, follow these steps to clone the repository and execute the modules.

### 1. Clone the Project
Use the following command to download the source code from GitHub:
```bash
git clone https://github.com/SMNpuneeth/-PYTHON-PY-Functions.git
cd -PYTHON-PY-Functions
```

### 2. Run the Python Modules
You can run any of the core utilities directly using the Python interpreter:

**For the Bank System:**
```bash
python atmbank.py
```

**For the Contact Book:**
```bash
python contactbook.py
```

**For the Calculator:**
```bash
python calculator.py
```

---

## 🖥️ Interface & Output (10%)

To provide a visual representation of the backend logic, the project includes a **Retro-OS Frontend**.

- **The Interface**: A minimalistic, mono-color (Total Black & Neon Orange) web page located at `frontend/index.html`.
- **Design Philosophy**: Built with a "Retro-Gaming" aesthetic, featuring CRT scanlines, 8-bit typography (`Press Start 2P`), and animated neon outlines.
- **Logic Mirroring**: The frontend is not a separate app; it is a **visual mirror**. Every button and input in the HTML corresponds exactly to a function and input in the Python scripts.

**How to view:** simply open `frontend/index.html` in any modern web browser.

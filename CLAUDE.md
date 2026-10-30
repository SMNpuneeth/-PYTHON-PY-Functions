# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
**Python Nexus** is a utility suite combining CLI-based Python tools with a premium, animated glassmorphic frontend.

## Architecture
- **Backend (Logic Layer)**: Independent Python scripts (`atmbank.py`, `contactbook.py`, `calculator.py`) that implement core utility logic using standard libraries.
- **Frontend (Presentation Layer)**: A single-page application located in `frontend/index.html`. 
    - **Design**: Glassmorphism, Obsidian/Indigo palette, and custom CSS animations.
    - **Logic**: The frontend mirrors the Python logic in JavaScript to provide a fully interactive web experience without modifying the original Python files.

## Common Commands
### Running Backend Logic
- Run ATM Bank: `python atmbank.py`
- Run Contact Book: `python contactbook.py`
- Run Calculator: `python calculator.py`

### Frontend Development
- View Website: Open `frontend/index.html` in a web browser.

## Development Guidelines
- **Backend Integrity**: Do NOT modify the original `.py` files unless explicitly asked to update the core logic.
- **Frontend Consistency**: When adding new apps to the Nexus, maintain the "Deep Obsidian" design tokens and glassmorphism styles defined in the CSS.
- **Logic Mirroring**: Any changes to the backend `.py` logic should be mirrored in the JavaScript within `frontend/index.html` to ensure consistency between the CLI and Web versions.
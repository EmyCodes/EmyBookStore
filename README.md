# EmyBookStore

EmyBookStore is a simple book inventory management system with a graphical user interface (GUI) built using Python and Tkinter. The application allows users to perform operations such as viewing all books, searching for specific books, adding new books, updating existing book information, and deleting books from the inventory.

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Creating Standalone Apps](#creating-standalone-apps)
- [Author](#author)
- [Contact](#contact)

## Project Structure

```bash
.
├── ./app.py
├── ./app.spec
├── ./AUTHOR
├── ./dist
│   └── ./dist/app
├── ./models
│   ├── ./models/backend.py
│   ├── ./models/__init__.py
├── ./README.md
└── ./requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/EmyCodes/EmyBookStore.git
```

2. Navigate to the project directory:

```bash
cd EmyBookStore
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Run the EmyBookStore application:

```bash
python app.py
```

### Creating Standalone Apps

#### Linux Standalone App

To create a standalone app for Linux, use the following command:

```bash
pyinstaller --onefile --windowed app.py
```

#### Windows Standalone App

For Windows, use the following command:

```bash
pyinstaller --onefile --noconsole app.py
```

The GUI will open, providing options to view, search, add, update, and delete books in the inventory.

## Author

- Full Name: Ogundare Olamide Emmanuel
- GitHub Username: [EmyCodes](https://github.com/EmyCodes)
- Twitter: [EmyCodes](https://twitter.com/EmyCodes)
- LinkedIn: [EmyCodes](https://linkedin.com/in/emycodes)

## Contact

For any inquiries or feedback, please contact [EmyCodes](ogundareolamideemmanuel@gmail.com).

```pl

This version of the README excludes the `build/` directory and `*/__pycache__/` entries from the project structure.
```
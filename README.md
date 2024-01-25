# EmyBookStore

EmyBookStore is a simple book inventory management system with a graphical user interface (GUI) built using Python and Tkinter. The application allows users to perform operations such as viewing all books, searching for specific books, adding new books, updating existing book information, and deleting books from the inventory.

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Author](#author)
- [Contact](#contact)

## Project Structure

```
.
├── AUTHOR
├── build
│   └── frontend
│       # ... (PyInstaller build artifacts)
├── dist
│   └── frontend
├── frontend.spec
├── README.md
├── requirements.txt
├── src
│   ├── backend.py
│   ├── frontend.py
│   └── __pycache__
│       └── backend.cpython-310.pyc
└── v1
    ├── AUTHOR
    ├── README.md
    └── src
        ├── backend
        │   ├── EmyBookStore.db
        │   ├── engine.py
        │   └── __init__.py
        ├── frontend
        │   ├── gui.py
        │   └── __init__.py
        └── __init__.py
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

Run the EmyBookStore application:

```bash
python src/frontend.py
```

The GUI will open, providing options to view, search, add, update, and delete books in the inventory.

## Author

- GitHub Username: EmyCodes
- Full Name: Ogundare Olamide Emmanuel
- Twitter: [@EmyCodes](https://twitter.com/EmyCodes)
- LinkedIn: [EmyCodes](https://linkedin.com/in/emycodes)

## Contact

For any inquiries or feedback, please contact [EmyCodes](https://twitter.com/EmyCodes).
# Number System Converter

A professional web application for converting between different number systems (decimal, binary, octal, and hexadecimal).

![Number System Converter](https://i.imgur.com/placeholder.png)

## Description

The Number System Converter is a Flask-based web application that allows users to convert numbers between different numeral systems. It provides a clean, professional interface for performing conversions with immediate results displayed below the input field.

### Features

- Convert between Decimal (Base-10), Binary (Base-2), Octal (Base-8), and Hexadecimal (Base-16) number systems
- Real-time input validation with helpful hints
- Professional and classical design
- Informative descriptions of each number system
- Responsive layout that works on various devices

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/PrerakPithadiya/number-system-converter.git
   cd number-system-converter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. To convert a number:
   - Select the source number system from the dropdown
   - Select the target number system from the dropdown
   - Enter the number you want to convert
   - Click the "Convert" button
   - View the result displayed below the input field

## How It Works

The application uses Python's built-in conversion functions to transform numbers between different bases:

- Decimal to Binary: `bin()`
- Decimal to Octal: `oct()`
- Decimal to Hexadecimal: `hex()`
- Other bases to Decimal: `int(number, base)`

The web interface is built with Flask, a lightweight Python web framework, and uses HTML, CSS, and JavaScript for the frontend.

## Project Structure

```
number-system-converter/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # CSS styling
└── templates/
    ├── base.html           # Base template
    ├── index.html          # Home page
    └── result.html         # Results page
```

## Number Systems Overview

- **Decimal (Base-10)**: The standard number system using digits 0-9, used in everyday mathematics and calculations.
- **Binary (Base-2)**: A number system using only digits 0 and 1, fundamental to digital computing and electronic systems.
- **Octal (Base-8)**: A number system using digits 0-7, providing a more compact representation of binary data.
- **Hexadecimal (Base-16)**: A number system using digits 0-9 and letters A-F, commonly used in programming and computer science.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Developed as a learning project for understanding number systems and web development
- Built with Flask, a micro web framework for Python

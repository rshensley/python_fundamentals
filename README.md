# Python Fundamentals — Temperature Converter
# Module 2: Assignment 1

## Overview

The program converts a temperature in Celsius to Fahrenheit, with string manipulation, input validation, exception handling, and formatted output.

## Features

- Accepts numeric Celsius temperatures with an optional `C` or `Celsius` suffix.
- Uses `strip()` and `split()` to process input.
- Uses `casefold()` for case-insensitive unit validation.
- Converts numeric strings to floating-point values using `float()`.
- Handles invalid inputs with `ValueError` and prompts the user to try again.
- Displays the converted temperature to two decimal places.

## Requirements

- Python 3.x
- No external libraries required.

## Running the Program

From the project directory, execute:

```bash
python temperature_converter.py
```

Example:

```text
Celsius to Fahrenheit Converter
Enter Celsius temperature: 25 C
25.00 °C = 77.00 °F
```

## Testing

The program was tested manually using valid and invalid inputs to verify temperature conversion, string processing, unit validation, and exception handling.

| Test Input | Expected Result | Actual Result | Status |
|---|---|---|---|
| `25` | 77.00 °F | 77.00 °F | Pass |
| `25 C` | 77.00 °F | 77.00 °F | Pass |
| `100 celsius` | 212.00 °F | 212.00 °F | Pass |
| `-40 C` | -40.00 °F | -40.00 °F | Pass |
| `25 c` | 77.00 °F | 77.00 °F | Pass |
| `25   c` | 77.00 °F | 77.00 °F | Pass |
| `34` | 93.20 °F | 93.20 °F | Pass |
| `45` | 113.00 °F | 113.00 °F | Pass |
| `35   c` | 95.00 °F | 95.00 °F | Pass |
| `abc` | Invalid numeric input | ValueError handled | Pass |
| `25 F` | Unsupported unit | ValueError handled | Pass |
| Empty input | Invalid input format | ValueError handled | Pass |
| `25c` | Invalid numeric input | ValueError handled | Pass |
| `n` and `cel` | Invalid numeric input | ValueError handled | Pass |
| `25 thousand` | Unsupported unit | ValueError handled | Pass |
| `--2` | Invalid numeric input | ValueError handled | Pass |

### Exception Handling

The program continued accepting new input after invalid entries. Multiple invalid inputs were tested before providing a valid temperature, demonstrating that exceptions are handled without terminating the program.

### Testing Environment

- Operating system: Omarchy Linux
- Python interpreter: `/usr/bin/python`
- Editor: Visual Studio Code
- Testing method: Manual execution through the terminal

## Author

Robert Seth Hensley

GitHub: [@rshensley](https://github.com/rshensley)

INFO-U762 — Interoperability

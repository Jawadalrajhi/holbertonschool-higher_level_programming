# Python – Test-Driven Development

This project introduces test-driven development (TDD) in Python.  
The goal was to write functions *guided by tests first*, using both **doctests** (inside docstrings) and **unittest** modules.

## Tests :heavy_check_mark:

All test cases are located inside the **[tests](./tests)** directory.  
Along with the files provided by Holberton School, the following custom tests were created:

- [`0-add_integer.txt`](./tests/0-add_integer.txt)
- [`2-matrix_divided.txt`](./tests/2-matrix_divided.txt)
- [`3-say_my_name.txt`](./tests/3-say_my_name.txt)
- [`4-print_square.txt`](./tests/4-print_square.txt)
- [`5-text_indentation.txt`](./tests/text_indentation.txt)
- [`6-max_integer_test.py`](./tests/6-max_integer_test.py)
- [`100-matrix_mul.txt`](./tests/100-matrix_mul.txt)
- [`101-lazy_matrix_mul.txt`](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes :floppy_disk:

| File                    | Prototype                                     |
| ----------------------- | --------------------------------------------- |
| `0-add_integer.py`      | `def add_integer(a, b=98):`                   |
| `2-matrix_divided.py`   | `def matrix_divided(matrix, div):`            |
| `3-say_my_name.py`      | `def say_my_name(first_name, last_name=""):`  |
| `4-print_square.py`     | `def print_square(size):`                     |
| `5-text_indentation.py` | `def text_indentation(text):`                 |

## Tasks :page_with_curl:

### **0. Integers addition**
* **File:** [`0-add_integer.py`](./0-add_integer.py)  
* Returns the sum of two integers.  
* Raises:
  - `TypeError` if either argument is not an integer or float.  
* Floats are cast to integers before performing the addition.

---

### **1. Divide a matrix**
* **File:** [`2-matrix_divided.py`](./2-matrix_divided.py)  
* Divides every element of a matrix by a given number.  
* Returns a new matrix with values rounded to 2 decimal places.  
* Validates:
  - Matrix must be a list of lists of integers/floats  
  - Rows must be of equal length  
  - `div` must be a number and not zero  
* Raises descriptive `TypeError` or `ZeroDivisionError` messages.

---

### **2. Say my name**
* **File:** [`3-say_my_name.py`](./3-say_my_name.py)  
* Prints a name in the format:  
  `My name is <first_name> <last_name>`  
* Raises:
  - `TypeError` if `first_name` or `last_name` is not a string.

---

### **3. Print square**
* **File:** [`4-print_square.py`](./4-print_square.py)  
* Prints a square of size `size` using the `#` symbol.  
* Raises:
  - `TypeError` if `size` is not an integer  
  - `ValueError` if `size < 0`

---

### **4. Text indentation**
* **File:** [`5-text_indentation.py`](./5-text_indentation.py)  
* Prints text with proper indentation.  
* Two newline breaks appear after `.`, `?`, or `:`  
* Input must be a string; otherwise a `TypeError` is raised.  
* Removes leading/trailing spaces from each printed line.

---

### **5. Max integer — Unittest**
* **File:** [`tests/6-max_integer_test.py`](./tests/6-max_integer_test.py)  
* A complete unittest suite for the function `max_integer(list=[])`.  
* Covers edge cases, typical lists, negative numbers, and empty inputs.

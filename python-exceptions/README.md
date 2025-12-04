# Python – Exceptions

This project focuses on understanding how Python handles runtime errors through exceptions.  
I practiced using `try`, `except`, and `finally` to write safer and more predictable programs.

## Tests :heavy_check_mark:

* All test files are available in the **[tests](./tests)** directory (provided by Holberton School).

## Function Prototypes :floppy_disk:

The functions implemented in this project follow the prototypes below:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |

## Tasks :page_with_curl:

### **0. Safe list printing**
* **File:** [`0-safe_print_list.py`](./0-safe_print_list.py)  
* Prints the first `x` elements of a list on one line.  
* Returns the actual number of printed elements.  
* Does not use `len()` or imports.

---

### **1. Safe printing of an integer**
* **File:** [`1-safe_print_integer.py`](./1-safe_print_integer.py)  
* Attempts to print a value as an integer using `"{:d}".format()`.  
* Returns `True` if successful and `False` otherwise.  
* No imports or `type()` checks.

---

### **2. Print and count integers**
* **File:** [`2-safe_print_list_integers.py`](./2-safe_print_list_integers.py)  
* Prints the first `x` elements of a list that are integers.  
* Returns the count of printed integers.  
* No imports or `len()` usage.

---

### **3. Integers division with debug**
* **File:** [`3-safe_print_division.py`](./3-safe_print_division.py)  
* Divides two integers and prints the result inside a `finally` block.  
* Returns the division result or `None` if an error occurs.  
* No imports.

---

### **4. Divide a list**
* **File:** [`4-list_division.py`](./4-list_division.py)  
* Divides elements from two lists one by one.  
* Returns a new list containing all results.  
* Handles multiple error cases:
  - `"wrong type"` → if elements are not integers/floats  
  - `"division by 0"` → if denominator is zero  
  - `"out of range"` → if either list is too short  
* No imports.

---

### **5. Raise exception**
* **File:** [`5-raise_exception.py`](./5-raise_exception.py)  
* Explicitly raises a `TypeError`.  
* No imports.

---

### **6. Raise a message**
* **File:** [`6-raise_exception_msg.py`](./6-raise_exception_msg.py)  
* Raises a `NameError` with a custom message.  
* No imports.

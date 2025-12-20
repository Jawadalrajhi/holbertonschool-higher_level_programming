# Python – Classes and Objects

In this project, I practiced object-oriented programming (OOP) in Python using
classes and objects. The goal was to understand attributes, methods, and
properties, as well as core concepts such as data abstraction, encapsulation,
and information hiding.

## Tests ✅

- **tests/**: Folder containing all test files provided by Holberton School.

## Tasks 📄

### 0. My first square
- **0-square.py**: Defines a basic `Square` class.

### 1. Square with size
- **1-square.py**: Adds:
  - A private instance attribute `size`
  - Instantiation with `size`

### 2. Size validation
- **2-square.py**:
  - Supports optional initialization: `def __init__(self, size=0)`
  - Raises:
    - `TypeError` if `size` is not an integer (`must be an integer`)
    - `ValueError` if `size` is less than 0 (`size must be >= 0`)

### 3. Area of a square
- **3-square.py**: Adds a public method `area()` that returns the square’s area.

### 4. Access and update private attribute
- **4-square.py**:
  - Getter for `size`
  - Setter for `size` with validation

### 5. Printing a square
- **5-square.py**:
  - Adds `my_print()` to print the square using `#`
  - Prints an empty line if `size == 0`

### 6. Coordinates of a square
- **6-square.py**:
  - Adds a private `position` attribute
  - Getter and setter for `position`
  - Optional initialization with `size` and `position`
  - Raises `TypeError` if `position` is not a tuple of two positive integers

### 7. Singly linked list
- **100-singly_linked_list.py**:
  - `Node` class with validated `data` and `next_node`
  - `SinglyLinkedList` class with `sorted_insert()` method

### 8. Print Square instance
- **101-square.py**:
  - Overrides `__str__` to match the output of `my_print()`

### 9. Compare 2 squares
- **102-square.py**:
  - Implements comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`)
  - Comparison is based on square area

### 10. ByteCode → Python #5
- **103-magic_class.py**:
  - Python function matching the provided bytecode exactly

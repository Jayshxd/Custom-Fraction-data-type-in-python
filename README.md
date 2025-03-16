# Fraction - A Custom Fraction Data Type in Python

Fraction is a Python library that provides a fraction data type with support for arithmetic operations, comparisons, and exponentiation.

## Features
- Addition, Subtraction, Multiplication, Division, Floor Division
- Power (`**` operator)
- Comparison Operators (`>`, `<`, `>=`, `<=`, `==`, `!=`)
- Simplifies fractions automatically
- Returns type as `<class 'Fraction'>`

---

## Installation
Clone this repository:

```sh
git clone https://github.com/yourusername/Fraction.git
```
Then, import it into your Python project:

```python
from Fraction import Fraction
```

---

## Usage

### Creating a Fraction
```
from Fraction import Fraction  

a = Fraction(3, 4)  
b = Fraction(5, 6)  
print(a)  # Output: 3/4  
print(b)  # Output: 5/6  
```

### Basic Arithmetic Operations
```
print(a + b)  # Output: 19/12
print(a - b)  # Output: -1/12
print(a * b)  # Output: 5/8
print(a / b)  # Output: 9/10
print(a // b) # Output: 0
```

### Comparisons
```
print(a > b)  # Output: False
print(a < b)  # Output: True
print(a == Fraction(6, 8))  # Output: True (Auto-simplified)
```

### Exponentiation
```
print(a ** 2)   # Output: 9/16
print(a ** -1)  # Output: 4/3 (Reciprocal)
```

### Getting Type
```
print(a.get_type())  # Output: <class 'Fraction'>

```

---

## Contributing
Contributions are welcome. Feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.


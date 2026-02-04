*This project has been created as part of the 42 curriculum by pmieres.*

# ft_printf

## Description

The **ft_printf** project consists of reimplementing the standard C function `printf`.  

This implementation reproduces the core behavior of `printf`, supporting several common format specifiers and returning the total number of characters printed.

---
## Instructions

### Compilation

To compile the library, run:

```
make
```
This will generate the `libftprintf.a` static library.

To remove object files:
```
make clean
```

To remove object files and the library:
```
make fclean
```

To recompile everything:
```
make re
```

### Usage

Include the header file in your project:

```
#include "ft_printf.h"
```
---
### Supported features

- `%c` → character

- `%s` → string

- `%d / %i` → signed integer

- `%u` → unsigned integer

- `%x` → lowercase hexadecimal

- `%X` → uppercase hexadecimal

- `%p` → pointer address

- `%%` → prints the % character

---

### Algorithm and Data Structures
Algorithm

The function parses the format string character by character:

 1. Regular characters are printed directly.

 2. When a % is encountered, the next character determines the format specifier.

 3. The corresponding handler function is called.

 4. Each handler returns the number of printed characters, which are accumulated and returned.


Data Structures

- va_list (from <stdarg.h>) to handle variable arguments safely.

- Dynamically allocated strings for number conversions (e.g., hexadecimal).

### Resources

- printf manual (man 3 printf)
- 42 subject
- Variadic functions


_This project has been done as part of the curriculum of 42 by pmieres-._

# Description

This project aims to recreate a set of standard C library functions, as well as additional utility functions. All functions are compiled into a library that can be used in other projects. A Makefile is included to manage the compilation.

# Instructions

### Build the library

To compile the library, run:
```
make
```
This will generate the `libft.a` static library.

Available Makefile rules:

```
make clean		# removes object files
make fclean		# removes object files and libft.a
make re			# recompiles the library
```

### Using the library 

Include the header file in your source code:
```
#include "libft.h"
```
Compile your program with `libft.a`:
```
gcc main.c libft.a
```

# Functions

### Part 1 - Libc functions

- ft_isalpha
- ft_isdigit
- ft_isalnum
- ft_isascii
- ft_isprint
- ft_strlen
- ft_memset
- ft_bzero
- ft_memcpy
- ft_memmove
- ft_strlcpy
- ft_strlcat
- ft_toupper
- ft_tolower
- ft_strchr
- ft_strrchr
- ft_strncmp
- ft_memchr
- ft_memcmp
- ft_strnstr
- ft_atoi
- ft_calloc
- ft_strdup

### Part 2 - Additional functions

- ft_substr
- ft_strjoin
- ft_strtrim
- ft_split
- ft_itoa
- ft_strmapi
- ft_striteri
- ft_putchar_fd
- ft_putstr_fd
- ft_putendl_fd
- ft_putnbr_fd

### Part 3 - Linked lists

- ft_lstnew
- ft_lstadd_front
- ft_lstsize
- ft_lstlast
- ft_lstadd_back
- ft_lstdelone
- ft_lstclear
- ft_lstiter
- ft_lstmap

# Resources

+ man pages
+ 42 subject
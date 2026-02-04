NAME = libftprintf.a
CC = cc

CFLAGS = -Wall -Werror -Wextra

SRC = ft_printf_char.c ft_printf_str.c ft_itoa_hex.c\
ft_printf_point.c ft_printf_hex.c ft_printf_d.c ft_printf_u.c\
ft_printf.c

OBJ =$(SRC:.c=.o)

INCLUDE = ft_printf.h libft/libft.h

AR = ar rcs
RM = rm -f

.PHONY: all clean fclean re

all: $(NAME)

$(NAME): $(OBJ)
	make -C libft
	cp libft/libft.a $(NAME)
	$(AR) $@ $^
%.o: %.c $(INCLUDE)
	$(CC) $(CFLAGS) -Ilibft -c -o $@ $<
clean:
	$(RM) $(OBJ)
	make -C libft clean
fclean: clean
	$(RM) $(NAME)
	$(MAKE) -C libft fclean
re: fclean all
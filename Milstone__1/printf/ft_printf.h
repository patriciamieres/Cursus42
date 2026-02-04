/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmieres- <pmieres-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 12:23:25 by pmieres-          #+#    #+#             */
/*   Updated: 2026/02/03 12:57:01 by pmieres-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include "libft/libft.h"
# include <stdarg.h>

int		ft_printf(char const *str, ...);
int		ft_printf_char(char c);
int		ft_printf_str(char *str);
char	*ft_itoa_hex(unsigned long n);
int		ft_printf_point(void *p);
int		ft_printf_hex(unsigned int n, char x);
int		ft_printf_d(int n);
int		ft_printf_u(unsigned int n);

#endif
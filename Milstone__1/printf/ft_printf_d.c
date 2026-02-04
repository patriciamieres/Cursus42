/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_d.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmieres- <pmieres-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 12:09:04 by pmieres-          #+#    #+#             */
/*   Updated: 2026/02/03 12:52:00 by pmieres-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf_d(int n)
{
	int		len;
	long	neg;

	len = 1;
	ft_putnbr_fd(n, 1);
	neg = n;
	if (neg < 0)
	{
		len++;
		neg = -neg;
	}
	while (neg > 9)
	{
		neg = neg / 10;
		len++;
	}
	return (len);
}

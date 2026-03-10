/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils_bonus.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmieres- <pmieres-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/04 12:04:43 by pmieres-          #+#    #+#             */
/*   Updated: 2026/02/18 11:36:00 by pmieres-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t				len;
	size_t				i;
	const unsigned char	*s;

	if (!dst || !src)
		return (0);
	s = (unsigned char *)src;
	i = -1;
	len = ft_strlen(src);
	if (size > len)
	{
		while (++i < len)
			dst[i] = s[i];
		dst[len] = '\0';
	}
	else if (size > 0)
	{
		while (++i < size - 1)
			dst[i] = s[i];
		dst[(size - 1)] = '\0';
	}
	return (len);
}

char	*ft_strdup(char *src)
{
	char	*dup;
	int		len;

	if (!src)
		return (NULL);
	len = ft_strlen(src);
	dup = malloc(sizeof(char) * (len + 1));
	if (!dup)
		return (NULL);
	ft_strlcpy(dup, src, (len + 1));
	return (dup);
}

size_t	ft_strlen(const char *str)
{
	size_t	len;

	if (!str)
		return (0);
	len = 0;
	while (str[len])
		len++;
	return (len);
}

char	*ft_strchr(const char *s, int c)
{
	size_t	i;
	size_t	len;

	if (!s)
		return (NULL);
	i = 0;
	len = ft_strlen(s) + 1;
	while (i < len)
	{
		if ((unsigned char)s[i] == (unsigned char)c)
			return ((char *)&s[i]);
		i++;
	}
	return (NULL);
}

char	*ft_strjoin(char *s1, char *s2)
{
	char	*join;
	int		i;
	int		j;

	if (!s2 && s1)
		join = ft_strdup(s1);
	else if (!s1 && s2)
		join = ft_strdup(s2);
	else if (!s2 && !s1)
		return (NULL);
	else
		join = malloc(sizeof(char) * (ft_strlen(s1) + ft_strlen(s2) + 1));
	if (!join)
		return (free_stash(s1, NULL));
	if (s1 && s2)
	{
		i = ft_strlen(s1);
		j = ft_strlen(s2);
		ft_strlcpy(join, s1, i + 1);
		ft_strlcpy(&join[i], s2, j + 1);
	}
	free_stash(s1, NULL);
	return (join);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmieres- <pmieres-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/12 16:06:58 by pmieres-          #+#    #+#             */
/*   Updated: 2026/02/18 12:05:05 by pmieres-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

char	*rest(char *stash)
{
	char	*new_stash;
	char	*nl;

	if (!stash)
		return (NULL);
	nl = ft_strchr(stash, '\n');
	if (!nl)
	{
		free(stash);
		stash = NULL;
		return (NULL);
	}
	if (*(nl + 1) == '\0')
	{
		free(stash);
		stash = NULL;
		return (NULL);
	}
	new_stash = ft_strdup(nl + 1);
	free(stash);
	stash = NULL;
	return (new_stash);
}

char	*lin(char *stash)
{
	size_t	i;
	char	*line;

	i = 0;
	if (!stash)
		return (NULL);
	while (stash[i] && stash[i] != '\n')
		i++;
	if (stash[i] == '\n')
		i++;
	line = malloc(i + 1);
	if (!line)
		return (NULL);
	i = 0;
	while (stash[i] && stash[i] != '\n')
	{
		line[i] = stash[i];
		i++;
	}
	if (stash[i] == '\n')
		line[i++] = '\n';
	line[i] = '\0';
	return (line);
}

char	*free_stash(char *stash, char *buf)
{
	if (buf)
		free(buf);
	if (stash)
		free(stash);
	return (NULL);
}

static char	*ini_stash(int fd, char *buf, char *stash)
{
	int	rd;

	rd = read(fd, buf, BUFFER_SIZE);
	if (rd == -1 || (!stash && rd == 0))
		return (free_stash(stash, buf));
	buf[rd] = '\0';
	stash = ft_strjoin(stash, buf);
	if (!stash)
		return (free_stash(NULL, buf));
	while (ft_strchr(stash, '\n') == NULL && rd > 0)
	{
		rd = read(fd, buf, BUFFER_SIZE);
		if (rd < 0)
			return (free_stash(stash, buf));
		buf[rd] = '\0';
		stash = ft_strjoin(stash, buf);
		if (!stash)
			return (free_stash(NULL, buf));
	}
	return (stash);
}

char	*get_next_line(int fd)
{
	char		*buf;
	static char	*stash[1024];
	char		*line;

	line = NULL;
	if (BUFFER_SIZE == 0 || fd == -1)
		return (NULL);
	buf = malloc(BUFFER_SIZE + 1);
	if (!buf)
	{
		stash[fd] = free_stash(stash[fd], NULL);
		return (NULL);
	}
	stash[fd] = ini_stash(fd, buf, stash[fd]);
	if (!stash[fd])
		return (stash[fd] = 0, NULL);
	line = lin(stash[fd]);
	if (!line)
	{
		stash[fd] = free_stash(stash[fd], buf);
		return (NULL);
	}
	stash[fd] = rest(stash[fd]);
	return (free(buf), line);
}

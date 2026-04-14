# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/04/14 22:55:39 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

if len(sys.argv) == 2:
    print("=== CYBER ARCHIVES RECOVERY  ===")
    file_name = sys.argv[1]
    try:
        print(f"Accessing file '{file_name}'")
        with open(file_name) as file:
            print("---\n")
            print(f"{file.read()}\n")
            print("---")
            print("File 'ancient_fragment.txt' closed")

            file.close()

    except (FileNotFoundError, PermissionError) as error:
        print(
            f"Error: opening file {file_name}: {error}")
else:
    print("Usage: ft_ancient_text.py <file>")

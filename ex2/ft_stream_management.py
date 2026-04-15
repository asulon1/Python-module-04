# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/04/15 14:04:26 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

if len(sys.argv) == 2:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    try:
        sys.stdout.write(f"Accessing file '{file_name}'")
        with open(file_name) as file:
            sys.stdout.write("---\n")
            sys.stdout.write(f"{file.read()}\n")
            sys.stdout.write("---\n")
            sys.stdout.write("\nFile 'ancient_fragment.txt' closed\n")
            file.close()

        # Get lines
        file_lines = []
        with open(file_name) as file:
            file_lines = file.readlines()
            file_lines = [line.rstrip('\n') + "#\n" for line in file_lines]
            file.close()
    except (FileNotFoundError, PermissionError) as error:
        sys.stderr.write(
            f"[STDERR] Error: opening file {file_name}: {error}")
    try:
        sys.stdout.write("\nTransform data:\n")
        sys.stdout.write("---\n")
        for data in file_lines:
            sys.stdout.write(data)
        sys.stdout.write("\n---\n")

        # Save new lines data
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_file_name = sys.stdin.readline().strip()
        if new_file_name and len(new_file_name) > 0:
            with open(new_file_name, "w") as update_file:
                sys.stdout.write(f"Saving data to {new_file_name}")
                for line in file_lines:
                    update_file.write(line)
                sys.stdout.write(f"Data saved in file {new_file_name}.")
                update_file.close()
        else:
            sys.stdout.write("Not saving data.")
    except (FileNotFoundError, PermissionError) as error:
        sys.stderr.write(
            f"[STDERR] Error: opening file {new_file_name}: {error}")
else:
    sys.stdout.write("Usage: ft_ancient_text.py <file>")

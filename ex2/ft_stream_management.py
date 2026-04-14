# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/04/15 01:04:47 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

if len(sys.argv) == 2:
    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    try:
        print(f"Accessing file '{file_name}'")
        with open(file_name) as file:
            print("---\n")
            print(f"{file.read()}\n")
            print("---")
            print("File 'ancient_fragment.txt' closed\n")
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
        print("Transform data:")
        print("---\n")
        for data in file_lines:
            print(data, end='')
        print("\n---\n")

        # Save new lines data
        new_file_name = input("Enter new file name (or empty): ")
        if new_file_name and len(new_file_name.strip()) > 0:
            with open(new_file_name, "w") as update_file:
                print(f"Saving data to {new_file_name}")
                for line in file_lines:
                    update_file.write(line)
                print(f"Data saved in file {new_file_name}.")
                update_file.close()
        else:
            print("Not saving data.")
    except (FileNotFoundError, PermissionError) as error:
        sys.stderr.write(
            f"[STDERR] Error: opening file {new_file_name}: {error}")
else:
    print("Usage: ft_ancient_text.py <file>")

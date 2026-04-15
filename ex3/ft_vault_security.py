# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/04/15 17:57:43 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Optional


def secure_archive(file_name: str, action: Optional[str] = 'r',
                   new_content: Optional[str] = ""
                   ) -> tuple[bool, str]:
    """ return True and content if action successed
        otherwise False and an Error message"""

    # Write in file
    if (action == "write" or action == "w") and new_content is not None:
        try:
            with open(file_name, "w") as file:
                file.write(new_content)
                return (True, new_content)
        except (FileNotFoundError, PermissionError) as error:
            return (False, f"{error}")
    else:
        # Read file
        try:
            with open(file_name) as file:
                return (True, file.read())
        except (FileNotFoundError, PermissionError) as error:
            return (False, f"{error}")


print("=== Cyber Archives Security ===\n")

print("Using 'secure_archive' to read from a nonexistent file:")
print(f"{secure_archive("/not/existing/file")}\n")

print("Using 'secure_archive' to read from an inaccessible file:")
print(f"{secure_archive("/etc/master.passwd")}\n")

print("Using 'secure_archive' to read from a regular file:")
print(f"{secure_archive("ancient_fragment.txt")}\n")

print("Using 'secure_archive' to write previous content to a new file:")
print(f"{secure_archive("ancient_fragment", "write",
                        'Content successfully written to file')}\n")

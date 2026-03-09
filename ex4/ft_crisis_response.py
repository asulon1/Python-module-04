# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/03/09 20:07:51 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")


def print_archive(data: str) -> None:
    print(f"SUCCESS: Archive recovered - : ''{data}''")


# lost_archive.txt
try:
    lost_file = "lost_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{lost_file}'...")
    with open(lost_file) as file:
        data = file.read()
        print_archive(data)
except (FileNotFoundError):
    print("RESPONSE: Archive not found in storage matrix")
finally:
    print("STATUS: Crisis handled, system stable\n")

# classified_vault.txt
try:
    archive_file = "classified_vault.txt"
    print(f"CRISIS ALERT: Attempting access to '{archive_file}'...")
    with open(archive_file) as file:
        data = file.read()
        print_archive(data)
except (FileNotFoundError, PermissionError):
    print("RESPONSE: Security protocols deny access")
finally:
    print("STATUS: Crisis handled, system stable\n")

try:
    standard = "standard_archive.txt"
    print(f"ROUTINE ACCESS: Attempting access to '{standard}'...")
    with open(standard) as file:
        data = file.read()
        print_archive(data)
except (FileNotFoundError, PermissionError):
    print("RESPONSE: Security protocols deny access")
finally:
    print("STATUS: Crisis handled, system stable\n")

print("All crisis scenarios handled successfully. Archives secure.")

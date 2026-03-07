# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/03/08 00:58:10 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

file_name = "new_discovery.txt"
entry_list = [
    "[ENTRY 001] New quantum algorithm discovered",
    "[ENTRY 002] Efficiency increased by 347%",
    "[ENTRY 003] Archived by Data Archivist trainee",
]

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
print(f"Initializing new storage unit: {file_name}")

try:
    with open(file_name, "w") as file:
        print("Storage unit created successfully....\n")
        print("Inscribing preservation data...")
        for entry in entry_list:
            file.write(f"{entry}\n")
            print(f"{entry}")
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")

except (FileNotFoundError, PermissionError) as error:
    print(f"CRITICAL ERROR: System integrity compromised. {error}")

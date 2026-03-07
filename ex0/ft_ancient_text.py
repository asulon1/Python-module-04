# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/03/08 00:55:09 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

file = None
file_name = "ancient_fragment.txt"
try:
    with open(file_name) as file:
        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f"{file.read()}\n")
        print("Data recovery complete. Storage unit disconnected.")

except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")

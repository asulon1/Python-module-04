# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/03/09 19:58:54 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")

try:
    print("Vault connection established with failsafe protocols\n")

    with open("classified_data.txt", "r") as vault_file:
        data = vault_file.read()
        print("SECURE EXTRACTION:")
        print(f"{data}\n")

    with open("classified_vault.txt", "w") as archive_file:
        archive_file.write("[CLASSIFIED] New security protocols archived")
        print("SECURE PRESERVATION:")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion\n")
except FileNotFoundError:
    print("Error: Vault source not found")
finally:
    print("All vault operations completed with maximum security.")

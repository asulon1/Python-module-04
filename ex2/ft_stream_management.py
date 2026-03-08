# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/03/08 00:24:33 by sulon           #+#    #+#               #
#  Updated: 2026/03/08 01:19:51 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

sys.stdout.write("Input Stream active. Enter archivist ID: ")
sys.stdout.flush()
archivist_id = sys.stdin.readline().strip()

sys.stdout.write("Input Stream active. Enter status report: ")
sys.stdout.flush()
status_report = sys.stdin.readline().strip()

print()
sys.stdout.write(
    f"[STANDARD] Archive status from {archivist_id}: {status_report}\n")

sys.stderr.write(
    "[ALERT] System diagnostic: Communication channels verified\n")


sys.stdout.write("[STANDARD] Data transmission complete\n\n")

print("Three-channel communication test successful.")

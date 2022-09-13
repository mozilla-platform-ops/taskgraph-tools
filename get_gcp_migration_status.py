#!/usr/bin/env python3

from subprocess import run

gcp_command = "./worker_report.py | grep gcp | wc -l" #.split(' ')
gcp_p = run(gcp_command, capture_output=True, check=True, shell=True)

total_command = "./worker_report.py | \
        grep -v releng-hardware | \
        grep -v autophone | \
        grep -v win | \
        grep -v scriptworker | \
        grep -v macosx | wc -l" #.split(' ')
total_p = run(total_command, capture_output=True, check=True, shell=True)

total_all_command = "./worker_report.py | wc -l"
total_all_p = run(total_all_command, capture_output=True, check=True, shell=True)

g_val = int(gcp_p.stdout.decode().strip())
t_val = int(total_p.stdout.decode().strip())
t_all_val = int(total_all_p.stdout.decode().strip())

print(f"gcp jobs: {g_val}")
print(f"non-win, non-macosx, non-bitbar, non-releng-hardware, non-scriptworker jobs: {t_val}")
print(f"all jobs: {t_all_val}")
print(f"percent migrated to gcp: {g_val}/{t_val} = {g_val / t_val}")

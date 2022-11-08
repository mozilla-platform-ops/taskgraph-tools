#!/usr/bin/env python3

from subprocess import run

# not that useful (background) vaules

total_all_command = "./worker_report.py | wc -l"
total_all_p = run(total_all_command, capture_output=True, check=True, shell=True)

gcp_command = "./worker_report.py | grep gcp | wc -l" #.split(' ')
gcp_p = run(gcp_command, capture_output=True, check=True, shell=True)

# useful values

# gcp-migrate-able tasks
cmd_migratable = "./worker_report.py | \
        grep -v releng-hardware | \
        grep -v autophone | \
        grep -v win | \
        grep -v 'built-in/succeed' | \
        grep -v scriptworker | \
        grep -v macosx"
# gcp-migrate-able tasks on gcp
cmd_migratable_not_on_gcp = f"{cmd_migratable} | grep gcp" 

total_p = run(f"{cmd_migratable} | wc -l", capture_output=True, check=True, shell=True)
migrated_p = run(f"{cmd_migratable_not_on_gcp} | wc -l", capture_output=True, check=True, shell=True)

g_val = int(migrated_p.stdout.decode().strip())
t_val = int(total_p.stdout.decode().strip())
t_all_val = int(total_all_p.stdout.decode().strip())

print(f"( all tasks: {t_all_val} )")
print(f"gcp-migratable tasks: {t_val}")
print("  (non-win, non-macosx, non-bitbar, non-releng-hardware, non-scriptworker, non-built-in tasks)")
print(f"gcp-migrateable tasks on gcp: {g_val}" )
print(f"percentage of migratable tasks migrated to gcp: {g_val}/{t_val} = {g_val / t_val}")

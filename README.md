# taskgraph-tools

Tools for inspecting taskgraph jobs.

## directions

Copy or symlink the scripts into the base of a mozilla-central hg clone.

```
# generate the full taskgraph (required for subsequent steps)
./generate.sh

# show a report detailing job and the provisioner/worker_type it runs on
./worker_report.py

# analyze status of GCP migration
./get_gcp_migration_status.py

```

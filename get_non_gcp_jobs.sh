#!/usr/bin/env bash

set -e
#set -x

# hmm, numbers are off by ~40 jobs
#   total - gcp - non-gcp != 0

./worker_report.py | \
        grep -v releng-hardware | \
        grep -v autophone | \
        grep -v win | \
        grep -v scriptworker | \
        grep -v macosx | \
	grep -v gcp

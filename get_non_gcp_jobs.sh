#!/usr/bin/env bash

set -e
# set -x

# hmm, numbers are off by ~40 jobs
#   total - gcp - non-gcp != 0

CMD=$(cat <<'END_HEREDOC'
./worker_report.py | 
        grep -v releng-hardware | 
        grep -v autophone | 
        grep -v win | 
        grep -v scriptworker | 
        grep -v macosx | 
        grep -v "built-in/succeed" | 
        grep -v gcp
END_HEREDOC
)

# echo $CMD
# exit 1

# run it
bash -c "$CMD"

# get list of worker types
echo ""
echo "unique worker types from above:"
bash -c "$CMD | cut -f 2 -d ':' | sort | uniq"

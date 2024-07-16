#!/usr/bin/env bash

set -e
set -x

./worker_report.py | grep gecko-t/t-linux-vm-2204-wayland

./worker_report.py | grep gecko-t/t-linux-vm-2204-wayland | wc -l

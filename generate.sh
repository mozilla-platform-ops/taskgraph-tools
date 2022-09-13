#!/usr/bin/env bash

set -e

./mach taskgraph tasks --json 2>/dev/null > tasks.json

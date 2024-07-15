#!/usr/bin/env bash

set -e

time bash -c './mach taskgraph tasks --json 2>/dev/null > tasks.json'

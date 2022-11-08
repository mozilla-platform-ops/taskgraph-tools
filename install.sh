#!/usr/bin/env bash

set -e

# TODO: check for fling and tell users to install it
# - https://github.com/bbkane/fling

# TODO: take mozilla-central client path as an arg

fling \
	-l $HOME/hg/mozilla-central \
	-s . \
	-i README \
	-i LICENSE \
	-i .git \
	link


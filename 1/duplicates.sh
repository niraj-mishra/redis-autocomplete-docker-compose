#!/bin/bash

sed ':f;N;$!bf; s/\b\(.*\)\n\1\b/\1\n/g; s/\b\(.*\)\b\1\b/\1/g' $1 ##pass the file name with script

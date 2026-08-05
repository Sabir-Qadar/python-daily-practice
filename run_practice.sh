#!/bin/bash
# Double-click (or run: bash run_practice.sh) to auto-generate and push
# 3-4 new Python practice solutions to your python-daily-practice repo.

cd "$(dirname "$0")" || exit 1

echo "Running daily practice generator..."
echo

python3 generate_and_push.py
status=$?

echo
if [ $status -ne 0 ]; then
    echo "Something went wrong - see the messages above."
else
    echo "All done - check GitHub to see the new commits."
fi

read -p "Press Enter to close..."

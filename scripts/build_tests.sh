#!/bin/bash
# This script runs basic lint and compile checks.
# The return codes from each test are captured for use with CircleCI

# Print files
find . -path ./venv -prune -o -name "*.py" -print

# Lint json files (the 'exit 255' fails xargs fast):
find . -name "*.json" -print | grep -v '/test/' | grep -v 'vendor' | xargs -Ixx bash -c "echo JSON linting xx 1>&2; cat xx | python -mjson.tool > /dev/null || exit 255"
STATUS+=($?)

# PyLint
find . -path ./venv -prune -o -name "*.py" -print0 | xargs -0 pylint --rcfile=.pylint
STATUS+=($?)
        
# Syntax Checks
find . -path ./venv -prune -o -name "*.py" -print0 | xargs -0 python -m py_compile
STATUS+=($?)

# If any of the tests failed, exit with that failure
for i in ${STATUS[@]}; do
  if (($i > 0)); then
    exit $i
  fi
done

exit 0

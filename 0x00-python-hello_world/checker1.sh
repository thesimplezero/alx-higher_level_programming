#!/bin/bash

# Get the current working directory
REPO_ROOT=$(pwd)

# Check Python version
# python_version=$(python3 --version)
# if [[ "$python_version" != "Python 3.8.5" ]]; then
#     echo "Failed: Python version is not 3.8.5"
#     exit 1
# fi

# Check if pycodestyle is installed and is the correct version
pycodestyle --version | grep -q '2.8'
if [ $? -ne 0 ]; then
    echo "pycodestyle is not installed or the wrong version is installed. Install version 2.8.*."
    exit 1
fi

# Check if there's a README.md in the root
if [[ ! -f "$REPO_ROOT/README.md" ]]; then
    echo "Failed: README.md is not present in the repository root"
    exit 1
fi

# Loop over all python files in the repo
find "$REPO_ROOT" -type f -name '*.py' | while read -r file; do

    echo "Checking file: $file"

    # Check if file ends with a new line
    if [[ $(tail -c1 "$file" | wc -l) -eq 0 ]]; then
        echo "Failed: File does not end with a new line"
        exit 1
    fi

    # Check if the first line is #!/usr/bin/python3
    first_line=$(head -n 1 "$file")
    if [[ "$first_line" != "#!/usr/bin/python3" ]]; then
        echo "Failed: First line is not #!/usr/bin/python3"
        exit 1
    fi

    # Check the Python style
    pycodestyle "$file"
    if [ $? -ne 0 ]; then
        echo "Failed: pycodestyle check"
        exit 1
    fi

    # Check if file is executable
    if [[ ! -x "$file" ]]; then
        echo "Failed: File is not executable"
        exit 1
    fi

    echo "$file passed all checks"
done

# Check file length
find "$REPO_ROOT" -type f | while read -r file; do
    length=$(wc -c <"$file")
    if [[ $length -eq 0 ]]; then
        echo "File $file is empty"
        exit 1
    fi
done

echo "File length check passed"

# If we've made it here, all checks passed
echo "All checks passed"

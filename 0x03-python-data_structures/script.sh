#!/bin/bash

# List of files
files=("README.md" "0-print_list_integer.py" "1-element_at.py" "2-replace_in_list.py" "3-print_reversed_list_integer.py" "4-new_in_list.py" "5-no_c.py" "6-print_matrix_integer.py" "7-add_tuple.py" "8-multiple_returns.py" "9-max_integer.py" "10-divisible_by_2.py" "11-delete_at.py" "13-is_palindrome.c" "linked-lists.c" "lists.h")

for file in "${files[@]}"
do
    # Check if file exists
    if [ -f "$file" ]; then
        git add "$file"
        echo "Enter the commit message for $file:"
        read commit_message
        git commit -m "$commit_message"
        git push origin main
    else
        echo "File $file does not exist."
    fi
done

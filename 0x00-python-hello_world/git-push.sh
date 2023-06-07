#!/bin/bash

# Change to the root directory of the git repository
cd "$(git rev-parse --show-toplevel)"

# Reset git staging area
git reset

# Check if the working directory is clean
if [[ -z $(git status --porcelain) ]]; then
  echo "Your working directory is clean. There are no changes to commit."
  exit 0
fi

# Function to commit and push individual files
commit_and_push() {
  local filepath="$1"
  local filename=$(basename "$filepath")
  git add "$filepath"
  git commit -m "$filename"
  git push
}

# Loop through changed files, commit, and push
for filepath in $(git diff --name-only); do
  if [ -e "$filepath" ]; then  # Check if the file or directory exists
    commit_and_push "$filepath"
  else
    echo "$filepath does not exist. Skipping."
  fi
done

echo "All individual files have been committed and pushed."

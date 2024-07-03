# Git Cheat Sheet

## Setup
- `git init`: Initialize a new Git repository
- `git clone <url>`: Clone a repository

## Basic Commands
- `git status`: Check repository status
- `git add <file>`: Stage file changes
- `git commit -m "message"`: Commit staged changes
- `git push`: Push commits to remote repository
- `git pull`: Fetch and merge changes from remote

## Branching
- `git branch`: List branches
- `git branch <name>`: Create a new branch
- `git checkout <branch>`: Switch to a branch
- `git merge <branch>`: Merge a branch into current branch

## Remote Repositories
- `git remote add <name> <url>`: Add a remote repository
- `git remote -v`: List remote repositories

## History
- `git log`: View commit history
- `git diff`: Show changes between commits

## Undoing Changes
- `git reset <file>`: Unstage file changes
- `git checkout -- <file>`: Discard changes in working directory
- `git revert <commit>`: Create new commit that undoes specified commit

## Advanced
- `git stash`: Temporarily store modified files
- `git tag <name>`: Create a tag for a commit
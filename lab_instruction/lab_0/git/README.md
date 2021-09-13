# Git

[Git](https://git-scm.com) is a version control system that commonly used
to track changes in software artefact (e.g. source code, HTML pages, stylesheets).
It works by capturing states of items in the software artefact as series of
**commits** that are internally arranged in linear manner from oldest commit to the
most recent commit. Think of it like a graph in which a node represents a commit and
directed edge(s) represent the connection from a commit to its subsequent commit(s).

## Install git

- Download

  - [Windows 64-bit](https://github.com/git-for-windows/git/releases/download/v2.33.0.windows.2/Git-2.33.0.2-64-bit.exe)

- Run the installer
  - Windows: execute the downloaded file
  - Linux (Ubuntu): `sudo apt install git`
  - macOS: `brew install git`

## Terminal Commands

- `cd` (change directory) : Change directory to outside or inside a folder.
- `dir` (directory?) : show files in the current directory
  > in Linux / macOS, use `ls` (list)
- `mkdir <folder_name>` (make directory) : create new folder
- `del <file_name>` (delete) : delete a file
  > in Linux / macOS, use `rm <file_name>` (remove)
- `rmdir <folder_name>` (remove directory) : delete a folder
  > in Linux / macOS, use `rm -rf <folder_name>` (remove)

## Commands

### git init

**Git init** command create a new empty git repository in the current working directory /
current folder.

```
git init
```

### git config

**Git config** command changes git settings for local config (current git repository)
or global config (current user).

```
git config <arguments>
```

To see current config, add `-l` or `--list`:

```
git config -l
```

You need to set `user.name` and `user.email` before making any commits.
If you already set them (see `user.name` and `user.email` in `git config -l`),
you **don't** have to do this part.

- Set user.name

  ```
  git config user.name "INSERT YOUR NAME HERE"
  ```

- Set user.email

  ```
  git config user.email "INSERT YOUR EMAIL HERE"
  ```

- check if you input your name and email correctly using `git config -l`

### git status

**Git status** command checks current status of the current repository.
If you add, delete, or modify some files, it will be shown in `git status`.

```
git status
```

To show the usage:

- **create a file** inside the repository.
- if you run `git status` you should see your file colored red.

### git add

**Git add** command adds a change in working directory to staging area.
Update in particular files that have been added to staging area will be included in the next commit.

```
git add <arguments>
```

- add program.py:

  ```
  git add program.py
  ```

- add all changes:

  ```
  git add .
  ```

  or

  ```
  git add -A
  ```

- Adds content from all \*.txt files under Documentation directory and its subdirectories:

  ```
  git add Documentation/\*.txt
  ```

### git commit

**git commit** command saves the changes you have added after you run `git add`.
It's like taking a _screenshot_ of your files.

```
git commit <arguments>
```

If you want to add a message to your commit (most of the time), use `-m` or `--message`:

```
git commit -m "INSERT YOUR COMMIT MESSAGE HERE"
```

> You **only can commit** once you already **staged** some files (using `git add`)to commit.

Example:

- Add all the files:

  ```
  git add .
  ```

- check your staged files (optional):

  ```
  git status
  ```

- Commit those files:

  ```
  git commit -m "add some files"
  ```

- If you have commit your files correctly, it should **not be shown** in `git status`

### git log

**git log** command print previous commits.

```
git log
```

> to **quit** from git log, press `Q`. move up and down using arrow keys.

useful arguments:

- **--all, -a** to view all commits
- **--graph** to view as a graph
- **--oneline** to view minimal log

or any combination of arguments. example:

```
git log --graph --all
```

### git diff

**git diff** command show difference unstaged files. It is very useful to see
changes before staging the files with `git add`

```
git diff
```

> to **quit** from git log, press `Q`. move up and down using arrow keys.

## More Commands

- `git clone REPO-URL` : Create new repository from REPO-URL
- `git push` : Upload commits to online repository
- `git branch -a` : List all existing branch in the repository
- `git branch BRANCH-NAME` : Create new branch in the repository named `BRANCH-NAME`
- `git checkout BRANCH-NAME` : Switch branch to `BRANCH-NAME`
- `git merge` : combine 2 branches into a single merged branch
- and more...

If you need help for the commands, add `--help` to the arguments. Example:

- `git --help`
- `git commit --help`
- `git log --help`

## Learning Materials

- https://learngitbranching.js.org/

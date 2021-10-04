# Tutorials and Assignment Repository

CSGE602022 - Platform-Based Programming (Pemrograman Berbasis Platform) @ Faculty of Computer Science Universitas Indonesia, Odd Semester 2021/2022

---

## Table of Contents

Welcome to the code repository.
This repository hosts weekly tutorial codes and other, such as course-related
code snippets.

1. Weekly Exercises
   1. [Lab 0](lab_instruction/lab_0/README.md) - Introduction to Git (on GitLab)
   2. [Lab 1](lab_instruction/lab_1/README.md) - Introduction to Django Framework
   3. [Lab 2](lab_instruction/lab_2/README.md) - Data Delivery Using HTML, XML, and JSON
   4. [Lab 3](lab_instruction/lab_3/README.md) - Form, Authentication, Session, and Cookie
   5. [Lab 4](lab_instruction/lab_4/README.md) - Web Design Using HTML and CSS3
2. [Quickstart Guide](#tldr)
3. [Initial Setup](#initial-setup)
4. [Doing the Tutorial](#doing-the-tutorial)
5. [Pulling Updates From Upstream](#pulling-updates-from-upstream)
6. [Show Code Coverage in Gitlab](#show-code-coverage-in-gitlab)
7. [Grading Scheme & Demonstration](#grading-scheme-demonstration)

## TL;DR

After you work at [Lab 1](lab_instruction/lab_1/README.md), make sure to link this repository to your Lab 1 Repository :

1. Add this repository link to your remote list as `upstream` (`git remote add upstream https://gitlab.com/PBP-2021/pbp-lab`)
2. Pull the latest update to check whether new tutorials have been updated (`git pull upstream master`)
3. Fix any merge conflict(s) that might arise (hopefully none)
   - Always choose latest commit from `upstream` when fixing merge
     conflict(s)
4. Do not forget to commit your merged `master` branch and push it
   to your own `master` branch at GitLab repository - Use Git command: `git push origin master`

Working on a tutorial problem set (This instructions applied for 3rd tutorials and so on):

1. Pull any updates from `upstream`
2. Create new apps on Django Project based on your tutorials `python manage.py startapp lab_n` where **n** is turoial number. E.g. **lab_2**
3. Do the exercises as instructed in README.md file ([click this](lab_instruction/lab_10/README.md) to see this week Tutorials README.md)
4. Commit your work frequently
5. Write good commit message(s)
6. If your work is ready for grading: `git push origin master`

If you want to know the detailed explanation about each instructions above,
please read the following sections.

## Initial Setup

If you previously haven't worked on [Lab 1](lab_1/README.md) Tutorial

1. then Create a fork of this repository to your GitLab account, which will
   create a copy of this repository under your own account.
2. Open the forked repository page at
   `https://gitlab.com/<YOURNAME>/pbp-lab` where `<YOURNAME>`
   is your GitLab username.
3. Set the clone URL to HTTPS and copy the URL into clipboard.
4. Clone the repository into your local machine. Use Git command:
   `git clone https://gitlab.com/<YOURNAME>/pbp-lab.git <PATH>`
   where `<PATH>` is a path to a directory in your local machine.
5. Go to the directory where the cloned repository is located in your
   local machine.
6. Add new remote called **upstream** that points to the original
   GitLab repository. Use Git command: `git remote add upstream https://gitlab.com/PBP-2021/pbp-lab`
7. Tell your TA about your GitLab username and URL to your tutorial
   repository so s/he can grade it later.
8. Ensure that your repository page has visibility level set to
   **Internal** or **Public**. Check it in **Edit Project** menu at
   your repository page.

If you did [Lab 1](lab_1/README.md) Tutorial

1. Add new remote called **upstream** that points to the original
   GitLab repository. Use Git command: `git remote add upstream git remote add upstream https://gitlab.com/PBP-2021/pbp-lab`
2. Tell your TA about your GitLab username and URL to your tutorial
   repository so s/he can grade it later.
3. Ensure that your repository page has visibility level set to
   **Internal** or **Public**. Check it in **Edit Project** menu at
   your repository page.

## Doing the Tutorial

1. Suppose that you want to work on Lab 1 problem set. Go to the
   directory that containing Lab 1 README.md.
2. To ensure your work regarding Lab 1 problem is isolated from
   your other attempts on other problems, create a new apps
   specifically for working on Lab 1 problem. Use Python command:
   `python manage.py startapp lab_1`
3. Read the README file carefully because It contains set of tasks and instructions that you can work on.
4. Do the tutorial.
5. Use `git add` or `git rm` to stage/unstage files that you want to
   save into Git later.
6. Once you want to save your progress, commit your work to Git. Use
   Git command: `git commit` A text editor will appear where you should
   write a commit message. Please try to follow the guidelines written
   in [this guide](http://chris.beams.io/posts/git-commit/) on how to
   write a good commit message.
7. Repeat steps 4 - 6 until you finish the tutorial.
8. Once you are ready to submit your work or you want to save it to
   your repository on GitLab, do a Git **push**. The Git command:
   `git push origin master`

## Pulling Updates From Upstream

If there are any updates from upstream, you can get the latest commits
and integrate it into your fork by using the following Git command:
`git pull upstream master`

Merge conflicts may arise since the repository is updated weekly and
may have overlapping changes with the `master` branch in your own
forked repository. If merge conflict happens, please always use latest
commit from `upstream`. Once you have resolved any merge conflicts and all commits from
upstream are merged succesfully to your own `master` branch, do not
forget to push it back to your own GitLab repository. Use Git command:
`git push origin master`

## Show Code Coverage in Gitlab

1. Go to CI/CD Settings (`Settings -> CI/CD`)
2. Go to section Coverage Settings (`General pipelines -> Test coverage parsing`)
3. Write this Regex (Regular Expression) in textbox `Test Coverage Parsing`
   ```
   TOTAL\s+\d+\s+\d+\s+(\d+)%
   ```
4. Save the changes.
5. To add coverage badge to gitlab like: [![Pipeline](https://gitlab.com/PBP-2021/pbp-lab/badges/master/pipeline.svg)](https://gitlab.com/PBP-2021/pbp-lab/pipelines) [![Coverage](https://gitlab.com/PBP-2021/pbp-lab/badges/master/coverage.svg)](https://gitlab.com/PBP-2021/pbp-lab/pipelines)
   - On top of the project:
     1. Go to General Settings (`Settings -> General`)
     2. Go to section Badges
     3. Create a new badge with `Badge image URL` for pipeline:
        ```
        https://gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg
        ```
     4. and for the coverage badge:
        ```
        https://gitlab.com/%{project_path}/badges/%{default_branch}/coverage.svg
        ```
   - On the `README.md`:
     1. Add 2 new lines to your `README.md`:
        ```
        [![Pipeline](https://gitlab.com/YOUR_GITLAB_USERNAME/YOUR_REPOSITORY_NAME/badges/master/pipeline.svg)](https://gitlab.com/YOUR_GITLAB_USERNAME/YOUR_REPOSITORY_NAME/pipelines)
        [![Coverage](https://gitlab.com/YOUR_GITLAB_USERNAME/YOUR_REPOSITORY_NAME/badges/master/coverage.svg)](https://gitlab.com/YOUR_GITLAB_USERNAME/YOUR_REPOSITORY_NAME/pipelines)
        ```
     2. Change `YOUR_GITLAB_USERNAME` and `YOUR_REPOSITORY_NAME` to match your
        repository. example for this repository:
        ```
        [![Pipeline](https://gitlab.com/PBP-2021/pbp-lab/badges/master/pipeline.svg)](https://gitlab.com/PBP-2021/pbp-lab/pipelines)
        [![Coverage](https://gitlab.com/PBP-2021/pbp-lab/badges/master/coverage.svg)](https://gitlab.com/PBP-2021/pbp-lab/pipelines)
        ```
6. Run a new pipeline for them to get updated. You can **push** a new commit
   or **retry** your last pipeline.

## Tutorial: Running Your Django Project

1. Get a copy of Repo PBP
   from one of your working station (PC Lab, laptop or homedesktop).
   in one of your working station (PC Lab, laptop or homedesktop) by executing the clone command.

It is possible to download and extract it to a different directory

2. Create a new project on GitLab where you will store this exercise.

3. Go to the directory where you extracted the Repo PBP and initialize
   the directory into a Git repository.
4. Add new Git remote that link the local Repo PBP repository to your
   new GitLab repository.

At this stage, you are now ready to continue the tutorial. To save your progress,
please add any new/modified file(s) and folder(s) to local Git repository and
save it as one or more commits. Once you are done or want to ensure your progress
is stored on GitLab, use `git push` to push your commits.

Now please proceed to the instructions as follows.

1.  Create a **virtual environment** for this tutorial by using this command:

    ```bash
    python -m venv env
    ```

    > Make sure that you executed the command in the root path of the repository.

2.  Activate your virtual environment and install required packages. Note that
    the command for activating virtual environment is different on Windows and
    Unix-based OS.

        Windows:

        ```bash
        env\Scripts\activate.bat
        pip install -r requirements.txt
        ```

        Linux & Mac OS:

        ```bash
        source env/bin/activate
        pip install -r requirements.txt
        ```

3.  Use your favourite editor to edit the code (Vim, VS Code, Atom) or use IDE (PyCharm).

4.  Let's try running the Web locally in your machine. Run it by typing:

    ```bash
    python manage.py runserver 8000
    ```

    > Ensure the current active directory in your shell/command-prompt
    > is in the folder containing `manage.py` before executing the command
    > above

5.  Access your local Web server by using your favorite Web browser. Put the
    address into your browser: `http://localhost:8000`
6.  See your work is shown in Web page rendered by browser.
7.  When you are done with your tutorial or you want to switch to another
    Python project, do not forget to deactivate your virtual environment. You
    can do so by executing:

        ```bash
        deactivate
        ```

## Grading Scheme & Demonstration

Weekly tutorials contribute **20%** to the final grade of this course.
For each exercises, student can obtain grade ranging from **A (4)** to
**E (0)**. The grading scheme is as follows:

1. **A** if student completed **all checklists**
2. **B** if student completed **80% of checklist**
3. **C** if student completed **at least half of the checklist**
4. **D** if student completed **30% of checklist**
5. **E** if student skipped the tutorial by doing nothing, e.g.
   no signs of work to the tutorial in the repository

All students required to demonstrate their work to teaching assistant.
This demonstration mechanism applies for both students in Regular and
International classes:

1. Demonstrations should be done no later than the end of the
   lab session week. The time allocation for the demonstration can be
   adjusted to the availability of the Teaching Assistants. As long as
   the demonstration is still done before **your lab session**, students have the chance
   to achieve maximum score for the tutorial.
2. If the demonstration is done after **your lab session**, you have to demonstrate
   your work to your **lecturer** and your score won't reach maximum point eventhough you
   **do all checklists**

### Happy Coding :)

## Additional Resources

- [Git Tutorials & Training by Atlassian](https://www.atlassian.com/git/tutorials)
- [Try Git in your Web browser](https://try.github.io)
- [Pro Git e-Book by Scott Chacon & Ben Straub](https://git-scm.com/book/en/v2)
- [Graph theory](http://think-like-a-git.net/sections/graph-theory.html) and
  [its application in Git](http://think-like-a-git.net/sections/graphs-and-git.html)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

## Credits

This document is based on [Exercise 0: Introduction to Git](https://gitlab.com/CSUI-AdvProg-2017/lab-exercises)
written by Advanced Programming 2017 Teaching Team ([@addianto](https://gitlab.com/addianto),
[@muhammad.ardhan](https://gitlab.com/muhammad.ardhan), [@fbenarto](https://gitlab.com/fbenarto),
et al.). The section about branching and handling merge conflicts are omitted
in this document to make sure the Git tutorial can be completed by students during
Web Design & Programming lab session.

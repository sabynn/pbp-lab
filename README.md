# Lab 1: Introduction to Git (on GitLab) & TDD (Test-Driven Development) with Django

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Learning Objectives

After completing this exercise, students will be able to:

- Remember essential Git commands for individual work
- Demonstrate essential Git commands for individual work
- Setup a local and online (GitLab) Git repository
- Setup a remote between local Git repository and its counterpart on GitLab
- Practice basic TDD development cycle
- Publish his/her work on a PaaS (Platform-as-a-Service) cloud service provider

## Introduction

During your life as a CS/IS student, you may have used some sort of **version
control system**. One of the most pervasive example is undo functionality in a
text editor. Whenever you made some mistakes, you can revert to previous correct
state of your work by using undo function in the text editor. Another example is
when you are working on a document collaboratively using Google Drive where you
can see every revisions made to the document and you can revert to any previous
prevision.

In this course, you are going to use a version control system called
[Git](https://git-scm.com). Git is a version control system that commonly used
to track changes in software artefact (e.g. source code, HTML pages, stylesheets).
It works by capturing states of items in the software artefact as series of
**commits** that are internally arranged in linear manner from oldest commit to the
most recent commit. Think of it like a graph in which a node represents a commit and
directed edge(s) represent the connection from a commit to its subsequent commit(s).

> Don't worry if you are not familiar with these terms: *node*, *edge*, and *graph*.
> You can learn about them in Data Structures & Algorithms and Discrete Mathematics
> course.

Before doing this exercise and any subsequent exercises later, make sure you have
installed the following tools:

- [Git](https://git-scm.com/downloads)
- [Python 3.6.2](https://www.python.org/downloads/release/python-362/)
- [EditorConfig](http://editorconfig.org)
- A **good** text editor, e.g. [Vim](http://www.vim.org/download.php),
[Visual Studio Code](https://code.visualstudio.com/), or
[Atom](https://atom.io)

  > Regardless your choice of text editor, try to learn how to use Vim
  > because it is the default editor in Git. At least, know how to
  > navigate using `hjkl` keys, and operating the editor in NORMAL mode
  > (e.g. `:w`, `:q`, `:wq`, `ESC` button to switch modes, `i` to switch
  > INSERT mode).

For brevity, the guides for installing and configuring each tool are omitted from
this document. You can refer to the linked sites in order to read the guide.

## Tutorial: Git & GitLab

1. Start your favourite command-prompt or shell. If you are using Windows, run
`Git Bash` or `cmd` (only applies if you have added path to git executable into PATH
environment variable). If you are using Unix-based OS (Linux or Mac OS), you can
use any shell provided in your OS, e.g. [bash](https://www.gnu.org/software/bash/).

    > Although it is possible to use GUI-based application, e.g. built-in Git GUI,
    > [GitKraken](https://www.gitkraken.com), or
    > [SourceTree](https://www.sourcetree.com), **we really recommend you to use Git
    > commands from shell**. Shell is the lowest common denominator environment that is
    > available for you during Web development, especially when you have to deploy your
    > Web application to a remote server. It will be useful to know shell commands, and
    > also Git commands, when you can't have a graphical environment. Plus, executing
    > commands by typing is **much** faster than point-and-click it on GUI.
2. Set your current directory to a directory where you will store your work related
to the course that you are currently take. Use `cd` command to navigate to a directory
of your choice.
3. Create a new directory to store new files related to this exercise. Try naming
the directory to `git-exercise` and set your current directory to the new directory.
4. Inside the new directory, type `git init` to create an empty Git repository.
5. Try execute `git status` to see the state of Git repository at the time of command
execution.

At this point, you have successfully created your first local Git repository. Before
we can continue the tutorial, there are several configurations need to be done to your
local Git repository.

1. Set the username and email that will be associated with your
work in this Git repository.

    ```bash
    git config user.name "<NAME>"
    git config user.email "<EMAIL>"
    ```

    Example:

    ```bash
    git config user.name "Pina Korata"
    git config user.email "pina.korata@ui.ac.id"
    ```
2. If you are behind proxy, e.g. using PC in Fasilkom labs, you need to set HTTP
proxy in Git configuration as well.

    ```bash
    git config http.proxy <PROXYHOST>:<PORT>
    ```

    Example (if you are using PC in Fasilkom labs):

    ```bash
    git config http.proxy 152.118.24.10:8080
    ```
3. If you want to set the configuration globally, i.e. for every local Git
repositories in your local machine), add `--global` flag in `git config`
calls.
4. If you want to know the configurations set to your local repository, you can
use the following command.

    ```bash
    git config --list --local
    ```

Once you have configured your Git repository, you may proceed to the next
tutorial instructions.

1. Create a new file named `README.md` in the directory where you initialised
the Git repository and write your name, NPM, and class in the **first**, **third**,
and **fifth** line within the new file, respectively.

    Example:

    ```
    Name    : Pina Korata

    NPM     : 1606123456

    Class   : Z
    ```
2. Run `git status`. Notice that there is an untracked file named `README.md`.
It means there is a file that is not yet tracked by Git.
3. Tell Git to track any changes to the `README.md`.

    ```bash
    git add README.md
    ```
4. Run `git status` again. The status message will be different from previous
execution. See that the file is put into a section named *Changes to be committed*.
It means the file will be tracked by Git in the next commit.

    > Internally, the file, i.e. `README.md` is not yet tracked by Git even
    > though you have run `git add` command. `git add` command only tells Git
    > to include changes in the specified file(s) into Git's *staging area*.
5. To save the changes permanently into Git, run `git commit`. A text editor
will appear where you have to write a message that describes *commit* you just
created and want to save into Git's history.

    > Loosely speaking, *commit* means changes that you just made in the local
    > repository. Changes may consist of adding, editing, or removing one or
    > more files.
6. Once you have finished writing the commit message, save it and exit the text
editor you use for composing the message. The changes will be bundled as a commit
and stored in Git's history.

You have just created a local Git repository and start tracking changes to a file
in the repository. If you are going to share your work with your tutor, you need
to have the repository accessible through the Internet. In order to do so, you
are going to put a copy of your local repository in an online Git hosting service
named [GitLab](https://gitlab.com).

1. Go to [GitLab](https://gitlab.com) using your favourite Web browser.
2. Create a new account or use an existing one if you have registered before
taking this tutorial.
3. Create a new repository named **My First Repo** and go to the repository
page. Ensure that you set the visibility to **Public**.
4. Find a section named **Clone URL** in the page. Notice that there are two kinds
of URL: **HTTPS** and **SSH**. Take note of the **HTTPS** URL.
5. Update your local Git repository so your commit(s) later can be stored in
GitLab as well. Use `git remote add` command and use the clone URL as the argument
for the command.

    ```bash
    git remote add origin <CLONEURL>
    ```

    Example:

    ```bash
    git remote add origin https://gitlab.com/pinakorata/my-first-repo.git
    ```

    > `git remote add origin` tells the local repository to add a path named
    > **origin** that points to the given URL. By having this path configured
    > in local repository, you will be able to store your commits to the online
    > repository as well using `git push` command.
5. To store your commits into your online repository on GitLab, run `git push`
command. You must specify the name of **remote path** and **branch** that will be
uploaded (or pushed).

    ```bash
    git push -u <REMOTE_NAME> <DEFAULT_BRANCH>
    ```

    Example:

    ```bash
    git push -u origin master
    ```

    > `git push` tells Git to push commit(s) in your local `master` branch to
    > repository pointed by `origin` remote. `-u` option ensures subsequent
    > `git push` calls when `master` branch is active will be sent to `master`
    > branch at `origin`.
6. Check your GitLab repository page. You will see that your files have been
stored and can be accessed on GitLab.

You can also download (i.e. **clone**) other Git repository to your local machine.
Let's try making a copy of your repository from GitLab to a different directory
in your local machine.

1. Go to your repository page on GitLab.
2. Take note of the **HTTPS** clone URL.
3. Switch back to your command-prompt or shell and go to a different directory
outside of your own local Git repository.
4. Run this command: `git clone <URL>` where `<URL>` is the clone URL.
5. Check that a new directory has been created with name equal to the name of
your repository.

At this point, you actually have 3 repositories: (1) The original, local
repository, (2) The online repository on GitLab that you linked with the
first repository, and (3) Another repository in your machine that you
cloned from (2). Now let's try to add new commit in (1), push it to (2), and
download (or in Git term: **pull**) it into (3).

1. Go to the directory where you initialised the first Git local repository.
2. Edit the `README.md` file by adding a string describing hobby at the
**seventh** line.

    Example:

    ```
    Name    : Pina Korata

    NPM     : 1606123456

    Class   : Z

    Hobby   : Singing
    ```
3. Save the file and add it into local Git repository.
4. Commit the file and push it to GitLab.
5. Check your GitLab repository page. You will see that your `README.md`
file has been updated. You can also compare it with the previous version
by checking the *diff* between the latest and previous commit.
6. Go to the directory where you cloned the repository from your own
repository on GitLab.
7. Update the repository by running this command: `git pull origin master`
8. Check your cloned repository. You should see that the `README.md` file
has been updated as well.

Congratulations. You have known, at least, the essential Git commands that
you can use for managing your work in Git and GitLab. You might be wondering
why bother doing this *add-commit-push-pull* cycle. Why don't we just use
Dropbox or Google Drive?

It is true that Dropbox, Google Drive, or any similar cloud file storage
service might be easier to use. However, those aforementioned tools are
designed for general use. They are not built specifically for handling changes
toward software artefact, especially when the changes are done **concurrently**
and involving multiple parties. Git, as a version control system, can ensure
the integrity of all changes when multiple parties are working on the same
repository concurrently. You will learn more about how to use version control
system in team work environment later in this course and in a more advanced
course (CS: Advanced Programming, IS: Enterprise-scale Programming).

## Tutorial: Test-Driven Development (TDD) with Django

1. Clone [Repo PPW Tutorial](https://gitlab.com/PPW-2017/Draft-Lab) into a separate directory.
2. Copy all files and folders from Repo PPW Tutorial into your GitLab repository directory.
3. To save this progress, just add and push all the files and folders to your GitLab repository. (Use a proper commit message)
4. Create a **virtual environment** for this tutorial by using this command:

    ```bash
    python -m venv env
    ```
    
    > Make sure that you executed the command in the root path of the repository.
5. Activate your virtual environment and install required packages. Note that
the command for activating virtual environment is different on Windows and
Unix-based OS.

    Windows:
    
    ```bash
    env/bin/activate
    pip install -r requirements.txt
    ```

    Linux & Mac OS:

    ```bash
    source env/bin/activate
    pip install -r requirements.txt
    ```
6. Use your favourite editor to edit the code (Vim, nano, Notepad++, etc), or use IDE (PyCharm, or IntelliJ IDEA).
7. Please open file `lab_1/views.py` and find line of code that has `# TODO IMPLEMENT`

    ```python
    # Enter Your Name Here
    mhs_name = '' # TODO IMPLEMENT

    # Create your views here.
    def index(request):
       response = {'name' : mhs_name}
       return render(request,'index.html',response)
    ```

8. Fill your name in that variable.
9. Run it locally by typing:

    ```bash
    python manage.py runserver 8000
    ```
10. Access your local webserver (`http://localhost:8000`).
11. See your name is shown in webpage.
12. When you are done with your tutorial or you want to switch to another
Python project, do not forget to deactivate your virtual environment. You
can do so by executing:

    ```bash
    deactivate
    ```

## Publish Your App In Heroku

1. Create your Heroku account in [Heroku Website](https://signup.heroku.com/).
2. Create your apps in heroku (Make sure that your appname is **Unique**).
3. Go to Gitlab Settings for Pipeline in your Gitlab Repo (*Settings* -> *Pipelines*).
4. Find Section **Secret Variable**, and try to add these variable to Gitlab *Pipeline*:
    - **Key** = HEROKU_APPNAME , **Value** = Your Heroku App Name
    - **Key** = HEROKU_APIKEY , **Value** = Your Heroku API Key (You can find it in *Account Settings* -> *Account* -> *API Key*)
    - **Key** = HEROKU_APP_HOST , **Value** = Your Heroku App URL
5. Push your editted code into your repo.
6. After waiting for some time (2 - 4 minutes), visit your app URL and you can find your web page has been published.

## Checklist

- Creating Your own Gitlab Repo
    - [ ] Write your Gitlab Repo link in README.md
- Your web that deployed in Heroku Instance
    - [ ] Create your Heroku Account
    - [ ] Write your apps link (`######`.herokuapp.com) in README.md
- Creating unit tests
    - [ ] Test whether your page has `<article>` tag that filled with simple paragraph
- Creating a functionality in Django framework and content in HTML
    - [ ] Create new URL for your own page
    - passing paragraph data from `views.py` to template HTML
    - [ ] Use data that passed from `views.py` and use it as a content for `<article>` tag HTML5 tag

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
in this document to make sure the tutorial can be completed by students during
Web Design & Programming lab session.

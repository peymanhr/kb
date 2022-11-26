# Git Basics

## Version Control System (VCS)

* Types of VSC:
    - Local  
        - Example is RCS
    - Centralized
        - Single point of failure
        - Need Connectivity
        - Examples are CVS, Subversion, Perforce, Bazzar
    - Distributed
        - They are called *DVCSs*
        - Everyone has the full repository
        - They are offline
        - Examples are Git, Mercurial, BitKeeper

* VCS does not replace backup

## About Git

* Linus Torvalds is the creator of Git
* Fully distributed
* Super fast
* Simple design
* Painless branch support
* Extremely reliable
* Can handle massive projects
* It revolutionized the world
* Snapshots, not Differences
* It is like a filesystem with magnificent tools operating on top of it
* Every operation is local
* Strict integrity
    - Everything is SHA-1 check-summed before being stored.
    - Files can not be corrupted without Git knowing.
    - It is possible to recover genuine repository from a completely untrusted source, after a data loss
- Git by nature is add-only

## Installation with binaries

* Redhat based Linux systems  
`sudo yum install git-all`
* Debian based Linux systems  
`sudo apt-get install git-all`
* MacOS  
https://git-scm.com/download/mac
* Windows  
http://git-scm.com/download/windows



## Git configuration

* /etc/gitconfig `git config --list --system`
* ~/.gitconfig `git config --list --global`
* .git/config `git config --list --local`

### Your identity
```bash
git config --global user.name "Peyman Hooshmandi Raad"
git config --global user.email phooshmand@gmail.com
```
### Print single key
```bash
git config user.name
```

### Get help
```bash
git help config
```

## Using Git  

### Create empty repository
```bash
mkdir foo
cd foo
git init
```

### Track and Stage files
```bash
git add <file>...
```
Track or Stage all files

```bash
git add -A
```

### Commit

```bash
git commit -m "<Message>"
```

### Untrack files

Untrack file and keep it in working directory.

```bash
git rm --cached <file>...
```

Untrack file and remove it from working directory.

```bash
git rm --force <file>...
```

### Unstage files
```bash
git reset HEAD <file>..
```

### Discard changes in working directory
Discard changes to siles  

```bash
git checkout -- <file>...
```

Discard all changes

```bash
git reset --hard HEAD
```

### Permanently remove files and folders from Git repo like it never existed
```bash
git filter-branch -f --tree-filter 'rm -f <file>' HEAD
```
[More on this](http://dalibornasevic.com/posts/2-permanently-remove-files-and-folders-from-a-git-repository)

### Remove untracked file
```bash
git clean -f
```

### Rename or Move
```bash
git mv <file-from> <file-to>
```

## Others

**Restore changes to a single file before commit**

```
git checkout -- file
```

**View all changed files done by merging a branch**

```
git diff --name-only <merge commit> <commit before merge>
```  
   

Without `--name-only`  you see full diff

**G reset back**

```
git reset --hard HEAD~1
```
or

```
git reset --hard 39adf3c
```

**Force merge without FF**

```
git checkout master
git merge some_branch --no-ff
```

**Show commit tree**

```
git log --oneline --graph --all --decorate
```

**Revert changes from a single commit on a single file**

```
git show <commit> -- <path> | git apply -R
```

**Unstage a file:**

```
git reset HEAD <file>
```


## Git Internals

[Git Internals](https://git-scm.com/book/en/v1/Git-Internals-Git-Objects)

[Git flight rules](https://github.com/k88hudson/git-flight-rules)

[Git blob format](https://matthew-brett.github.io/curious-git/reading_git_objects.html)

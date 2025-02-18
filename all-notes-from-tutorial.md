# git-learning-notes

some notes for git learners

# Git Commands

1. **Initializing a Git Project:**
   A repository (or repo) in Git is a storage location where your project's files, along with their entire version history, are stored. It tracks all changes, allowing you to collaborate, revert, and manage versions effectively.

   To start a new Git repository for your project, use the following command:
   ```
   git init
   ```
    - It creates a hidden .git folder, which stores all the repository’s
    metadata (branches, commits, configurations, etc.).
    - Used when starting a new project or making an existing directory a Git
    repository.

2. **Checking the Status:**

  - To view the current status of your local repository:
    ```
    git status
    ```
   - Tells you which files are modified, staged, or untracked and helps you understand what changes need to be committed.
  
  - To show the log (history) of the all commits you have made:
    ```
    git log
    ```
  - To see the content of a specific commit:
    ```
    git show <commit-hash-string>
    ```

3. **Adding Files to the Staging Area:**

   To Add files to the staging area to prepare them for commit. You have several options:

    - To add all (the changed) files:
      ```
      git add -A
      ```
    
    - To add specific file types, e.g., all HTML files:
      ```
      git add "*.html"
      ```

    - To add a specific file :
      ```
      git add <file>
      ```

    - To add more than one file at the same time:
      ```
      git add “file1.txt” “file2.txt”
      ```

    - To add any file that has "hello" in its name:
      ```
      git add “hello*”
      ```


4. **Removing a file from the local repository:**
      To remove a file from Git and your project, use:
    ```
    git rm 'file-name'
    ```
5. **Committing Changes:**

   To save the staged changes as a new snapshot, use the `git commit` command:
   ```
   git commit -m "Your comment about the changes"
   ```
    - `git commit`: You can also write this command (without adding -m "comment") and insert your comment in the editor. 
    - Always include a comment with your commit.

6. **Viewing Differences:**

   Git provides several ways to view differences:

    - See the differences between the unstaged changes vs. latest commit (HEAD) \> Shows **unstaged** modifications.
      ```
      git diff HEAD
      ```
     - HEAD: is a special pointer that refers to the current branch's latest commit. However, the location of this pointer can be changed to any commit you want. 

    - See the differences between staged changes vs. latest commit (HEAD) \> Shows **staged** modifications.
      ```
      git diff --staged
      ```

    Example:

    I make one change in the pag1.html, then add it to the stage then make
    another change, without adding:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: center;">$ git diff HEAD</th>
    <th style="text-align: center;">$ git diff --staged</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <th><p><strong>diff --git a/page1.html b/page1.html</strong></p>
    <p><strong>index d637411..b11a95a 100644</strong></p>
    <p><strong>--- a/page1.html</strong></p>
    <p><strong>+++ b/page1.html</strong></p>
    <p>@@ -2,5 +2,7 @@</p>
    <p>&lt;body&gt;</p>
    <p>project 1!</p>
    <p>Hi there!</p>
    <p>+ I am Jalal.</p>
    <p>+ I love programming!</p>
    <p>&lt;html&gt;</p>
    <p>&lt;body&gt;</p>
    <p>\ No newline at end of file</p></th>
    <td><p><strong>diff --git a/page1.html b/page1.html</strong></p>
    <p><strong>index d637411..b2f8fc6 100644</strong></p>
    <p><strong>--- a/page1.html</strong></p>
    <p><strong>+++ b/page1.html</strong></p>
    <p>@@ -2,5 +2,6 @@</p>
    <p>&lt;body&gt;</p>
    <p>project 1!</p>
    <p>Hi there!</p>
    <p>+ I am Jalal.</p>
    <p>&lt;html&gt;</p>
    <p>&lt;body&gt;</p>
    <p>\ No newline at end of file</p></td>
    </tr>
    </tbody>
    </table>

7. **Reseting and Exiting the Staging Area:**

   To manipulate the state of your working directory, staging area, and commit history, you can use the `git reset`
   command:

    - To unstage a file, use:
      ```
      git reset <file>
      ```

    - To move the HEAD pointer to a specific commit and optionally modify the staging area and working directory, use:
      ```
      git reset --soft <commit>
      git reset --mixed <commit>
      git reset --hard <commit>
      ```

8. **Restoring Files:**

   To manipulate the state of your working directory and staging area without affecting the commit history, you can use the `git restore` command:

    - To unstage a file, use:
      ```
      git restore --staged <file>
      ```
      - it works similarly to the `(git reset <file>)` command.

    - To restore all staged files:
      ```
      git restore --staged *
      ```

    - To  restore file content back to latest commit:
      ```
      git restore <file>
      ```

    - To restore a specific file from a previous commit to your working directory, use:
      ```
      git restore --source=<commit> <file>
      ```
      - It restores the content of <file> to match the version from the specified <commit>. This will overwrite the file in your working directory with the version from the given commit, but it won't affect the staging area or commit history.

    - To restore your entire working directory to match a specific commit, use:
      ```
      git restore --source=<commit> .
      ```
      
    - To replace a file with the version from the HEAD (latest commit), use:
      ```
      git checkout -- <file>
      ```
      - if you have not yet committed the changes, it will undo all changes and brings the file back to the previous commit file status. So, it restores all the changes back to the latest commit.
      - `'--'`: Refers to the HEAD (latest commit).


9. **Working With Branches:**
  
   When you create a new branch, it **inherits the current state** of your working directory and index.Managing branches is essential for collaboration and project organization. Here are some branch-related commands:

    - To show all branches in the project:
      ```
      git branch
      ```
      - The output highlights your current working branch with an astrix (\*). 
      Example:
      > \$ git branch
      >
      > fixhtml
      >
      > \* master

    - To Create a new branch for your project:
      ```
      git branch 'branch-name'
      ```

    - To delete a branch from the project:
      ```
      git branch -d 'branch-name'
      ```

    - To switch to a different branch and replace all the files in your current branch with those from 'branch-name',
      use:
      ```
      git checkout 'branch-name'
      ```
      - so, let’s say you make a new branch and go to this branch, make some files and change the contents of the other. If you switch back the master using checkout, all the files and changes that you have made will disappear from your computer directory!

    - To merge a branch into your current branch, use:
      ```
      git merge 'branch-name'
      ```
      - it merges the changes you made in the new branch on the branch master. note that before using this command you have to checkout first to the branch master.
      - When you switch from one branch to the other (let’s say from master to a new branch named "linkingpages") the git bash interface will show a message, telling you what is different in your working directory compared to linkingpages after switching. D means deleted, and M means modified.
      In this example, one file has been modified and one has been deleted, comparing the branch content with the working directory:

      > \$ git checkout linkingpages
      >
      > D 2_project.html
      >
      > M Git init.docx
      >
      > D index.txt
      >
      > Switched to branch 'linkingpages'
      - When you make changes in your working directory without staging them and then switch branches, Git will try to preserve your changes, but the behavior depends on whether those changes conflict with the files in the branch you're switching to.
      - until you merge the branch with the master, you cannot see the changes you made on that branch also in the master.

10. **Cloning a Remote Repository**
  
    Remote is a reference to a repository on a server, like github or
    gitlab, or even another machine. If you clone a repository from
    GitHub, Git automatically creates a remote reference called origin.

    Origin is the default name given to a remote repository when you
    clone a project. It acts as a shortcut to refer to the original
    repository's URL, so you don’t have to type the full address every
    time.

    In Git, a **remote is a reference** because it's essentially a
    **pointer** or **label** that Git uses to keep track of where a
    repository is located. So, a **remote** is a **reference to the
    location of a repository**—this **location** can be a URL, and Git
    uses that reference to fetch and push data. Technically speaking, Git stores remotes as **configuration entries** in your repository. So, remote is a **configuration entry** stored as plain text in the Git configuration file. Git keeps this information in a special file called .git/config in your local repository.
    For example, a typical section in .git/config looks like this:
      > \[remote "origin"\]
      >
      > url = https://github.com/user/repo.git
      >
      > fetch = +refs/heads/\*:refs/remotes/origin/\*
      >
    This configuration section is where **origin** is the reference, and
    the **URL** (https://github.com/user/repo.git) is the data that Git
    uses to access the remote repository.

    - Clonning a project means making a copy of the remote project on your local directory. To do so we use this command:
          ```
          git clone <remote repository url>
          ```
    - When you already have the repository cloned and want to update it, you want to fetch and merge the latest changes from a remote branch into your current local branch. This is Git terminology is called "pulling". We pull the file from the origin and write them on the master branch
        ```
          git pull origin master
        ```
    - If you made some changes on your local repository, and want to effect them also on the remote repository, you "push" these changes from your master brach to the origin by:
        ```
          git push origin master
        ```
    - if you want to tell Git, to make this push path (from master branch to the origin), as a default pushing path, you need to first write:
        ```
          git push -u origin master
        ```  
        (which -u stands for --set-upstream). the next time you want to do the same thing, you only
        need to write `git push`. 



13. **Push to a Remote Repository:**

    To push all the changes from your local `master` branch to a remote repository (usually in the cloud, like GitHub or
    GitLab), use:
    ```
    git push origin master
    ```
    - `origin`: Represents the remote repository.
    - `git push -u origin master`: After using this parameter, you can use `git push` instead
      of `git push origin master`.

14. **Pull from a Remote Repository:**

    To update, retrieve, and replace the changes from the remote repository into your local `master` branch, use:
    ```
    git pull origin master
    ```

15. **Clone a Repository:**

    To copy an existing repository from a remote location (like GitHub) to your local machine, use:
    ```
    git clone <repository_URL>
    ```

16. **Push Changes to Remote:**

    To send committed changes from your local repository to the remote server, use:
    ```
    git push
    ```

17. **Add Remote Repository:**

    To add a remote address to your current project on your local machine, use:
    ```
    git remote add origin <remote_URL>
    ```

18. **Change Remote URL:**

    To replace the current remote URL with a new one, use:
    ```
    git remote set-url origin <new_remote_URL>
    ```

19. **Pull Changes from Remote:**

    To fetch and merge changes from the remote server into your local branch, use:
    ```
    git pull origin main
    ```

20. **Set Upstream Branch:**

    To track a remote branch, use:
    ```
    git branch --set-upstream-to=origin/main main
    ```

21. **Push with Upstream:**

    To push the current branch and set the remote as the upstream branch, use:
     ```
     git push --set-upstream origin <local-branch>
     ```

22. **Tagging:**

    Tags are used to mark specific points in the commit history. 
    **also you can make versions for your application**

    - Show all tags:
      ```
      git tag
      ```

    - Create a tag for the last commit:
      ```
      git tag -a <tag-name or version-number> -m "Your message"
      ```

    - Create a tag for a specific commit:
      ```
      git tag -a <version-number> <commit-id> -m "Your message"
      ```

    - Search between tags (e.g., tags starting with 'v0'):
      ```
      git tag -l 'v0*'
      ```

    - Push a specific tag to the remote:
      ```
      git push origin <tag-name>
      ```

    - Push all tags to the remote:
      ```
      git push origin --tags
      ```

    - Switch to a Tag:
      ```
      git switch <tag-name>
      ```
    - Verify your tag:
      ```
      git tag -v <tag-name or version-number>
      ```

23. **GPG Keys and Commit Signing:**

    - Show all keys:
      ```
      gpg --list-keys
      ```
    - Generate a new key:
      ```
      gpg --gen-key
      ```
    - Show my secret keys:
      ```
      gpg --list-secret-keys --keyid-format LONG
      ```
    - Set your signing key for this project:
      ```
      git config user.signingKey 'your-secret-key'
      ```
    - Show your signing key for this project:
      ```
      git config user.signingKey
      ```

    - Set a global signing key for all projects:
      ```
      git config user.signingKey 'your-secret-key' --global
      ```

    - Sign your version/tag:
      ```
      git tag -s 'version-number' -m "your-message"
      ```

    - Sign your commit:
      ```
      git commit -S -m 'your-message'
      ```

    - Verify your tag:
      ```
      git tag -v 'tag-name or version-number'
      ```

24. **Blame History:**

    - Show all the change history about your file:
      ```
      git blame <file>
      ```
    - Show all the change history about your requested line in the requested file:
      ```
      git blame <file> -L5
      ```
    - Git Blame is useful for tracing the changes made to a file, and using the `-L` parameter, you can specify a specific line range to investigate. It helps in understanding who made the changes and when they were made, which can be valuable for tracking alterations, identifying contributors, and understanding the evolution of the codebase.

Remember to use these commands as needed in your Git projects. It's important to maintain a clean and organized version
control process for effective collaboration and project management.

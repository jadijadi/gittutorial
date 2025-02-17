# git-learning-notes

some notes for git learners

# Git Commands

1. **Initializing a Git Project:**

   To start a new Git repository for your project, use the following command:
   ```
   git init
   ```
    - It creates a hidden .git folder, which stores all the repository’s
    metadata (branches, commits, configurations, etc.).
    - Used when starting a new project or making an existing directory a Git
    repository.

2. **Checking the Status:**

   To view the current status of your project and its files, use:
   ```
   git status
   ```
   - Tells you which files are modified, staged, or untracked.
   - Helps you understand what changes need to be committed.

3. **Adding Files to the Staging Area:**

   Add files to the staging area to prepare them for commit. You have several options:

    - Add all (the changed) files:
      ```
      git add -A
      ```
    
    - Add specific file types, e.g., all HTML files:
      ```
      git add "*.html"
      ```

    - Add specific file :
      ```
      git add "file-name"
      ```

    - Add more than one file at the same time:
      ```
      git add “file1.txt” “file2.txt”
      ```

    - Adding any file that have "hello" in its name:
      ```
      git add “hello\*”
      ```
      
4. **Committing Changes:**

   To save the staged changes as a new snapshot, use the `git commit` command:
   ```
   git commit -m "Your comment about the changes"
   ```
    - `git commit`: You can also write this command (without adding -m "comment") and insert your comment in the editor. 
    - Always include a comment with your commit.


5. **Viewing Differences:**

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

6. **Reset and Exit the Staging Area:**

   To manipulate the state of your working directory, staging area, and commit history, you can use the `git reset`
   command:

    - To unstage a file, use:
      ```
      git reset 'filename'
      ```

    - To move the HEAD pointer to a specific commit and optionally modify the staging area and working directory, use:
      ```
      git reset --soft <commit>
      git reset --mixed <commit>
      git reset --hard <commit>
      ```

7. **Restore Files:**

   To manipulate the state of your working directory and staging area without affecting the commit history, you can use
   the `git restore` command:

    - To unstage a file, use:
      ```
      git restore --staged <file>
      ```

    - To restore a specific file from a previous commit to your working directory, use:
      ```
      git restore --source=<commit> <file>
      ```

    - To restore your entire working directory to match a specific commit, use:
      ```
      git restore --source=<commit> .
      ```

8. **Branches:**

   Managing branches is essential for collaboration and project organization. Here are some branch-related commands:

    - Show all branches in the project:
      ```
      git branch
      ```

    - Create a new branch for your project:
      ```
      git branch 'branch-name'
      ```

    - Delete a branch from the project:
      ```
      git branch -d 'branch-name'
      ```

9. **Checkout Branch and Files:**

    - To switch to a different branch and replace all the files in your current branch with those from 'branch-name',
      use:
      ```
      git checkout 'branch-name'
      ```
    - To replace a file with the version from the HEAD (latest commit), use:
      ```
      git checkout -- 'filename'
      ```
        - `'--'`: Refers to the HEAD (latest commit).


10. **Merge Branches:**

    To merge a branch into your current branch, use:
    ```
    git merge 'branch-name'
    ```

11. **View Commit History:**

    To see all the commit logs, use:
    ```
    git log
    ```

12. **Remove a File:**

    To remove a file from Git and your project, use:
    ```
    git rm 'file-name'
    ```

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
      git blame 'filename'
      ```
    - Show all the change history about your requested line in the requested file:
      ```
      git blame 'filename' -L5
      ```
    - Git Blame is useful for tracing the changes made to a file, and using the `-L` parameter, you can specify a specific line range to investigate. It helps in understanding who made the changes and when they were made, which can be valuable for tracking alterations, identifying contributors, and understanding the evolution of the codebase.

Remember to use these commands as needed in your Git projects. It's important to maintain a clean and organized version
control process for effective collaboration and project management.

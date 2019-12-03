### This is a quick reference of git commands.
#### Sorry guys, I'm to lazy to update this file. For more up to date commands, please see [README.txt](https://github.com/su6i/gittutorial/edit/master/README.txt).

1. `git init`
2. `git status`
3. `git add FILENAME`
4. `git add -A`		----------> -A: add all files
5. `git commit -S -m 'COMMENT'`		----------> -m: Comment, -S: Signing
6. `git log`
9. `git diff HEAD`
10. `git diff --staged`
11. `git reset FILENAME`
12. `git checkout -- FILENAME`
13. `git branch`
14. `git branch BRANCHNAME`
15. `git checkout BRANCHNAME`
16. `git merge BRANCHNAME`		----------> When we are in the master and want to merge files from other branches
17. `git branch -d BRANCHNAME`		----------> remove a branch
18. `git clone ADDRESS OF A GIT PAGE`
19. `git push -u origin master`
20. `git pull origin master`
21. `git config user.name "USERNAME"`		----------> for just a repository
22. `git config user.email "EMAIL ADDRESS"`		----------> for just a repository
23. `git config --global user.email`		----------> for all repositories
24. `git config --global user.name`		----------> for all repositories
25. `git config --global user.signingkey`
26. `git remote -v`		----------> for verbus
27. `git remote add origin ADDRESS OF GIT's SITE`
28. `git show COMMIT HASH`		----------> for example: 4a7b7bad55a0a16409f6603592116cc5a20e95ab
29. `git show VERSION`		----------> ex: git show v1.8, that shows signing message
30. `git tag -v VERSION`		----------> Verifying the information of signature, -v: verify
31. `git tag -a VERSION -m 'COMMENT'`		----------> Create a version number for the last verified hash log, for ex: v2.0
32. `git tag -a VERSION COMMIT HASH -m 'COMMENT'`		----------> ex: git tag -a v2.3 4a7b7bad55a0a16409f6603592116cc5a20e95ab -m 'myVersion 2.3'
33. `git tag -s VERSION COMMIT HASH -m 'COMMENT'`		----------> -s: Sign the tag version
34. `git push origin VERSION`		----------> Push tag version into remote (origin)
35. `git push origin --tags`
36. `git checkout VERSION`
37. `git config --global user.signingkey SECRET KEY`
38. `git blame FILENAME -L8`		----------> Shows who wrote each line of the codes, -L: line's number like: -L8,10
39. `git bisect start`
40. `git bisect bad`		----------> Find bugs
41. `git bisect good`
42. `git help COMMAND`		----------> find help about a COMMAND, ex: git help remote
41. `git ls-files -u` 				  ----------> HashID of 3 stages
42. `git pull remote master --allow-unrelated-histories` ----------> for resolving error "fatal: refusing to merge unrelated histories"

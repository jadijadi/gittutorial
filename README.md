This is a quick reference of git commands. ##

`git init`: 
git status
git add FILENAME
git add -A                                        ----------> -A: add all files	
git commit -S -m 'COMMENT'                        ----------> -m: Comment, -S: Signing
git log
git diff HEAD
git diff --staged
git reset FILENAME
git checkout -- FILENAME
git branch
git branch BRANCHNAME
git checkout BRANCHNAME
git merge BRANCHNAME                              ----------> When we are in the master and want to merge files from other branches
git branch -d BRANCHNAME                          ----------> remove a branch
git clone ADDRESS OF A GIT PAGE
git push -u origin master
git pull origin master
git config user.name "USERNAME"                   ----------> for just a repository
git config user.email "EMAIL ADDRESS"             ----------> for just a repository
git config --global user.email                    ----------> for all repositories
git config --global user.name                     ----------> for all repositories
git config --global user.signingkey
git remote -v                                     ----------> for verbus
git remote add origin ADDRESS OF GIT's SITE
git show COMMIT HASH                              ----------> for example: 4a7b7bad55a0a16409f6603592116cc5a20e95ab
git show VERSION                                  ----------> ex: git show v1.8, that shows signing message
git tag -v VERSION                                ----------> Verifying the information of signature, -v: verify
git tag -a VERSION -m 'COMMENT'                   ----------> Create a version number for the last verified hash log, for ex: v2.0
git tag -a VERSION COMMIT HASH -m 'COMMENT'       ----------> ex: git tag -a v2.3 4a7b7bad55a0a16409f6603592116cc5a20e95ab -m 'myVersion 2.3'
git tag -s VERSION COMMIT HASH -m 'COMMENT'       ----------> -s: Sign the tag version
git push origin VERSION                           ----------> Push tag version into remote (origin)
git push origin --tags
git checkout VERSION
------------------------------------------
gpg --list-keys
gpg --gen-key
gpg --list-secret-keys --keyid-format long        ----------> Create an electronic signature
git config --global user.signingkey SECRET KEY
------------------------------------------
git blame FILENAME -L8                            ----------> Shows who wrote each line of the codes, -L: line's number like: -L8,10
------------------------------------------
git bisect start
git bisect bad                                    ----------> Find bugs
git bisect good
------------------------------------------ 
git help COMMAND                                  ----------> find help about a COMMAND, ex: git help remote


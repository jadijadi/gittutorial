## passwordless github connection
(https://github.com/abu2020/)
#### 1. you should have cloned your repo as SSH :
 `https >> git clone https://github.com/USERNAME/REPOSITORY.git`             
 `SSH   >> git clone git@github.com:USERNAME/REPOSITORY.git`
#
#### 2. making SSH key pair:
    ssh-keygen
- skip all questions
- now you have ssh key pair in ~/.ssh/
- ( id_rsa ) > (private key)
- ( id_rsa.pub ) > (public key)
- note: now you can send your public key (id_rsa.pub) anywhere you wanna have ssh access.
#
#### 3. adding public key to your github account:
**go to:**
1. setting
2. SSH and GPG keys
3. new ssh key
4. enter a title
5. copy the content of your id-rsa.pub into the Key field
6. submit add key
7. Done
#
###### now in git push , you do not need to enter username and password.
###### its going to be done by SSH key pair, you have private key and your github account has public key.
#### DONE


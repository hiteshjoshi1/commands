## Showing the remote URL your repo is pointing to -
```
git remote get-url origin
```

## Showing the Remote which a git points - all Info
```
git remote show origin

```
## Changing the remote URL of a Repository
```
git remote set-url origin http://your_remote_git_url.git</code>
```
Example-
git remote set-url origin  git@github.com:hiteshjoshi1/microservice-docker-cart-example.git

## To delete a branch in GIT -

- Delete Local -
```
git branch -d UR_BRANCH_NAME
```
- Delete Remote -
```
git push origin  --delete UR_BRANCH_NAME
```

## Show a commit- Will show the author and timestamp
```
git show <commit_num>
```

## Show all the files in a commit :-
```
git show <commit_num> --stat
```

## AutoCRLF settings for commiting :-
```
git config --global core.autocrlf true
```

## Difference between two commit hashes :-
```
git log -p <commit_hash1> <commit_hash_2>
```

## Check Global Settings in Git :-
```
git config --global --edit
```


## Switching a git remote 
Example from bitbucket to github
- Clone the existing repo
- cd to the cloned folder
- switch the remote repo url
```
git remote add new_repo_name new_repo_url
```

-Push to the new repo
```
git push new_repo_name master
```

-Remove the old remote  ORIGIN
```
git remote rm origin
```

- rename the new_repo to ORIGIN
```
git remote rename new_repo_name origin
```


 

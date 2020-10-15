if [ -z "$(git status --porcelain)" ]; then 
    BRANCH=$(git rev-parse --abbrev-ref HEAD)
    if [[ "$BRANCH" != "main" ]]; then
        echo "Wrong branch"
        exit 1
    fi

    cowsay "First push changes to origin if not yet there..."
    git push origin

    source `dirname $0`/remotes.sh
    TMP="temporary_branch_for_remote_"
    
    for remote in ${remotes[@]}; do
        branchname="$TMP$remote"
        cowsay "Deploying new exercises to $branchname"
        git branch -d $branchname
        git checkout -b $branchname $remote/main
        git pull
        git merge origin/main
        git push $remote HEAD:main
        git checkout main
        git branch -d $branchname
    done
else
    echo "Commit changes first"
    exit 2
fi 



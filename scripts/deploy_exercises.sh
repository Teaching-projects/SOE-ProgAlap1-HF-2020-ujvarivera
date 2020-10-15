if [ -z "$(git status --porcelain)" ]; then 
    BRANCH=$(git rev-parse --abbrev-ref HEAD)
    if [[ "$BRANCH" != "main" ]]; then
        echo "Wrong branch"
        exit 1
    fi

    cowsay "First push changes to origin if not yet there..."
    git push origin

    source `dirname $0`/remotes.sh
    TMP="temporary_branch_to_deploy_to_remotes"
    
    for remote in ${remotes[@]}; do
        cowsay "Deploying new exercises to $remote"
        git branch -d $TMP
        git checkout -b $TMP $remote/main
        git merge origin/main && git push $remote HEAD:main
        git checkout main
    done
    git branch -d $TMP
else
    echo "Commit changes first"
    exit 2
fi 



source `dirname $0`/remotes.sh

TMP="temporary_branch_to_deploy_to_remotes"

for remote in ${remotes[@]}; do
    cowsay "Deploying new exercises to $remote"
    git branch -d $TMP
    git checkout -b $TMP $remote/main
    git merge origin/main && git push $remote HEAD:main
    git checkout main
done



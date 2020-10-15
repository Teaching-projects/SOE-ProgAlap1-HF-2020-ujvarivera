source `dirname $0`/remotes.sh

for remote in ${remotes[@]}; do
    cowsay "Deploying new exercises to $remote"
    git push $remote
done



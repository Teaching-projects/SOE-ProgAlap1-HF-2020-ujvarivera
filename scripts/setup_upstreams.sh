source `dirname $0`/remotes.sh

for remote in ${remotes[@]}; do
    git remote add $remote "$baseurl$remote.git"
done



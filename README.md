generator
=========
git clone git@github.com:syuvivida/generator.git

cd generator

git remote add upstream git@github.com:syuvivida/generator.git

git add scripts/powheg/run_powheg_tarball.sh

git commit -m "remove lines"

git pull --rebase upstream master

git push origin master

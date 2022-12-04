#!/bin/sh

git clone https://github.com/huggingface/transformers.git

cd transformers

echo 'commit_#,changed_files,diff_+,diff_-' > ../commit_info.csv
git log --shortstat --pretty='@%H,' | tr "\n" " " | tr "@" "\n" >> ../commit_info.csv

git log --pretty='%s' > ../commit_message.txt

cd ../

python3 get_list_of_commits.py

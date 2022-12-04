import pandas as pd
import numpy as np

def get_list_of_commits():

    df = pd.read_csv("commit_info.csv")

    df.drop("changed_files", axis=1, inplace=True)

    df.fillna(0, inplace=True)

    df['diff_+'] = df['diff_+'].str.extract('(\d+)')
    df['diff_-'] = df['diff_-'].str.extract('(\d+)')

    f = open("commit_message.txt", "r")
    messages = [line.strip() for line in f]

    df.insert(1, 'commit_message', messages)

    df.to_csv("list_of_commits.csv")

get_list_of_commits()

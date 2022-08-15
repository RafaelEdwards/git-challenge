import numpy as np 
import pandas as pd 

def main():
    df = pd.read_json('farmers-protest-tweets-2021-03-5.json',lines=True)

    print("what do you want to see?")
    print("0. Exit")
    print("1. Most retweeted tweets")
    print("2. Users with most tweets")


    choice = int(input("Enter your choice: "))
    while choice != 0:
        if choice == 1:
            print(get_most_retweeteds_tweets(df))
        elif choice == 2:
            print(get_users_with_most_tweets(df))
        else:
            print("Invalid choice")
        print("what do you want to see?")
        print("0. Exit")
        print("1. Most retweeted tweets")
        print("2. Users with most tweets")
        choice = int(input("Enter your choice: "))


def get_most_retweeteds_tweets(df):
    """
    Returns the 10 most retweeted tweet in the dataframe
    """
    return df.sort_values(by='retweetCount', ascending=False).iloc[0:10]

def get_users_with_most_tweets(df):
    """
    Returns the 10 users with the most tweets in the dataframe
    """
    return df.sort_values(by='user_id', ascending=False).iloc[0:10]


main()

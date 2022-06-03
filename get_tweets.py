import csv
import os
from twitter_util import TwitterUtil

if __name__ == "__main__":
    print("hello world")
    tw = TwitterUtil()
    olddic=[]
    with open('./data/tweets.txt', 'r',newline='',encoding='utf-8') as g:
        line = g.readline() # 1行を文字列として読み込む(改行文字も含まれる)
        while line:
            olddic.append([line.replace('\n','').replace('\'','&sing').replace('\"','&quot').replace(',','&cam')])
            line = g.readline()
    old_id=olddic[0]
    olddic.pop(0)
    #ツイート取得
    tweet_data = olddic
    count=0
    users = [os.environ["USER1"], os.environ["USER2"], os.environ["USER3"], os.environ["USER4"], os.environ["USER5"], os.environ["USER6"], os.environ["USER7"], os.environ["USER8"], os.environ["USER9"]]
    for uid in users:
        for tweet in tw.get_tweets_from_user(uid):
            if count==0:
                new_id=tweet.id
            if int(tweet.id)>int("".join(old_id)):
                tweet_data.append([tweet.text.replace('\n','').replace('\'','&sing').replace('\"','&quot').replace(',','&cam')])
            count+=1
    #txt出力
    with open('./data/tweets.txt', 'w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([new_id])
        writer.writerows(tweet_data)
    pass
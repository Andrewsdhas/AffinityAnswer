import re
import pandas as pd

def tokenize(text): 
    return re.findall(r'\w+', text.lower())

profane_tokens = {"fuck","fucker","naked"}
fd=open('tweet_sample.txt','r')
id=[]
profanity=[]
for line in fd:
    id.append(line[0:5])
    tweet=str(line[6:])
    tokens = tokenize(tweet)
    degree= sum(1 for t in tokens if t in profane_tokens) / len(tokens)
    profanity.append(degree)
    
data={'id':id,'profanity':profanity}
df=pd.DataFrame(data)
print(df)
print(id)
print(profanity)
## Example to use twitter api and call google sentiment analyzer API

from TwitterAPI import TwitterAPI
import boto3
import json
import requests

## twitter credentials
'''
Get the twitter API credentials and input below.
How to get Twitter keys:
To get Consumer Key & Consumer Secret, you have to create an app in Twitter via
https://apps.twitter.com/app/new
Then you'll be taken to a page containing Consumer Key & Consumer Secret.
'''

consumer_key = "xxxxXXXXXyyyyyYYYYYYYYYYY"
consumer_secret = "xxxxxxxxxxxxxXXXXXXXXXXXXXyyyyyyyyYYYYYYYYYYYYYYYY"
access_token_key = "xxxxxxxxxxaaaaaaaXXXXXXXXXXXYYYYYYYYYYYYYYY1111111"
access_token_secret = "xxxxxxxxxYYYYYYYYYYYaaaaaaaaaBBBBBBBBBBBBBBBBBB"


'''
Calling Twitter API, change the @google to any other twitter account name to do
sentiment analysis on the tweets for that company/entity.
Note - Twitter API parameters can be changed based on requirement, refer:
https://dev.twitter.com/rest/reference 
'''
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('search/tweets', {'q':'@google','count':10,'lang':'en','result_type':'recent'})

'''
Google Cloud Sentiment Analyzer API call
Get the API key from Google Cloud Platform:https://support.google.com/cloud/answer/6158862?hl=en
'''
headers = {'Content-type': 'application/json'}
url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=PutYourOwnKeyHerexxxxxxxxxx111111111111'

#Going through the tweets and calling sentiment API for each tweet

for item in r:
    #getting just the tweet
    x=item['text']
    print(item['text'])
    #put the tweet in data part of GCP API
    data = {
    "document":{
    "content": x ,
    "type":"PLAIN_TEXT"
    },
    "encodingType": "UTF8"
    }
    data_json = json.dumps(data)
    #calling the GCP Sentiment Analyzer API, data_json has the tweet
    response = requests.post(url, data=data_json,headers=headers)
    #printing the sentiment output
    print(json.dumps(response.json(),indent=4,sort_keys=True))
    print('******************************************************************************************')
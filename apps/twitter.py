

import requests
import os
import json
import bs4
import searchtweets


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGlDSgEAAAAAOzJ%2BwUv1YYzWEemYx4XNojd4ugE%3D8EoPqgSqf75ayJQl13Z9ICGTcr4DMjB1xBE1aYssj3C4mEhBCu'

search_url = "https://api.twitter.com/2/tweets/counts/all"



def create_url():
    tweet_fields = "tweet.fields=lang,author_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids=1278747501642657792,1255542774432063488"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = f"https://api.twitter.com/2/tweets?{ids}&{tweet_fields}"
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            f"Request returned an error: {response.status_code} {response.text}")
    return response.json()


def create_headers(bearer_token):
    return {"Authorization": f"Bearer {bearer_token}"}


def main():
    url = create_url()
    #url = "https://api.twitter.com/2/tweets/counts/recent"
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


#headers = create_headers(bearer_token)
#r = requests.get('https://api.twitter.com/2/tweets/1212092628029698048?tweet.fields=context_annotations,entities', headers=headers)





if __name__ == "__main__":
    main()



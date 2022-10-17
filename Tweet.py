import tweepy
import requests


# Authenticate to Twitter
#auth = tweepy.OAuthHandler("KEY", "SECRET_KEY")
#auth.set_access_token("TOKEN", "SECRET_TOKEN")


auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

# Create API object
api = tweepy.API(auth)

def tweet(img,msg):
	
	r = requests.get(img, allow_redirects=True)
	open('tmp.png', 'wb').write(r.content)
	api.update_with_media(filename='tmp.png',status=msg)
def tweet_tread(text):

	tmp = None
	for i in text:
		if tmp == None:

			tmp = api.update_status(status=i)
		else:

			tmp = api.update_status(status=i, in_reply_to_status_id=tmp.id, auto_populate_reply_metadata=True)



if __name__ == "__main__":
	pass

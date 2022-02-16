import tweepy
import requests


# Authenticate to Twitter
#auth = tweepy.OAuthHandler("KEY", "SECRET_KEY")
#auth.set_access_token("TOKEN", "SECRET_TOKEN")


auth = tweepy.OAuthHandler("9f9YFxGNALK6Fq4xyzrdjZo6E", "ZoLexDlcoI9lD5yVcborHoDg5KqfNNe6EezNHB0er1IZ1vD3Qb")
auth.set_access_token("1493936998519824384-trdrlTrLrpawc9Sf0hDeUpQM56Ynlh", "JRWOoAfxx2cO91G9GWkN3ByN09q1HEdBL0lNxflDDHZpg")

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

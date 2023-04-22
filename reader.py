import serial
import pygame
import tweepy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def email_setup():
	#TODO #recv info from user in pygame
	sender = "mrsbearrealofficial@gmail.com"
	password = "cxybmstangojtvnq"
	print("email to send photos to?")
	recipients = input()
	recipients = "mrsbearrealofficial@gmail.com"
	return sender, password, recipients

def send_email(subject, body, sender, recipient, password, image_path):
	with open(image_path, 'rb') as f:
		image_part = MIMEImage(f.read())
	
	message = MIMEMultipart()
	message['Subject'] = subject
	message['From'] = sender
	message['To'] = recipient
	html_part = MIMEText(body)
	message.attach(html_part)
	message.attach(image_part)

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(sender, password)
	server.sendmail(sender, recipient, message.as_string())
	server.quit()


def tweet():
    access_key = "1649858249120686082-KSUIFWs7rJnlVWQhVmX0VV3qOiaYg8"
    access_secret = "vvUThkWbA5eOLA86KsehG56n56sTwone1Wc0tKZz1EcbV"
    bear = "AAAAAAAAAAAAAAAAAAAAAJKrmwEAAAAA88qNm544CN69%2B8mBzA%2BwvnuEEZI%3D6mdAaxVopiIZCV67gsRiJEUMxP6p831NfWALdMH9GNReIX5d2s"
    client_id = "MFhPLVdDMnl4QjBNWFF3S2RFLW06MTpjaQ"
    client_secret = "zbrhZubMYxmd26im52ru_LlJ67vlREObHTXgURdteP6BF6n7La"

    # auth = tweepy.OAuth2AppHandler(access_token, access_token_secret)
    # auth = tweepy.OAuth2BearerHandler(bear)
    # auth = tweepy.OAuth2AppHandler(access_token, access_token_secret)

    client = tweepy.Client(bearer_token=bear)
    # Pull tweets from twitter
    query = '#elonmusk -is:retweet lang:en'
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)
    # client.create_tweet(text="Hi testing", user_auth=False)

    # try:
    #     api.verify_credentials()
    #     print("Authentication OK")  
    # except:
    #     print("Error during authentication")

    return


def main():
	
	#set serial input port
	#ser = serial.Serial('/dev/cu.usbserial-546F1153241', 115200)
		
	# initialize the game
	pygame.init()
	pygame.display.set_caption("BE(A)Real")
	screen = pygame.display.set_mode((800,600))
	clock = pygame.time.Clock()

	tweet()
	running = True
	
	subject = "subject"
	body = "includes image"
	image_path = "cat.jpg"
	sender, password, recipients = email_setup()
	# send_email(subject, body, sender, recipients, password, image_path)
        

	while(running):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			#https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
		

		#setup: choose twitter or email, enter user auth
		#if ():
		#	twitter_setup()
		#else:
		#	email_setup()

		#if recieve serial input
			#if picture, start countdown clock

			#if button, wait 1 minute


		clock.tick(60)


if __name__ == "__main__":
	main()
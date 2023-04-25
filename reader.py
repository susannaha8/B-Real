import serial
import pygame
import tweepy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def send_email(recipient, image_path):
	subject = "subject"
	body = "includes image"
	sender = "mrsbearrealofficial@gmail.com"
	password = "cxybmstangojtvnq"
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

    #client = tweepy.Client(bearer_token=bear)
    # Pull tweets from twitter
    #query = '#elonmusk -is:retweet lang:en'
    #tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)
    # client.create_tweet(text="Hi testing", user_auth=False)

    # try:
    #     api.verify_credentials()
    #     print("Authentication OK")  
    # except:
    #     print("Error during authentication")

    return

def button(msg,x,y,w,h,ic,ac,screen,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    #https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
    #smallText = pygame.font.SysFont("comicsansms",20)
    #textSurf, textRect = text_objects(msg, smallText)
   #textRect.center = ( (x+(w/2)), (y+(h/2)) )
    #screen.blit(textSurf, textRect)

def email_setup(screen):
    font = pygame.font.SysFont(None, 25)
    text = font.render("{}".format(word), True, "red")
    screen.blit(text,(300,400))
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    word+=str(chr(event.key))
                if event.key == pygame.K_b:
                    word+=chr(event.key)
                if event.key == pygame.K_c:
                    word+=chr(event.key)
                if event.key == pygame.K_d:
                    word+=chr(event.key)
                if event.key == pygame.K_RETURN:
                    done=False
                #events...
    return word

def main():
	
	#set serial input port
	#ser = serial.Serial('/dev/cu.usbserial-546F1153241', 115200)
		
	# initialize the game
	pygame.init()
	pygame.display.set_caption("BE(A)Real")
	screen = pygame.display.set_mode((800,600))
	clock = pygame.time.Clock()

	#tweet()
	running = True
	
	#set up authentification information
	#recipient = email_setup(screen)

	#periodically send image
	image_path = "cat.jpg"
	# send_email(recipient, image_path)

	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render('Welcome to BE(A)Real!', True, "black", "white")
	textRect = text.get_rect()
	textRect.center = (400 // 2, 300 // 2)
        

	while(running):
		
		screen.fill("white")

		screen.blit(text, textRect)

		#button("email",150,450,100,50,"green","blue", screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			pygame.display.update()


		clock.tick(60)


if __name__ == "__main__":
	main()

#https://stackoverflow.com/questions/27713855/how-to-get-an-input-from-user-in-pygame-and-save-it-as-a-variable

			#https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
		

		#setup: choose twitter or email, enter user auth
		#if ():
		#	twitter_setup()
		#else:
		#	email_setup()

		#if recieve serial input
			#if picture, start countdown clock

			#if button, wait 1 minute
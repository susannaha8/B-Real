import serial
import pygames
import tweepy
import smtplib

def email_setup():
	#TODO #recv info from user in pygame
	email = "email"
	password = "password"
	recv_email = "recv_email"
	return email, password, recv_email

def email_send(email, password, recv_email, message): #message is photo recv from serial
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
 
	# start TLS for security
	s.starttls()
 
	# Authentication
	s.login(email, password)
 
	# sending the mail
	s.sendmail(email, recv_email, message)
 
	# terminating the session
	s.quit()


def main():
	
	#set serial input port
	ser = serial.Serial('/dev/cu.usbserial-546F1153241', 115200)
		
	# initialize the game
	pygame.init()
	pygame.display.set_caption("BE(A)Real")
	screen = pygame.display.set_mode((800,600))
	clock = pygame.time.Clock()


	running = True

	while(running):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			#https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
		
		#setup: choose twitter or email, enter user auth
		if ():
			twitter_setup()
		else:
			email_setup()

		#if recieve serial input
			#if picture, start countdown clock

			#if button, wait 1 minute


		clock.tick(60)


if __name__ == "__main__":
	main()
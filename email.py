from bs4 import *
import requests
import os
 
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
        

# CREATE FOLDER
def folder_create(images, url):


	folder_name = "images"
	# folder creation
	try:
		os.mkdir(folder_name)
	except:
		pass
 
    	# image downloading start
	download_images(images, folder_name, url)

 
 
# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name, url):

    found = 0
    # checking if images is not zero
    if len(images) != 0:
        print(len(images))
        while(not found):
            for i, image in enumerate(images):
                # From image tag ,Fetch image Source URL
    
                            # 1.data-srcset
                            # 2.data-src
                            # 3.data-fallback-src
                            # 4.src
    
                # Here we will use exception handling
    
                # first we will search for "data-srcset" in img tag
                try:
                    print(image)
                    # In image tag ,searching for "data-srcset"
                    image_link = image["data-srcset"]
                    
                # then we will search for "data-src" in img
                # tag and so on..
                except:
                    try:
                        # In image tag ,searching for "data-src"
                        image_link = image["data-src"]
                    except:
                        try:
                            # In image tag ,searching for "data-fallback-src"
                            image_link = image["data-fallback-src"]
                        except:
                            try:
                                # In image tag ,searching for "src"
                                image_link = image["src"]
    
                            # if no Source URL found
                            except:

                                pass
    
                # After getting Image Source URL
                # We will try to get the content of image
                try:
                    if image_link is not None:
                        print("found!")
                        #print(image_link)
                        found = 1   
                    r = requests.get(url + image_link).content
                    try:
    
                        # possibility of decode
                        r = str(r, 'utf-8')
                        print(r)

    
                    except UnicodeDecodeError:
    
                        # After checking above condition, Image Download start
                        with open(f"images/picture.jpg", "wb+") as f:
                            f.write(r)
    
                        # counting number of image downloaded
                        count += 1
                except:
                    pass


 
# MAIN FUNCTION START
def main(url):
   
    # content of URL
    r = requests.get(url)
 
    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')
 
    # find all images in URL
    images = soup.findAll('img')
 
    # Call folder create function
    folder_create(images, url)

    send_email("mrsbearrealofficial@gmail.com", "images/picture.jpg")


 
 
# take url
url = input("Enter URL:- ")
 
# CALL MAIN FUNCTION
main(url)

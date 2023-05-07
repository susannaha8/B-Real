# B-Real

In this project, we used an ESP32CAM, specifically the ESP32-Wrover-Dev, to take one photo during a timed study session and display the photo on a website. The code is mainly adapted from https://randomnerdtutorials.com/esp32-cam-take-photo-display-web-server/. 

## Hardware Setup

Connect the camera itself to the ESP32 and use a Micro USB to USB cable to connect the ESP32 to a computer. You also may need to set up a hotspot that both the ESP32 and the device that you want to display the website on are connected to. Once the code is flashed to the ESP32, you can use a portable battery or any other device to power the ESP32. This is all that is needed for hardware setup!

## Software Setup

### Install Libraries

### How does the code work?

The code begins by initing the camera, starting the web server, and mounting SPIFFS, a file system for the ESP32. On a GET request from a client (ex. a browser trying to reach the webpage), the ESP32 sends an HTML page saved in the variable `index_html`. When the client clicks one of the timer buttons, the `timer()` function begins. After some time, the `capturePhoto()` function in the HTML is called, which allows the ESP32 to change the `takeNewPhoto` flag and `capturePhotoSaveSpiffs()` gets called on the ESP32 and takes the photo. After the timer is up, a new button appears that refreshes the page and the photo appears. 

### Modify the Code

For the code to work on your device, adjust the `ssid` and `password` with your network information, and you may need to adjust the pins for the camera. Finally, if you prefer different time options for studying, go into the block of html and adjust the input parameter for the `timer()` function. 


## Additional Code: Photos via Email


## Usage

Upload the code to your ESP32 and click the button on it. Now the server is up, and the IP address that you need to use to connect to the server is displayed in Arduino. Go to that address (ex. http://172.20.10.7) and you should see the BE(A)Real homepage. Face the bear with the ESP32 toward you and select either the 30 minute timer or the 60 minute timer. Once clicked, the timer will begin and you can begin studying. After the timer is up, click "get photo" to view the image that was taken of you while you were studying. You can download this image with the button at the bottom of the page.

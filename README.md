# Twitch-Cut-Stream-Downloader

A program that allows you to cut and download the streams you watch on the Twitch platform. So you don't have to download entire stream.
# İmportant!!
You have to download ffmpeg packeges here: [ffmpeg](https://we.tl/t-AjLlef0iBq) 
After that, put ffmpeg on project files directory **../Twitch-Cut-Stream-Downloader/**

# Install
You can get project with: "**git clone https://github.com/FatihTheConqueror/Twitch-Cut-Stream-Downloader.git**"

# How can you use project

## Chrome settings:
If you start the program for the first time, you have to set your chrome setting into program.
![alt text](https://i.hizliresim.com/rdhr25m.png)

You can find your chrome settings in **chrome://version** link.
![alt text](https://i.hizliresim.com/q1qxivx.png)

Now, you completed your chrome settings..

## Requirements For Twitch
If you want to download a twitch stream, you've log in your twitch account in your chrome browser and you have to **and be sure that you stream is available for taking a clip**. 
If you've already logged in your twitch account in your browser, it will be in your ChromeProfile already.
-There are some requirements to get a clip from certain streamers. For instance, you have subscribe or follow them. Please be sure that you can get a clip from the stream..

## How to use

First, you have to get stream_id from the stream link. you can find it here.
![alt text](https://i.hizliresim.com/osqovhg.png)

After that you have tu put stream_id, start stream minute by hour:minute:second, end stream minute by hour:minute:second and the name of file that will be named.

![alt text](https://i.hizliresim.com/iajvpae.png)

Now program is ready. 

Program is getting clips then merge them. The clips are 90 seconds. Program is getting them by one by after them merging clips and giving you mergered video file.
We want a video that has 4 minute. So program will get 3 clips and they're equals 4.5 minute. Then it will cutting the excess part and will give us the 4 minute version of video


Here is program tells you how many clips will be created

![alt text](https://i.hizliresim.com/sj84957.png)


After getting clips, program will download those clips.

![alt text](https://i.hizliresim.com/gltoijl.png)

When clips download progress is finished, program is starting to merge clips.

![alt text](https://i.hizliresim.com/7vtg3nl.png)

After that, you already got the video file :)

![alt text](https://i.hizliresim.com/ikstuq0.png)

Videos are saved in your windows desktop by default. If you want to change save directory, you can change it in **merger.py** file.

# About the program

Program is using your chrome browser for progress.
You cannot acces to your browser untill progress finish. And you can view the progress in your chrome browser.


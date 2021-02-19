# What is this?
This is an Android app. It consists of two parts:
 
The frontend (written in Java).
The backend (the server) (written in Python).
 
# Frontend
Under the directory "Partyholic (frontend)"  

Preview:  
![Markdown Logo](https://i.postimg.cc/C1fThqTJ/7261343d-080e-48bd-b8e2-80a54d1c7216.jpg)
## What it is
This is the frontend of Partyholic. This is the part that the user gets the .apk file (you can find it in the repo, 
named "Partyholic 0.1.0.apk) of.
It is done using Android Studio. So, we recommend using it to check it out. Since Android Studio has its own way of 
showing the project files, it will show you the structure of the project in the best way possible.
The layout files under the directory "Partyholic (frontend)\app\src\main\res\layout" specify how the activities
of the app look like. The .java files under "Partyholic (frontend)\app\src\main\java\p\p" have the functionality of the
app.  

## Installation
- Install Android Studio
- Configure Java in your Android Studio:
>The project was made with the following setting:
>
>java version "1.8.0_281"  
>Java(TM) SE Runtime Environment (build 1.8.0_281-b09)  
>Java HotSpot(TM) 64-Bit Server VM (build 25.281-b09, mixed mode)` 
- [Get an API-key from Google.](https://developers.google.com/maps/documentation/embed/get-api-key "visit https://developers.google.com/maps/documentation/embed/get-api-key")
- Open the file "local.properties" which is located in "Partyholic (frontend)"
- Insert your API-key directly after "MAPS_API_KEY=" in the same line.
- Insert your Java SDK directory directly after "sdk.dir=" in the same line.
- Open the project.

# Backend
Under the directory "Partyholic (backend)"

## What this server is
This is a backend server for Partyholic.
The client sends an image "poster of a Party" and the server returns the extracted details.

## Description
_this server runs on Flask framework and wait for an HTTPS connection from the app in a POST method.
The Body of the request should have an image encoded in binary format.
The response will be a .json file. The file includes the extracted data which is address, date, time, and the coordinates of the party._ 

## Before instalation
- This server uses an OCR-API for transforming the image into a String.
And for this you need to [get a free API-KEY for OCR-API](https://ocr.space/ocrapi "visit ocr.space").
- Open the file image_processing.py
- Replace the empty string in the variable api_key with your API-KEY.

## Running it locally:
- Clone the repo onto your machine.
- Open the project folder via Pycharm or any IDE. 
- Create a new environment for Python (This demo is based on Python 3.8.5) 
- Install the required packages which is in requirements.txt
```bash
pip install -r requirements.txt
```
- Run the file "main.py" 
- Test it independently from the frontend part, using [Postman](https://www.postman.com/).

### Running it on Heroku:
- Create an account on [Heroku](https://id.heroku.com/ "go to Heroku") or login if you have one :
- Create a new app on Heroku and give it a name.
- Open the Terminal in the directory where you cloned the repo from Github.
- Login into your Heroku account:
```bash
heroku login
```
- Give your credentials  
- Run the commands:
```bash
heroku git:remote -a <name of the app on Heroku that you chose>
git push heroku main
```
- And now the server should be running on Heroku.

## Usages example (locally)
![Markdown Logo](https://i.postimg.cc/ZnPGNxMK/Screenshot-from-2021-02-18-21-21-51.png)
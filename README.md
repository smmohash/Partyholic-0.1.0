# What this Server about

this is a backend server for an android app .
the Client sends an image "Brochure of a Party" and the Server return 
the extracted details.

# Description
_this Server run Flask framework and wait for an HTTPS connection from the app in POST method
the Body of the request should have an image in a binary format coded 
The response will be a json file include the extracted data which is address, date, time, and the coordinate of the Party_ 

# Before instalation
This Server use an OCR-API for transforming the image into a String

get a free api_key from the link:

[Link to home page of OCR-API](https://ocr.space/ocrapi "got to ocr.space")

open the file image_processing.py

replace the empty string in the variable api_key with

your API-KEY which you get from the link above

# How to install 

After cloning the repo on your local machine

### RUN IT LOCALLY : 

open the Project folder via Pycharm or any IDE 

create a new environment for python (this demo based on Python 3.8.5) 

install the required packages which is in requirements.txt

```bash
pip install -r requirements.txt
```
run the main.py 

and now you can test it with postman !

### RUN IT ON HEROKU :

create an account on Heroku or login if you have one :

[link to Heroku](https://id.heroku.com/ "go to Heroku")

create a new app on Heroku and give it a name.

open the Terminal in the directory where you clone the repo from github

login to Heroku :

```bash
heroku login
```
give your credential  

Run the commands :
```bash
heroku git:remote -a <name of the app on Heroku>
git push heroku main
```
And now should the server running on Heroku.




# Usages example 

### testing the server locally 

![Markdown Logo](https://i.postimg.cc/ZnPGNxMK/Screenshot-from-2021-02-18-21-21-51.png)
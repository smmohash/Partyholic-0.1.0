import json
from PIL import Image
import os
import requests
import re
from geopy.geocoders import Nominatim

# put your API-KEY heer
api_key = ''

# send a request to the OCR-API
# and receive the response which has the extracted text from the image
def get_text(file_name: str):
    url_api = "https://api.ocr.space/parse/image"  # url-api
    payload = {'isOverlayRequired': False,  # payload api
               'apikey': api_key,
               'language': 'ger',
               }
    # sending the request to the api
    with open(file_name, "rb") as f:
        result = requests.post(url_api,
                               files={file_name: f},
                               data=payload
                               )
    result = result.content.decode()
    json_object = json.loads(result)
    text_result = json_object.get("ParsedResults")[0].get("ParsedText")
    return text_result

# receive the image from the client (our mobile app)
def get_image(request):
    data = request.get_data()
    file_name = request.remote_addr
    with open(str(file_name) + ".jpg", "wb") as f:
        f.write(data)
    return str(file_name) + ".jpg"


def get_image_less_than_1MB(file_name: str) -> str:
    file_size = os.stat(file_name).st_size  # determine the size of th image in bytes
    quality = 60
    while file_size > 1000000:  # while the image size more then 1 MB
        image = Image.open(file_name)  # open the old image
        image.save("compressed-" + file_name, optimize=True, quality=quality)  # save the new low quality image
        file_size = os.stat("compressed-" + file_name).st_size  # determine the new file size
        quality -= 10  # try with less quality
    file_name = "compressed-" + file_name
    return file_name

# extract the coordinate of the address
def get_coordinate(adress):
    geolocator = Nominatim(user_agent="Partyholic")
    location = geolocator.geocode(adress)
    if location == None:
        return None
    else:
        location_address = location.address
        location_latitude = location.latitude
        location_longitude = location.longitude
    return (location_latitude,location_longitude)


# make the text in one line
def get_clean_text(text: str) -> str:
    text = text.replace('\n', " ")
    text = text.replace('\t', " ")
    text = text.replace('\r', "")

    return text


# getting the address
def get_address(clean_string: str) -> str:
    # [^\W_]+ instate of [A-Za-Z]+ to match also a non english caracters
    # the Post code in germany is always 5 digits
    # to catch the addresses which include (STR oder Straße ..) the most german adresses ends with "straße"
    adress_pattern1 = re.compile(
        r'\b[^\W_]+\s?(STR|str|Str|Straße|straße)\.?\s?\d+\w?\s?(,|.|-)?\s?\d{5}\s?[^\W_]+'
        , re.IGNORECASE)
    adress_matche1 = adress_pattern1.search(clean_string)
    # to catch the addresses which include ( an , am,.. ) in the street name EX : "An der Bicke"
    adress_pattern2= re.compile(
        r'\b(an|am|auf|bei|beim|zum|zur|zu)\s?[^\W_]+\s?[^\W_]+?\s?\.?\s?\d+\w?\s?(,|.|-)?\s?\d{5}\s?[^\W_]+'
        , re.IGNORECASE)
    adress_matche2=adress_pattern2.search(clean_string)
    # to catch the addresses which include (weg) EX : "Zweiweiherweg "
    adress_pattern3= re.compile(
        r'\b[^\W_]+\s?(weg|hof|alle|berg|berger|sieglung|ring|platz|damm|gasse|dorf)\s?[^\W_]{0,10}\s?\.?\s?\d+\w?\s?(,|.|-)?\s?\d{5}\s?[^\W_]+'
        , re.IGNORECASE)
    adress_matche3=adress_pattern3.search(clean_string)
    # the general case
    adress_pattern4 = re.compile(
        r'\b[^\W_]+\s?\.?\s?\d+\w?\s?(,|.|-)?\s?\d{5}\s?[^\W_]+'
        , re.IGNORECASE)
    adress_matche4 = adress_pattern4.search(clean_string)


    if adress_matche1 != None:
        return adress_matche1.group()
    elif adress_matche2 !=None:
        return adress_matche2.group()
    elif adress_matche3 !=None:
        return adress_matche3.group()
    elif adress_matche4 !=None:
        return adress_matche4.group()
    else:
        return "Unknown"


# getting the date
def get_date(clean_string: str) -> str:  # returned as dd.dd.dddd
    # if the date has just digits
    date_pattern1 = re.compile(r'\b(\d{2})\s?([.\-/])\s?(\d{2})\s?([.\-/])\s?(\d{4})', re.IGNORECASE)
    date_matche1 = date_pattern1.search(clean_string)
    # if the date have digit and month name
    date_pattern2 = re.compile(r'\b(\d{2})\s?([.\-/])\s?([^\W_]+)\s?([.\-/])\s?(\d{4})', re.IGNORECASE)
    date_matche2 = date_pattern2.search(clean_string)

    if date_matche1 != None:
        return date_matche1.group(1) + "." + date_matche1.group(3) + "." + date_matche1.group(5)
    elif date_matche2 != None:
        return date_matche2.group(1) + "." + \
               month_string_to_number(date_matche2.group(3)) + "." \
               + date_matche2.group(5)
    else:
        return "Unknown"


# getting the time
def get_time(clean_string: str) -> str:
    time_pattern1 = re.compile(r'\b\s?(UM|Um|um)?\s?(\d{2}:\d{2})\s?(UHR|Uhr|uhr)',
                               re.IGNORECASE)  # (uhr) is an important factor
    time_matche1 = time_pattern1.search(clean_string)

    time_pattern2 = re.compile(r'\b\s?(UM|Um|um)?\s?(\d{2})\s?(UHR|Uhr|uhr)',
                               re.IGNORECASE)  # (uhr) is an important factor
    time_matche2 = time_pattern2.search(clean_string)

    if time_matche1 != None:
        return time_matche1.group(2)
    elif time_matche2 != None:
        return time_matche2.group(2) + ":00"
    else:
        return "Unknown"


# help function to replace the month names with their number
def month_string_to_number(string):
    m = {
        "jan": "01",
        "feb": "02",
        "mär": "03",
        "apr": "04",
        "mai": "05",
        "jun": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "okt": "10",
        "nov": "11",
        "dez": "12"
    }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError("Not a month")

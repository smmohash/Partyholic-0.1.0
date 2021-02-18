# v2
import os
from flask import Flask, request, jsonify
import image_processing

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    # define an empty dict to store the result in it
    result_dict = {}
    # check if the data is present
    if (not request.data):
        return "No data was sent !"
    # getting the image from client
    image_name = image_processing.get_image(request)

    # check if the file less than 1 MB
    if os.stat(image_name).st_size > 1000000:
        # reduce the size of the received image and delete the old one
        new_image_name = image_processing.get_image_less_than_1MB(image_name)
        os.remove(image_name)
    else:
        new_image_name = image_name

    # extract the text from the image through an api
    extracted_text = image_processing.get_text(new_image_name)
    print("extracted_text", extracted_text)
    # get a clean text without (\n) or (\t)
    clean_text = image_processing.get_clean_text(extracted_text)

    # extract the address,date,time from the clean text
    address = image_processing.get_address(clean_text)
    date = image_processing.get_date(clean_text)
    time = image_processing.get_time(clean_text)
    # trying to extract the geocode of the address if it is not "Uknown"
    if address =="Unknown" or image_processing.get_coordinate(address)== None:
    # no coordinate are found
        result_dict.update({"address": address,
                                "date": date,
                                "time": time,
                                "coordinatesAreValid": 0
                            })
    # coordinate are found
    else:
        coordinate=image_processing.get_coordinate(address)
        result_dict.update({"address": address,
                                "date": date,
                                "time": time,
                                "coordinatesAreValid": 1,
                                "coordinate": {
                                "latitude": coordinate[0],
                                "longitude": coordinate[1]
                                }})

    # delete the second image if it exist
    if os.path.exists(new_image_name):
        os.remove(new_image_name)

    # return the result to the frontend
    return jsonify(result_dict)


@app.route('/', methods=['GET'])
def index():
    return "<h1>No POST request found !! Please send an image with Post method</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

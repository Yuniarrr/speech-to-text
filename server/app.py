from flask import Flask, jsonify, request
from flask_cors import CORS
import speech_recognition as sr
from pydub import AudioSegment
import io
import json
import fleep
import requests
import pymongo
from geopy.distance import geodesic

# from google.cloud import speech

app = Flask(__name__)
CORS(app)

# Set path to FFmpeg
AudioSegment.ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"


def replace_id(obj):
    # Replace mongodb _id parameter with an id parameter
    if obj.get('_id'):
        id = str(obj.get('_id'))
        del obj['_id']
        obj['id'] = id

    return obj


@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        transcript = ""
        if "file" not in request.files:  # no file exist/ uploaded
            print(" Debug: Line 1")
            # return redirect(request.url)  # redirect the user to the home page

        file = request.files['file']  # if file exist it will give me that file
        lang = request.form['voiceSelect']
        lang = lang.replace("\"", "")
        print(f"lang: {lang}")
        if file.filename == "":  # if file is blank/empty, return to the main page
            print(" Debug: Line 2")
            # return redirect(request.url)

        # convert the file to wav
        if file.filename.endswith('.mp3'):
            file = io.BytesIO(file.read())
            file = AudioSegment.from_file(file, format="mp3")
            file = file.export(format="wav")

        if file:
            print(" Debug: Line 3")
            recognizer = sr.Recognizer()  # initilaize instance of the speech recognition class
            audioFile = sr.AudioFile(file)  # pass in the file
            with audioFile as source:  # reading the file
                data = recognizer.record(source)  # through the recognizer
            # using Google API will return the
            transcript = recognizer.recognize_google(
                data, key=None, language=lang, show_all=False)

        return jsonify({'text': transcript})

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400


@app.route('/products/search/<string:text>', methods=['POST'])
def search(text):
    try:
        coordinates = request.json['coordinates']
        latitude = coordinates['latitude']
        longitude = coordinates['longitude']

        # connect to api search
        api_endpoint = "https://magneto.api.halodoc.com/api/v1/buy-medicine/products/search/" + \
            text+"?page=1&per_page=100"
        data = requests.get(api_endpoint).json()

        next_page = data['next_page']
        result = data['result']
        total_count = data['total_count']
        total_hits = data['total_hits']

        # connect to database
        client = pymongo.MongoClient(
            "mongodb://user:pass1234@localhost:27017/")
        db = client["halodoc"]
        collection = db["medicine"]
        items = []
        for item in collection.find():
            items.append(replace_id(item))

        temps = []
        # check data
        for slug_res in result:
            for slug_db in items:
                if slug_res['slug'] in slug_db['slug']:
                    temp = {}
                    temp.update(slug_res)
                    temp.update(slug_db)
                    temp['distance'] = geodesic(
                        (latitude, longitude), temp['coordinate']).kilometers
                    temp['distance'] = ('%.2f' % temp['distance'])
                    temps.append(temp)

        return jsonify({'result': temps, 'next_page': next_page, 'total_count': total_count, 'total_hits': total_hits}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400


@app.route('/products/detail/<string:text>', methods=['POST'])
def detail(text):
    try:
        coordinates = request.json['coordinates']
        latitude = coordinates['latitude']
        longitude = coordinates['longitude']

        # connect api to detail product
        api_endpoint = "https://magneto.api.halodoc.com/api/v1/buy-medicine/products/detail/"+text
        data = requests.get(api_endpoint).json()

        # connect to database
        client = pymongo.MongoClient(
            "mongodb://user:pass1234@localhost:27017/")
        db = client["halodoc"]
        collection = db["medicine"]
        items = []
        for item in collection.find():
            items.append(replace_id(item))

        # check data
        for slug_db in items:
            if text in slug_db['slug']:
                temp = {}
                temp.update(data)
                temp.update(slug_db)
                temp['distance'] = geodesic(
                    (latitude, longitude), temp['coordinate']).kilometers
                temp['distance'] = ('%.2f' % temp['distance'])
                data = temp
                break
        return data, 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400


@app.route('/categories/all', methods=['GET'])
def categories():
    try:
        # connect api to detail product
        api_endpoint = "https://magneto.api.halodoc.com/api/v1/buy-medicine/categories/list/l1-categories"
        data = requests.get(api_endpoint).json()
        return data, 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400


@app.route('/categories/<string:text>/subcategories', methods=['GET'])
def subcategories(text):
    try:
        # connect api to detail subcategories
        api_endpoint = f"https://magneto.api.halodoc.com/api/v1/buy-medicine/categories/slug/{text}/sub-categories"
        data = requests.get(api_endpoint).json()
        return data, 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400


@app.route('/categories/<string:text>/products', methods=['POST'])
def subcategories_product(text):
    try:
        coordinates = request.json['coordinates']
        latitude = coordinates['latitude']
        longitude = coordinates['longitude']

        api_endpoint = f"https://magneto.api.halodoc.com/api/v1/buy-medicine/categories/{text}/products?page=1&size=20"
        data = requests.get(api_endpoint).json()

        next_page = data['next_page']
        result = data['result']
        total_count = data['total_count']
        total_hits = data['total_hits']

        # connect to database
        client = pymongo.MongoClient(
            "mongodb://user:pass1234@localhost:27017/")
        db = client["halodoc"]
        collection = db["medicine"]
        items = []
        for item in collection.find():
            items.append(replace_id(item))

        temps = []
        # check data
        for slug_res in result:
            for slug_db in items:
                if slug_res['slug'] in slug_db['slug']:
                    temp = {}
                    temp.update(slug_res)
                    temp.update(slug_db)
                    temp['distance'] = geodesic(
                        (latitude, longitude), temp['coordinate']).kilometers
                    temp['distance'] = ('%.2f' % temp['distance'])
                    temps.append(temp)

        return jsonify({'result': temps, 'next_page': next_page, 'total_count': total_count, 'total_hits': total_hits}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400


@app.route('/database', methods=['GET'])
def database():
    try:
        myclient = pymongo.MongoClient(
            "mongodb://user:pass1234@localhost:27017/")
        mydb = myclient["halodoc"]
        mycol = mydb["medicine"]
        items = []
        for item in mycol.find():
            items.append(replace_id(item))
        return jsonify(items)

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)

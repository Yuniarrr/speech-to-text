from flask import Flask, jsonify, request
from flask_cors import CORS
import speech_recognition as sr
from pydub import AudioSegment
import io
from google.cloud import speech

app = Flask(__name__)
CORS(app)

# Initialize the recognizer
r = sr.Recognizer()

# Set path to FFmpeg
AudioSegment.ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"


@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        transcript = ""
        if "file" not in request.files:  # no file exist/ uploaded
            print(" Debug: Line 1")
            # return redirect(request.url)  # redirect the user to the home page

        file = request.files['file']  # if file exist it will give me that file
        if file.filename == "":  # if file is blank/empty, return to the main page
            print(" Debug: Line 2")
            # return redirect(request.url)

        if file:
            print(" Debug: Line 3")
            recognizer = sr.Recognizer()  # initilaize instance of the speech recognition class
            audioFile = sr.AudioFile(file)  # pass in the file
            with audioFile as source:  # reading the file
                data = recognizer.record(source)  # through the recognizer
            # using Google API will return the text
            transcript = recognizer.recognize_google(data, key=None)

        return jsonify({'text': transcript})

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)

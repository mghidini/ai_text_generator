from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
from openai import OpenAI
import os
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the key from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

# Set OpenAI API key
client = OpenAI(api_key=OPENAI_API_KEY)

#Define endpoint to generate a poem
@app.route('/generate-poem', methods=['GET'])
def generate_poem():
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Write a short poem in rhyme. Make sure it ends completely with a rhyming word.",
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].text)
    return jsonify({"poem": response.choices[0].text})

@app.route('/generate-recipe', methods=['GET'])
def generate_recipe():
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Write a short and simple recipe. Make sure it ends completely.",
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].text)
    return jsonify({"recipe": response.choices[0].text})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
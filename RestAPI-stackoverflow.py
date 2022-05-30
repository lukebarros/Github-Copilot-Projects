'''RESTAPI for stackoverflow questions'''
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from pymongo import MongoClient
import requests
import json
import re
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient()
db = client.stackoverflow

@app.route('/api/v1/questions', methods=['POST'])
def create_question():
    '''Create a new question'''
    if not request.json or not 'title' in request.json:
        abort(400)
    question = {
        'title': request.json['title'],
        'body': request.json.get('body', ''),
        'tags': request.json.get('tags', []),
        'author': request.json.get('author', ''),
        'comments': []
    }
    db.questions.insert_one(question)
    return jsonify({'question': question}), 201


@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    '''Get all questions'''
    questions = db.questions.find()
    return jsonify({'questions': [question for question in questions]})

@app.route('/api/v1/questions/<question_id>', methods=['GET'])
def get_question(question_id):
    '''Get a question by id'''
    question = db.questions.find_one({'_id': ObjectId(question_id)})
    if question is None:
        abort(404)
    return jsonify({'question': question})


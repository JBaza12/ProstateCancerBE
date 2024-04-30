from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from auth_middleware import token_required
from model.users import User
from datetime import datetime

prostate_quiz_api = Blueprint('prostate_quiz_api', __name__,
                              url_prefix='/api/prostate-quiz')

api = Api(prostate_quiz_api)

class ProstateQuizAPI:
    class _Quiz(Resource):
        def post(self):
            data = request.get_json()
            answers = data.get('answers')
            
            if not answers:
                return {'error': 'No answers provided'}, 400
            
            num = 0
            for answer in answers:
                if answer.lower() == 'yes' or answer.lower() == "Yes":
                    num += 1
                elif answer.lower() == 'no' or answer.lower() == 'No':
                    num = num
                else:
                    result = 'Please enter yes or no.'
            
            result = ""
            if num <= 9 and num >= 7:
                result = 'You have a high probability of having prostate cancer.'
            elif num < 7 and num >= 4:
                result = 'You have a moderate probability of having prostate cancer.'
            else:
                result = 'You have a low probability of having prostate cancer.'
            
            return jsonify({'result': result})

    api.add_resource(_Quiz, '/')
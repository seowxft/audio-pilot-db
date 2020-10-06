"""users routes"""
from flask import current_app as app, jsonify, request
from models import AudioPilot, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/audio_pilot/<user_id>', methods=['POST', 'GET'])
def create_pilot_data(user_id):
    content = request.json
    audio_pilot = AudioPilot()
    audio_pilot.userID = str(content['userID'])
    audio_pilot.qnTime = str(content['qnTime'])
    audio_pilot.qnRT = str(content['qnRT'])
    audio_pilot.qnNum = str(content['qnNum'])
    audio_pilot.soundIndex = str(content['soundIndex'])
    audio_pilot.soundFocus = str(content['soundFocus'])
    audio_pilot.freqFocus = str(content['freqFocus'])
    audio_pilot.volume = str(content['volume'])
    audio_pilot.playNum = str(content['playNum'])
    audio_pilot.averRating = str(content['averRating'])
    audio_pilot.arouRating = str(content['arouRating'])
    audio_pilot.domRating = str(content['domRating'])
    audio_pilot.averRatingDef = str(content['averRatingDef'])
    audio_pilot.arouRatingDef = str(content['arouRatingDef'])
    audio_pilot.domRatingDef = str(content['domRatingDef'])

    BaseObject.check_and_save(audio_pilot)
    result = dict({"success": "yes"})
    return jsonify(result)

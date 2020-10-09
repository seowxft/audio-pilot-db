"""users routes"""
from flask import current_app as app, jsonify, request
from models import AudioFreq, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/audio_freq/<user_id>', methods=['POST', 'GET'])
def create_freq_data(user_id):
    content = request.json
    audio_freq = AudioFreq()
    audio_freq.userID = str(content['userID'])
    audio_freq.qnTime = str(content['qnTime'])
    audio_freq.qnRT = str(content['qnRT'])
    audio_freq.qnNum = str(content['qnNum'])
    audio_freq.volume = str(content['volume'])
    audio_freq.volumeNotLog = str(content['volumeNotLog'])
    audio_freq.freqThresIndiv = str(content['freqThresIndiv'])
    audio_freq.sliderFreqDefault = str(content['sliderFreqDefault'])

    BaseObject.check_and_save(audio_freq)
    result = dict({"success": "yes"})
    return jsonify(result)

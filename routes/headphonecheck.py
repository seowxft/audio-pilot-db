"""users routes"""
from flask import current_app as app, jsonify, request
from models import HeadphoneCheck, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/headphone_check/<user_id>', methods=['POST', 'GET'])
def create_headphone_data(user_id):
    content = request.json
    headphone_check = HeadphoneCheck()
    headphone_check.userID = str(content['userID'])
    headphone_check.date = str(content['date'])
    headphone_check.startTime = str(content['startTime'])
    headphone_check.checkTry = str(content['checkTry'])
    headphone_check.checkStage = str(content['checkStage'])
    headphone_check.qnNum = str(content['qnNum'])
    headphone_check.volume = str(content['volume'])
    headphone_check.qnTime = str(content['qnTime'])
    headphone_check.qnRT = str(content['qnRT'])
    headphone_check.quizSoundsIndiv = str(content['quizSoundsIndiv'])
    headphone_check.quizAnsIndiv = str(content['quizAnsIndiv'])
    headphone_check.qnPressKey = str(content['qnPressKey'])
    headphone_check.qnCorrIndiv= str(content['qnCorrIndiv'])

    BaseObject.check_and_save(headphone_check)
    result = dict({"success": "yes"})
    return jsonify(result)

"""users routes"""
from flask import current_app as app, jsonify, request
from models import PsychQuiz, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/psych_quiz/<user_id>', methods=['POST', 'GET'])
def create_psych_data(user_id):
    content = request.json
    psych_quiz = PsychQuiz()
    psych_quiz.userID = str(content['userID'])
    psych_quiz.qnTimeStart = str(content['qnTimeStart'])
    psych_quiz.qnTimeEnd = str(content['qnTimeEnd'])
    psych_quiz.PgFinish_OCIR = str(content['PgFinish_OCIR'])
    psych_quiz.PgFinish_STAI_Y1 = str(content['PgFinish_STAI_Y1'])
    psych_quiz.PgFinish_STAI_Y2 = str(content['PgFinish_STAI_Y2'])
    psych_quiz.PgRT_OCIR = str(content['PgRT_OCIR'])
    psych_quiz.PgRT_STAI_Y1 = str(content['PgRT_STAI_Y1'])
    psych_quiz.PgRT_STAI_Y2 = str(content['PgRT_STAI_Y2'])
    psych_quiz.OCIR = str(content['OCIR'])
    psych_quiz.STAI_Y1= str(content['STAI_Y1'])
    psych_quiz.STAI_Y2= str(content['STAI_Y2'])

    BaseObject.check_and_save(psych_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)

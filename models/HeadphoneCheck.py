"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class HeadphoneCheck(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    checkTry             = Column(Text(length=10000))
    checkStage           = Column(Text(length=10000))
    qnNum                = Column(Text(length=10000))
    volume               = Column(Text(length=10000))
    qnTime               = Column(Text(length=10000))
    qnRT                 = Column(Text(length=10000))
    quizSoundsIndiv      = Column(Text(length=10000))
    quizAnsIndiv         = Column(Text(length=10000))
    qnPressKey           = Column(Text(length=10000))
    qnCorrIndiv          = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_start_time(self):
        return str(self.startTime)

    def get_check_try(self):
        return str(self.checkTry)

    def get_check_stage(self):
        return str(self.checkStage)

    def get_set_vol(self):
        return str(self.volume)

    def get_qn_time(self):
        return str(self.qnTime)

    def get_qn_RT(self):
        return str(self.qnRT)

    def get_qn_num(self):
        return str(self.qnNum)

    def get_quiz_sound(self):
        return str(self.quizSoundsIndiv)

    def get_quiz_ans(self):
        return str(self.quizAnsIndiv)

    def get_qn_keypress(self):
        return str(self.qnPressKey)

    def get_qncorr(self):
        return str(self.qnCorrIndiv)

    def errors(self):
        errors = super(HeadphoneCheck, self).errors()
        return errors

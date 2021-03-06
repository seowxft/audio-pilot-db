"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class AudioPilot(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    date                 = Column(Text(length=10000))
    startTime            = Column(Text(length=10000))
    qnNum                = Column(Text(length=10000))
    qnTime               = Column(Text(length=10000))
    qnRT                 = Column(Text(length=10000))
    soundIndex           = Column(Text(length=10000))
    soundFocus           = Column(Text(length=10000))
    freqFocus            = Column(Text(length=10000))
    volume               = Column(Text(length=10000))
    volumePer            = Column(Text(length=10000))
    checkBox             = Column(Text(length=10000))
    playNum              = Column(Text(length=10000))
    averRating           = Column(Text(length=10000))
    arouRating           = Column(Text(length=10000))
    averRatingDef        = Column(Text(length=10000))
    arouRatingDef        = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_start_time(self):
        return str(self.startTime)

    def get_qn_num(self):
        return str(self.qnNum)

    def get_qn_time(self):
        return str(self.qnTime)

    def get_qn_RT(self):
        return str(self.qnRT)

    def get_sound_indx(self):
        return str(self.soundIndex)

    def get_sound_name(self):
        return str(self.soundFocus)

    def get_freq_name(self):
        return str(self.freqFocus)

    def get_volume(self):
        return str(self.volume)

    def get_volume_per(self):
        return str(self.volumePer)

    def get_checkbox(self):
        return str(self.checkBox)

    def get_playNum(self):
        return str(self.playNum)

    def get_aver(self):
        return str(self.averRating)

    def get_arou(self):
        return str(self.arouRating)

    def get_aver_def(self):
        return str(self.averRatingDef)

    def get_arou_def(self):
        return str(self.arouRatingDef)

    def errors(self):
        errors = super(AudioPilot, self).errors()
        return errors

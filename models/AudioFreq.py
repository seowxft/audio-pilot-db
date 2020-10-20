"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class AudioFreq(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID              = Column(Text(length=10000))
    date              = Column(Text(length=10000))
    startTime                = Column(Text(length=10000))
    qnNum               = Column(Text(length=10000))
    qnTime              = Column(Text(length=10000))
    qnRT                = Column(Text(length=10000))
    volume              = Column(Text(length=10000))
    volumeNotLog              = Column(Text(length=10000))
    freqThresIndiv      = Column(Text(length=10000))
    sliderFreqDefault   = Column(Text(length=10000))


    def get_id(self):
        return str(self.id)

    def get_userID(self):
        return str(self.userID)

    def get_date(self):
        return str(self.date)

    def get_start_time(self):
        return str(self.startTime)

    def get_qn_num(self):
        return str(self.qnNum)

    def get_qn_Time(self):
        return str(self.qnTime)

    def get_qn_RT(self):
        return str(self.qnRT)

    def get_volume(self):
        return str(self.volume)

    def get_volume(self):
        return str(self.volumeNotLog)

    def get_freq_thres(self):
        return str(self.freqThresIndiv)

    def get_freq_default(self):
        return str(self.sliderFreqDefault)

    def errors(self):
        errors = super(AudioFreq, self).errors()
        return errors

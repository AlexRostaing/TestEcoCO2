# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CO2Data(models.Model):
    datetime = models.DateTimeField()
    co2_rate = models.IntegerField()

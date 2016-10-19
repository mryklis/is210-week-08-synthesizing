#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module checks day and time to raise an alarm"""


DAY = raw_input('What day is it?').decode('utf-8').lower()
DAY = DAY[0:3]

TIME = raw_input('What time is it?')
TIME = float(TIME)

SNOOZE = False

WEEKEND = ['sat', 'sun']

if DAY in WEEKEND or TIME < 0600:
	SNOOZE = True
else:
	print 'Beep! ' * 5

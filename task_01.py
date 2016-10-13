#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module asks questions and prints results"""


BASEc = ['Seattle Gray', 'Manatee']
ACCENTc = ['Ceramic Glaze', 'Cumulus Nimbus', 'Platinum Mist', 'Spartan Sage']
HIGHLIGHTc = ['Basically White', 'White', 'Off-White', 'Paper White', 'Bone White', 'Just White', 
             'Fractal White', 'Not White']

BASE = raw_input('Which base color, {} or {}?'.format(BASEc[0], BASEc[1]))
if BASE in BASEc[0]:
	ACCENT = raw_input('Which accent color, {} or {}?'.format(ACCENTc[0], ACCENTc[1]))
	if ACCENT in ACCENTc[0]:
		HIGHLIGHT = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHTc[0], HIGHLIGHTc[1]))
	elif ACCENT in ACCENTc[1]:
		HIGHLIGHT = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHTc[2], HIGHLIGHTc[3]))
elif BASE in BASEc[1]:
	ACCENT = raw_input('Which accent color, {} or {}?'.format(ACCENTc[2], ACCENTc[3]))
	if ACCENT in ACCENTc[2]:
		HIGHLIGHT = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHTc[4], HIGHLIGHTc[5]))
	elif ACCENT in ACCENTc[3]:
		HIGHLIGHT = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHTc[6], HIGHLIGHTc[7]))
		
print 'Your color selection is, {}, {} and {}'.format(BASE, ACCENT, HIGHLIGHT)

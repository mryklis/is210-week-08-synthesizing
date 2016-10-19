#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD


BASE = ['Seattle Gray', 'Manatee']
ACCENT = ['Ceramic Glaze', 'Cumulus Nimbus', 'Platinum Mist', 'Spartan Sage']
HIGHLIGHT = ['Basically White', 'White', 'Off-White', 'Paper White',
             'Bone White', 'Just White', 'Fractal White', 'Not White']
=======
"""This module asks questions and prints results"""

>>>>>>> 7299765bf8baa52f66da42eedb9d2cd8b6d496bd

BASEc = ['Seattle Gray', 'Manatee']
ACCENTc = ['Ceramic Glaze', 'Cumulus Nimbus', 'Platinum Mist', 'Spartan Sage']
HIGHLIGHTc = ['Basically White', 'White', 'Off-White', 'Paper White', 'Bone White', 'Just White', 
             'Fractal White', 'Not White']

<<<<<<< HEAD
Q1 = raw_input('Which base color, {} or {}?'.format(BASE[0], BASE[1]))
if Q1 in BASE[0]:
    Q2 = raw_input('Which accent color, {} or {}?'.format(ACCENT[0],
                                                          ACCENT[1]))
    if Q2 in ACCENT[0]:
        Q3 = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHT[0],
                                                                 HIGHLIGHT[1]))
    elif Q2 in ACCENT[1]:
        Q3 = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHT[2],
                                                                 HIGHLIGHT[3]))
elif Q1 in BASE[1]:
    Q2 = raw_input('Which accent color, {} or {}?'.format(ACCENT[2], ACCENT[3]))
    if Q2 in ACCENT[2]:
        Q3 = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHT[4],
                                                                 HIGHLIGHT[5]))
    elif Q2 in ACCENT[3]:
        Q3 = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHT[6],
                                                                 HIGHLIGHT[7]))

print 'Your selected colors are, {}, {}, and {}'.format(Q1, Q2, Q3)
=======
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
>>>>>>> 7299765bf8baa52f66da42eedb9d2cd8b6d496bd

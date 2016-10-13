#!/usr/bin/env python
# -*- coding: utf-8 -*-


BASE = ['Seattle Gray', 'Manatee']
ACCENT = ['Ceramic Glaze', 'Cumulus Nimbus', 'Platinum Mist', 'Spartan Sage']
HIGHLIGHT = ['Basically White', 'White', 'Off-White', 'Paper White',
             'Bone White', 'Just White', 'Fractal White', 'Not White']


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

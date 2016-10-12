
BASE = ['Seattle Gray', 'Manatee']
ACCENT = ['Ceramic Glaze', 'Cumulus Nimbus', 'Platinum Mist', 'Spartan Sage']
HIGHLIGHT = ['Basically White', 'White', 'Off-White', 'Paper White', 'Bone White', 'Just White', 
             'Fractal White', 'Not White']




Q1 = raw_input('Which base color, {} or {}?'.format(BASE[0], BASE[1]))
if Q1 in BASE[0]:
	Q2 = raw_input('Which accent color, {} or {}?'.format(ACCENT[0], ACCENT[1]))
	if Q2 in ACCENT[0]:
		Q3 = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHT[], HIGHLIGHT[]))
	elif Q2 in ACCENT[1]:
		Q3 = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHT[], HIGHLIGHT[]))
elif Q1 in BASE[1]:
	Q2 = raw_input('Which accent color, {} or {}?'.format(ACCENT[2], ACCENT[3]))
	if Q2 in ACCENT[2]:
		Q3 = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHT[], HIGHLIGHT[]))
	elif Q2 in ACCENT[3]:
		Q3 = raw_input('Which highlight color, {} or {}?'.format(HIGHLIGHT[], HIGHLIGHT[]))


BASEC = ['Seattle Gray', 'Manatee']
ACCENTC = ['Ceramic Glaze', 'Cumulus Nimbus', 'Platinum Mist', 'Spartan Sage']
HIGHLIGHTC = ['Basically White', 'White', 'Off-White', 'Paper White', 'Bone White', 'Just White', 
             'Fractal White', 'Not White']




Q1 = raw_input('Which base color, {} or {}?'.format(*BASEC))
if Q1 in BASEC[0]:
	print 'hey'
elif Q1 in BASEC[1]:
	print 'no way'

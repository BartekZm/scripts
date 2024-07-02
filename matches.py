import string
for a in string.ascii_uppercase[6]:
	for i in range (1,7):
		print('$postParams = @{scenario=\'Crusade on Novgorod\';hidden=\'true\';notice=\'Group '+str(a)+' Match ' +str(i)+ '\'};')
		print('Invoke-WebRequest -Uri \'https://www.rally-the-troops.com/create/nevsky\' -Method POST -WebSession $RTT -Body $postParams;')
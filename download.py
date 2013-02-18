import json
import urllib2

n = 0
access_token = 'PUT_YOUR_ACCESS_TOKEN_HERE'
url = "https://graph.facebook.com/160284404008688/feed?access_token=" + access_token
while(True):
	response = urllib2.urlopen(url)
	json_str = response.read()

	f = open('data/' + str(n) + '.json', 'w')
	f.write(json_str)
	f.close()

	data = json.loads(json_str)
	url = data['paging']['next']
	n += 1

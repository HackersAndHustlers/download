import json
import os
import sys
import urllib2

all_posts = []
access_token = os.environ.get('HNH_FB_AT',raw_input('access_token:'))
url = "https://graph.facebook.com/160284404008688/feed?limit=250&access_token=" + access_token

while(True):
    response = urllib2.urlopen(url)
    json_str = response.read()

    data = json.loads(json_str)
    posts = data['data']
    all_posts += posts

    if 'paging' not in data:
        break
    url = data['paging']['next']
    sys.stdout.write('.')
    sys.stdout.flush()
print

out_file = open('hackersandhustlers.json', 'w')
out_file.write(json.dumps(all_posts))
out_file.close()

import json
import urllib2

all_posts = []
access_token = 'PUT_YOUR_ACCESS_TOKEN_HERE'
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

out_file = open('hackersandhustlers.json', 'w')
out_file.write(json.dumps(all_posts))
out_file.close()

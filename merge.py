import json

all_posts = []
try:
	n = 0
	while(True):
		f = open('data/' + str(n) + '.json')
		json_str = f.read()
		data = json.loads(json_str)
		posts = data['data']
		all_posts += posts
		f.close()
		n += 1
except:
	out_file = open('hackersandhustlers.json', 'w')
	out_file.write(json.dumps(all_posts))
	out_file.close()

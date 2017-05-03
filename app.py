from flask import Flask, redirect, url_for, request, render_template
import json
import requests
app = Flask(__name__)


@app.route('/<url_name>')
def main(url_name):
	data = json
	with open("data2.json") as a:
		data = json.load(a)
	id = data[url_name]
	r = requests.get("http://api.github.com/users/"+url_name)
	y = json.loads(r.content.decode())
	return render_template('test.html', name=id['name'],image=y['avatar_url'],bio=id['bio'],email=id['email'],github_handle=id['github_handle'], fbid=id['fbid'])






if __name__ == "__main__":  # This is for local testin
    app.run(host='localhost', port=3453, debug=True)

# if __name__ == "__main__":  # This will come in use when
#     port = int(os.environ.get("PORT", 5000))  # the app is deployed on heroku
#     app.run(host='0.0.0.0', port=port)

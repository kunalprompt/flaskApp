#import modules
from flask import Flask, render_template

#intializing and configuring the application
app = Flask(__name__,
	static_folder="static",
	template_folder="templates")

@app.route('/', methods=['GET'])
def index1():
	return render_template('index.html', message='Data Science')

@app.route('/<path:path>', methods=['GET'])
def index2(path):
	return render_template('index.html', message='Data Science')

if __name__=="__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)

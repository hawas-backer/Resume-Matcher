from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
	return "<H1>Hello human</H1>"

@app.route('/test')
def test():
	return "<H1>Testing </H!>"



if __name__ == '__main__':
	app.run(debug=True)

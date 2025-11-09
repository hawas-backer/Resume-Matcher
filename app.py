from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#ALLOWED_EXTENSIONS = {'txt','pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello_world():
	return render_template("index.html")


@app.route("/upload",methods =['POST','GET'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file.filename == '':
			flash('NO selected file')
			return redirect(request.url)
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		return f"File {filename} uploaded succesffuly to {UPLOAD_FOLDER}"




if __name__ == '__main__':
	app.run(debug=True)

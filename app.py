from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, flash
from werkzeug.utils import secure_filename
from uuid import uuid4
import pdfplumber 
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#ALLOWED_EXTENSIONS = {'txt','pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def extract_from_pdf(path):
	text = ""
	with pdfplumber.open(path) as pdf:
		for page in pdf.pages:
			text += page.extract_text()
	return text 
	

def make_unique(string):
	ident = uuid4().hex[:8]
	return f"{ident}-{string}"

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
		unique_filename = make_unique(filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],unique_filename))

		text = extract_from_pdf(f"uploads/{unique_filename}")

		print("_________EXTRACTED______")
		print(text)


		return f"File {filename} uploaded succesffuly to {UPLOAD_FOLDER}"


@app.route('/test')
def test():
	return "<H1>TESTING</H2>"

if __name__ == '__main__':
	app.run(debug=True)

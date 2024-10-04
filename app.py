from flask import Flask, render_template, request, flash, url_for, redirect, jsonify
import os
import json

from utils import FileToDataFrame

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'csv', 'xlsx'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Ensure the UPLOAD_FOLDER directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


#@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']

        # If the user does not select a file, browser may submit an empty file part
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            obj = FileToDataFrame(file_path=file_path)
            try:
                obj.load_file()
                data = obj.get_dataframe()
                out = obj.output()
                json_obj = json.dumps(out)
                return jsonify(out)
            except Exception as e:
                return redirect(url_for('home'))
        else:
            flash('File not supported!')
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)
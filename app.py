from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from audio2text import crop2chunk, chunk2text
import time
import os

app = Flask(__name__)


@app.route('/')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      crop2chunk(f.filename) # crop uploaded audio to small chunks
      #return 'file uploaded successfully'
      return render_template('audioPlayer.html', val1=time.time())

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    data = request.json['data']
    #return jsonify(username=username)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a')
    text = chunk2text(a)
    return jsonify(result=text)
		
if __name__ == '__main__':
   #app.config['TEMPLATES_AUTO_RELOAD'] = True
   #app.config['STATIC_AUTO_RELOAD'] = True
   #app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
   app.run(debug=True)
   #app.run()
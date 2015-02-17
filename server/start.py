from flask import Flask
from flask import request
from DiskLogger import DiskLogger
app = Flask(__name__)

@app.route("/")
def hello():
    return "Anxiety-sound server. To see the data: <a href='/data'>data</a>"


@app.route("/data" , methods=['GET','POST'] )
def data():	
	if request.method == 'GET':
		return "DATA"
	elif request.method == 'POST':
		_subject = request.form['subject']
		_start_time       = request.form['start_time']
		_end_time        = request.form['end_time']
		_question_number = request.form['question_number']
		_awn = request.form['awn']
		dl = DiskLogger()
                print [_subject,_question_number,_start_time,_end_time,_awn]
		dl.write([_subject,_start_time,_end_time,_question_number,_awn])
		return _start_time
	else:
		return "Method not supported"

if __name__ == "__main__":
    app.run(debug=True)

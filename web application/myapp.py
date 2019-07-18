#------------------1. imports---------------------------------------------
from flask import Flask,render_template
#------------------2.initialize app(init)----------------------------------
app = Flask(__name__)

#-----------------3. Routers------------------------------------------------
@app.route('/')
def index():
	return 'Hello World'
#to run, type http://127.0.0.1:5000/.....'/'is the app route or location


@app.route('/whereami')
def whereami():
        return 'Ghana!'
#to run, type http://127.0.0.1:5000/whereami.....'/whereami'is the app route or location

#dynamic parameters....changes <name >
@app.route('/foo/<name>')
def foo(name):
	return render_template('index.html',to=name)

#-----------------4. Start server--------------------------------------
#runs if above conditions are true
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0' )

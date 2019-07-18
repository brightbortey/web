from flask import Flask,render_template

app= Flask(__name__)

#Building a hompage
@app.route('/')
def index():
	return render_template('index1.html') #index.html is the template that will be run

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

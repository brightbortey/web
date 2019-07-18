
#-----------------1. imports--------------------------------------------
from flask import Flask, render_template


#-----------------2. init app-------------------------------------------
app=Flask(__name__)

#-----------------3. Routers--------------------------------------------
#dynamic parameters....changes <name >
@app.route('/foo')
def foo():
        return render_template('foo.html')

#-----------------4. Start server--------------------------------------
#runs if above conditions are true
if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0' )


from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          						#This is the main URL
@app.route('/index')
def index():
    return render_template("index.html", title="Home", name="index")		#The argument should be in templates folder

@app.route('/interests')
def interests():
    return render_template("interests.html", title="Interests", name="interests")

#Add the code for courses
@app.route('/courses')
def courses():
    return render_template("courses.html", title="Courses", name="courses")

#Add the code for other
@app.route('/other')
def other():
    return render_template("other.html", title="Other", name="other")
#Hmmm, do we need another one?


if __name__ == '__main__':
    app.run(debug=True, port=4500)		#debug=True is optional

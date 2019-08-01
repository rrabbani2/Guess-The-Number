from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
    
@app.route("/results",methods =['GET','POST'])
def results():
    answer = ""
    answer_dictionary = model.number_checker(request.form['numguesser'])
    if answer_dictionary["win"]:
        answer="Congrats you are the number master"
    else:
        answer="Sorry, you didn't get the number :(\nthe correct answer was "+str(answer_dictionary["answer"])
    return render_template("results.html",answer=answer, num=request.form['numguesser'])
    





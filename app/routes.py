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
    print(answer_dictionary)
    if answer_dictionary["win"]:
        answer="Congrats you are the number jedi"
        return render_template("results.html",answer=answer, num=request.form['numguesser'])
    else:
        hint=(answer_dictionary["hint"])
        answer="Sorry, you didn't get the number :(\nthe correct answer was "+str(answer_dictionary["answer"])
        return render_template("keepguessing.html",num=request.form['numguesser'], x=answer_dictionary["answer"], hint=hint)
        
        
@app.route('/keepguessing', methods = ['GET','POST'])
def guessing():
    answer = ""
    answer_dictionary = model.repeatcheck(request.form['numguesser'],request.form['realanswer'])
    print(answer_dictionary)
    if answer_dictionary["win"]:
        answer="Congrats you are the number jedi"
        return render_template("results.html",answer=answer, num=request.form['numguesser'])
    else:
        hint=(answer_dictionary["hint"])
        return render_template('keepguessing.html', num=request.form['numguesser'], x=answer_dictionary["answer"], hint=hint)
        



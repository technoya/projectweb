from flask import *
import data
app=Flask(__name__,template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def home1():
    username=request.form['name']
    a,b,c,d,e,f,g=data.rollno(username)
    print(username)
    return render_template('page.html',name=a,fname=b,english=c,rollno=d,maths=e,plotics=f,science=g)

if __name__=="__main__":
    app.run(debug=True)
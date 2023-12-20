from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def djkfkj():
    return render_template('page.html')
@app.route('/info',methods=['GET','POST'])
def fkjfkj():
    try:
        x=int(request.form['a'])
        y=int(request.form['b'])
    except:
        return render_template('page.html',result='Invalid Input')    
    ans=x+y
    return render_template('page.html',result=ans)
if __name__=='__main__':
    app.run()
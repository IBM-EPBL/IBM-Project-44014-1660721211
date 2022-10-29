from flask import Flask ,render_template ,request ,url_for ,redirect

app =Flask(__name__ ,static_url_path='/static') 

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/config",methods=['POSt','GET'])
def  register():
     if request.method=='POST':
         n=request.form.get('first_name') 
         n1=request.form.get('last_name')
         r=request.form.get('company_name') 
         c=request.form.get('Email') 
         s=request.form.get('subject')
         return render_template('confirm.html',
            first_name=n,last_name=n1,rollno=c,Email=r,subject=s)  


if __name__ == '__main__':
    app.run(debug=True)    
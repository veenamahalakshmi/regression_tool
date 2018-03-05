from flask import Flask, render_template,url_for,request,redirect,session

import sqlite3


from passlib.hash import sha256_crypt

from os import walk
app = Flask(__name__)

from runscript import *
from regression_report import*

value = os.urandom(24)
app.secret_key = value

pvalue=0

def getcon():
    conn = sqlite3.connect('spirent.db')
    print "Opened database successfully";
    return conn

def checklogin():
    if(session.has_key("uname")):
        pass
    else:
        return "login"


# conn.execute('CREATE TABLE spirent (name TEXT, emailid TEXT,mobilenumber INTEGER,empid INTEGER,password TEXT)')
# print "Table created successfully";
#conn.close()


@app.route('/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        conn = getcon()
        cur = conn.cursor()
        username = request.form['uname']
        password = request.form['psw']
        cur.execute("""select username,password from spirent where username = '%s'""" % (username))
        row = cur.fetchone()
        if (row == None):
            return render_template('login.html', error="Wrong Username")
        if username == row[0] and sha256_crypt.verify(password, row[1]):

            session['uname'] = username
            os.chdir("E:")
            cwd = os.getcwd()
            print(cwd)
            name = session['uname']
            rootpath = cwd + session['uname']
            print "The current working director is" + cwd
            if (os.path.exists(rootpath)):
                shutil.rmtree(rootpath, True)
            os.mkdir(rootpath)
            print"created new directory" + rootpath
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error="Enter username and password")
    else:
        if(session.has_key("login")):
            error=session['login']
            session['login']=''
            return render_template('login.html', error = error)
        else:
            error=''
            return render_template('login.html',error=error)


@app.route('/register', methods=['POST', 'GET'])
def Register():
    if request.method == 'POST':
        try:

            username = request.form['uname']

            password = request.form['psw']
            password = sha256_crypt.hash(password)
            print(password)
            conn = getcon()
            cur = conn.cursor()
            cur.execute("""select username, password from spirent where username = '%s' or password = '%s' """ % (username, password))
            row = cur.fetchone()
            if (row):
                msg = "Username or password already exists. Please go back and login."
                done = 0


            else:

                cur.execute("""INSERT INTO spirent (username,password) VALUES ('%s', '%s')""" % (username, password))
                conn.commit()
                conn.close()
                msg = "Record successfully added"
                done = 1
                print "msg"
        except Exception as e:
            done = 0
            conn.rollback()
            msg = "error in insert operation"
        finally:
            if(done):
                session['login']='Record added successfully'
                return redirect(url_for('login'))
            else:
                return render_template('Registration.html', msg=msg)
                conn.close()
    else:
        return render_template('Registration.html')


@app.route("/first-page",methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        val = request.form['submit']
        if val == 'Analyze':
            url = request.form['fname']

            nextpage = running_script(url)
            print ">>>>>>>>>>>>>>>>>>>>>>>>"
            print nextpage

            if nextpage == True:
               #print "zipfile exist:"+str(files)
                cwd = os.getcwd().strip()
                print(cwd)
                mypath = cwd + ""
                session['url'] = mypath
                return redirect(url_for('nextpage'))
            else:
                return render_template('index.html', error="zipfile dosen't exist")

    #if request.method == "GET":
    return render_template("index.html")



@app.route('/nextpage', methods=['POST', 'GET'])
def nextpage():
    ch=checklogin()
    if(ch):
        return render_template("login.html",error="Login to continue")
    url = session['url']
    if(url):
        list = []
        for filename in os.listdir(url):
            if filename.endswith(".txt"):
                list.append(filename)
        return render_template('nextpage.html',  list_of_elements = list)

    else:
        return render_template("login.html",error="You have been signed out")

@app.route('/display',methods=['POST','GET'])
def display():
    ch = checklogin()
    if (ch):
        return render_template("login.html", error="Login to continue")
    if(request.method=='POST'):
        filename=request.form['filename']
        url=session['url']
        loc=os.path.join(url,filename)
        f = open(loc, "r")
        var = f.read()
        return render_template("nextpage.html",read=var)
    else:
        return redirect(url_for('main'))


@app.route("/regression_report",methods=['POST', 'GET'])
def analyse():
    nextpage = regression_report()
    print ">>>>>>>>>>>>>>>>>>>>>>>>"
    print nextpage

    if nextpage == True:
        return render_template("nextpage.html")
    else:
        return redirect(url_for('main'))


if __name__ == "__main__":
    #app.run(debug='True', host='10.62.150.68')
    app.run(debug='True')


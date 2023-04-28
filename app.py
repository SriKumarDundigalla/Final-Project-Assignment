from flask import Flask, redirect
from flask import render_template
from flask import request,session
from flask_session import Session
import sqlite3




app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/")
def home():
    session.clear()
    session['email']=""
    session['status']='loggedOut'
    return render_template('home.html')

@app.route("/signup",methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        try:
            
            firstname = request.form['fn']
            lastname = request.form['ln']
            email = request.form['Email1'].lower()
            password = request.form['Password1']
            password2 = request.form['Password2']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("""SELECT email FROM users""")
                rows = cur.fetchall() 
                result = list(map(lambda x: x[0].lower(), rows))
                if(email in result):
                    raise Exception("You are already signed in with this email address.")
                else:
                    cur.execute("INSERT INTO users (first_name, last_name,email , password ) VALUES (?,?,?,?)",(firstname,lastname,email,password))
                    con.commit()
                    msg = "Record successfully added to database."
                    row= firstname+" "+lastname
                    return render_template('welcome.html',msg=row)
        except Exception as e:
            con.rollback()
            error_msg = str(e.args[0])
            return render_template('signup.html',msg=error_msg)

        finally:
            con.close()


    if request.method=='GET':
        return render_template("signup.html",msg="") 
@app.route("/about")  
def about():  
    return render_template("about.html") 
@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route("/myaccount",methods = ['POST', 'GET'])
def myaccount():
    con=sqlite3.connect('database.db')
    try:
        if request.method=='GET': 
            cur = con.cursor()
            cur.execute("""SELECT * FROM users  WHERE email =?""",(session['email'],))
            row = cur.fetchone()
            ls=[row,'','']
            return render_template('myaccount.html',rows=ls)
        if request.method=='POST':
            firstname = request.form['myfn']
            lastname = request.form['myln']
            password = request.form['myPassword1']
            cur = con.cursor()
            cur.execute("""SELECT * FROM users  WHERE email =?""",(session['email'],))
            row = cur.fetchone()
            if(row[0]!=firstname or row[1]!=lastname or row[3]!=password):
                cur.execute( """UPDATE users SET first_name = ?,last_name = ?,password = ? WHERE email = ?;""",(firstname,lastname,password,session['email'],))
                con.commit()
                cur.execute("""SELECT * FROM users  WHERE email =?""",(session['email'],))
                row = cur.fetchone()
                ls=[row,'','Your account details have been successfully updated.']
                return render_template('myaccount.html',rows=ls)
            else:
                cur.execute("""SELECT * FROM users  WHERE email =?""",(session['email'],))
                row = cur.fetchone()
                ls=[row,'No changes detected. Please update any fields and try again.','']
                return render_template('myaccount.html',rows=ls)
    except Exception as e:
        pass
    finally:
        con.close()

@app.route("/landing")
def landing():
    return render_template('landing_login.html')
@app.route("/myreview",methods=["GET", "POST"])
def myreview():
    if request.method=='POST':
        try:
            print('hi')
            name = request.form['username']
            review = request.form['review']
            rating = int(request.form.get('rating_stars'))
            with sqlite3.connect('database.db') as con:
                con.row_factory = sqlite3.Row


                cur = con.cursor()
                cur.execute("INSERT INTO Reviews (name, review, rating) VALUES (?,?,?)",(name,review,rating))
                con.commit()


                return render_template("myreview.html",msg="Review Added Sucessfully") 
        except:
            con.rollback()
            msg = "Error in the INSERT"
        finally:
            con.close()
            
    if request.method=='GET':
        return render_template('myreview.html',msg="")
@app.route("/reviews",methods = ['POST', 'GET'])  
def reviews():
    if request.method == 'GET':
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM Reviews")

        rows = cur.fetchall()
        con.close() 
        return render_template("reviews.html",rows=rows) 
    

@app.route("/courses")  
def courses():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM About_Course")

    rows = cur.fetchall()
    con.close()
    
    if(session['email']=="" or session['status']=='loggedOut'):
        return render_template("course.html",rows=rows)
    else:
        rows=[rows,'','']
        return render_template("layoutCourse.html",rows=rows)


@app.route("/addtocart",methods = ['POST', 'GET'])
def addtocart():
    try:
        if request.method=='POST':
            if(session['email']=="" or session['status']=='loggedOut'):   
                return render_template("login.html",msg="")
            else:
                cardtitle = request.form.get('Card_title')
                con=sqlite3.connect('database.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM About_Course")
                rows = cur.fetchall()
                rows=[rows,'The course has been successfully added to the cart.','']
                cur.execute("INSERT INTO userCourses (Email,courseName ) VALUES (?,?)",(session['email'],cardtitle))
                con.commit()
                con.close()
                return render_template("layoutCourse.html",rows=rows) 
    except Exception as e:
        con.rollback()
        error_msg = str(e.args[0])
        rows[2]='The course has already been added to the cart.'
        rows[1]=''
        return render_template('layoutCourse.html',rows=rows)


            
 
@app.route("/mycart", methods = ['POST', 'GET'])
def mycart():
    con=sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("""SELECT courseName FROM userCourses  WHERE Email =?""",(session['email'],))
    rows = cur.fetchall()
    result = tuple(map(lambda x: x[0], rows))
    cur.execute("SELECT * FROM About_Course WHERE courseName IN ({})".format(','.join('?' * len(result))), result)
    rows = cur.fetchall()
    prices=list(rows)
    cost= sum(list(map(lambda x: list(x)[3], prices)))
    con.close()
    return render_template('mycart.html',rows=[rows,cost])


@app.route("/mycourses", methods = ['POST', 'GET'])
def mycourses():
    con=sqlite3.connect('database.db')
    try:
        if request.method=='POST':
            cur = con.cursor()
            cur.execute("SELECT * FROM userCourses WHERE Email = ?", (session['email'],))
            rows = cur.fetchall()
            for i in list(rows):
                cur.execute("INSERT INTO mycourse (Email, usercourse) VALUES (?, ?)", i)
            con.commit()
            courses = tuple(list(map(lambda x: x[1], list(rows))))
            cur.execute("DELETE FROM userCourses WHERE Email = ?", (session['email'],))
            con.commit()
            cur.execute("SELECT * FROM About_Course WHERE courseName IN ({})".format(','.join('?' * len(courses))), courses)
            rows = cur.fetchall()

            return render_template('mycourses.html',rows=rows)
        if request.method == 'GET':
            cur = con.cursor()
            cur.execute("SELECT * FROM mycourse  WHERE Email = ?", (session['email'],))
            rows = cur.fetchall()
            courses = tuple(list(map(lambda x: x[1], list(rows))))
            cur.execute("SELECT * FROM About_Course WHERE courseName IN ({})".format(','.join('?' * len(courses))), courses)
            rows = cur.fetchall()
            return render_template('mycourses.html',rows=rows)
    except Exception as e:
        print(e)
        return redirect('/mycart')
    finally:
        con.close()

@app.route("/removeitem",methods = ['POST', 'GET'])
def removeitem():
    con=sqlite3.connect('database.db')
    try:
        if request.method=='POST':
            title = request.form['coursetitle']
            url  =request.form['url']
            cur = con.cursor()
            cur.execute("DELETE FROM userCourses WHERE Email = ? AND courseName = ?", (session['email'], title))
            con.commit()
            return redirect('/mycart')
        
    except:
        return redirect('/mycart')
    finally:
        con.close()
@app.route("/checkout",methods = ['POST', 'GET'])
def checkout():
    pass

@app.route("/login",methods = ['POST', 'GET'])  
def login():
    if request.method == 'POST':
        try:
            email = request.form['lEmail1'].lower()
            password = request.form['lPassword1']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("""SELECT email,password FROM users WHERE email=?""",(email,))
                rows = cur.fetchone()
                if(not(rows)):
                    raise Exception("Invalid email or account not found. Please check your email or sign up to continue.")
                else:
                    print(rows)
                    if(rows[1]!=password):
                        raise Exception("Kindly verify the password.")
                    session['email']=email
                    session['status']='loggedIn'
                    return render_template('landing_login.html') 
                
        except Exception as e:
            con.rollback()
            error_msg = str(e.args[0])
            return render_template('login.html',msg=error_msg)
        finally:
            con.close()

            
    if request.method=='GET':
        return render_template("login.html",msg="") 
# @app.route("/signup")  
# def signup():  
#     return render_template("signup.html") 

if __name__ == '__main__':
   app.run(debug = True)
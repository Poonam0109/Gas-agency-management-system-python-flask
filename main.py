from flask import Flask, render_template, session, request, redirect, url_for
import mysql.connector
app = Flask(__name__)
app.secret_key = "tp"

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    msg=""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        mb = mysql.connector.connect(host="localhost", user='root', password='root', port=3306,
                                     database='cable')
        c = mb.cursor()
        query = "SELECT * FROM user WHERE username =%s and password =%s;"
        v = (username, password)
        c.execute(query, v)
        rows = c.fetchall()
        for i in rows:
            if username == i[0] and password == i[1]:
                return render_template('userhome.html', rows=rows)
        else:
            msg = "Please enter valid Username and Password"
    return render_template('login.html', msg=msg)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/addregister', methods=["GET", "POST"])
def addregister():
    msg = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        mailid = request.form["mailid"]
        address = request.form["address"]
        city = request.form["city"]
        state = request.form["state"]
        mb = mysql.connector.connect(host="localhost", user='root', password='root', port=3306,
                                     database='cable')
        c = mb.cursor()
        query ="INSERT INTO user (username , password , name ,mailid ,address,city, state) VALUES ( %s,%s,%s,%s,%s,%s,%s)"
        v = (username , password , name ,mailid ,address,city, state)
        c.execute(query, v)
        mb.commit()
        msg = "Your are Registered successfully..."
    else:
        msg = "*Ooops Something wents Wrong"
    return render_template('login.html',msg=msg)

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/addadmin', methods=["GET", "POST"])
def addadmin():
    msg=""
    if request.method == 'POST':
        auname = request.form['username']
        apswd = request.form['password']
        if auname=="admin" and apswd=="admin":
            mb = mysql.connector.connect(host="localhost", user='root', password='root', port=3306,
                                             database='cable')
            c = mb.cursor()
            query = "select * from bill"
            c.execute(query)
            rows = c.fetchall()
            return render_template('adminhome.html', rows=rows)
        else:
            msg = "Please enter valid Username and Password"
    return render_template('adminlogin.html', msg=msg)



@app.route("/packform", methods=["GET", "POST"])
def packform():
    return render_template("billpayment.html")


@app.route("/packselect", methods=["GET", "POST"])
def packselect():
    if (request.method == "POST"):
        number = request.form["cardno"]
        customername = request.form["cname"]
        amount = request.form["amount"]
        mb = mysql.connector.connect(host="localhost", user='root', password='root', port=3306,
                                     database='cable')
        c = mb.cursor()
        query = "INSERT INTO bill (cname,cardno ,amount) VALUES ( %s,%s,%s)"
        v = (customername, number, amount )
        c.execute(query, v)
        mb.commit()
        return render_template("billapaymentrequest.html")

    else:
        msg = "*Ooops Something wents Wrong"
    return render_template("userhome.html" , msg=msg)

@app.route("/complaintform", methods=["GET", "POST"])
def complaintform():
    return render_template("compaintform.html")

@app.route("/complaint", methods=["GET", "POST"])
def complaint():
    if (request.method == "POST"):
        number = request.form["cardno2"]
        customername = request.form["cname2"]
        complaint = request.form["usercomplaint"]
        contact = request.form["contact2"]
        mb = mysql.connector.connect(host="localhost", user='root', password='root', port=3306,
                                     database='cable')
        c = mb.cursor()
        query = "INSERT INTO comp ( cardno2,cname2 ,usercomplaint,contact2) VALUES ( %s,%s,%s,%s)"
        v = (number, customername, complaint,contact )
        c.execute(query, v)
        mb.commit()
        msg = "Your Complaint Added successfully"
        return render_template("complaintreceived.html")

    else:
        msg = "*Ooops Something wents Wrong"
    return render_template("login.html", msg=msg)

@app.route("/dispcomp", methods=["GET", "POST"])
def dispcomp():
    mb = mysql.connector.connect(host="localhost", user='root', password='root', port=3306,
                                 database='cable')
    c = mb.cursor()
    query = "select * from comp"
    c.execute(query)
    rows = c.fetchall()
    return render_template("displaycomplaint.html" ,rows= rows)

@app.route("/logout")
def logout():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)

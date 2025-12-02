from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)

# Start page
@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/clothes")
def clothes_page():
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM clothes")
    result = cursor.fetchall()
    mydb.close()
    return render_template("clothes.html", clothes=result)


@app.route('/add', methods=['POST', 'GET'])
def add_clothing():
    if request.method == "POST":
        navn = request.form['navn']
        pris = request.form['pris']
        beskrivelse = request.form['beskrivelse']

        mydb = get_connection()
        cursor = mydb.cursor()
        cursor.execute(
            "INSERT INTO clothes (navn, pris, beskrivelse) VALUES (%s, %s, %s)",
            (navn, pris, beskrivelse)
        )

        mydb.commit()
        mydb.close()
        return redirect('/clothes')

    return render_template("nyttprodukt.html")


@app.route("/bestill/<int:cid>", methods=["POST"])
def bestill(cid):
    # TEMP: until you add login, we use a dummy user id (example: 1)
    bruker_id = 1

    mydb = get_connection()
    cursor = mydb.cursor()

    cursor.execute(
        "INSERT INTO bestilling (bruker_id, clothes_id) VALUES (%s, %s)",
        (bruker_id, cid)
    )

    mydb.commit()
    mydb.close()

    return redirect("/clothes")


@app.route("/edit/<int:cid>")
def edit_clothes(cid):
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id, navn, pris, beskrivelse FROM clothes WHERE id = %s", (cid,))
    clothes = cursor.fetchone()
    mydb.close()
    return render_template("edit_clothes.html", clothes=clothes)


@app.route("/update", methods=["POST"])
def update_clothes():
    cid = request.form["id"]
    navn = request.form["navn"]
    pris = request.form["pris"]
    beskrivelse = request.form["beskrivelse"]

    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "UPDATE clothes SET navn = %s, pris = %s, beskrivelse = %s WHERE id = %s",
        (navn, pris, beskrivelse, cid)
    )
    mydb.commit()
    mydb.close()
    return redirect("/clothes")


@app.route("/delete/<int:cid>")
def delete_clothes(cid):
    mydb = get_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM clothes WHERE id = %s", (cid,))
    mydb.commit()
    mydb.close()
    return redirect("/clothes")

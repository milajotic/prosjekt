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


@app.route("/bestill/<int:cid>", methods=["GET", "POST"])
def bestill(cid):
    mydb = get_connection()
    cursor = mydb.cursor()

    # Get product info
    cursor.execute("SELECT id, navn, pris FROM clothes WHERE id = %s", (cid,))
    clothes = cursor.fetchone()

    if request.method == "POST":
        # Get customer info from the form
        fornavn = request.form["fornavn"]
        etternavn = request.form["etternavn"]
        epost = request.form["epost"]
        telefon = request.form.get("telefonnummer")
        adresse = request.form.get("adresse")

        # Check if user already exists
        cursor.execute("SELECT id FROM bruker WHERE epost = %s", (epost,))
        existing_user = cursor.fetchone()

        if existing_user:
            bruker_id = existing_user[0]
        else:
            # Insert new user
            cursor.execute(
                "INSERT INTO bruker (fornavn, etternavn, epost, telefonnummer, adresse) VALUES (%s, %s, %s, %s, %s)",
                (fornavn, etternavn, epost, telefon, adresse)
            )
            mydb.commit()
            bruker_id = cursor.lastrowid

        # Insert into bestilling
        cursor.execute(
            "INSERT INTO bestilling (bruker_id, clothes_id) VALUES (%s, %s)",
            (bruker_id, cid)
        )
        mydb.commit()
        mydb.close()

        # Redirect to confirmation page
        return redirect(f"/bestill/{cid}/bekreftelse")

    mydb.close()
    return render_template("bestill_form.html", clothes=clothes)


# ✅ CONFIRMATION PAGE ROUTE ADDED HERE
@app.route("/bestill/<int:cid>/bekreftelse")
def bestill_bekreftelse(cid):
    mydb = get_connection()
    cursor = mydb.cursor()

    cursor.execute("""
        SELECT 
            b.id, 
            b.bestillingsdato, 
            u.fornavn, 
            u.etternavn, 
            c.navn, 
            c.pris
        FROM bestilling b
        JOIN bruker u ON b.bruker_id = u.id
        JOIN clothes c ON b.clothes_id = c.id
        WHERE c.id = %s
        ORDER BY b.id DESC
        LIMIT 1
    """, (cid,))

    order = cursor.fetchone()
    mydb.close()

    return render_template("bekreftelse.html", order=order)


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

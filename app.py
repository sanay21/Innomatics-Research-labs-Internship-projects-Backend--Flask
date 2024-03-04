from flask import Flask, request, render_template , redirect , url_for

app = Flask(__name__)

notes = []

##################################
@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:  
            notes.append(note)  
            return redirect(url_for('thankyou'))  
    return render_template("home_page.html", notes=notes)

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou_page.html")

##################################

if __name__ == "__main__":
    app.run(debug=True)
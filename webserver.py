from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/hi", methods=['GET'])
def handle_hi():
    if request.method == 'GET':
        name = "Gitu"
        text = render_template("hi.html",
                               target="handle_hi",
                               greet = name)
        return text

@app.route("/hi", methods=['GET', 'POST'] )
def handle_hipost():
    name = request.form['name']
    age = int(request.form['age'])
    if age < 18:
            message = "sorry, you have to wait till 18 to drive"
    else:
            message = "Hurry!!!!!!, you can drive"

    text = render_template("hi_response.html",
                               target="handle_hi",
                               name = name,
                               message = message)

    #return text    # to send HTML back
    return message  # if you want to send plain text back


@app.route("/bye")
def bye():
    text = render_template("bye.html")
    return text


if __name__ == "__main__":
    app.run(debug=True)   # this debug flag detects "code file chagnes & start Flash server automatically"

from flask import Flask, request

app = Flask(__name__)
NOTEPAD_FILE = "notepad.txt"

@app.route("/updatefortoday", methods=['GET', 'POST'])  #http://localhost:5000/updatefortoday
def update_for_today():
    if request.method == 'POST':
        note = request.form.get('note', '')
        with open(NOTEPAD_FILE, 'a') as file:
            file.write(note + '\n')
        return "Note updated successfully!"
    else:
        return '''
    <html>
    <head>
        <title>Update for Today</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f4f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: #fff;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                width: 500px;
                text-align: center;
            }
            textarea {
                width: 100%;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #ccc;
                resize: none;
                font-size: 16px;
                margin-bottom: 15px;
            }
            input[type="submit"] {
                background-color: #007BFF;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
            h2 {
                margin-bottom: 20px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Update for Today</h2>
            <form method="post" action="/updatefortoday">
                <textarea name="note" rows="5" cols="50" placeholder="Write your note here..."></textarea><br>
                <input type="submit" value="Submit Note" />
            </form>
        </div>
    </body>
    </html>
    '''


@app.route("/share", methods=['GET'])           #http://localhost:5000/share
def share():
    try:
        with open(NOTEPAD_FILE, 'r') as file:
            content = file.read()
        return f"<h2>Today's Notes:</h2><pre>{content}</pre>"
    except FileNotFoundError:
        return "<h2>No notes available yet.</h2>"

@app.route("/clearnotepadtxt", methods=['GET']) ##http://localhost:5000/clearnotepadtxt
def clear_notepad_txt():
    open(NOTEPAD_FILE, 'w').close()
    return "<h2>Notepad cleared successfully!</h2>"

if __name__ == '__main__':
    app.run()

import os

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        return render_template('index.html', result=text)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

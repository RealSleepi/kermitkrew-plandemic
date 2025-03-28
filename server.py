from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This will look for index.html in the templates folder

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Run the app on port 80

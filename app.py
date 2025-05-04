import webview
import threading
from flask import Flask, render_template

# Set up the Flask app
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return render_template("index.html")  # Loads from /templates/index.html

# Run Flask on a separate thread
def run_flask():
    flask_app.run(debug=False, port=5000)

if __name__ == '__main__':
    # Start Flask server in background
    threading.Thread(target=run_flask, daemon=True).start()

    # Create the webview window pointing to local server
    webview.create_window("Media App", "http://localhost:5000")

from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Define folder paths
FIRST_PRINT_FOLDER = "uploads/first_print"
SECOND_PRINT_FOLDER = "uploads/second_print"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    file_path = request.form.get("folder")
    
    if file_path == "first_print":
        result = "Original"
    elif file_path == "second_print":
        result = "Counterfeit"
    else:
        result = "Unknown"
    
    return f"Result: {result}"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request
import os
from datetime import datetime
import openpyxl

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
EXCEL_FILE = 'log.xlsx'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(EXCEL_FILE):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Timestamp", "Image Path"])
    workbook.save(EXCEL_FILE)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    if file:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        workbook = openpyxl.load_workbook(EXCEL_FILE)
        sheet = workbook.active
        sheet.append([timestamp, filepath])
        workbook.save(EXCEL_FILE)
        
        return "File uploaded successfully", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

import os
from flask import Flask, send_from_directory

app = Flask(__name__)

# Thay đổi: trỏ vào thư mục 'images' nằm cùng cấp với app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_FOLDER = os.path.join(BASE_DIR, 'images')

@app.route('/')
def index():
    # Tìm file có tên '1' bất kể đuôi là gì
    for f in os.listdir(IMG_FOLDER):
        if f.startswith('1.'):
            return f'</h1><img src="/images/{f}" style="max-width:1000px;">'
    return "Không tìm thấy file tên là 1"

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMG_FOLDER, filename)

if __name__ == '__main__':
    app.run()

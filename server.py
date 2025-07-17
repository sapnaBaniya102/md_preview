from flask import Flask, send_from_directory, jsonify, request
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(BASE_DIR, filename)

@app.route('/list-md')
def list_md():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith('.md')]
    return jsonify(files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if not file.filename.endswith('.md'):
        return jsonify({'error': 'Only .md files allowed'}), 400
    save_path = os.path.join(BASE_DIR, file.filename)
    file.save(save_path)
    return jsonify({'filename': file.filename})

# --- EDIT FEATURE (NEW) ---
@app.route('/edit', methods=['POST'])
def edit_md():
    data = request.get_json()
    filename = data.get('filename')
    content = data.get('content')
    if not filename or not filename.endswith('.md'):
        return jsonify({'error': 'Invalid filename'}), 400
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File does not exist'}), 404
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return jsonify({'success': True, 'filename': filename})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- DELETE FEATURE (NEW) ---
@app.route('/delete', methods=['POST'])
def delete_md():
    data = request.get_json()
    filename = data.get('filename')
    if not filename or not filename.endswith('.md'):
        return jsonify({'error': 'Invalid filename'}), 400
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File does not exist'}), 404
    try:
        os.remove(filepath)
        return jsonify({'success': True, 'filename': filename})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)

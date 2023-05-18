from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file.filename.endswith('.pdf'):
        pdf = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

        with open('output.txt', 'w') as output_file:
            output_file.write(text)

        return render_template('preview.html', text=text)

    return 'Invalid file format. Please upload a PDF file. <a href="/">Go back</a>'

@app.route('/download')
def download():
    return app.send_static_file('output.txt')

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, make_response
import pdfkit

app = Flask(__name__)

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title', 'Başlık Yok')
        content = request.form.get('content', 'İçerik Yok')
        
        html = render_template('template.html', title=title, content=content)
        
        pdf = pdfkit.from_string(html, False, configuration=config)
        
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
        return response
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
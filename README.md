# Flask HTML to PDF Converter

This project is a Flask application that allows users to convert text entered via a web interface into a PDF file. It features a modern and responsive design using Tailwind CSS.

## Features
- Users can enter a title and content.
- The entered data is converted into a PDF file.
- Modern and responsive design using Tailwind CSS.
- Fast and efficient web application powered by Flask.

## Installation
Follow these steps to run the project on your local machine.

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/utkyfact/python-html-to-pdf.git
   cd python-html-to-pdf
   ````
   1.Create and Activate a Virtual Environment (Optional):
   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate     # Windows
   ````
   2.Install Required Packages:
   ```bash
   pip install -r requirements.txt
   ````
   3.Install wkhtmltopdf:
    Download and install wkhtmltopdf from the official website.
    After installation, specify the path to wkhtmltopdf in the app.py file:
   ```bash
   config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
   ````
   4.Run the Application:
   ```bash
   python app.py
   ````
   5.Open in Browser:
   The application will run at http://127.0.0.1:5000/. Open this URL in your browser.
   
### Usage
  1.Enter a title and content on the homepage.
  2.Click the "Create PDF" button.
  3.The PDF file will be automatically downloaded.

### Contributing
If you'd like to contribute, please open an issue or submit a pull request. We welcome your contributions!

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Acknowledgments
-Thanks to Flask.
-Thanks to Tailwind CSS.
-Thanks to pdfkit and wkhtmltopdf.

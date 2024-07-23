from flask import Flask, render_template, request, jsonify
import requests
import PyPDF2
import os
import traceback

proxies = {
    'http': 'http://127.0.0.1:5000',
}

colab_url = 'https://f663-35-227-129-167.ngrok-free.app'  # Replace with your actual Colab endpoint URL

def call_colab_endpoint(url: str, text: str):
    try:
        print('CALLING')
        response = requests.post(url, json={"prompt": text}, verify=False, proxies=proxies, timeout=1200)
        if response.status_code == 200:
            print(response.json().get('completion'))
            return response.json().get('completion', 'The Model did not respond :(')
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        print(f"Exception in call_colab_endpoint: {e}")
        return f"Exception: {str(e)}"

def convert_pdf(pdf_file: str):
    try:
        pdf_text = []
        with open(pdf_file, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file, strict=False)
            for page in pdf_reader.pages:
                content = page.extract_text()
                if content:
                    pdf_text.append(content)
        return " ".join(pdf_text)
    except Exception as e:
        print(f"Exception in convert_pdf: {e}")
        return ""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showInterface')
def show_interface():
    return render_template('input.html')

@app.route('/submitform', methods=["POST"])
def send_text_to_colab():
    try:
        # Extract form data
        symptoms = request.form.get('symptoms')
        family_history = request.form.get('family_history')
        diagnosis = request.form.get('diagnosis')
        recent_surgeries = request.form.get('recent_surgeries')
        medications = request.form.get('medications')
        allergies = request.form.get('allergies')
        social_history = request.form.get('social_history')
        physical_exam = request.form.get('physical_exam')

        # Combine the extracted data for demonstration purposes
        result_text = f"""
History of Present Illness:
{symptoms if symptoms != '' else "None"}

Past Medical History:
{recent_surgeries if recent_surgeries != '' else "None"}
{diagnosis if diagnosis != '' else "None"}

Medications:
{medications if medications != '' else "None"}

Allergies:
{allergies if allergies != '' else "None"}

Social History:
{social_history if social_history != '' else "None"}

Family History:
{family_history if family_history != '' else "None"}

Physical Examination:
{physical_exam if physical_exam != '' else "None"}   
"""
        print('FINISHED FORMATTING')

        colab_response = call_colab_endpoint(colab_url + '/formrequest', result_text)

        print('FINISHED CALLING')

        # Render the result template with the combined text
        return render_template('result.html', answer=colab_response)
    except Exception as e:
        print(f"Exception in send_text_to_colab: {e}")
        return render_template('result.html', answer="Error occurred while processing the form")

@app.route('/submitpdf', methods=["POST"])
def send_pdf_to_colab():
    try:
        if 'pdf' not in request.files:
            return render_template('result.html', answer="~~Please Select A File!~~")
        
        file = request.files['pdf']
        
        if file.filename == '':
            return render_template('result.html', answer="~~Please Select A File~~")
        
        if file:
            if not os.path.exists('uploads'):
                os.makedirs('uploads')
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            
            pdf_to_text = convert_pdf(file_path)
            os.remove(file_path)

            colab_response = call_colab_endpoint(colab_url + '/pdfrequest', pdf_to_text)
            
            return render_template('result.html', answer=colab_response)
    except Exception as e:
        print(f"Exception in send_pdf_to_colab: {e}")
        return render_template('result.html', answer="Error occurred while processing the PDF")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

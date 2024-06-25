# MedicAI: Transforming Symptoms into Solutions

## Overview

MedicAI is an innovative tool designed to diagnose diseases and suggest treatment plans based on user-provided symptoms. By leveraging advanced data analysis techniques and machine learning, MedicAI aims to reduce misdiagnoses and optimize patient recovery times. It also ensures the privacy of users by hiding Sensitive Personal Identifiable Information (SPII).

## Features

- **Enhanced Precision**: MedicAI analyzes patient symptoms and medical history to provide highly accurate diagnostic suggestions, reducing the risk of misdiagnosis.
- **Comprehensive Data Analysis**: It processes vast amounts of medical literature, clinical guidelines, and patient records to ensure thorough and evidence-based diagnostic support.
- **Tailored Recommendations**: By considering individual patient profiles, including genetic information and previous treatment responses, MedicAI offers personalized treatment options that maximize effectiveness.
- **Reduced Trial and Error**: Streamlining the selection of therapies, MedicAI minimizes the guesswork, leading to faster and more effective patient recovery.

## Technologies Used

- **Visual Studio Code**
- **Flask**
- **Spacy**
- **Google Colab**
- **Python**
- **HTML/CSS**

## Challenges

- **Limited Datasets**: We encountered very few trustworthy datasets, managing to find only one good dataset on Hugging Face.
- **Computational Power**: Due to limited computational power, fine-tuning large language models (LLMs) was challenging. However, we were able to accomplish this for a few epochs using multiple Google Colab accounts.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/TXAED/MedicAI.git
   cd MedicAI
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```sh
   flask run
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000` to access MedicAI.

## Usage

1. **Input Symptoms**: Enter the symptoms and any relevant medical history.
2. **Diagnosis**: MedicAI will analyze the input data and provide a diagnostic suggestion.
3. **Treatment Plan**: Based on the diagnosis, MedicAI will suggest a personalized treatment plan.


PDF Text Extraction using Google Cloud Vision API

This Python script extracts text from PDF files using the Google Cloud Vision API. It converts each page of the PDF into an image and performs Optical Character Recognition (OCR) to extract text.
Prerequisites

    Python 3.x installed on your system.
    Install required Python packages:

    pip install google-cloud-vision pdf2image

Setup

    Obtain Google Cloud Vision API credentials JSON file. Follow the instructions here to create a service account and download the JSON file containing your credentials.

    Replace 'YOURJSONPATH' in the script with the path to your JSON credentials file.

Usage

Replace 'YOURPDFFILEPATH' with the path to the PDF file you want to extract text from.

python

from google.cloud import vision
import os
from pdf2image import convert_from_path
from io import BytesIO

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'YOURJSONPATH'

def detect_document(path):
    # Check if Path Exists
    if not os.path.exists(path):
        print("The provided path doesn't exist.")
        return

    # Convert PDF to images
    images = convert_from_path(path)

    # Create Google Vision Client
    client = vision.ImageAnnotatorClient()

    for i, image in enumerate(images):
        # Convert image to bytes
        with BytesIO() as output:
            image.save(output, format="JPEG")
            content = output.getvalue()

        # Convert image content to Google Vision Image
        image = vision.Image(content=content)

        # Make OCR Request
        response = client.document_text_detection(image=image)

        # Check if Error Message Exists
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )

        # Extract text from response
        text = response.full_text_annotation.text
        print(f"Extracted text from page {i+1}:\n{text}")

# Call the function with the path to your PDF file
detect_document('YOURPDFFILEPATH')

Run the script, and it will print the extracted text from each page of the provided PDF file.

from google.cloud import vision
import os
from pdf2image import convert_from_path

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


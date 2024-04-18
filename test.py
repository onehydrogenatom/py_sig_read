from google.cloud import vision
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/bendw/Downloads/arkidssig-37345b404336.json'

def detect_document(path):
    # Check if Path Exists
    if not os.path.exists(path):
        print("The provided path doesn't exist.")
        return

    # Create Google Vision Client
    client = vision.ImageAnnotatorClient()

    # Read the image file
    with open(path, 'rb') as image_file:
        content = image_file.read()

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
    print("Extracted text:\n", text)

# Call the function with the path to your JPEG image
detect_document('/Users/bendw/Downloads/text_sig.jpg')

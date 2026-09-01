import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image):
    """
    Extract text from a preprocessed image using Tesseract OCR.

    Parameters:
        image: Preprocessed image as a NumPy array.

    Returns:
        str: Extracted text.
    """
    try:
       text = pytesseract.image_to_string(image, config="--psm 3")
       return text.strip()

    except Exception as error:
        print(f"OCR Error: {error}")
        return ""
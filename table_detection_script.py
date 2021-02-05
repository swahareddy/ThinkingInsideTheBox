import camelot_detection
import boundingboxes_method_detection

input_pdf_filepath="input samples\Important Formulae.pdf"

import pdfplumber
with pdfplumber.open(input_pdf_filepath) as pdf:
    page = pdf.pages[0] #Sampling the first page to draw conclusion about the whole PDF
    text = page.extract_text()
    if(text)==None:
        print("PDF without digital text")
        boundingboxes_method_detection.find_boundingboxes_tables(input_pdf_filepath)

    else:
        if (camelot_detection.find_camelot_tables(input_pdf_filepath)): #Returns 1 if failed, prints "Digital PDF, Camelot detection done if succesful"
            #"PDF with digital text, but no easily identified tables"
            boundingboxes_method_detection.find_boundingboxes_tables(input_pdf_filepath)

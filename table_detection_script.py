import camelot_detection
import boundingboxes_method_detection

input_pdf_filepath=r"input samples\twotables_2.pdf"

import pdfplumber
import pandas as pd
dataframes_found=1
with pdfplumber.open(input_pdf_filepath) as pdf:
    page = pdf.pages[0] #Sampling the first page to draw conclusion about the whole PDF
    text = page.extract_text()

    '''
    if(text is not None): #Hoping to get clean responses from digital PDFs
        dataframes_found=camelot_detection.find_camelot_tables(input_pdf_filepath)
    '''

    if not (isinstance(dataframes_found, list)): #if the above (camleot) method has not found anything. (Since not all digital PDFs present their tables we need to use image processing etc)
        dataframes_found=boundingboxes_method_detection.find_boundingboxes_tables(input_pdf_filepath)

    if (isinstance(dataframes_found, list)):
        print("Number of tables found = "+str(len(dataframes_found)))
        # print(dataframes_found)
        print("One of our methods found table(s)")
    else:
        print("No tables found using any of the methods")

    '''
    if(text)==None:
        print("PDF without digital text")
        dataframes_found=boundingboxes_method_detection.find_boundingboxes_tables(input_pdf_filepath)

    else:
        dataframes_found=camelot_detection.find_camelot_tables(input_pdf_filepath)
        if (isinstance(dataframes_found, pd.DataFrame)): #Returns 1 if failed and prints "Digital PDF, Camelot detection done if succesful". Else returns the dataframe
            #Prints "PDF with digital text, but no easily identified tables"
            dataframes_found=boundingboxes_method_detection.find_boundingboxes_tables(input_pdf_filepath)
    
        else:

            print("No tables found using any of the methods")
    '''

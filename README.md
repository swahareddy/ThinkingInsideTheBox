# Table detection in PDFs using Python

Nothing new that I'm doing here, just trying to fine tune it for my use case.
GCP's DocumentAI already does a great job at extracting structured data, but the ask was for an open source solution due to security constraints.

Inspired by these blogs:
 - https://towardsdatascience.com/a-table-detection-cell-recognition-and-text-extraction-algorithm-to-convert-tables-to-excel-files-902edcf289ec

Notes:
- C:/Users/swaha/AppData/Local/Programs/Python/Python39/python.exe -m pip install opencv-python

### Questions for ythe team:
- How do you distinguish between digital text and scanned PDFs
- Is it okay to assume that a PDF that is digital is digital throughout and vice versa?
- In your current pipeline are you breaking the PDF into a PDF per page? I can use those page PDFs itself then.
- Is there too much time complexity right now?
- Please share sample PDFs
- What does the swiss method do about multiple tables in the same page

### Things to do
- OpenCV method forcefully makes one table in a page even when there are multiple tables.


## Conclusion
![](alogostrategy.png)

If the PDF is text-based, use Camelot for 100% accurate results 
    But not all text based PDF's tables get detected.

If the PDF is scanned/image-based, use bounding boxes method
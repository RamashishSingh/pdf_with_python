from os import write
from re import template
import PyPDF2
# import sys

# input = sys.argv[1:]

# def watermarker(pdf_file):

#     with open ('wtr.pdf','rb') as file:
#         reader = PyPDF2.PdfFileReader('wtr.pdf')
#         page = reader.getpage(0)

#     with open ('two.pdf','rb') as file1:
#         reader = PyPDF2.PdfFileReader('twopage.pdf')
#         page1 = reader.getpage(0)
    
#     writer = PyPDF2.PdfFilewriter()
#     writer.mergepage(page1)

# watermarker(input)

#solution by vid

teplate = PyPDF2.PdfFileReader(open('merged_pdf.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb')) 
output = PyPDF2.PdfFileWriter()

for i in range(teplate.getNumPages()):
    page = teplate.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open("watermarked.pdf",'wb')as file:
    output.write(file)
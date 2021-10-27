import PyPDF2 # it is a module with which we can do manipulation with PDF files

with open('dummy.pdf','rb')as file: # to open dummy.pdf file in Read in binary mode
    reader = PyPDF2.PdfFileReader('dummy.pdf') # once file opened then we have to read our dummy.pdf file with .pdfFileReader
    page = reader.getPage(0) # with .getpage(0) we  are in page no 1 in pdf
    page.rotateClockwise(90) # rotate the page which we have readed with clockwise 90 degree
    writer = PyPDF2.PdfFileWriter() #created writer object to write a file
    writer.addPage(page) #added a page which we have to manipulate
    with open('new_dummy.pdf','wb')as new_file: #open new file in which we have to add and make changes if new_dummy file is not their then it will create the new_dummy file
        writer.write(new_file) # now saved at new page in new_dummyfile 

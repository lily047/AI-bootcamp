from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

doc = PdfReader('doc.pdf')

writer = PdfWriter() #used to write in pdfs. 

def output_file():

    with open("output.txt", 'w', encoding='utf-8',) as output_file: 

        for page in doc.pages: 

            line = page.extract_text()

            output_file.write(line)

            output_file.write("\n==========================================================")

            output_file.write('\n\n') 

def making_pdf():

    c = canvas.Canvas('output2.pdf') #creates a canvas, like a blank pdf. 

    with open('output.txt', 'r', encoding = 'utf-8') as sourcefile: 

        lines = sourcefile.readlines()

        y = 800 #starting coordinate of the file. 
        #800 points from the bottom of the file 
        #In pdfs, coordinates start from the bottom of the file. 

        for i, line in enumerate(lines): 

            if i%2==0: 

                c.drawString(50, y, line.strip())
                #drawSting() is a method used to write text on canvas
                # 50 is the horizontal position, stating that the text starts from here. 
                # y is the vertical position, starts from  800 then we decrease it. 
                # line.strip() removes neline chars from the end  

                y-=15

    c.save() #saving the canvas


if __name__ == '__main__': 

    making_pdf()
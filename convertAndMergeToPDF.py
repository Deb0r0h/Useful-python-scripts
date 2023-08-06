from PIL import Image
from PyPDF2 import PdfWriter, PdfReader
import os

def convertTo(source_dir, output_dir):
    for file in os.listdir(source_dir):
        if file.split('.')[-1] in ('png','jpg','jpeg'):
            image = Image.open(os.path.join(source_dir,file))
            image_converted = image.convert('RGB')
            image_converted.save(os.path.join(output_dir,'{0}.pdf'.format(file.split('.')[-2])))

def mergePDF():
    pdf_writer = PdfWriter()
    pdf_files = [_ for _ in os.listdir('./PDFs') if _.endswith('.pdf')]
    t = 1
    for pdf_file in pdf_files:
        print(str(t) + " done")
        with open('./PDFs/{0}'.format(pdf_file),'rb') as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                page.compress_content_streams()
                pdf_writer.add_page(page)
        t = t+1
    with open('./PDFs/Slides.pdf','wb') as output:
        pdf_writer.write(output)


#stub 
def ConvertAndMergeImageToPDF(source_dir,output_dir):
    convertTo(source_dir,output_dir)
    mergePDF()


#Nome della cartella contenente le immagini
source_dir= './Images'
#Nome della cartella in cui vengono salvati i file
output_dir = './PDFs'
mergePDF()

#ConvertAndMergeImageToPDF(source_dir,output_dir)



from fpdf import FPDF
import os

# Any results you write to the current directory are saved as output.
#MEDIA_ROOT = os.path.join(BASE_DIR,"media")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def createPDF(content, file_path):
    print("file path obtained is {}".format(file_path))
    pdf = FPDF()
    pdf.set_font("Arial", size=8)
    pdf.add_page()
    pdf.cell(0, 3, txt="List of nearby hospitals for your treatment - ",ln=2)
    for i in range(len(content)):
        name = content[i]['name']
        address = content[i]['address']
        dis = content[i]['dis']
        pdf.cell(0, 3, txt="{}".format(name), ln=1)
        pdf.cell(0, 3, txt="{}".format(address), ln=1)
        pdf.cell(0, 3, txt="distance: {} metres".format(dis), ln=1)
        pdf.cell(0, 3, txt="", ln=2)
    pdf.output(file_path)
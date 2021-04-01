import docx
from docx import Document

def create_nda(partyname,title):
    document = Document()
    document.add_paragraph('Test NDA for ' + str(partyname))
    document.save(title + '.docx')


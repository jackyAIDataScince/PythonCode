from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise

document = load_file("resume.pdf")

visualise(document)

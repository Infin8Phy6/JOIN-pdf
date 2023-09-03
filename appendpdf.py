import PyPDF2

# Open the PDF files you want to append
pdf1 = open('1.pdf', 'rb')
pdf2 = open('2.pdf', 'rb')

# Create PDF file readers
pdf_reader1 = PyPDF2.PdfReader(pdf1)
pdf_reader2 = PyPDF2.PdfReader(pdf2)

# Create a PDF file writer
pdf_writer = PyPDF2.PdfWriter()

# Append the pages from the first PDF
for page in pdf_reader1.pages:
    pdf_writer.add_page(page)

# Append the pages from the second PDF
for page in pdf_reader2.pages:
    pdf_writer.add_page(page)

# Create a new PDF file to save the result
output_pdf = open('combined.pdf', 'wb')

# Write the combined PDF to the output file
pdf_writer.write(output_pdf)

# Close the input and output files
pdf1.close()
pdf2.close()
output_pdf.close()

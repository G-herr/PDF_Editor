from PyPDF2 import PdfFileWriter, PdfFileReader


watermark = PdfFileReader("water.pdf")
reader = PdfFileReader("merged.pdf")
writer = PdfFileWriter()

for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    page.mergePage(watermark.getPage(0))
    writer.addPage(page)

# finally, write the new document with a watermark
with open("watermarked.pdf", "wb") as outputFile:
    writer.write(outputFile)

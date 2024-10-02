import PyPDF2


def rotate_page(file_name, new_name, page, angle):
    with open(file_name, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(page)
        page.rotateCounterClockwise(angle)

        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open(new_name, 'wb') as new_file:
            writer.write(new_file)


if __name__ == '__main__':
    page_to_rotate = 0
    angle = 90
    file_name = 'dummy.pdf'
    new_name = 'tilt.pdf'

    rotate_page(file_name, new_name, page_to_rotate, angle)

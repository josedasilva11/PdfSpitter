import os
from io import BytesIO, StringIO

import dateutil.parser
from PyPDF2 import PdfReader, PdfWriter, PdfFileReader
from PyPDF2.generic import createStringObject, NameObject
from flask import send_file
from fpdf import FPDF

from pdf_test import fill_pdf


def print_pdf(data):
    fix_dates(data)
    data['text_48csyn'] = data['store_prefix'] + str(data['id'])
    data['textarea_1deug'] = data['obs']
    data['text_38bfne'] = data['car_license']
    buf = BytesIO()
    fill_pdf("root_2.pdf", buf, data)
    buf.seek(0)
    return send_file(buf, mimetype='application/pdf',
                     download_name=f"{data['store_prefix']}{data['client_renter_name']}.{data['id']}.pdf")


def add_mark(out_file, text):
    pdf = FPDF(format='letter', unit='pt')

    pdf.add_page()
    pdf_style = 'B'


    pdf.set_font("Arial",   size=7)
    pdf.set_xy(480, 730)
    pdf.cell(1, 1, txt=text, ln=0)
    pdf.output(out_file + "_tmp.pdf")
    pdf.close()

    reader = PdfReader(out_file)
    overlay_pdf = PdfReader(out_file + "_tmp.pdf")
    writer = PdfWriter()

    reader.getPage(0).mergePage(overlay_pdf.getPage(0))
    writer.addPage(reader.getPage(0))
    writer.set_need_appearances_writer()
    writer.write(out_file + "_marked.pdf")
    os.unlink(out_file + "_tmp.pdf")


def fix_dates(data):
    for key in data:
        if key.count('_date') or key.count('date_'):
            if isinstance(data[key], str):
                try:
                    data[key] = dateutil.parser.parse(data[key]).strftime("%d/%m/%Y")

                except BaseException as b:
                    print(b)
            else:
                data[key] = data[key].strftime("%d/%m/%Y")


def add_suffix(data, param):
    new_dict = {}
    for a in data :
        new_dict[a + param] = data[a]

    return new_dict


def print_three_pdf(data):
    fix_dates(data)
    buf = BytesIO()
    data['text_38bfne'] = data['car_license']
    data['footertext'] = "1. ORIGINAL"
    data['textarea_1deug'] = data['obs']
    data['text_48csyn'] = data['store_prefix'] + str(data['id'])
    pdf_one = f"{data['store_prefix']}{data['client_renter_name']}.{data['id']}_1.pdf"
    with open(pdf_one, 'wb') as outfile:
        fill_pdf("root_2.pdf", outfile, data)


    data['footertext'] = "2. AUTORIDADE"
    pdf_two = f"{data['store_prefix']}{data['client_renter_name']}.{data['id']}_2.pdf"
    with open(pdf_two, 'wb') as outfile:
        fill_pdf("root_2_page2.pdf", outfile, add_suffix(data,'_page2'))

    data['footertext'] = "3. CLIENTE"
    pdf_three = f"{data['store_prefix']}{data['client_renter_name']}.{data['id']}_3.pdf"
    with open(pdf_three, 'wb') as outfile:
        fill_pdf("root_2_page3.pdf", outfile, add_suffix(data,'_page3'))



    writer = PdfWriter()

    # Merge the overlay page onto the template page
    files = []
    three_additional_pdf_ = [pdf_one , pdf_two, pdf_three ,
                             'additional.pdf']
    for pdf in three_additional_pdf_:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.addPage(page)

    writer.set_need_appearances_writer()
    writer.write(buf)
    for item in files:
        item.close()

    buf.seek(0)

    os.unlink(pdf_one)
    os.unlink(pdf_two)
    os.unlink(pdf_three)

    return send_file(buf, mimetype='application/pdf',
                     download_name=f"{data['client_renter_name']}{data['store_prefix']}.{data['id']}_combined.pdf")

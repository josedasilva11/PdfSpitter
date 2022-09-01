import datetime
from io import BytesIO

import pdfrw
from datetime import date

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import createStringObject, NameObject, IndirectObject, BooleanObject
from pdfrw import PdfArray, PdfDict

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_FIELD_BORDER = '/Border'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
PARENT_KEY = '/Parent'
WIDGET_SUBTYPE_KEY = '/Widget'


def dump_pdf(input_pdf_path):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        if annotations is not None:
            for annotation in annotations:
                if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                    if annotation[ANNOT_RECT_KEY]:
                        rect = annotation[ANNOT_RECT_KEY]
                    if PARENT_KEY in annotation:
                        annotation = annotation[PARENT_KEY]
                    if annotation[ANNOT_FIELD_KEY]:
                        key = annotation[ANNOT_FIELD_KEY][1:-1]
                        # print(f"{key}:string = ''")
                        # print(f"'{key}':'{key}',")
                        print(f"'{key}':{rect}")
                        # if key.count('date')>0:
                        #     print(f"{key} =  db.Column(db.DateTime )")
                        # else:
                        #     print(f"{key} =  db.Column(db.String(100))")
                        # label = string.capwords(key.replace("_", " "))
                        # print(
                        #     f" <div class=\"col-md-3\">  <b-form-group label=\"{label}\">    <b-form-input v-model=\"{key}\"  placeholder=\"{label}\"></b-form-input> </b-form-group> </div>")


def fill_pdf(input_pdf_path, buf, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        if annotations is not None:
            for annotation in annotations:
                if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                    annotation.update(
                        pdfrw.PdfDict(Border=PdfArray([0, 0, 0]))
                    )
                    annotation.update(
                        pdfrw.PdfDict(MK=PdfDict(BC=PdfArray([0, 0, 0])))
                    )
                    if PARENT_KEY in annotation:
                        annotation = annotation[PARENT_KEY]
                    if annotation[ANNOT_FIELD_KEY]:
                        key = annotation[ANNOT_FIELD_KEY][1:-1]
                        key = key.replace('\\137','_')
                        if key in data_dict.keys():
                            annotation.update(
                                pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                            )
                            annotation.update(pdfrw.PdfDict(AP=''))
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(buf, template_pdf)
    buf.seek(0)


# NEW
def fill_simple_pdf_file(data, template_input, template_output):
    some_date = date.today()
    data_dict = {
        'name': data.get('name', ''),
        'phone': data.get('phone', ''),
        'date': some_date,
        'account_number': data.get('account_number', ''),
        'cb_1': data.get('cb_1', False),
        'cb_2': data.get('cb_2', False),
    }
    return fill_pdf(template_input, template_output, data_dict)


def clone_pdf(sfx):
    template = PdfFileReader(open("root_2.pdf", "rb"))
    page = template.pages[0]
    for j in range(0, len(page['/Annots'])):

        annots_j_ = page['/Annots'][j].getObject()
        if '/Parent' not in annots_j_:
            continue
        parent = annots_j_['/Parent']
        if parent is None:
            continue
        item = parent.getObject()
        writer_annot = item.getObject()
        annot_get = writer_annot.get('/T')
        if annot_get is not None:
            writer_annot.update({
                NameObject("/T"): createStringObject(annot_get + sfx)
            })
    writer = PdfFileWriter()
    writer.appendPagesFromReader(template)
    with open(f"root_2{sfx}.pdf",'wb') as output:
        set_need_appearances_writer(writer)
        writer.write(output)

def set_need_appearances_writer(writer):
    # See 12.7.2 and 7.7.2 for more information:
    # http://www.adobe.com/content/dam/acom/en/devnet/acrobat/
    #     pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree and add "/NeedAppearances attribute
        if "/AcroForm" not in catalog:
            writer._root_object.update(
                {
                    NameObject("/AcroForm"): IndirectObject(
                        len(writer._objects), 0, writer
                    )
                }
            )

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print("set_need_appearances_writer() catch : ", repr(e))
        return writer
def to_data_buf():
    from flask import send_file
    buf = io.BytesIO()
    data = write_fillable_pdf()  # With some arguments
    return send_file(buf, mimetype='application/pdf')
    return buf

#_page1
if __name__ == '__main__':
    dump_pdf('root_2.pdf')
    clone_pdf('_page3')
    # print(datetime.date.today().strftime("%d-%m-%Y"))
    # # pdf_template = "template.pdf"
    # # pdf_output = "output.pdf"
    # #
    # sample_data_dict = {
    #     'to_be_paid': 'to_be_paid',
    #     'to_be_paid2': 'to_be_paid2',
    #     'to_be_paid3': 'to_be_paid3',
    #     'client_renter_name': 'client_renter_name',
    #     'client_renter_name2': 'client_renter_name2',
    #     'renter_address': 'renter_address',
    #     'renter_address2': 'renter_address2',
    #     'renter_address3': 'renter_address3',
    #     'renter_address4': 'renter_address4',
    #     'cont_no': 'cont_no',
    #     'business_address': 'business_address',
    #     'business_address2': 'business_address2',
    #     'business_tel': 'business_tel',
    #     'license_number': 'license_number',
    #     'license_country': 'license_country',
    #     'license_date': 'license_date',
    #     'passport_number': 'passport_number',
    #     'passport_country': 'passport_country',
    #     'passport_date': 'passport_date',
    #     'text_24also': 'text_24also',
    #     'text_25uuel': 'text_25uuel',
    #     'additional_driver': 'additional_driver',
    #     'license2_number': 'license2_number',
    #     'license2_country': 'license2_country',
    #     'license2_date': 'license2_date',
    #     'to_be_checked_in_at': 'to_be_checked_in_at',
    #     'date_form': 'date_form',
    #     'time_form': 'time_form',
    #     'car_model': 'car_model',
    #     'car_license': 'car_license',
    #     'car_owner': 'car_owner',
    #     'car_checked_in_at': 'car_checked_in_at',
    #     'car_rented_at': 'car_rented_at',
    #     'date_in': 'date_in',
    #     'date_out': 'date_out',
    #     'time_in': 'time_in',
    #     'time_out': 'time_out',
    #     'form_number': 'form_number',
    #
    # }
    # buf = BytesIO()
    # fill_pdf("root_2.pdf", buf, sample_data_dict)
    # with open("testout.pdf", "wb") as out_file:
    #     out_file.write(buf.read())
    # fill_simple_pdf_file(sample_data_dict, pdf_template, pdf_output)

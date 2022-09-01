from datetime import date
from typing import Dict

import dateutil.parser
from sqlalchemy_serializer import SerializerMixin
from dateutil.parser import isoparse
from app import db

car_applicant_allowed_fields = ['is_black_listed',
                                'to_be_paid',
                                'to_be_paid2',
                                'to_be_paid3',
                                'client_renter_name',
                                'client_renter_name2',
                                'renter_address',
                                'renter_address2',
                                'renter_address3',
                                'renter_address4',
                                'cont_no',
                                'business_address',
                                'business_address2',
                                'business_tel',
                                'license_number',
                                'license_country',
                                'license_date',
                                'passport_number',
                                'passport_country',
                                'passport_date',
                                'place_of_birth',
                                'date_of_birth',
                                'additional_driver',
                                'license2_number',
                                'license2_country',
                                'license2_date',
                                'to_be_checked_in_at',
                                'date_form',
                                'time_form',
                                'car_model',
                                'car_license',
                                'car_owner',
                                'car_checked_in_at',
                                'car_rented_at',
                                'date_in',
                                'date_out',
                                'time_in',
                                'time_out',
                                'form_number',
                                ]


class CarApplicant(db.Model, SerializerMixin):
    serialize_rules = ()
    serialize_only = ()
    id = db.Column(db.Integer, primary_key=True)
    is_black_listed = db.Column(db.Boolean, default=False)
    to_be_paid = db.Column(db.String(100), default='')
    to_be_paid2 = db.Column(db.String(100), default='')
    store_prefix = db.Column(db.String(100), default='')
    to_be_paid3 = db.Column(db.String(100), default='')
    client_renter_name = db.Column(db.String(100), default='')
    client_renter_name2 = db.Column(db.String(100), default='')
    renter_address = db.Column(db.String(100), default='')
    renter_address2 = db.Column(db.String(100), default='')
    renter_address3 = db.Column(db.String(100), default='')
    renter_address4 = db.Column(db.String(100), default='')
    cont_no = db.Column(db.String(100), default='')
    business_address = db.Column(db.String(100), default='')
    business_address2 = db.Column(db.String(100), default='')
    business_tel = db.Column(db.String(100), default='')
    license_number = db.Column(db.String(100), default='')
    license_country = db.Column(db.String(100), default='')
    license_date = db.Column(db.DateTime, default=date.min)
    passport_number = db.Column(db.String(100), default='')
    passport_country = db.Column(db.String(100), default='')
    passport_date = db.Column(db.DateTime, default=date.min)
    place_of_birth = db.Column(db.String(100), default='')
    date_of_birth = db.Column(db.DateTime, default=date.min)
    additional_driver = db.Column(db.String(100), default='')
    license2_number = db.Column(db.String(100), default='')
    license2_country = db.Column(db.String(100), default='')
    license2_date = db.Column(db.DateTime, default=date.min)
    to_be_checked_in_at = db.Column(db.String(100), default='')
    date_form = db.Column(db.DateTime, default=date.min)
    time_form = db.Column(db.String(100), default='')
    car_model = db.Column(db.String(100), default='')
    car_license = db.Column(db.String(100), default='')
    car_owner = db.Column(db.String(100), default='')
    car_checked_in_at = db.Column(db.String(100), default='')
    car_rented_at = db.Column(db.String(100), default='')
    date_in = db.Column(db.DateTime, default=date.min)
    date_out = db.Column(db.DateTime, default=date.min)
    time_in = db.Column(db.String(100), default='')
    time_out = db.Column(db.String(100), default='')
    form_number = db.Column(db.String(100), default='')
    car_group = db.Column(db.String(100), default='')
    car_chargd = db.Column(db.String(100), default='')
    car_tarrif = db.Column(db.String(100), default='')
    obs = db.Column(db.String(100), default='')
def new_applicant():
    with db.session.begin():
        applicant = CarApplicant()
        db.session.add(applicant)

        db.session.flush()
        id = applicant.id
    return id


def search_applicant(filter: Dict[str, any]):
    with db.session.begin():
        items = list(map(lambda x: x.to_dict(), CarApplicant.query.filter_by(**filter)))
    return items


def update_applicant(id: int, data: Dict[str, any]):
    with db.session.begin():
        applicant = CarApplicant.query.filter(CarApplicant.id == id).first()
        if applicant is None:
            return None
        for field in data:
            if field == "id":
                continue
            if not hasattr(applicant, field):
                continue

            if field.count('_date') > 0 or field.count('date_') > 0:
                try:
                    datetime_field = dateutil.parser.parse(data[field])
                    if getattr(applicant, field) != datetime_field:
                        setattr(applicant, field, datetime_field)
                except BaseException as b:
                    print(f"Invalid date for {field} {data[field]}")
            else:
                if getattr(applicant, field) != data[field]:
                    setattr(applicant, field, data[field])

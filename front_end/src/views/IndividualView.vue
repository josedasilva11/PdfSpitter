<template>
  <div class="row">
    <div class="offset-10 col-md-2">
      <b-button @click="home()">{{ Translate('Home3') }}</b-button>
    </div>
    <div class="row">

      <div class="col-md-2 offset-10">
        <b-form-group :label="Translate('Form Number')">
          <b-form-input v-model="rental_form.id" disabled :placeholder="Translate('Form Number')"></b-form-input>
        </b-form-group>
      </div>
    </div>

    <div class="card  col-md-3">
      <b-form-group :label="Translate('Client Renter Name')">
        <b-form-input v-model="rental_form.client_renter_name" :placeholder="Translate('Client Renter Name')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Client Renter Name2')">
        <b-form-input v-model="rental_form.client_renter_name2" :placeholder="Translate('Client Renter Name2')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card  col-md-3 ">
      <b-form-group :label="Translate('Renter Address')">
        <b-form-input v-model="rental_form.renter_address" :placeholder="Translate('Renter Address')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Renter Address2')">
        <b-form-input v-model="rental_form.renter_address2" :placeholder="Translate('Renter Address2')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Renter Address3')">
        <b-form-input v-model="rental_form.renter_address3" :placeholder="Translate('Renter Address3')"></b-form-input>
      </b-form-group>
      <div class="row">
        <div class="col-md-6">
          <b-form-group :label="Translate('Renter Address4')">
            <b-form-input v-model="rental_form.renter_address4" :placeholder="Translate('Renter Address4')"></b-form-input>
          </b-form-group>
        </div>

        <div class="col-md-6">
          <b-form-group :label="Translate('Cont No')">
            <b-form-input v-model="rental_form.cont_no" :placeholder="Translate('Cont No')"></b-form-input>
          </b-form-group>
        </div>
      </div>
    </div>
    <div class="card  col-md-3">
      <b-form-group :label="Translate('Business Address')">
        <b-form-input v-model="rental_form.business_address" :placeholder="Translate('Business Address')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Business Address2')">
        <b-form-input v-model="rental_form.business_address2" :placeholder="Translate('Business Address2')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Business Tel')">
        <b-form-input v-model="rental_form.business_tel" :placeholder="Translate('Business Tel')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card  col-md-3">
      <b-form-group :label="Translate('License Number')">
        <b-form-input v-model="rental_form.license_number" :placeholder="Translate('License Number')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('License Country')">
        <b-form-input v-model="rental_form.license_country" :placeholder="Translate('License Country')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('License Date')">
        <b-form-input type="date" v-model="rental_form.license_date" :placeholder="Translate('License Date')"></b-form-input>
      </b-form-group>
    </div>


    <div class="card  col-md-3">
      <b-form-group :label="Translate('Passport Number')">
        <b-form-input v-model="rental_form.passport_number" :placeholder="Translate('Passport Number')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Passport Country')">
        <b-form-input v-model="rental_form.passport_country" :placeholder="Translate('Passport Country')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Passport Date')">
        <b-form-input type="date" v-model="rental_form.passport_date" :placeholder="Translate('Passport Date')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card  col-md-3">
      <b-form-group :label="Translate('Place Of Birth')">
        <b-form-input v-model="rental_form.place_of_birth" :placeholder="Translate('Place Of Birth')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Date Of Birth')">
        <b-form-input type="date" v-model="rental_form.date_of_birth" :placeholder="Translate('Date Of Birth')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card  col-md-3">
      <b-form-group :label="Translate('Additional Driver')">
        <b-form-input v-model="rental_form.additional_driver" :placeholder="Translate('Additional Driver')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Additional Driver License Number')">
        <b-form-input v-model="rental_form.license2_number"
                      :placeholder="Translate('Additional Driver License Number')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Additional Driver License Country')">
        <b-form-input v-model="rental_form.license2_country"
                      :placeholder="Translate('Additional Driver License Country')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Additional Driver License Date')">
        <b-form-input type="date" v-model="rental_form.license2_date"
                      :placeholder="Translate('Additional Driver License Date')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card  col-md-3">
      <b-form-group :label="Translate('To Be Checked In At')">
        <b-form-input v-model="rental_form.to_be_checked_in_at" :placeholder="Translate('To Be Checked In At')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Date Form')">
        <b-form-input type="date" v-model="rental_form.date_form" :placeholder="Translate('Date Form')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Time Form')">
        <b-form-input type="time" v-model="rental_form.time_form" :placeholder="Translate('Time Form')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card col-md-3">
      <b-form-group :label="Translate('To Be Paid')">
        <b-form-input v-model="rental_form.to_be_paid" :placeholder="Translate('To Be Paid')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('To Be Paid2')">
        <b-form-input v-model="rental_form.to_be_paid2" :placeholder="Translate('To Be Paid2')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('To Be Paid3')">
        <b-form-input v-model="rental_form.to_be_paid3" :placeholder="Translate('To Be Paid3')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card  col-md-3">
      <b-form-group :label="Translate('Car Model')">
        <b-form-input v-model="rental_form.car_model" :placeholder="Translate('Car Model')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Car License')">
        <b-form-input v-model="rental_form.car_license" :placeholder="Translate('Car License')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Car Owner')">
        <b-form-input v-model="rental_form.car_owner" :placeholder="Translate('Car Owner')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card col-md-3">
      <b-form-group :label="Translate('Car Rented At')">
        <b-form-input v-model="rental_form.car_rented_at" :placeholder="Translate('Car Rented At')"></b-form-input>
      </b-form-group>
      <b-form-group :label="Translate('Car Checked In At')">
        <b-form-input v-model="rental_form.car_checked_in_at" :placeholder="Translate('Car Checked In At')"></b-form-input>
      </b-form-group>


      <b-form-group :label="Translate('Date In')">
        <b-form-input type="date" v-model="rental_form.date_in" :placeholder="Translate('Date In')"></b-form-input>
      </b-form-group>
      <b-form-group :label="Translate('Time In')">
        <b-form-input type="time" v-model="rental_form.time_in" :placeholder="Translate('Time In')"></b-form-input>
      </b-form-group>
    </div>
    <div class="card col-md-3">
      <b-form-group :label="Translate('Date Out')">
        <b-form-input type="date" v-model="rental_form.date_out" :placeholder="Translate('Date Out')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Time Out')">
        <b-form-input type="time" v-model="rental_form.time_out" :placeholder="Translate('Time Out')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Is Black Listed?')">
        <b-form-checkbox :value="true"
                         :unchecked-value="false" v-model="rental_form.is_black_listed"
                         :placeholder="Translate('Is Black Listed?')"></b-form-checkbox>
      </b-form-group>
      <div class="card  btn-group">
        <b-button @click="Submit()">Save</b-button>
        {{ api_message }}
        <a target="_blank" class="btn btn-danger" :href="PdfHref()">Print Pdf</a>
        <a target="_blank" class="btn btn-danger" :href="Pdf3Href()">Print 3 Pdf</a>

      </div>
    </div>


  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
//@ts-ignore
import {API} from '@/api/api.js'
import {RentalForm} from "@/views/rental_form";

import {_translate} from "../../translated";
@Component({
  components: {},
})
export default class IndividualView extends Vue {

  rental_form: RentalForm = new RentalForm()
  api_message: string = ''

  created() {
    this.Load(+this.$route.params['id'])
  }
  Translate(text:string){
         return _translate(text)
  }
  Pdf3Href() {
    return '/generate3_pdf/' + this.$route.params['id']
  }

  PdfHref() {
    return '/generate_pdf/' + this.$route.params['id']
  }

  async Submit() {
    this.api_message = 'Saving...'
    try {
      const new_form_result = await API.update_form(+this.$route.params['id'], this.rental_form)
      console.log(new_form_result)
      if (new_form_result.success) {
        this.api_message = 'Saved'
        setTimeout(() => {
          this.api_message = ''
        }, 2000)
      } else {
        this.api_message = 'Error!'
      }
    } catch (e) {
      this.api_message = 'Error!'
    }
  }

  home() {
    this.$router.push('/')
  }

  async Load(form_id: number) {
    const new_form_result = await API.search_form({id: form_id})

    if (new_form_result.success) {
      if (new_form_result.items.length > 0) {

        let item = new_form_result.items[0];

        for (const key of Object.keys(item)) {
          if (key.startsWith('date_') || key.endsWith('_date')) {
            item[key] = item[key].split(' ')[0]
          }
        }
        this.rental_form = item
      }
    }
  }

}

</script>

<template>
  <div class="row">
    <div class="offset-10 col-md-2">
      <b-button @click="new_item()">+ New Item</b-button>
    </div>


    <div class="card  col-md-12">
      <b-form-group :label="Translate('Form Number')">
        <b-form-input v-model="search_form.form_number" :placeholder="Translate('Form Number')"></b-form-input>
      </b-form-group>
      <b-form-group :label="Translate('Client Renter Name')">
        <b-form-input v-model="search_form.client_renter_name"
                      :placeholder="Translate('Client Renter Name')"></b-form-input>
      </b-form-group>

      <b-form-group :label="Translate('Client Renter Name2')">
        <b-form-input v-model="search_form.client_renter_name2"
                      :placeholder="Translate('Client Renter Name2')"></b-form-input>
      </b-form-group>
      <b-form-group :label="Translate('Cont nº')">
        <b-form-input v-model="search_form.cont_no" :placeholder="Translate('Client Renter Name2')"></b-form-input>
      </b-form-group>
    </div>
    {{ Translate('Home') }}
    <b-button @click="Search()">Search</b-button>
    <table class="table table-responsive table-striped table-bordered">
      <thead>
      <th>
        {{ Translate('Renter Name') }}
      </th>
      <th> {{ Translate('Renter Name 2') }}

      </th>
      <th>
        {{ Translate('Cont nº') }}
      </th>

      </thead>
      <tbody>
      <tr v-for="item in search_results" :class="RowClass(item)">
        <td>
          <a :href="`/view_form/${item.id}`" target="_blank">{{ item.client_renter_name }}</a>
        </td>
        <td>
          {{ item.client_renter_name2 }}
        </td>
        <td>
          {{ item.cont_no }}
        </td>
      </tr>
      </tbody>
    </table>


  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
//@ts-ignore
import {API} from '@/api/api.js'
import {SearchForm, RentalForm} from "@/views/rental_form";
import {_translate} from "../../translated";

@Component({
  components: {},
})
export default class SearchView extends Vue {

  search_form: SearchForm = new SearchForm()
  search_results: RentalForm[] = [];

  new_item() {
    this.$router.push('/new_item')
  }

  RowClass(row: RentalForm) {
    if (row.is_black_listed) {
      return ['table-danger']
    }
    return []
  }

  Translate(text: string) {
    return _translate(text)
  }

  async Search() {
    const new_form_result = await API.search_form(this.search_form)

    if (new_form_result.success) {
      if (new_form_result.items.length > 0) {

        for (const item of new_form_result.items) {

          for (const key of Object.keys(item)) {
            if (key.startsWith('date_') || key.endsWith('_date')) {
              item[key] = item[key].split(' ')[0]
            }
          }
        }
        this.search_results = new_form_result.items
      }
    }
  }

}

</script>

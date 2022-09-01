<template>
  <div class="row">
    <div class="offset-10 col-md-2">
      <b-button @click="home()">{{ Translate('Home') }}</b-button>
    </div>
    <b-form inline>
      <label class="sr-only" for="inline-form-input-name">User</label>
      <b-form-input v-model="user_name" prepend="@"
                    id="inline-form-input-name"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    placeholder="Username"
      ></b-form-input>

      <label class="sr-only" for="inline-form-input-username">Password</label>
      <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
        <b-form-input type="password" id="inline-form-input-username" placeholder="" v-model="password"></b-form-input>
      </b-input-group>
      <span class="text-danger text-muted">{{ error_message }}</span>

      <b-button variant="primary" @click="Login()">Login</b-button>
    </b-form>

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
export default class LoginView extends Vue {
  error_message: string = ''

  async Login() {
    try {
      const login_result = await API.login(this.user_name, this.password)
      if (login_result.success) {
        this.home()
      } else {
        this.error_message = login_result.error_message
      }
    } catch (e: any) {
      this.error_message = e.error_message
    }
  }

  Translate(text: string) {
    return _translate(text)
  }

  user_name: string = ''
  password: string = ''

  home() {
    this.$router.push('/')
  }
}

</script>

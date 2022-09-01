import {Component, Vue} from "vue-property-decorator";
// @ts-ignore
import {API} from "@/api/api.js";
import {_translate} from "../../translated";


@Component
export default class login_vue extends Vue {
    error_message: string = ''
    loading: boolean = false

    Translate(text: string) {
        return _translate(text)
    }

    async check_login() {
        this.loading = true
        try {
            const login_result = await API.is_login()
            if (!login_result.success) {
                this.login()
            } else {
                this.error_message = login_result.error_message
            }
        } catch (e: any) {
            this.error_message = e.error_message
        } finally {
            this.loading = false
        }
    }

    login() {
        this.$router.push('/login')
    }

    created() {
        this.check_login()
    }
}
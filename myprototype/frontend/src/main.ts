import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/aura-light-noir/theme.css'
import ToastService from 'primevue/toastservice'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './style.css'
const app = createApp(App)

const pinia = createPinia()

app.use(pinia)
app.use(ToastService)
app.use(PrimeVue)
app.use(router)
app.mount('#app')

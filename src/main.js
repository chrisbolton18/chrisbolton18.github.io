import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './style.css';  // Tailwind CSS import
import 'vueperslides/dist/vueperslides.css'


const app = createApp(App)
.use(router)
.mount('#app');

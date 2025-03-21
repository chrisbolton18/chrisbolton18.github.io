import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import MyWork from '../views/MyWork.vue';
import Contact from '../views/Contact.vue';

const routes = [
  { path: '/vue-portfolio/', component: Home },
  { path: '/vue-portfolio/about', component: About },
  { path: '/vue-portfolio/mywork', component: MyWork },
  { path: '/vue-portfolio/contact', component: Contact },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

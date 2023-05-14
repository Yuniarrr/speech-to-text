import { createApp } from "vue";
// import './style.css'
import "./index.css";
import App from "./App.vue";
import { createPinia } from "pinia";

import router from "./router";
import { Carousel, initTE } from "tw-elements";
initTE({ Carousel });

const pinia = createPinia();

createApp(App).use(router).use(pinia).mount("#app");

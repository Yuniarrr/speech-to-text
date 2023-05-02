import { createApp } from "vue";
// import './style.css'
import "./index.css";
import App from "./App.vue";

import router from "./router";
import { Carousel, initTE } from "tw-elements";
initTE({ Carousel });

createApp(App).use(router).mount("#app");

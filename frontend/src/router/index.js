import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HelloWorld.vue"),
    },
    {
      path: "/product",
      name: "product",
      component: () => import("../views/product.vue"),
    },
  ],
});

export default router;

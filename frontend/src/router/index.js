import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomePage.vue"),
    },
    {
      path: "/stt",
      name: "stt",
      component: () => import("../views/SpeechToText.vue"),
    },
    {
      path: "/products",
      name: "products",
      component: () => import("../views/Products.vue"),
    },
    {
      path: "/subcategory/:slug",
      name: "subcategory",
      component: () => import("../views/SubCategory.vue"),
    },
    {
      path: "/mic",
      name: "mic",
      component: () => import("../views/Mic.vue"),
    },
    {
      path: "/product/:slug",
      name: "product",
      component: () => import("../views/Details.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: () => import("../views/NotFound.vue"),
    },
  ],
});

export default router;

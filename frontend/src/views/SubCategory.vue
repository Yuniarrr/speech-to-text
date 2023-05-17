<template>
  <div class="bg-white w-full">
    <div class="pt-4 mx-10">
    <router-link
        to="/products"
        class="inline-flex items-center py-2.5 px-3 text-sm font-medium text-white bg-blue-700 rounded-full border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6.75 15.75L3 12m0 0l3.75-3.75M3 12h18"
          />
        </svg>

        <p class="mx-4">Back</p>
      </router-link>
    </div>
  </div>
</template>

<script>
import { useApp } from "../store/index.js";

export default {
  setup() {
    const app = useApp();

    return {
      app,
    };
  },
  mounted() {
    this.app.getProductSubCategories(this.$route.params.slug);
    console.log(this.$route.params.slug);
  },
};
</script>

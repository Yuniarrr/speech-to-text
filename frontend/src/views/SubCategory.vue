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
    <!-- category -->
    <div class="flex flex-col justify-around">
      <h1 class="mt-5 text-2xl font-bold mx-10">
        {{ slugToTitle($route.params.slug) }}
      </h1>
    </div>
    <div class="flex flex-wrap items-center justify-center">
      <!--Card 1-->
      <div
        v-for="(product, index) in app.product_sub_categories.result"
        :key="index"
      >
        <div
          class="mx-2 my-2 w-64 h-[480px] -hidden border border-gray-300 rounded shadow-lg col-span-1 flex flex-col gap-4"
        >
          <img
            class="w-full h-48"
            :src="product.thumbnail_url"
            :alt="product.slug"
          />
          <div class="p-4">
            <div class="text-xl font-bold cursor-pointer">
              {{ product.name }}
            </div>
            <div class="text-base font-semibold">
              {{ product.selling_unit }}
            </div>
            <div class="flex flex-wrap">
              <div class="font-semibold text-sm text-orange-400 flex">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="orange"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="orange"
                  class="w-3 h-3 mr-1 mt-[4px]"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
                  />
                </svg>
                {{ product.ratings }}
              </div>
            </div>
            <div class="flex flex-wrap">
              <div class="font-semibold text-sm text-orange-400 flex">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-3 h-5"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"
                  />
                </svg>
                &nbsp;{{ product.distance }}
              </div>
            </div>
            <div class="text-base">
              Rp
              {{ product.min_price }} - {{ product.base_price }}
            </div>
          </div>
          <router-link
            :to="`/product/${product.slug}`"
            @click="app.getProduct(product.slug)"
            type="button"
            class="flex mt-auto focus:outline-none text-white bg-sky-700 hover:bg-sky-800 focus:ring-4 focus:ring-sky-300 font-medium rounded-lg text-sm px-4 py-2.5 dark:bg-sky-600 dark:hover:bg-sky-700 dark:focus:ring-sky-800"
          >
            <span class="mx-auto">Detail</span>
          </router-link>
        </div>
      </div>
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
  methods: {
    slugToTitle(slug) {
      var words = slug.split("-");
      var title = "";

      for (var i = 0; i < words.length; i++) {
        var word = words[i];
        var capitalizedWord = word.charAt(0).toUpperCase() + word.slice(1);
        title += capitalizedWord + " ";
      }

      return title.trim();
    },
  },
};
</script>

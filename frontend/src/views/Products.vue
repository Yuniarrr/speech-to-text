<template>
  <div class="mx-10 bg-white">
    <div class="flex items-center justify-center lg:space-x-20 sm:space-x-5">
      <!-- category -->
      <div class="">
        <div class="inline-block dropdown">
          <button
            class="inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 border border-gray-300 rounded focus:ring-blue-500 focus:border-blue-500"
          >
            <span class="mr-1">Category</span>
            <svg
              class="w-4 h-4 fill-current"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <path
                d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
              />
            </svg>
          </button>
          <ul class="absolute z-10 hidden pt-1 text-gray-700 dropdown-menu">
            <li class="">
              <a
                class="block px-4 py-2 whitespace-no-wrap bg-gray-200 rounded-t hover:bg-gray-400"
                href="/product"
                >Ratings
              </a>
            </li>
            <li class="">
              <a
                class="block px-4 py-2 whitespace-no-wrap bg-gray-200 rounded-b hover:bg-gray-400"
                href="#"
                >Medicine</a
              >
            </li>
          </ul>
        </div>
      </div>

      <!-- Search -->
      <div class="flex">
        <div class="relative w-96">
          <div
            class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
          >
            <svg
              aria-hidden="true"
              class="w-5 h-5 text-gray-500"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </div>
          <input
            type="text"
            id="voice-search"
            v-model="app.search"
            @keydown.enter="app.getProducts()"
            class="border border-gray-300 text-gray-900 text-sm rounded-3xl focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Input complaint / medicine here "
            required
          />
          <button
            v-if="!mic.record"
            @click="mic.onRecord"
            type="button"
            class="absolute inset-y-0 right-0 flex items-center pr-3"
          >
            <svg
              aria-hidden="true"
              class="w-4 h-4 text-gray-500 hover:text-gray-900"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M7 4a3 3 0 016 0v4a3 3 0 11-6 0V4zm4 10.93A7.001 7.001 0 0017 8a1 1 0 10-2 0A5 5 0 015 8a1 1 0 00-2 0 7.001 7.001 0 006 6.93V17H6a1 1 0 100 2h8a1 1 0 100-2h-3v-2.07z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </button>
          <button
            v-if="mic.record"
            @click="mic.stopRecord"
            type="button"
            class="absolute inset-y-0 right-0 flex items-center pr-3"
          >
            <svg
              fill="white"
              class="w-4 h-4 text-gray-500 hover:text-gray-900"
              stroke="currentColor"
              stroke-width="1.5"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M5.25 7.5A2.25 2.25 0 017.5 5.25h9a2.25 2.25 0 012.25 2.25v9a2.25 2.25 0 01-2.25 2.25h-9a2.25 2.25 0 01-2.25-2.25v-9z"
              ></path>
            </svg>
          </button>
        </div>
        <button
          type="button"
          @click="app.getProducts()"
          class="inline-flex items-center py-2.5 px-3 ml-2 text-sm font-medium text-white bg-blue-700 rounded-full border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          <svg
            aria-hidden="true"
            class="w-5 h-5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            ></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- promo -->
    <swiper />

    <div v-if="app.products.length == 0 && app.categories.length != 0">
      <!-- Category -->
      <div class="flex flex-col justify-around">
        <h1 class="mt-10 text-2xl font-bold">CATEGORY</h1>
        <div class="flex flex-row my-2 space-x-5 overflow-auto">
          <div v-for="(category, index) in app.categories" :key="index">
            <category
              v-if="category.sub_categories.length != 0"
              :name="category.name"
              :category_id="category.category_id"
              :slug="category.slug.value"
              @click="
                (app.slug_category = category.slug.value),
                  app.getSubCategories(category.slug.value)
              "
            />
          </div>
        </div>
      </div>

      <!-- Sub Category -->
      <div class="flex flex-col justify-around">
        <h1 class="mt-10 text-2xl font-bold">
          {{
            app.categories.find((item) => item.slug.value == app.slug_category)
              .name
          }}
        </h1>
        <div class="flex flex-col space-y-2">
          <div
            v-for="sub_category in app.sub_categories"
            :key="sub_category.category_id"
          >
            <router-link :to="`/subcategory/${sub_category.slug.value}`">
              <div
                @click="app.getProductSubCategories(sub_category.slug.value)"
                class="p-3 overflow-hidden bg-white border border-gray-200 rounded-lg shadow-lg cursor-pointer dark:border-gray-700 dark:bg-gray-800 hover:bg-slate-100"
              >
                {{ sub_category.name }}
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- CARD -->
    <div
      class="flex flex-col justify-around space-y-8"
      v-if="app.products.length != 0"
    >
      <h1 class="text-2xl font-bold text-center">
        Search for "{{ app.search }}"
      </h1>
      <h1 class="text-2xl font-bold">PRODUCTS!</h1>
      <div
        class="flex flex-wrap items-center justify-center my-2 lg:space-y-3 sm:space-y-5"
      >
        <!--Card 1-->
        <div v-for="(product, index) in app.products.result" :key="index">
          <div
            class="max-w-sm ml-10 overflow-hidden border border-gray-300 rounded shadow-lg"
          >
            <img
              class="w-full"
              :src="product.thumbnail_url"
              :alt="product.slug"
            />
            <div class="px-6 py-4">
              <div class="mb-2 text-xl font-bold cursor-pointer">
                {{ product.name }}
              </div>
              <div class="mb-2 text-base font-semibold">
                {{ product.selling_unit }}
              </div>
              <div class="mb-2 text-base text-center">
                {{ product.min_price }} - {{ product.base_price }}
              </div>
              <div class="mb-2 text-base">
                {{ product.ratings }}
              </div>
              <!-- <p class="text-base text-gray-700">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Voluptatibus quia, Nonea! Maiores et perferendis eaque,
                exercitationem praesentium nihil.
              </p> -->
              <router-link
                :to="`/product/${product.slug}`"
                @click="app.getProduct(product.slug)"
                type="button"
                class="self-center focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
              >
                Detail
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Swiper from "../components/Products/Swiper.vue";
import { useApp, useMicrophone } from "../store/index.js";
import Card from "../components/Products/Card.vue";
import Category from "../components/Products/Category.vue";

export default {
  components: {
    Swiper,
    Card,
    Category,
  },
  setup() {
    const app = useApp();
    const mic = useMicrophone();

    return {
      app,
      mic,
    };
  },
  mounted() {
    this.app.getCategories();
    this.app.getSubCategories(this.app.slug_category);
  },
};
</script>

<style>
.dropdown:hover .dropdown-menu {
  display: block;
}
</style>

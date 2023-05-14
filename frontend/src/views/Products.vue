<template>
  <div class="w-full bg-white">
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

    <!-- Category -->
    <div class="flex flex-col justify-around">
      <h1 class="mt-10 text-2xl font-bold lg:ml-32 sm:ml-10">CATEGORY</h1>
      <div
        class="grid grid-cols-10 items-center justify-center my-2 space-x-5 overflow-auto"
      >
        <div v-for="(category, index) in app.categories" :key="index">
          <category :name="category.name" :category_id="category.category_id" />
        </div>
      </div>
    </div>

    <!-- Sub Category -->
    <div class="flex flex-col justify-around" v-if="app.products.length == 0">
      <div v-for="(category, index) in app.categories" :key="index">
        <h1 class="mt-10 text-2xl font-bold lg:ml-32 sm:ml-10">
          {{ category.name }}
        </h1>
        <div
          v-for="sub_category in category.sub_categories"
          :key="sub_category.category_id"
        >
          <router-link :to="`/sub_category/${sub_category.category_id}`">
            <div
              class="cursor-pointer overflow-hidden rounded-lg border border-gray-200 bg-white p-3 shadow-lg dark:border-gray-700 dark:bg-gray-800 hover:bg-slate-100"
            >
              {{ sub_category.name }}
            </div>
          </router-link>
        </div>
      </div>
    </div>

    <!-- Card One -->
    <!-- <div
      class="flex flex-wrap items-center justify-center my-2 lg:space-y-3 sm:space-y-5"
    >
      <div v-for="(item, index) in 3" :key="index">
        <div
          class="max-w-sm ml-10 overflow-hidden border border-gray-300 rounded shadow-lg"
        >
          <img class="w-full" src="../assets/obat.jpg" alt="Mountain" />
          <div class="px-6 py-4">
            <div class="mb-2 text-xl font-bold cursor-pointer">Mountain</div>
            <p class="text-base text-gray-700">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Voluptatibus quia, Nonea! Maiores et perferendis eaque,
              exercitationem praesentium nihil.
            </p>
          </div>
          <div class="px-6 pt-4 pb-2">
            <span
              class="inline-block px-3 py-1 mb-2 mr-2 text-sm font-semibold text-gray-700 bg-gray-200 rounded-full"
              >#photography</span
            >
            <span
              class="inline-block px-3 py-1 mb-2 mr-2 text-sm font-semibold text-gray-700 bg-gray-200 rounded-full"
              >#travel</span
            >
            <span
              class="inline-block px-3 py-1 mb-2 mr-2 text-sm font-semibold text-gray-700 bg-gray-200 rounded-full"
              >#winter</span
            >
          </div>
        </div>
      </div>
    </div> -->

    <!-- CARD two -->
    <div class="flex flex-col justify-around" v-if="app.products.length != 0">
      <h1 class="mt-10 text-2xl font-bold lg:ml-32 sm:ml-10">PRODUCTS!</h1>
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
  },
};
</script>

<style>
.dropdown:hover .dropdown-menu {
  display: block;
}
</style>

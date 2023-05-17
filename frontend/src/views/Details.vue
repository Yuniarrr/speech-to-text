<template>
  <div class="bg-slate-50 w-full">
    <div class="items-center pt-4 mx-10">
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

      <!-- gambar -->
      <div class="flex mt-6 space-x-10">
        <div class="rounded shadow-lg border border-gray-300 w-1/3 h-80">
          <img
            class="w-full"
            :src="app.product.image_url"
            :alt="app.product.slug"
          />

          <!-- toko -->
          <div class="">
            <img src="../assets/ingat.png" alt="ingat" class="w-72  mx-auto" />
          </div>
        </div>

        <!-- deskripsi -->
        <div class="w-2/3">
          <h1 class="w-5/6 font-bold text-2xl">
            {{ app.product.name }} ({{ app.product.selling_unit }})
          </h1>
          <!-- bintang -->
          <div class="mt-2 flex flex-wrap items-center">
            <p class="underline text-orange-400 text-sm underline-offset-6">
              {{ app.product.ratings }}
            </p>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="orange"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="orange"
              class="w-6 h-6 ml-2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
              />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="orange"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="orange"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
              />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="orange"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="orange"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
              />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="orange"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="orange"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
              />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="orange"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="orange"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
              />
            </svg>
          </div>
          <!-- harga -->
          <div class="mt-3 flex items-end">
            <h1 class="font-bold text-4xl text-blue-900">
              Rp {{ app.product.min_price }} - Rp {{ app.product.base_price }}
            </h1>
            <p class="mx-2">{{ app.product.selling_unit }}</p>
          </div>
          <!-- deskripsi -->
          <div class="mt-3 w-5/6">
            <h1 class="font-bold text-lg">Deskripsi</h1>
            <p class="">
              {{ app.product.description }}
            </p>
            <h1 class="font-bold text-lg mt-4">Komposisi</h1>
            <p class="">{{ app.product.composition }}</p>
            <h1 class="font-bold text-lg mt-4">Kemasan</h1>
            <p class="">{{ app.product.packaging }}</p>
            <h1 class="font-bold text-lg mt-4">
              Indikasi / Manfaat / Kegunaan
            </h1>
            <p class="">{{ app.product.general_indication }}</p>
            <h1 class="font-bold text-lg mt-4">Dosis</h1>
            <p class="">{{ app.product.dosage }}</p>
            <h1 class="font-bold text-lg mt-4">Sub Kategori</h1>
            <div class="flex flex-row space-x-3">
              <div
                v-for="category in app.product.categories"
                :key="category.external_id"
              >
                <router-link
                  to="/"
                  @click="app.getSubCategories(category.slug)"
                >
                  <div
                    class="underline underline-offset-8 text-green-500 hover:text-green-400"
                  >
                    {{ category.name }} 
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from "swiper/vue";

// Import Swiper styles
import "swiper/css";

import "swiper/css/navigation";

// import required modules
import { Navigation } from "swiper";

import { useApp } from "../store/index.js";

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    const app = useApp();

    return {
      app,
      modules: [Navigation],
    };
  },
  mounted() {
    let slug = this.$route.params.slug;
    this.app.getProduct(slug);
  },
  methods: {
    createStarSvg(star) {
      const fullStarCount = Math.floor(star);
      const hasHalfStar = star % 1 !== 0;
      const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
      svg.setAttribute("fill", "orange");
      svg.setAttribute("viewBox", "0 0 24 24");
      svg.setAttribute("stroke-width", "1.5");
      svg.setAttribute("stroke", "orange");
      svg.setAttribute("class", "w-6 h-6");
      for (let i = 0; i < fullStarCount; i++) {
        const path = document.createElementNS(
          "http://www.w3.org/2000/svg",
          "path"
        );
        path.setAttribute("stroke-linecap", "round");
        path.setAttribute("stroke-linejoin", "round");
        path.setAttribute(
          "d",
          "M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
        );
        svg.appendChild(path);
      }
      if (hasHalfStar) {
        const path = document.createElementNS(
          "http://www.w3.org/2000/svg",
          "path"
        );
        path.setAttribute("stroke-linecap", "round");
        path.setAttribute("stroke-linejoin", "round");
        path.setAttribute(
          "d",
          "M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-2.671-2.287 1.027-4.31a.562.562 0 01.527-.42z"
        );
        svg.appendChild(path);
      }
      return svg;
    },
  },
};
</script>

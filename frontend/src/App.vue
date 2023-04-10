<template>
  <header>
    <div class="sticky  top-0 bg-black" id="app">
    <nav class="flex items-center justify-between flex-wrap bg-teal p-4">
      <div class="flex items-center flex-no-shrink text-white mr-6">
        <img
          class="fill-current h-8 w-8 mr-2 w-32 h-32"
          src="../assets/logo.png"
          alt="logo"
        />
        <span class="font-semibold text-xl tracking-tight">SORA</span>
      </div>
     

      <ul
        :class="open ? 'block' : 'hidden'"
        class="w-full sm:flex sm:items-center sm:w-auto"
      >
        <div class="text-sm sm:flex-grow flex">
          <li>
            <a
            @click="setPage('Home')"
              class="block mt-4 sm:inline-block sm:mt-0 text-teal-lighter text-white hover:text-white mr-4"
            >
              Home
            </a>
          </li>
          <li>
            <button
              class="no-underline text-gray-300 block mt-4 sm:inline-block sm:mt-0 text-teal-lighter hover:text-white mr-4"
            >
              Examples
            </button>
          </li>
          <li>
            <button
              class="no-underline text-gray-300 block mt-4 sm:inline-block sm:mt-0 text-teal-lighter hover:text-white"
            >
              Blog
            </button>
          </li>
        </div>
       
      </ul>
    </nav>
  </div>
  </header>
  <router-view />
</template>

<script>
import Header from "./layouts/Header.vue";
import TextRainbow from "./components/TextRainbow.vue";

export default {
  name: "App",
  components: {
    // Layout,
    TextRainbow,
    Header,
    // Footer
  },
};
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>

<template>
  <!-- <div class="w-full p-4 bg-sky-300 sticky top-0 z-10">
    <nav class="flex items-center justify-between max-w-screen-xl mx-auto"> -->
  <!-- <div class="font-bold text-2xl text-slate-100">
        <TextRainbow class="cursor-pointer" text="SORA" />
      </div> -->
  <!-- <div
        class="sm:flex sm:items-center sm:space-x-2 text-slate-800 font-medium"
      >
        <a
          class="px-3 py-2 text-sm hover:text-slate-950 hover:underline hover:underline-offset-8"
          href="/"
          >Home</a
        >
        <a
          class="px-3 py-2 text-sm hover:text-slate-950 hover:underline hover:underline-offset-8"
          href="/product"
          >Product</a
        >
        <a
          class="px-3 py-2 text-sm hover:text-slate-950 hover:underline hover:underline-offset-8"
          href="/"
          >About Us</a
        >
      </div> -->
  <div class="top-0 bg-sky-300">
    <nav class="flex flex-wrap items-center justify-between p-4 mx-5 bg-teal">
      <div class="flex items-center w-1/5 text-white flex-no-shrink">
        <!-- <img
          class="w-8 w-32 h-8 h-32 mr-2 fill-current"
          src="../assets/logo.png"
          alt="logo"
        /> -->
        <span class="text-xl font-bold tracking-tight text-black">SORA</span>
      </div>

      <div class="flex justify-center md:w-3/5">
        <lottie-player
          src="https://assets1.lottiefiles.com/packages/lf20_KUFdS6.json"
          background="transparent"
          speed="2"
          style="width: 50px; height: 50px"
          loop
          autoplay
        ></lottie-player>
        <lottie-player
          src="https://assets1.lottiefiles.com/packages/lf20_KUFdS6.json"
          background="transparent"
          speed="2"
          style="width: 200px; height: 50px"
          loop
          autoplay
        ></lottie-player>
      </div>
      <ul class="w-full sm:flex sm:items-center sm:w-auto">
        <div class="flex text-sm">
          <li>
            <router-link
              to="/"
              class="block mt-4 mr-4 text-black sm:mt-0"
              :class="
                $route.path == '/'
                  ? 'underline underline-offset-8 font-semibold'
                  : ''
              "
            >
              Home
            </router-link>
          </li>
          <li>
            <router-link
              to="/product"
              class="block mt-4 mr-4 text-black sm:mt-0"
              :class="
                $route.path == '/product'
                  ? 'underline underline-offset-8 font-semibold'
                  : ''
              "
            >
              Product
            </router-link>
          </li>
          <li>
            <router-link to="/" class="block mt-4 mr-4 text-black sm:mt-0">
              About
            </router-link>
          </li>
        </div>
      </ul>
    </nav>
  </div>
</template>
<script>
import TextRainbow from "../components/TextRainbow.vue";
export default {
  name: "Header",
  components: {
    TextRainbow,
  },
};
</script>

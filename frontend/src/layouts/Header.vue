<template>
  <div class="sticky top-0 bg-sky-300" id="app">
    <nav class="flex items-center justify-between flex-wrap bg-teal p-4">
      <div class="flex items-center flex-no-shrink text-white mr-6">
        <!-- <img
          class="fill-current h-8 w-8 mr-2 w-32 h-32"
          src="../assets/logo.png"
          alt="logo"
        /> -->
        <span class="font-bold text-xl text-black tracking-tight">SORA</span>
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
      <ul
        class="w-full sm:flex sm:items-center sm:w-auto"
      >
        <div class="text-sm flex">
          <li>
            <button
              @click="setPage('Home')"
              class="block font-semibold underline underline-offset-8 mt-4  sm:mt-0 text-black mr-4"
            >
              Home
          </button>
          </li>
          <li>
            <button
              class="text-black block mt-4 sm:mt-0  hover:font-semibold hover:underline hover:underline-offset-8 "
            >
              About
            </button>
          </li>
          
        </div>
      </ul>
    </nav>
  </div>
</template>
<script>
export default {
  name: "Header",
};
</script>

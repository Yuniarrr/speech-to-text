<template>
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
            <button
              @click="setPage('Home')"
              class="block mt-4 mr-4 font-semibold text-black underline underline-offset-8 sm:mt-0"
            >
              Home
            </button>
          </li>
          <li>
            <button
              class="block mt-4 text-black sm:mt-0 hover:font-semibold hover:underline hover:underline-offset-8"
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

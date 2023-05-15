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

      <!-- <div class="flex justify-center md:w-3/5">
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
      </div> -->
      <ul class="h-full sm:flex sm:items-center sm:w-auto">
        <div class="flex text-sm">
          <item name="Home" path="/" />
          <item name="Products" path="/products" />
          <item name="About" path="/about" />
        </div>
      </ul>
    </nav>
  </div>
</template>
<script>
import TextRainbow from "../components/TextRainbow.vue";
import Item from "../components/Menu/Item.vue";

export default {
  name: "Header",
  components: {
    TextRainbow,
    Item,
  },
};
</script>

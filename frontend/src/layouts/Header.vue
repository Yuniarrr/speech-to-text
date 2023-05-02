<template>
  <div class="w-full p-4 bg-sky-300 sticky top-0">
    <nav class="flex items-center justify-between max-w-screen-xl mx-auto">
      <div class="font-bold text-2xl text-slate-100"><TextRainbow
            class="cursor-pointer"
            text="SORA"
          /></div>
        <div
          class="sm:flex sm:items-center sm:space-x-2 text-slate-800 font-medium"
        >
          <a
            class="px-3 py-2 text-sm hover:text-slate-950  hover:underline hover:underline-offset-8 "
            href="/"
            >Home</a
          >
          <a
            class="px-3 py-2 text-sm hover:text-slate-950  hover:underline hover:underline-offset-8 "
            href="/product"
            >Product</a
          >
          <a
            class="px-3 py-2 text-sm hover:text-slate-950  hover:underline hover:underline-offset-8 "
            href="/"
            >About Us</a
          >
         
        </div>
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

<template>
  <div class="top-0 bg-sky-500 ">
    <nav class="flex flex-wrap  items-center mx-24 justify-between bg-teal ">
      <div class="flex w-24 my-2 ">
          <img
            class="w-full"
            src="../assets/sora.png"
            alt="logo"
          />
      </div>
      <ul class="h-full text-white sm:flex sm:items-center sm:w-auto">
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
import Item from "../components/Menu/Item.vue";

export default {
  name: "Header",
  components: {
    Item,
  },
};
</script>

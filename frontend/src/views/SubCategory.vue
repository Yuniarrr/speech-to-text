<template>
  <div>p</div>
</template>

<script>
import { useApp } from "../store/index.js";

export default {
  setup() {
    const app = useApp();

    return {
      app,
    };
  },
  mounted() {
    this.app.getProductSubCategories(this.$route.params.slug);
    console.log(this.$route.params.slug);
  },
};
</script>

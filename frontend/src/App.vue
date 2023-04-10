<template>
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

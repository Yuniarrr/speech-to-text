<template>
  <div>
    <Header />
    <router-view class="my-5" />
    <Footer />
  </div>
</template>

<script>
import Header from "./layouts/Header.vue";
import Footer from "./layouts/Footer.vue";
import { useApp } from "./store/index.js";

export default {
  name: "App",
  components: {
    Header,
    Footer,
  },
  setup() {
    const app = useApp();

    return {
      app,
    };
  },
  mounted() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(this.showPosition);
    } else {
      alert("Geolocation is not supported by this browser.");
    }
  },
  methods: {
    showPosition(position) {
      console.log(
        "Latitude: " +
          position.coords.latitude +
          " Longitude: " +
          position.coords.longitude
      );
      this.app.coordinates = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
      };
    },
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

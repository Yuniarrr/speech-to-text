<template>
  <div>
    <Header />
    <router-view />
    <Footer class="mt-10" />
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
  watch: {
    "app.multisort": {
      handler() {
        if (this.app.multisort.length == 0) {
          if (this.app.product_sub_categories.result) {
            this.app.product_sub_categories.result.sort((a, b) => {
              return a.name - b.name;
            });
          } else if (this.app.products.result) {
            this.app.products.result.sort((a, b) => {
              return a.name - b.name;
            });
          }
        } else {
          for (let i = 0; i < this.app.multisort.length; i++) {
            if (this.app.multisort[i] == "ratings") {
              if (this.app.product_sub_categories.result) {
                this.app.product_sub_categories.result.sort((a, b) => {
                  return a.ratings - b.ratings;
                });
              } else if (this.app.products.result) {
                this.app.products.result.sort((a, b) => {
                  return a.ratings - b.ratings;
                });
              }
            } else if (this.app.multisort[i] == "jarak") {
              if (this.app.product_sub_categories.result) {
                this.app.product_sub_categories.result.sort((a, b) => {
                  return a.distance - b.distance;
                });
              } else if (this.app.products.result) {
                this.app.products.result.sort((a, b) => {
                  return a.distance - b.distance;
                });
              }
            } else if (this.app.multisort[i] == "A-Z") {
              if (this.app.product_sub_categories.result) {
                this.app.product_sub_categories.result.sort((a, b) => {
                  return a.name - b.name;
                });
              } else if (this.app.products.result) {
                this.app.products.result.sort((a, b) => {
                  return a.name - b.name;
                });
              }
            } else if (this.app.multisort[i] == "Z-A") {
              if (this.app.product_sub_categories.result) {
                this.app.product_sub_categories.result.sort((a, b) => {
                  return b.name - a.name;
                });
              } else if (this.app.products.result) {
                this.app.products.result.sort((a, b) => {
                  return b.name - a.name;
                });
              }
            }
          }
        }
        console.log(this.app.products);
      },
      deep: true,
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

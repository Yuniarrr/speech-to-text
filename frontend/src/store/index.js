import { defineStore } from "pinia";
import axios from "axios";

const URL_API = "http://localhost:5000";

export const useApp = defineStore({
  id: "app",
  state: () => ({
    products: [],
    product: {},
    categories: [],
    slug_category: "obat-dan-perawatan",
    sub_categories: [],
    product_sub_categories: [],
    search: "",
    loading: false,
    coordinates: {},
    multisort: [],
  }),
  actions: {
    async getProducts() {
      this.loading = true;
      this.products = [];
      try {
        const { data } = await axios.post(
          URL_API + "/products/search/" + this.search,
          {
            coordinates: this.coordinates,
          }
        );
        this.products = data;
        console.log("this products");
        console.log(this.products);
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
    async getProduct(slug) {
      this.loading = true;
      this.product = {};
      try {
        const { data } = await axios.post(
          URL_API + "/products/detail/" + slug,
          {
            coordinates: this.coordinates,
          }
        );
        this.product = data;
        console.log(this.product);
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
    async getCategories() {
      this.loading = true;
      this.categories = [];
      try {
        const { data } = await axios.get(URL_API + "/categories/all");
        this.categories = data;
        console.log(this.categories);
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
    async getSubCategories(slug) {
      this.loading = true;
      this.sub_categories = [];
      try {
        const { data } = await axios.get(
          URL_API + "/categories/" + slug + "/subcategories"
        );
        this.sub_categories = data;
        console.log(this.sub_categories);
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
    async getProductSubCategories(slug) {
      this.loading = true;
      this.product_sub_categories = [];
      try {
        const { data } = await axios.post(
          URL_API + "/categories/" + slug + "/products",
          {
            coordinates: this.coordinates,
          }
        );
        this.product_sub_categories = data;
        console.log(this.product_sub_categories);
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
    sortBy(name) {
      if (name == "ratings") {
        this.products.result = this.products.result.sort((a, b) => {
          return a.ratings - b.ratings;
        });
      } else if (name == "distance") {
        this.products.result = this.products.result.sort((a, b) => {
          return a.distance - b.distance;
        });
      }
    },
  },
});

export const useMicrophone = defineStore({
  id: "microphone",
  state: () => ({
    file: null,
    transcription: null,
    loading: false,
    voiceSelect: {
      // name: "English",
      // lang: "en-US",
      name: "Indonesia",
      lang: "id-ID",
    },
    voiceList: [
      {
        name: "English",
        lang: "en-US",
      },
      {
        name: "Español",
        lang: "es-ES",
      },
      {
        name: "Indonesia",
        lang: "id-ID",
      },
      {
        name: "Italiano",
        lang: "it-IT",
      },
      {
        name: "Jepang",
        lang: "ja-JP",
      },
      {
        name: "Korea",
        lang: "ko-KR",
      },
    ],
    record: false,
    recording: null,
  }),
  actions: {
    onFileChange(event) {
      this.file = event.target.files[0];
    },
    async transcribe() {
      this.loading = true;
      const formData = new FormData();
      formData.append("file", this.file);
      formData.append("voiceSelect", JSON.stringify(this.voiceSelect.lang));

      const response = await fetch("http://localhost:5000/transcribe", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      if (data) {
        this.transcription = data.text;
        this.loading = false;
      }
    },
    onRecord() {
      const app = useApp();

      this.record = !this.record;
      // this.transcription = "";
      const sr = new webkitSpeechRecognition();
      sr.continuous = true;
      sr.interimResults = true;
      sr.lang = this.voiceSelect.lang;
      sr.start();
      sr.onresult = (e) => {
        const t = Array.from(e.results)
          .map((result) => result[0])
          .map((result) => result.transcript)
          .join("");

        this.transcription = t;
        app.search = t;
      };
      this.recording = sr;
    },
    stopRecord() {
      this.record = false;
      this.recording.stop();
    },
  },
});

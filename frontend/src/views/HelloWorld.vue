<template>
  <div class="mb-16">
    <div class="text-white pt-6">
      <div
        class="container mx-auto flex flex-wrap flex-col w-full md:flex-row items-center"
      >
        <!--Left Col-->
        <div
          class="flex flex-col w-full md:w-2/5 justify-center items-start text-center"
        >
          <p class="uppercase tracking-loose w-full">
            <TextRainbow
              class="text-black cursor-pointer"
              text="Hello, This is Speech to text"
            />
            <br />
          </p>
          <h1 class="my-3 text-5xl font-bold leading-tight">
            <TextRainbow
              class="text-black cursor-pointer"
              text="Hello! Nice to meet you! Is there anything I can help?"
            />
          </h1>
          <p class="leading-normal text-2xl mb-8"></p>
        </div>
        <div class="w-full flex items-center justify-center md:w-3/5">
          <lottie-player
            src="https://assets9.lottiefiles.com/private_files/lf30_h04isle8.json"
            background="transparent"
            speed="1"
            style="width: 450px; height: 400px"
            loop
            autoplay
          ></lottie-player>
        </div>
      </div>
    </div>

    <div class="container flex flex-col w-full md:flex-row mx-auto my-7">
      <div
        class="flex flex-col items-center justify-center mt-10 w-full md:w-2/5"
      >
        <div class="mb-1">
          <select
            v-model="voiceSelect"
            class="border-solid rounded-full w-full text-left px-24"
          >
            <option
              class="w-full text-left"
              v-for="voice in voiceList"
              :data-name="voice.name"
              :data-lang="voice.lang"
              :key="voice"
              :value="voice"
            >
              {{ voice.name }}
            </option>
          </select>
        </div>
        <div class="flex flex-col items-center mb-1">
          <div class="uppercase dark:text-gray-300 text-lg font-semibold">
            Choose Audio File
          </div>
          <div
            class="flex flex-row items-center justify-center flex-wrap gap-x-8"
          >
            <input
              type="file"
              @change="onFileChange"
              class="text-left text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
            />
            <button
              @click="transcribe"
              type="button"
              class="bg-gray-800 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700 text-white hover:bg-blue-600"
            >
              Transcribe
            </button>
          </div>
        </div>
        <div class="flex-col items-center justify-center">
          <button
            type="button"
            class="inline-flex items-center py-2.5 px-3 text-sm font-medium text-white bg-gray-800 rounded-lg border hover:bg-blue-600 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
          >
            <svg
              aria-hidden="true"
              class="w-5 h-5 mr-2 text-white dark:text-gray-400 hover:text-gray-900 dark:hover:text-white"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M7 4a3 3 0 016 0v4a3 3 0 11-6 0V4zm4 10.93A7.001 7.001 0 0017 8a1 1 0 10-2 0A5 5 0 015 8a1 1 0 00-2 0 7.001 7.001 0 006 6.93V17H6a1 1 0 100 2h8a1 1 0 100-2h-3v-2.07z"
                clip-rule="evenodd"
              ></path></svg
            >Voice
          </button>
          <lottie-player
            src="https://assets5.lottiefiles.com/packages/lf20_fgwiaub8.json"
            background="transparent"
            speed="1"
            style="width: 300px; height: 50px"
            loop
            autoplay
          ></lottie-player>
        </div>
      </div>
      <div
        class="md:w-3/5 w-full flex justify-center border-4 border-b-8 border-black rounded-3xl flex-wrap"
      >
        <lottie-player
          class="absolute md:right-5"
          src="https://assets5.lottiefiles.com/packages/lf20_yoAOMj.json"
          background="transparent"
          speed="1"
          style="width: 200px; height: 200px"
          loop
          autoplay
        ></lottie-player>
        <h2 class="font-semibold mt-5 text-xl">Speech to Text</h2>
        <div class="flex items-center justify-center" v-if="loading">
          <svg
            aria-hidden="true"
            role="status"
            class="w-6 h-6 animate-spin text-blue-700 mr-3"
            viewBox="0 0 100 100"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle
              cx="50"
              cy="50"
              fill="none"
              r="40"
              stroke="currentColor"
              stroke-width="10"
            />
          </svg>
        </div>
        <div class="border-b w-full flex items-center flex-col">
          <img src="../assets/paper.png" class="-z-10 relative" alt="" />
          <div class="flex flex-wrap items-center justify-center">
            <p class="text-center mb-2" v-if="transcription && !loading">
              {{ transcription }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TextRainbow from "../components/TextRainbow.vue";

export default {
  name: "HelloWorld",
  data() {
    return {
      file: null,
      transcription: null,
      loading: false,
      voiceSelect: {
        name: "English",
        lang: "en-US",
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
    };
  },
  components: {
    TextRainbow,
  },
  methods: {
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
  },
};
</script>

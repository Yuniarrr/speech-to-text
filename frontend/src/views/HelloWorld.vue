<template>
  <div class="text-white">
    <div
      class="container mx-auto flex flex-wrap flex-col w-full md:flex-row items-center "
    >
      <!--Left Col-->
      <div
        class="flex flex-col w-full md:w-2/5 justify-center items-start text-center md:text-left mx-auto"
      >
        <p class="uppercase tracking-loose w-full">
          <TextRainbow
            class="text-gray-500 cursor-pointer"
            text="Hello, This is Speech to text"
          />
          <br />
        </p>
        <h1 class="my-3 text-5xl font-bold leading-tight">
          <TextRainbow
            class="text-gray-400 cursor-pointer"
            text="Hello! Nice to meet you! Is there anything I can help?"
          />
        </h1>
        <p class="leading-normal text-2xl"></p>
      </div>
      <div class="flex flex-col items-center justify-center">
        <lottie-player
          src="https://assets3.lottiefiles.com/private_files/lf30_bkvgqudf.json"
          background="transparent"
          speed="1"
          style="width: 450px; height: 400px"
          loop
          autoplay
        ></lottie-player>
      </div>
    </div>
  </div>

 
  <!-- speech -->
  <section class="bg-white mx-auto">
    <div class="container mx-auto flex flex-wrap pb-3 px-10">
      
      <div class="w-full md:w-1/3 p-2 flex flex-col flex-grow flex-shrink">
        <div
          class="flex-1 bg-sky-100 rounded-t rounded-b-none overflow-hidden shadow"
        >
         <!-- voice -->
         <div
      class="flex flex-col pt-5 mx-auto items-center justify-center w-full"
    >
      <div class="mb-3">
        <div class="mb-2 text-center dark:text-gray-300 text-lg font-semibold">
          SPEECH
        </div>
        <div class="flex flex-row items-center justify-center flex-wrap ">
        <h1 class="mb-2">Choose Language</h1>
          <select
            v-model="voiceSelect"
            class="border-solid rounded-full w-full text-left px-5"
          >
            <option
              class=""
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
      </div>

      <div class="flex flex-col items-center">
        <h1 class="mb-2">Choose Audio File</h1>
        <div
          class="flex flex-row items-center justify-center flex-wrap"
        >
          <input
            type="file"
            @change="onFileChange"
            class="text-left text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
          />
        </div>
      </div>
      <div class="flex items-center justify-center mx-auto mt-2 space-x-2">
        <div>
          <button
            type="button"
            class="inline-flex items-center py-2 px-3 text-sm font-medium text-white bg-gray-800 rounded-lg border hover:bg-blue-600 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
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
        </div>
        <button
          @click="transcribe"
          type="button"
          class="inline-flex items-center py-2 px-3 text-sm font-medium text-white bg-gray-800 rounded-lg border hover:bg-blue-600 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
        >
          Transcribe
        </button>

      </div>
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
      </div>
      <div class="w-full md:w-1/3 p-2 flex flex-col flex-grow flex-shrink">
        <div
          class="flex-1 bg-sky-100 rounded-t rounded-b-none overflow-hidden shadow"
        >
        <div
      class="flex flex-col pt-5 mx-auto items-center justify-center w-full"
    >
      <div class="mb-3">
        <div class="uppercase mb-2 dark:text-gray-300 text-lg font-semibold">
          SPEECH TO TEXT
        </div>
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
       
        <div class="flex flex-wrap items-center justify-center">
          <p class="text-center mb-2" v-if="transcription && !loading">
            {{ transcription }}
          </p>
        </div>
      </div>
       
        </div>
        </div>
        </div>
      </div>
      
    </div>
  </section>
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

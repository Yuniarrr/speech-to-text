<template>
  <div>
    <div class="text-white">
      <div
        class="container flex flex-col flex-wrap items-center w-full mx-auto md:flex-row"
      >
        <div
          class="flex flex-col items-start justify-center w-full md:mx-auto text-center md:w-2/5 md:text-left"
        >
          <p class="w-full uppercase tracking-loose mt-4 md:mt-0">
            <TextRainbow
              class="text-gray-500 cursor-pointer"
              text="Hello, This is Speech to text"
            />
            <br />
          </p>
          <h1 class="my-3 text-5xl font-bold leading-tight mx-6 md:mx-0">
            <TextRainbow
              class="text-gray-400 cursor-pointer"
              text="Hello! Nice to meet you! Is there anything I can help?"
            />
          </h1>
          <p class="text-2xl leading-normal"></p>
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
    <section class="mx-auto bg-white">
      <div class="container flex flex-wrap px-10 pb-3 mx-auto">
        <div class="flex flex-col flex-grow flex-shrink w-full p-2 md:w-1/3">
          <div
            class="flex-1 pb-6 overflow-hidden rounded-t rounded-b-none shadow bg-sky-100"
          >
            <!-- voice -->
            <div
              class="flex flex-col items-center justify-center w-full pt-5 mx-auto"
            >
              <div class="mb-3">
                <div
                  class="mb-2 text-lg font-semibold text-center dark:text-gray-300"
                >
                  SPEECH
                </div>
                <div
                  class="flex flex-row flex-wrap items-center justify-center"
                >
                  <h1 class="mb-2">Choose Language</h1>
                  <select
                    v-model="voiceSelect"
                    class="w-full px-5 text-left border-solid rounded-full"
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
                  class="flex flex-row flex-wrap items-center justify-center"
                >
                  <input
                    type="file"
                    @change="onFileChange"
                    class="text-left text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
                  />
                </div>
              </div>
              <div
                class="flex items-center justify-center mx-auto mt-2 space-x-2"
              >
                <button
                  v-if="!record"
                  @click="onRecord"
                  type="button"
                  class="inline-flex items-center px-3 py-2 text-sm font-medium text-white bg-gray-800 border rounded-lg hover:bg-blue-600 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
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
                <button
                  v-if="record"
                  @click="stopRecord"
                  type="button"
                  class="inline-flex items-center px-3 py-2 text-sm font-medium text-white bg-gray-800 border rounded-lg hover:bg-blue-600 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
                >
                  <svg
                    fill="white"
                    class="w-5 h-5 mr-2 text-white dark:text-gray-400 dark:hover:text-white"
                    stroke="currentColor"
                    stroke-width="1.5"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                    aria-hidden="true"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M5.25 7.5A2.25 2.25 0 017.5 5.25h9a2.25 2.25 0 012.25 2.25v9a2.25 2.25 0 01-2.25 2.25h-9a2.25 2.25 0 01-2.25-2.25v-9z"
                    ></path></svg
                  >Stop
                </button>
                <button
                  @click="transcribe"
                  type="button"
                  class="inline-flex items-center px-3 py-2 text-sm font-medium text-white bg-gray-800 border rounded-lg hover:bg-blue-600 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
                >
                  Transcribe
                </button>
              </div>
              <lottie-player
                v-if="record"
                class="mt-2 -mb-2"
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
        <div class="flex flex-col flex-grow w-full p-2 md:w-1/3">
          <div
            class="flex-1 overflow-hidden rounded-t rounded-b-none shadow bg-sky-100"
          >
            <div
              class="flex flex-col items-center justify-center w-full pt-5 pb-5"
            >
              <div
                class="mb-2 text-lg font-semibold uppercase dark:text-gray-300"
              >
                SPEECH TO TEXT
              </div>
              <div class="flex items-center justify-center" v-if="loading">
                <svg
                  aria-hidden="true"
                  role="status"
                  class="w-6 h-6 mr-3 text-blue-700 animate-spin"
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
              <div class="flex flex-col items-center w-full text-center">
                <p class="mx-5" v-if="transcription && !loading">
                  {{ transcription }}
                </p>
                <!-- <p class="mx-5" v-if="transcription == null && !loading">
                  Here's the message
                </p> -->
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
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
      record: false,
      recording: null,
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
    onRecord() {
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
      };
      this.recording = sr;
    },
    stopRecord() {
      this.record = false;
      this.recording.stop();
    },
  },
};
</script>

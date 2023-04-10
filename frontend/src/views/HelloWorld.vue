<script setup>
import TextRainbow from "../components/TextRainbow.vue";
</script>

<template>
  <div class="bg-black text-white">
    <div
      class="container mx-auto flex flex-wrap flex-col md:flex-row items-center"
    >
      <!--Left Col-->
      <div
        class="flex flex-col w-full md:w-2/6 justify-center items-start text-center"
      >
        <p class="uppercase tracking-loose w-full">
          <TextRainbow
            class="text-white cursor-pointer"
            text="Hello, This is Speech to text"
          />
          <br />
        </p>
        <h1 class="my-3 text-5xl font-bold leading-tight">
          <TextRainbow
            class="text-zinc-500 cursor-pointer"
            text="Hello! Nice to meet you! Is there anything I can help?"
          />
        </h1>
        <p class="leading-normal text-2xl mb-8"></p>
      </div>
      <!-- speech -->
      <div class="h-full">
        <form class="flex items-center">
          <div class="relative w-full">
            <div
              class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
            ></div>
          </div>
        </form>
      </div>
    </div>
  </div>

  <div class="relative -mt-12 lg:-mt-24 bg-black">
    <svg
      viewBox="0 0 1428 174"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
    >
      <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g
          transform="translate(-2.000000, 44.000000)"
          fill="#FFFFFF"
          fill-rule="nonzero"
        >
          <path
            d="M0,0 C90.7283404,0.927527913 147.912752,27.187927 291.910178,59.9119003 C387.908462,81.7278826 543.605069,89.334785 759,82.7326078 C469.336065,156.254352 216.336065,153.6679 0,74.9732496"
            opacity="0.100000001"
          ></path>
          <path
            d="M100,104.708498 C277.413333,72.2345949 426.147877,52.5246657 546.203633,45.5787101 C666.259389,38.6327546 810.524845,41.7979068 979,55.0741668 C931.069965,56.122511 810.303266,74.8455141 616.699903,111.243176 C423.096539,147.640838 250.863238,145.462612 100,104.708498 Z"
            opacity="0.100000001"
          ></path>
          <path
            d="M1046,51.6521276 C1130.83045,29.328812 1279.08318,17.607883 1439,40.1656806 L1439,120 C1271.17211,77.9435312 1140.17211,55.1609071 1046,51.6521276 Z"
            id="Path-4"
            opacity="0.200000003"
          ></path>
        </g>
        <g
          transform="translate(-4.000000, 76.000000)"
          fill="#FFFFFF"
          fill-rule="nonzero"
        >
          <path
            d="M0.457,34.035 C57.086,53.198 98.208,65.809 123.822,71.865 C181.454,85.495 234.295,90.29 272.033,93.459 C311.355,96.759 396.635,95.801 461.025,91.663 C486.76,90.01 518.727,86.372 556.926,80.752 C595.747,74.596 622.372,70.008 636.799,66.991 C663.913,61.324 712.501,49.503 727.605,46.128 C780.47,34.317 818.839,22.532 856.324,15.904 C922.689,4.169 955.676,2.522 1011.185,0.432 C1060.705,1.477 1097.39,3.129 1121.236,5.387 C1161.703,9.219 1208.621,17.821 1235.4,22.304 C1285.855,30.748 1354.351,47.432 1440.886,72.354 L1441.191,104.352 L1.121,104.031 L0.457,34.035 Z"
          ></path>
        </g>
      </g>
    </svg>
  </div>

  <div class="flex flex-col items-center mt-5">
    <div class="mb-1 px-20">
      <select
        data-te-select-init
        v-model="voiceSelect"
        @change="onVoiceSelect"
        class="border-solid rounded-full text-left px-24 flex items-center justify-center"
      >
        <option
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
      <div class="dark:text-gray-300 text-lg font-semibold">
        CHOOSE AUDIO FILE
      </div>
      <div class="flex flex-row items-center justify-center flex-wrap gap-x-8">
        <input
          type="file"
          @change="onFileChange"
          class="text-left text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
        />
        <button
          @click="transcribe"
          type="button"
          class="transition ease-in-out delay-150 bg-gray-800 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-l px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700 text-white hover:scale-110 hover:bg-green-500 duration-300 ..."
        >
          Transcribe
        </button>
      </div>
    </div>
    <div class="flex-col items-center justify-center">
      <button
        type="button"
        class="inline-flex items-center py-2.5 px-3 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
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
  </div>

  <div class="flex items-center justify-center my-4" v-if="loading">
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
  <section v-else class="bg-white border-b w-full mt-1" v-if="transcription">
    <div class="flex flex-wrap items-center justify-center">
      <p class="text-center mb-2">
        {{ transcription }}
        <br />
      </p>
    </div>
  </section>
</template>

<script>
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

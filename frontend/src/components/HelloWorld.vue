<template>
  <div class="flex flex-col items-center justify-center">
    <div class="flex items-center" v-if="loading">
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
      <p>Loading...</p>
    </div>
    <div v-else class="flex flex-col items-center">
      <h1 class="mb-8 text-xl font-bold">Speech-to-Text</h1>
      <div class="flex">
        <input type="file" @change="onFileChange" />
        <button
          @click="transcribe"
          type="button"
          class="text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
        >
          Transcribe
        </button>
      </div>

      <div class="flex justify-center">
        <div class="mb-3 xl:w-96">
          <select
            data-te-select-init
            v-model="voiceSelect"
            @change="onVoiceSelect"
            class="border-solid rounded-lg"
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
      </div>

      <p v-if="transcription">{{ transcription }}</p>
    </div>
  </div>
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
    onVoiceSelect() {
      this.voiceSelect = this.voiceSelect;
      console.log(this.voiceSelect);
    },
    async transcribe() {
      this.loading = true;
      const formData = new FormData();
      formData.append("file", this.file);

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

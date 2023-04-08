<template>
  <div class="flex flex-col items-center justify-center">
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
    <p v-if="transcription">{{ transcription }}</p>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      file: null,
      transcription: null,
    };
  },
  methods: {
    onFileChange(event) {
      this.file = event.target.files[0];
    },
    async transcribe() {
      const formData = new FormData();
      formData.append("file", this.file);

      const response = await fetch("http://localhost:5000/transcribe", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      this.transcription = data.text;
    },
  },
};
</script>

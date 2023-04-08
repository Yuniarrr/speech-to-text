<template>
  <div class="hello">
    <h1>Speech-to-Text</h1>
    <input type="file" @change="onFileChange" />
    <button @click="transcribe">Transcribe</button>
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

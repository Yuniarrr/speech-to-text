<script setup>
const props = defineProps({
  text: {
    type: String,
    required: true,
  },
});

let colors = [
  "hover:text-orange-300",
  "hover:text-sky-300",
  "hover:text-rose-300",
  "hover:text-purple-300",
  "hover:text-yellow-300",
];
</script>

<template>
  <span>
    <span
      v-for="(char, index) in props.text.split('')"
      :key="index"
      :class="[
        'transition-colors delay-[5000ms] duration-[5000ms] hover:delay-[0ms] hover:duration-[0ms]',
        colors[index % colors.length],
      ]"
      >{{ char }}</span
    >
  </span>
</template>

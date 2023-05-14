<script setup>
const props = defineProps({
  text: {
    type: String,
    required: true,
  },
});

let colors = [
  "hover:text-orange-200",
  "hover:text-emerald-200",
  "hover:text-red-200",
  "hover:text-purple-200",
  "hover:text-yellow-200",
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

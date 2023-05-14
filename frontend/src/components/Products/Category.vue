<template>
  <router-link :to="`/category/${category_id}`">
    <div
      class="cursor-pointer overflow-hidden rounded-lg border border-gray-200 bg-white p-3 shadow-lg dark:border-gray-700 dark:bg-gray-800 hover:bg-slate-100"
    >
      {{ name }}
    </div>
  </router-link>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    category_id: {
      type: String,
      required: true,
    },
  },
};
</script>

<template>
  <div
    class="cursor-pointer overflow-hidden rounded-lg border border-gray-200 bg-white p-3 shadow-lg hover:bg-slate-100 w-max"
    :class="categoryClass(slug)"
  >
    {{ name }}
  </div>
</template>

<script>
import { useApp } from "../../store/index.js";

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
    slug: {
      type: String,
      required: true,
    },
  },
  setup() {
    const app = useApp();

    return {
      app,
    };
  },
  computed: {
    categoryClass() {
      return (slug) => ({
        "bg-slate-200": slug == this.app.slug_category,
      });
    },
  },
};
</script>

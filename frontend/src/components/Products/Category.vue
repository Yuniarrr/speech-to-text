<template>
  <div
    class="rounded-lg border border-gray-200 bg-white p-2 shadow-sm hover:bg-slate-100 w-max cursor-pointer my-2"
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

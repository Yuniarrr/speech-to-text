<template>
  <li>
    <router-link
      :to="path"
      class="block mt-4 mr-4 text-white sm:mt-0 hover:text-slate-100 hover:underline hover:underline-offset-8"
      :class="
        $route.path == `${path}`
          ? 'underline underline-offset-8 font-semibold'
          : ''
      "
    >
      {{ name }}
    </router-link>
  </li>
</template>

<script>
export default {
  props: {
    path: {
      type: String,
      required: false,
    },
    name: {
      type: String,
      required: true,
    },
  },
};
</script>

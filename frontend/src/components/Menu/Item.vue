<template>
  <li>
    <router-link
      :to="path"
      class="block mt-4 mr-4 text-black sm:mt-0"
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

<template>
  <div class="sticky top-0 bg-black" id="app">
    <nav class="flex items-center justify-between flex-wrap bg-teal p-4">
      <div class="flex items-center flex-no-shrink text-white mr-6">
        <img
          class="fill-current h-8 w-8 mr-2 w-32 h-32"
          src="../assets/logo.png"
          alt="logo"
        />
        <span class="font-semibold text-xl tracking-tight">SORA</span>
      </div>

      <ul
        :class="open ? 'block' : 'hidden'"
        class="w-full sm:flex sm:items-center sm:w-auto"
      >
        <div class="text-sm sm:flex-grow flex">
          <li>
            <a
              @click="setPage('Home')"
              class="block mt-4 sm:inline-block sm:mt-0 text-teal-lighter text-white hover:text-white mr-4"
            >
              Home
            </a>
          </li>
          <li>
            <button
              class="no-underline text-gray-300 block mt-4 sm:inline-block sm:mt-0 text-teal-lighter hover:text-white mr-4"
            >
              Examples
            </button>
          </li>
          <li>
            <button
              class="no-underline text-gray-300 block mt-4 sm:inline-block sm:mt-0 text-teal-lighter hover:text-white"
            >
              Blog
            </button>
          </li>
        </div>
      </ul>
    </nav>
  </div>
</template>
<script>
export default {
  name: "Header",
};
</script>

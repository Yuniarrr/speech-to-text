<template>
  <div class="bg-white mx-10 my-5">
    <div class="flex items-center justify-center lg:space-x-20 sm:space-x-5">
      <!-- category -->
      <div class="bg-white w-3/4 ml-auto">
        <div>
          <div class="relative z-40 lg:hidden" role="dialog" aria-modal="true">
            <div
              class="relative ml-auto flex h-full w-full max-w-xs flex-col overflow-y-auto bg-white py-4 pb-12 shadow-xl"
            >
              <div class="flex items-center justify-between px-4">
                <h2 class="text-lg font-medium text-gray-900">Filters</h2>
                <button
                  type="button"
                  class="-mr-2 flex h-10 w-10 items-center justify-center rounded-md bg-white p-2 text-gray-400"
                >
                  <span class="sr-only">Close menu</span>
                  <svg
                    class="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>

              <!-- Filters -->
              <form class="mt-4 border-t border-gray-200">
                <h3 class="sr-only">Categories</h3>
                <ul role="list" class="px-2 py-3 font-medium text-gray-900">
                  <li>
                    <a href="#" class="block px-2 py-3">Totes</a>
                  </li>
                  <li>
                    <a href="#" class="block px-2 py-3">Backpacks</a>
                  </li>
                  <li>
                    <a href="#" class="block px-2 py-3">Travel Bags</a>
                  </li>
                  <li>
                    <a href="#" class="block px-2 py-3">Hip Bags</a>
                  </li>
                  <li>
                    <a href="#" class="block px-2 py-3">Laptop Sleeves</a>
                  </li>
                </ul>

                <div class="border-t border-gray-200 px-4 py-6">
                  <h3 class="-mx-2 -my-3 flow-root">
                    <!-- Expand/collapse section button -->
                    <button
                      type="button"
                      class="flex w-full items-center justify-between bg-white px-2 py-3 text-gray-400 hover:text-gray-500"
                      aria-controls="filter-section-mobile-0"
                      aria-expanded="false"
                    >
                      <span class="font-medium text-gray-900">Color</span>
                      <span class="ml-6 flex items-center">
                        <!-- Expand icon, show/hide based on section open state. -->
                        <svg
                          class="h-5 w-5"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            d="M10.75 4.75a.75.75 0 00-1.5 0v4.5h-4.5a.75.75 0 000 1.5h4.5v4.5a.75.75 0 001.5 0v-4.5h4.5a.75.75 0 000-1.5h-4.5v-4.5z"
                          />
                        </svg>
                        <!-- Collapse icon, show/hide based on section open state. -->
                        <svg
                          class="h-5 w-5"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            fill-rule="evenodd"
                            d="M4 10a.75.75 0 01.75-.75h10.5a.75.75 0 010 1.5H4.75A.75.75 0 014 10z"
                            clip-rule="evenodd"
                          />
                        </svg>
                      </span>
                    </button>
                  </h3>
                  <!-- Filter section, show/hide based on section state. -->
                  <div class="pt-6" id="filter-section-mobile-0">
                    <div class="space-y-6">
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-color-0"
                          name="color[]"
                          value="white"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-color-0"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >White</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-color-1"
                          name="color[]"
                          value="beige"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-color-1"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Beige</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-color-2"
                          name="color[]"
                          value="blue"
                          type="checkbox"
                          checked
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-color-2"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Blue</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-color-3"
                          name="color[]"
                          value="brown"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-color-3"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Brown</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-color-4"
                          name="color[]"
                          value="green"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-color-4"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Green</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-color-5"
                          name="color[]"
                          value="purple"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-color-5"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Purple</label
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <div class="border-t border-gray-200 px-4 py-6">
                  <h3 class="-mx-2 -my-3 flow-root">
                    <!-- Expand/collapse section button -->
                    <button
                      type="button"
                      class="flex w-full items-center justify-between bg-white px-2 py-3 text-gray-400 hover:text-gray-500"
                      aria-controls="filter-section-mobile-1"
                      aria-expanded="false"
                    >
                      <span class="font-medium text-gray-900">Category</span>
                      <span class="ml-6 flex items-center">
                        <!-- Expand icon, show/hide based on section open state. -->
                        <svg
                          class="h-5 w-5"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            d="M10.75 4.75a.75.75 0 00-1.5 0v4.5h-4.5a.75.75 0 000 1.5h4.5v4.5a.75.75 0 001.5 0v-4.5h4.5a.75.75 0 000-1.5h-4.5v-4.5z"
                          />
                        </svg>
                        <!-- Collapse icon, show/hide based on section open state. -->
                        <svg
                          class="h-5 w-5"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            fill-rule="evenodd"
                            d="M4 10a.75.75 0 01.75-.75h10.5a.75.75 0 010 1.5H4.75A.75.75 0 014 10z"
                            clip-rule="evenodd"
                          />
                        </svg>
                      </span>
                    </button>
                  </h3>
                  <!-- Filter section, show/hide based on section state. -->
                  <div class="pt-6" id="filter-section-mobile-1">
                    <div class="space-y-6">
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-category-0"
                          name="category[]"
                          value="new-arrivals"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-category-0"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >New Arrivals</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-category-1"
                          name="category[]"
                          value="sale"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-category-1"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Sale</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-category-2"
                          name="category[]"
                          value="travel"
                          type="checkbox"
                          checked
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-category-2"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Travel</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-category-3"
                          name="category[]"
                          value="organization"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-category-3"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Organization</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-category-4"
                          name="category[]"
                          value="accessories"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-category-4"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >Accessories</label
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <div class="border-t border-gray-200 px-4 py-6">
                  <h3 class="-mx-2 -my-3 flow-root">
                    <!-- Expand/collapse section button -->
                    <button
                      type="button"
                      class="flex w-full items-center justify-between bg-white px-2 py-3 text-gray-400 hover:text-gray-500"
                      aria-controls="filter-section-mobile-2"
                      aria-expanded="false"
                    >
                      <span class="font-medium text-gray-900">Size</span>
                      <span class="ml-6 flex items-center">
                        <!-- Expand icon, show/hide based on section open state. -->
                        <svg
                          class="h-5 w-5"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            d="M10.75 4.75a.75.75 0 00-1.5 0v4.5h-4.5a.75.75 0 000 1.5h4.5v4.5a.75.75 0 001.5 0v-4.5h4.5a.75.75 0 000-1.5h-4.5v-4.5z"
                          />
                        </svg>
                        <!-- Collapse icon, show/hide based on section open state. -->
                        <svg
                          class="h-5 w-5"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            fill-rule="evenodd"
                            d="M4 10a.75.75 0 01.75-.75h10.5a.75.75 0 010 1.5H4.75A.75.75 0 014 10z"
                            clip-rule="evenodd"
                          />
                        </svg>
                      </span>
                    </button>
                  </h3>
                  <!-- Filter section, show/hide based on section state. -->
                  <div class="pt-6" id="filter-section-mobile-2">
                    <div class="space-y-6">
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-size-0"
                          name="size[]"
                          value="2l"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-size-0"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >2L</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-size-1"
                          name="size[]"
                          value="6l"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-size-1"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >6L</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-size-2"
                          name="size[]"
                          value="12l"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-size-2"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >12L</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-size-3"
                          name="size[]"
                          value="18l"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-size-3"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >18L</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-size-4"
                          name="size[]"
                          value="20l"
                          type="checkbox"
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-size-4"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >20L</label
                        >
                      </div>
                      <div class="flex items-center">
                        <input
                          id="filter-mobile-size-5"
                          name="size[]"
                          value="40l"
                          type="checkbox"
                          checked
                          class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                        />
                        <label
                          for="filter-mobile-size-5"
                          class="ml-3 min-w-0 flex-1 text-gray-500"
                          >40L</label
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>

          <main class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="flex items-baseline justify-between">
              <h1 class="text-l font-bold tracking-tight text-gray-900">
                FILTER
              </h1>

              <div class="flex items-center"></div>
            </div>
            <section aria-labelledby="products-heading" class="pb-24 pt-6">
              <div class="grid grid-cols-1 gap-x-8 gap-y-10 lg:grid-cols-4">
                <!-- Filters -->
                <form class="hidden lg:block">
                  <h3 class="sr-only">Medicine</h3>
                  <ul
                    role="list"
                    class="space-y-4 border-b border-gray-200 pb-6 text-sm font-medium text-gray-900"
                  >
                    <li>
                      <a href="#">Medicine</a>
                    </li>
                  </ul>

                  <div class="border-b border-gray-200 py-6">
                    <h3 class="-my-3 flow-root">
                      <!-- Expand/collapse section button -->
                      <button
                        type="button"
                        class="flex w-full items-center justify-between bg-white py-3 text-sm text-gray-400 hover:text-gray-500"
                        aria-controls="filter-section-0"
                        aria-expanded="false"
                      >
                        <span class="font-medium text-gray-900">Ratings</span>
                        <span class="ml-6 flex items-center">
                          <!-- Expand icon, show/hide based on section open state. -->
                          <svg
                            @click="toggleShow"
                            :class="{
                              '-rotate-180': show,
                              'rotate-0': !show,
                              '-mr-1': show,
                              'ml-1': !show,
                              'h-5': true,
                              'w-5': true,
                              'flex-shrink-0': true,
                              'text-gray-400': true,
                              'group-hover:text-gray-500': true,
                            }"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                          >
                            <path
                              fill-rule="evenodd"
                              d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                              clip-rule="evenodd"
                            />
                          </svg>
                        </span>
                      </button>
                    </h3>
                    <!-- Filter section, show/hide based on section state. -->
                    <div v-if="show" class="pt-6" id="filter-section-0">
                      <div class="space-y-4">
                        <div class="flex items-center">
                          <input
                            id="filter-color-0"
                            name="color[]"
                            value="white"
                            type="checkbox"
                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                          />
                          <!-- 5 star -->
                          <div class="flex items-center">
                            <svg
                              class="h-5 w-5 text-yellow-500"
                              xmlns="http://www.w3.org/2000/svg"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                            >
                              <path
                                class="fill-current text-yellow-500"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                              />
                            </svg>
                            <svg
                              class="h-5 w-5 text-yellow-500"
                              xmlns="http://www.w3.org/2000/svg"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                            >
                              <path
                                class="fill-current text-yellow-500"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                              />
                            </svg>
                            <svg
                              class="h-5 w-5 text-yellow-500"
                              xmlns="http://www.w3.org/2000/svg"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                            >
                              <path
                                class="fill-current text-yellow-500"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                              />
                            </svg>
                            <svg
                              class="h-5 w-5 text-yellow-500"
                              xmlns="http://www.w3.org/2000/svg"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                            >
                              <path
                                class="fill-current text-yellow-500"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                              />
                            </svg>
                            <svg
                              class="h-5 w-5 text-yellow-500"
                              xmlns="http://www.w3.org/2000/svg"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                            >
                              <path
                                class="fill-current text-yellow-500"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                              />
                            </svg>

                            <!-- 4 star -->
                          </div>
                        </div>
                        <div class="flex items-center">
                          <input
                            id="filter-color-1"
                            name="color[]"
                            value="beige"
                            type="checkbox"
                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                          />
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>

                          <!-- 3 star -->
                        </div>
                        <div class="flex items-center">
                          <input
                            id="filter-color-2"
                            name="color[]"
                            value="blue"
                            type="checkbox"
                            checked
                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                          />
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>

                          <!-- 2 star -->
                        </div>
                        <div class="flex items-center">
                          <input
                            id="filter-color-3"
                            name="color[]"
                            value="brown"
                            type="checkbox"
                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                          />
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              class="fill-current text-yellow-500"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                          <svg
                            class="h-5 w-5 text-yellow-500"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M12 2l3.09 6.31L22 9.25l-5 4.87 1.18 6.84L12 17.77l-6.18 3.19L7 14.12 2 9.25l6.91-0.94L12 2z"
                            />
                          </svg>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="border-b border-gray-200 py-6">
                    <h3 class="-my-3 flow-root">
                      <!-- Expand/collapse section button -->
                      <button
                        type="button"
                        class="flex w-full items-center justify-between bg-white py-3 text-sm text-gray-400 hover:text-gray-500"
                        aria-controls="filter-section-1"
                        aria-expanded="false"
                      >
                        <!-- Urut Abjad -->
                        <span class="font-medium text-gray-900"
                          >Urut Abjad</span
                        >
                        <span class="ml-6 flex items-center">
                          <!-- Expand icon, show/hide based on section open state. -->
                          <svg
                            @click="toggleShow"
                            :class="{
                              '-rotate-180': show,
                              'rotate-0': !show,
                              '-mr-1': show,
                              'ml-1': !show,
                              'h-5': true,
                              'w-5': true,
                              'flex-shrink-0': true,
                              'text-gray-400': true,
                              'group-hover:text-gray-500': true,
                            }"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                          >
                            <path
                              fill-rule="evenodd"
                              d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                              clip-rule="evenodd"
                            />
                          </svg>
                        </span>
                      </button>
                    </h3>
                    <!-- Filter section, show/hide based on section state. -->
                    <div v-if="show" class="pt-6" id="filter-section-1">
                      <div class="space-y-2">
                        <div class="flex items-center">
                          <input
                            id="filter-category-0"
                            name="category[]"
                            value="new-arrivals"
                            type="checkbox"
                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                          />
                          <label
                            for="filter-category-0"
                            class="ml-3 text-sm text-gray-600"
                            >A-Z</label
                          >
                        </div>
                        <div class="flex items-center">
                          <input
                            id="filter-category-1"
                            name="category[]"
                            value="sale"
                            type="checkbox"
                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                          />
                          <label
                            for="filter-category-1"
                            class="ml-3 text-sm text-gray-600"
                            >Z-A</label
                          >
                        </div>
                      </div>
                    </div>

                </div>
                </form>

                <!-- Product grid -->
                <div class="lg:col-span-3">
                  <!-- Your content -->
                </div>
              </div>
            </section>
          </main>
        </div>
      </div>

      <!-- Search -->
      <div class="flex">
        <div class="relative w-96">
          <div
            class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
          >
            <svg
              aria-hidden="true"
              class="w-5 h-5 text-gray-500"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </div>
          <input
            type="text"
            id="voice-search"
            v-model="app.search"
            @keydown.enter="app.getProducts()"
            class="border border-gray-300 text-gray-900 text-sm rounded-3xl focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Input complaint / medicine here "
            required
          />
          <button
            v-if="!mic.record"
            @click="mic.onRecord"
            type="button"
            class="absolute inset-y-0 right-0 flex items-center pr-3"
          >
            <svg
              aria-hidden="true"
              class="w-4 h-4 text-gray-500 hover:text-gray-900"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M7 4a3 3 0 016 0v4a3 3 0 11-6 0V4zm4 10.93A7.001 7.001 0 0017 8a1 1 0 10-2 0A5 5 0 015 8a1 1 0 00-2 0 7.001 7.001 0 006 6.93V17H6a1 1 0 100 2h8a1 1 0 100-2h-3v-2.07z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </button>
          <button
            v-if="mic.record"
            @click="mic.stopRecord"
            type="button"
            class="absolute inset-y-0 right-0 flex items-center pr-3"
          >
            <svg
              fill="white"
              class="w-4 h-4 text-gray-500 hover:text-gray-900"
              stroke="currentColor"
              stroke-width="1.5"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M5.25 7.5A2.25 2.25 0 017.5 5.25h9a2.25 2.25 0 012.25 2.25v9a2.25 2.25 0 01-2.25 2.25h-9a2.25 2.25 0 01-2.25-2.25v-9z"
              ></path>
            </svg>
          </button>
        </div>
        <button
          type="button"
          @click="app.getProducts()"
          class="inline-flex items-center py-2.5 px-3 ml-2 text-sm font-medium text-white bg-blue-700 rounded-full border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          <svg
            aria-hidden="true"
            class="w-5 h-5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            ></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- promo -->
    <swiper />

    <div v-if="app.products.length == 0 && app.categories.length != 0">
      <!-- Category -->
      <div class="flex flex-col justify-around">
        <h1 class="mt-10 text-2xl font-bold">CATEGORY</h1>
        <div class="flex flex-row my-2 space-x-5 overflow-auto">
          <div v-for="(category, index) in app.categories" :key="index">
            <category
              v-if="category.sub_categories.length != 0"
              :name="category.name"
              :category_id="category.category_id"
              :slug="category.slug.value"
              @click="
                (app.slug_category = category.slug.value),
                  app.getSubCategories(category.slug.value)
              "
            />
          </div>
        </div>
      </div>

      <!-- Sub Category -->
      <div class="flex flex-col justify-around">
        <h1 class="mt-10 text-2xl font-bold">
          {{
            app.categories.find((item) => item.slug.value == app.slug_category)
              .name
          }}
        </h1>
        <div class="flex flex-col space-y-2">
          <div
            v-for="sub_category in app.sub_categories"
            :key="sub_category.category_id"
          >
            <router-link :to="`/subcategory/${sub_category.slug.value}`">
              <div
                @click="app.getProductSubCategories(sub_category.slug.value)"
                class="p-3 overflow-hidden bg-white border border-gray-200 rounded-lg shadow-lg cursor-pointer dark:border-gray-700 dark:bg-gray-800 hover:bg-slate-100"
              >
                {{ sub_category.name }}
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- CARD -->
    <div
      class="flex flex-col justify-around space-y-8"
      v-if="app.products.length != 0"
    >
      <h1 class="text-2xl font-bold text-center">
        Search for "{{ app.search }}"
      </h1>
      <div class="flex flex-wrap items-center justify-center">
        <!--Card 1-->
        <div v-for="(product, index) in app.products.result" :key="index">
          <div
            class="mx-2 my-2 w-64 h-[520px] -hidden border border-gray-300 rounded shadow-lg col-span-1 flex flex-col gap-4"
          >
            <img
              class="w-full h-52"
              :src="product.thumbnail_url"
              :alt="product.slug"
            />
            <div class="p-4">
              <div class="flex flex-wrap">
                <div class="text-xl font-bold cursor-pointer">
                  {{ product.name }}
                </div>
                <div class="font-semibold text-sm text-orange-400 flex">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="orange"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="orange"
                    class="w-3 h-3 mr-1 mt-[4px]"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
                    />
                  </svg>
                  {{ product.ratings }}
                </div>
              </div>
              <div class="mb-2 text-base font-semibold">
                {{ product.selling_unit }}
              </div>
              <div class="mb-6 text-base">
                Rp {{ product.min_price }} - {{ product.base_price }}
              </div>
            </div>
            <router-link
              :to="`/product/${product.slug}`"
              @click="app.getProduct(product.slug)"
              type="button"
              class="flex mt-auto focus:outline-none text-white bg-sky-700 hover:bg-sky-800 focus:ring-4 focus:ring-sky-300 font-medium rounded-lg text-sm px-4 py-2.5 dark:bg-sky-600 dark:hover:bg-sky-700 dark:focus:ring-sky-800"
            >
              <span class="mx-auto">Detail</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Swiper from "../components/Products/Swiper.vue";
import { useApp, useMicrophone } from "../store/index.js";
import Card from "../components/Products/Card.vue";
import Category from "../components/Products/Category.vue";

export default {
  components: {
    Swiper,
    Card,
    Category,
  },
  data() {
    return {
      show: false,
    };
  },
  setup() {
    const app = useApp();
    const mic = useMicrophone();

    return {
      app,
      mic,
    };
  },
  mounted() {
    this.app.getCategories();
    this.app.getSubCategories(this.app.slug_category);
  },
  methods: {
    toggleShow() {
      this.show = !this.show;
    },
  },
};
</script>

<style>
.dropdown:hover .dropdown-menu {
  display: block;
}
</style>

<template>
  <div>
    <swiper
      :spaceBetween="30"
      :centeredSlides="true"
      :autoplay="{
        delay: 2500,
        disableOnInteraction: false,
      }"
      :pagination="{
        clickable: true,
      }"
      :navigation="true"
      :modules="modules"
      class="mySwiper my-5 w-3/4 mx-auto h-96"
    >
      <swiper-slide>
        <img
          className="object-fill w-full h-full"
          src="https://cdn.pixabay.com/photo/2022/03/20/15/40/nature-7081138__340.jpg"
          alt="image slide 1"
        />
      </swiper-slide>
      <swiper-slide>
        <img
          className="object-fill w-full h-full"
          src="https://cdn.pixabay.com/photo/2022/07/24/17/55/wind-energy-7342177__340.jpg"
          alt="image slide 2"
        />
      </swiper-slide>
      <swiper-slide>
        <img
          className="object-fill w-full h-full"
          src="https://cdn.pixabay.com/photo/2022/07/26/03/35/jogger-7344979__340.jpg"
          alt="image slide 3"
        />
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from "swiper/vue";

// Import Swiper styles
import "swiper/css";

import "swiper/css/pagination";
import "swiper/css/navigation";

// import required modules
import { Autoplay, Pagination, Navigation } from "swiper";

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules: [Autoplay, Pagination, Navigation],
    };
  },
};
</script>

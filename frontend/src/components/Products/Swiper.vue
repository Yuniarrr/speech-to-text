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
          src="https://down-aka-id.img.susercontent.com/e803a6a20062c47931a6d26693531a79"
          alt="image slide 1"
        />
      </swiper-slide>
      <swiper-slide>
        <img
          className="object-fill w-full h-full"
          src="https://blog.klikindomaret.com/wp-content/uploads/2022/02/HERO_BNR_PILIHAN-HEMAT-SEHAT-23-FE.jpg"
          alt="image slide 2"
        />
      </swiper-slide>
      <swiper-slide>
        <img
          className="object-fill w-full h-full"
          src="https://o-cdf.sirclocdn.com/unsafe/700x343/https://o-cdf.sirclocdn.com/unsafe/cdn-omp.orami.co.id/media/block-node/EZ_Featured_-_Musim_Hujan_Siapa_Takut-.jpg"
          alt="oks"
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

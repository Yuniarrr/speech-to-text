<script>
export default {
  data() {
    return {
      faqs: [
        {
          question: "Apa itu SORA?",
          answer:
            "SORA adalah suatu teknologi yang menyajikan solusi dari penyakit siapapun yang sedang terhubung dengan internet dengan cara memberikan obat yang sesuai dengan keluhan user serta menampilkan apotek terdekat.",
          open: false,
        },
        {
          question: "Kenapa harus menggunakan SORA?",
          answer:
            'SORA dapat menampilkan obat yang akurat sesuai dengan keluhan user karena teknologi SORA memiliki pedoman yaitu "YOUR MIND IS MINE", dengan begitu SORA dapat mengetahui pasti apa saja yang dibutuhkan oleh user.',
          open: false,
        },
        {
          question:
            "Berapa uang yang harus dikeluarkan untuk menggunakan SORA?",
          answer:
            "Seluruh fitur yang ada di SORA dapat digunakan secara GRATIS oleh khalayak umum.",
          open: false,
        },
        {
          question: "Kapan jam operasional SORA dibuka?",
          answer:
            "SORA merupakan layanan berbasis website yang tersedia selama 24 JAM penuh tanpa terkecuali",
          open: false,
        },
        {
          question: "Bagaimana jika saya memerlukan informasi lebih lanjut?",
          answer:
            "Bisa langsung menghubungi nomor layanan pelanggan SORA melalui WhatsApp di +62-83847019803",
          open: false,
        },
      ],
    };
  },
  methods: {
    toggleFAQ(index) {
      this.faqs[index].open = !this.faqs[index].open;
    },
  },
};
</script>

<template>
  <div
    class="max-w-4xl flex items-center flex-wrap mx-auto my-32 lg:my-0 mt-10"
  >
    <!--Main Col-->
    <div
      id="profile"
      class="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none shadow-2xl bg-white opacity-75 mx-6 lg:mx-0"
    >
      <div class="p-4 md:p-12 text-center lg:text-left">
       

        <h1 class="text-3xl font-bold pt-8 lg:pt-0">Muhammad Azril Fathoni</h1>
        <div
          class="mx-auto lg:mx-0 w-4/5 pt-3 border-b-2 border-green-500 opacity-25"
        ></div>
        <p
          class="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"
        >
          <svg
            class="h-4 fill-current text-green-700 pr-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path
              d="M9 12H1v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6h-8v2H9v-2zm0-1H0V5c0-1.1.9-2 2-2h4V2a2 2 0 0 1 2-2h4a2 2 .
			0 0 1 2 2v2h4a2 2 0 0 1 2 2v4h-8v-2zm-4 0H2V5h3v6zm12 0h-3V5h3v6zM7 7h6V5H7v2zm0 4h6v-2H7v2z"
            /></svg
          >5027211003
        </p>
        <p class="pt-8 text-sm">
          Sebagai mahasiswa Teknologi Informasi, saya memiliki minat mendalam di
          bidang keamanan cyber. Saya telah mengasah keterampilan melalui
          kursus, pelatihan, dan memenangkan beberapa lomba Capture The Flag
          (CTF). Memahami konsep pengujian penetrasi, analisis malware, dan
          pemantauan keamanan jaringan, saya memiliki pemahaman yang kuat
          tentang kerentanan dan ancaman dalam lingkungan digital. Saya terus
          bersemangat untuk belajar dan mengembangkan keterampilan untuk
          melindungi data dan sistem dari serangan cyber yang berbahaya.
        </p>

        <div
          class="mt-6 pb-16 lg:pb-0 w-4/5 lg:w-full mx-auto flex flex-wrap items-center space-x-5"
        >
          <a
            class="link"
            href="https://github.com/0xazr"
            data-tippy-content="@github_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>GitHub</title>
              <path
                d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
              /></svg
          ></a>
          <a
            class="link"
            href="https://www.instagram.com/azril.id/"
            data-tippy-content="@instagram_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>Instagram</title>
              <path
                d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"
              /></svg
          ></a>
        </div>
      </div>
    </div>

    <!--Img Col-->
    <div class="w-full lg:w-2/5 mt-10">
      <!-- Big profile image for side bar (desktop) -->
      <img
        src="../assets/azril.jpg" alt="azril"
        class="rounded-none lg:rounded-lg shadow-2xl hidden lg:block"
      />
    </div>
    <!--Main Col-->
    <div class="w-full lg:w-2/5 mt-10">
      <!-- Big profile image for side bar (desktop) -->
      <img
        src="../assets/deya.JPG" alt="deya"
        class="rounded-none lg:rounded-lg shadow-2xl hidden lg:block"
      />
    </div>
    <div
      id="profile"
      class="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none shadow-2xl bg-white opacity-75 mx-6 lg:mx-0"
    >
      <div class="p-4 md:p-12 text-center lg:text-left">
        <!-- Image for mobile view-->
        <!-- <div class="block lg:hidden rounded-full shadow-xl mx-auto -mt-16 h-48 w-48 bg-cover bg-center" >
			<img src="../assets/deya.jpg" alt="deya">
		</div> -->

        <h1 class="text-3xl font-bold pt-8 lg:pt-0">Dhea Arfryza Ananda P.</h1>
        <div
          class="mx-auto lg:mx-0 w-4/5 pt-3 border-b-2 border-green-500 opacity-25"
        ></div>
        <p
          class="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"
        >
          <svg
            class="h-4 fill-current text-green-700 pr-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path
              d="M9 12H1v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6h-8v2H9v-2zm0-1H0V5c0-1.1.9-2 2-2h4V2a2 2 0 0 1 2-2h4a2 2 .
			0 0 1 2 2v2h4a2 2 0 0 1 2 2v4h-8v-2zm-4 0H2V5h3v6zm12 0h-3V5h3v6zM7 7h6V5H7v2zm0 4h6v-2H7v2z"
            /></svg
          >5027211013
        </p>
        <p class="pt-8 text-sm">
          Sebagai mahasiswa Teknologi Informasi, saya memiliki minat kuat di
          pengembangan aplikasi mobile. Saya memiliki pengetahuan dan
          keterampilan dalam bahasa pemrograman Java, Kotlin, dan Swift, serta
          penggunaan Android Studio dan Xcode. Saya telah mengembangkan berbagai
          aplikasi mobile dengan fokus pada antarmuka pengguna yang intuitif dan
          performa yang optimal. Saya mampu menganalisis kebutuhan pengguna,
          merancang arsitektur aplikasi, dan mengimplementasikan fitur-fitur
          yang diinginkan. Saya selalu bersemangat untuk terus belajar dan
          mengikuti tren terbaru dalam pengembangan aplikasi mobile, dengan
          tujuan menciptakan solusi teknologi kreatif dan bermanfaat bagi
          pengguna.
        </p>

        <div
          class="mt-6 pb-16 lg:pb-0 w-4/5 lg:w-full mx-auto flex flex-wrap items-center space-x-5"
        >
          <a
            class="link"
            href="https://github.com/dheaarfryza"
            data-tippy-content="@github_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>GitHub</title>
              <path
                d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
              /></svg
          ></a>
          <a
            class="link"
            href="https://www.instagram.com/dhea.arfryza/"
            data-tippy-content="@instagram_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>Instagram</title>
              <path
                d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"
              /></svg
          ></a>
        </div>
      </div>
    </div>

    <!--Main Col-->
    <div
      id="profile"
      class="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none shadow-2xl bg-white opacity-75 mx-6 lg:mx-0"
    >
      <div class="p-4 md:p-12 text-center lg:text-left">

        <h1 class="text-3xl font-bold pt-8 lg:pt-0">
          Yohannes Hasahatan Tua Alexandro
        </h1>
        <div
          class="mx-auto lg:mx-0 w-4/5 pt-3 border-b-2 border-green-500 opacity-25"
        ></div>
        <p
          class="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"
        >
          <svg
            class="h-4 fill-current text-green-700 pr-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path
              d="M9 12H1v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6h-8v2H9v-2zm0-1H0V5c0-1.1.9-2 2-2h4V2a2 2 0 0 1 2-2h4a2 2 .
			0 0 1 2 2v2h4a2 2 0 0 1 2 2v4h-8v-2zm-4 0H2V5h3v6zm12 0h-3V5h3v6zM7 7h6V5H7v2zm0 4h6v-2H7v2z"
            /></svg
          >5027211022
        </p>
        <p class="pt-8 text-sm">
          Seorang mahasiswa Teknologi Informasi, memiliki pengetahuan dan
          keterampilan yang kuat dalam menganalisis bukti digital untuk
          keperluan investigasi kriminal dan keamanan informasi. Memiliki
          pemahaman yang baik tentang regulasi dan hukum yang terkait dengan
          forensik digital. Memiliki kemampuan untuk bekerja secara teliti dan
          rapi, dan dapat beradaptasi dengan cepat dalam menghadapi situasi yang
          kompleks. Berkomitmen untuk mengembangkan keterampilan saya dalam
          forensik digital dan berperan aktif dalam menjaga keamanan informasi
          yang kritis di era modern ini.
        </p>

        <div
          class="mt-6 pb-16 lg:pb-0 w-4/5 lg:w-full mx-auto flex flex-wrap items-center space-x-5"
        >
          <a
            class="link"
            href="https://github.com/yohanneslex"
            data-tippy-content="@github_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>GitHub</title>
              <path
                d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
              /></svg
          ></a>
          <a
            class="link"
            href="https://www.instagram.com/yohanneslex_/"
            data-tippy-content="@instagram_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>Instagram</title>
              <path
                d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"
              /></svg
          ></a>
        </div>
      </div>
    </div>

    <!--Img Col-->
    <div class="w-full lg:w-2/5 mt-10">
      <!-- Big profile image for side bar (desktop) -->
      <img
        src="../assets/alek.jpg" alt="alek"
        class="rounded-none lg:rounded-lg shadow-2xl hidden lg:block"
      />
    </div>
    <div class="w-full lg:w-2/5 mt-10">
      <!-- Big profile image for side bar (desktop) -->
      <img
        src="../assets/yuni.jpg" alt="yuni"
        class="rounded-none lg:rounded-lg shadow-2xl hidden lg:block"
      />
    </div>
    <!--Main Col-->
    <div
      id="profile"
      class="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none shadow-2xl bg-white opacity-75 mx-6 lg:mx-0"
    >
      <div class="p-4 md:p-12 text-center lg:text-left">
       

        <h1 class="text-3xl font-bold pt-8 lg:pt-0">Midyanisa Yuniar</h1>
        <div
          class="mx-auto lg:mx-0 w-4/5 pt-3 border-b-2 border-green-500 opacity-25"
        ></div>
        <p
          class="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"
        >
          <svg
            class="h-4 fill-current text-green-700 pr-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path
              d="M9 12H1v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6h-8v2H9v-2zm0-1H0V5c0-1.1.9-2 2-2h4V2a2 2 0 0 1 2-2h4a2 2 .
			0 0 1 2 2v2h4a2 2 0 0 1 2 2v4h-8v-2zm-4 0H2V5h3v6zm12 0h-3V5h3v6zM7 7h6V5H7v2zm0 4h6v-2H7v2z"
            /></svg
          >5027211025
        </p>
        <p class="pt-8 text-sm">
          Sebagai seorang mahasiswa Teknologi Informasi dengan minat yang kuat
          di bidang robotik, saya telah bergabung dengan tim robotika kampus
          yang telah memberikan pengalaman berharga dalam merancang, membangun,
          dan mengoperasikan robot. Saya telah berpartisipasi dalam kontes Robot
          Indonesia, di mana tim kami berhasil meraih kemenangan dengan
          kemampuan robot yang inovatif dan efektif. Selama perjalanan ini, saya
          telah mengembangkan keterampilan dalam pemrograman robot, penggunaan
          sensor dan perangkat keras, serta pemecahan masalah dalam lingkungan
          yang dinamis. Saya memiliki keinginan yang besar untuk terus menggali
          lebih dalam di bidang robotik, menerapkan teknologi yang baru dan
          menciptakan solusi yang kreatif untuk tantangan yang dihadapi dalam
          industri ini.
        </p>

        <div
          class="mt-6 pb-16 lg:pb-0 w-4/5 lg:w-full mx-auto flex flex-wrap items-center space-x-5"
        >
          <a
            class="link"
            href="https://github.com/Yuniarrr"
            data-tippy-content="@github_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>GitHub</title>
              <path
                d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
              /></svg
          ></a>
          <a
            class="link"
            href="https://www.instagram.com/mnyuniar_1406/"
            data-tippy-content="@instagram_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>Instagram</title>
              <path
                d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"
              /></svg
          ></a>
        </div>
      </div>
    </div>

    <!--Main Col-->
    <div
      id="profile"
      class="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none shadow-2xl bg-white opacity-75 mx-6 lg:mx-0"
    >
      <div class="p-4 md:p-12 text-center lg:text-left">
       

        <h1 class="text-3xl font-bold pt-8 lg:pt-0">Fina Keiza Arismana</h1>
        <div
          class="mx-auto lg:mx-0 w-4/5 pt-3 border-b-2 border-green-500 opacity-25"
        ></div>
        <p
          class="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"
        >
          <svg
            class="h-4 fill-current text-green-700 pr-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path
              d="M9 12H1v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6h-8v2H9v-2zm0-1H0V5c0-1.1.9-2 2-2h4V2a2 2 0 0 1 2-2h4a2 2 .
			0 0 1 2 2v2h4a2 2 0 0 1 2 2v4h-8v-2zm-4 0H2V5h3v6zm12 0h-3V5h3v6zM7 7h6V5H7v2zm0 4h6v-2H7v2z"
            /></svg
          >5027211028
        </p>
        <p class="pt-8 text-sm">
          Sebagai mahasiswa Teknologi Informasi, memiliki pengetahuan dan
          keterampilan yang mendalam dalam merancang dan mengembangkan aplikasi
          web yang responsif, interaktif, dan estetis. Memiliki pemahaman yang
          kuat tentang HTML, CSS, JavaScript, dan framework web seperti React
          dan Angular. Selama perjalanan, memiliki berbagai proyek web, termasuk
          pembuatan tampilan frontend yang menarik, pengembangan fungsionalitas
          backend, dan integrasi basis data. Memiliki pengalaman dalam bekerja
          dengan Git untuk manajemen versi kode. Memiliki kreativitas dalam
          merancang antarmuka yang responsif guna memenuhi kebutuhan berbisnis
          dan inovasi di era modern.
        </p>

        <div
          class="mt-6 pb-16 lg:pb-0 w-4/5 lg:w-full mx-auto flex flex-wrap items-center space-x-5"
        >
          <a
            class="link"
            href="https://github.com/alweismiau"
            data-tippy-content="@github_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>GitHub</title>
              <path
                d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
              /></svg
          ></a>
          <a
            class="link"
            href="https://www.instagram.com/keizafina/"
            data-tippy-content="@instagram_handle"
            ><svg
              class="h-6 fill-current text-gray-600 hover:text-green-700"
              role="img"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>Instagram</title>
              <path
                d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"
              /></svg
          ></a>
        </div>
      </div>
    </div>

    <!--Img Col-->
    <div class="w-full lg:w-2/5 mt-10">
      <!-- Big profile image for side bar (desktop) -->
      <img
        src="../assets/kei.jpg" alt="kei"
        class="rounded-none lg:rounded-lg shadow-2xl hidden lg:block"
      />
    </div>
  </div>
  <div id="app">
    <section class="bg-white dark:bg-gray-900 my-4">
      <div class="container max-w-4xl px-6 py-10 mx-auto">
        <h1
          class="text-2xl font-semibold text-center text-gray-800 lg:text-3xl dark:text-white"
        >
          SORA
        </h1>
        <div class="mt-12 space-y-8">
          <div
            v-for="(faq, index) in faqs"
            :key="index"
            class="border-2 border-gray-100 rounded-lg dark:border-gray-700"
          >
            <button
              @click="toggleFAQ(index)"
              class="flex items-center justify-between w-full p-8"
            >
              <h1 class="font-semibold text-gray-700 dark:text-white">
                {{ faq.question }}
              </h1>
              <span
                :class="{ 'bg-gray-200': !faq.open, 'bg-blue-500': faq.open }"
                class="text-gray-400 rounded-full"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M18 12H6"
                  />
                </svg>
              </span>
            </button>
            <hr class="border-gray-200 dark:border-gray-700" />
            <p
              v-show="faq.open"
              class="p-8 text-sm text-gray-500 dark:text-gray-300"
            >
              {{ faq.answer }}
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

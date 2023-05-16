<template>
  <div class="bg-slate-50 w-full h-screen">
    <!-- ====== Hero Section Start -->
    <div class="lg:pt-20 bg-blue-100 h-screen">
      <div class="mx-auto ml-20">
        <div class="flex flex-wrap">
          <div class="w-full mx-4 lg:w-1/2">
            <div class="hero-content">
              <h1
                class="text-base font-semibold text-blue-500 text-xl text-primary"
              >
                Hi, Sora here~
              </h1>
              <span
                class="text-dark text-4xl font-bold leading-normal sm:text-[42px] lg:text-[40px] xl:text-[42px]"
              >
                Feel better about <br />
                finding healthcare <br />
              </span>
              <h2 class="font-medium text-slate-500 text-lg mb-5">
                May i help you?
              </h2>
              <p class="text-body-color mb-8 text-base">
                Dengan Sora, menyediakan solusi dan layanan kesehatan berupa,
                rekomendasi rekomendasi obat, alat kesehatan, diet dan nutrisi,
                vitamin, mineral dan suplemen, kebutuhan bayi dan anak, hingga
                perawatan pribadi. Memanfaatkan era digital, kami meluncurkan
                website Sora yang memungkinkan pengguna dengan mudah mengakses
                berbagai macam produk farmasi, perawatan kesehatan, dan
                kecantikan. Melalui layanan ini, pengguna bisa menentukan outlet
                pilihan mereka.
              </p>
              <ul class="flex flex-wrap items-center">
                <li>
                  <a
                    href=""
                    class="bg-sky-400 inline-flex items-center justify-center rounded-lg py-4 px-6 text-center text-base font-normal text-white hover:bg-opacity-90 sm:px-10 lg:px-8 xl:px-10"
                  >
                    About Us
                  </a>
                </li>
              </ul>
              <div class="flex items-center"></div>
            </div>
          </div>

          <div class="lg:ml-auto lg:text-right mr-24">
            <div class="relative z-auto inline-block pt-11 lg:pt-0">
              <img
                src="/src/assets/hospital.jpg"
                alt="hero"
                class="max-w-full lg:ml-auto"
              />
              <span class="absolute top-60 z-10 left-0 -translate-x-1/2">
                <svg
                  width="400"
                  height="400"
                  viewBox="0 0 200 200"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill="#3F83F8"
                    d="M30.8,-37.6C38.1,-30.5,40.9,-19.1,49.1,-4C57.3,11.1,70.9,29.9,67.9,43.2C65,56.4,45.6,64.1,27.9,65.8C10.3,67.5,-5.6,63.3,-18.6,56.3C-31.7,49.4,-41.9,39.7,-53.7,27.2C-65.5,14.6,-79,-0.8,-77,-13.9C-75.1,-26.9,-57.7,-37.6,-42.4,-43.2C-27,-48.9,-13.5,-49.6,-0.9,-48.6C11.7,-47.6,23.5,-44.7,30.8,-37.6Z"
                    transform="translate(100 100)"
                  />
                </svg>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ====== Hero Section End -->

    <!-- ====== Blog Section Start -->
    <form class="pt-20 pb-10">
      <div class="container mx-auto">
        <div class="-mx-4 flex flex-wrap">
          <div class="w-full px-4">
            <div class="mt-14 mx-auto mb-[60px] max-w-[510px] text-center">
              <p class="text-primary mb-2 block text-lg font-semibold">
                Our Website
              </p>
              <h2
                class="text-dark mb-4 text-3xl font-bold sm:text-4xl md:text-[40px]"
              >
                Sora Website
              </h2>
              <p>
                Ada banyak sekali Website yang serupa dengan kami. Akan tetapi,
                website kami berbeda. Dengan Sora, banyak orang bisa menemukan
                solusi dari keluhan mereka menggunakan Speech to Text. Speech to
                Text memanfaatkan transkripsi otomatis yang akan menghemat waktu
                dan usaha yang diperlukan untuk mengetik ulang atau
                menerjemahkan secara manual melalui rekam audio menjadi teks.
              </p>
            </div>
          </div>
        </div>
        <div class="flex flex-wrap">
          <div class="w-full">
            <div class="mx-auto mb-10 max-w-[370px]">
              <div class="mb-8 overflow-hidden rounded">
                <img src="src/assets/anggota.jpg" alt="image" class="w-full" />
              </div>
              <div>
                <span
                  class="bg-primary mb-5 inline-block rounded py-1 px-4 text-center text-xs font-semibold leading-loose text-white"
                >
                  May 13, 2023
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </form>
    <!-- ====== Blog Section End -->

    <!-- ====== Footer Section Start -->

    <div class="container">
      <div class="-mx-4">
        <div class="w-full px-4 sm:w-1/2 lg:w-3/12 text-center mx-auto">
          <div class="mb-10 w-full">
            <h1 class="font-bold text-3xl">Feedback</h1>
            <form>
              <div class="w-full px-4 mb-8 text-justify">
                <label for="name" class="text-base font-bold text-blue-400"
                  >Nama</label
                >
                <input
                  type="text"
                  id="name"
                  class="w-full bg-slate-200 text-black p-3 rounded-md focus:outline-none focus:ring-blue-400 focus:ring-1 focus:border-blue-400"
                />
              </div>
              <div class="w-full px-4 mb-8 text-justify">
                <label for="email" class="text-base font-bold text-blue-400"
                  >Email</label
                >
                <input
                  type="email"
                  id="email"
                  class="w-full bg-slate-200 text-black p-3 rounded-md focus:outline-none focus:ring-blue-400 focus:ring-1 focus:border-blue-400"
                />
              </div>
              <div class="w-full px-4 mb-8 text-justify">
                <label for="message" class="text-base font-bold text-blue-400"
                  >Pesan</label
                >
                <textarea
                  type="email"
                  id="email"
                  class="w-full bg-slate-200 text-black p-3 rounded-md focus:outline-none focus:ring-blue-400 focus:ring-1 focus:border-blue-400"
                ></textarea>
              </div>
              <div class="w-full px-4">
                <button
                  class="text-base font-semibold text-white bg-blue-400 py-3 px-8 rounded-full w-full hover:opacity-80 hover:shadow-lg transition duration-500"
                >
                  Kirim
                </button>
              </div>
            </form>
          </div>
      </div>
    </div>
  </div>
           <!-- footer -->
           <footer class="bg-slate-500 pt-20 pb-12 ">
              <div class="container ">
                <div class="flex flex-warp">
                  <div class="w-full px-4 mb-12 text-slate-300 ">
                    <h4 class="text-dark mb-2 text-lg font-semibold text-center">
                      Find Us On
                    </h4>
                    <p class="text-center mb-9">Institut Teknologi Sepuluh Nopember</p>
                    <div class="mb-6 flex justify-center">
                      <a
                        href=""
                        class="text-dark hover:bg-primary hover:border-primary mr-3 flex h-8 w-8 items-center justify-center rounded-full border border-[#E5E5E5] hover:text-white sm:mr-4 lg:mr-3 xl:mr-4"
                      >
                        <svg
                          width="8"
                          height="16"
                          viewBox="0 0 8 16"
                          class="fill-current"
                        >
                          <path
                            d="M7.43902 6.4H6.19918H5.75639V5.88387V4.28387V3.76774H6.19918H7.12906C7.3726 3.76774 7.57186 3.56129 7.57186 3.25161V0.516129C7.57186 0.232258 7.39474 0 7.12906 0H5.51285C3.76379 0 2.54609 1.44516 2.54609 3.5871V5.83226V6.34839H2.10329H0.597778C0.287819 6.34839 0 6.63226 0 7.04516V8.90323C0 9.26452 0.243539 9.6 0.597778 9.6H2.05902H2.50181V10.1161V15.3032C2.50181 15.6645 2.74535 16 3.09959 16H5.18075C5.31359 16 5.42429 15.9226 5.51285 15.8194C5.60141 15.7161 5.66783 15.5355 5.66783 15.3806V10.1419V9.62581H6.13276H7.12906C7.41688 9.62581 7.63828 9.41935 7.68256 9.10968V9.08387V9.05806L7.99252 7.27742C8.01466 7.09677 7.99252 6.89032 7.85968 6.68387C7.8154 6.55484 7.61614 6.42581 7.43902 6.4Z"
                          />
                        </svg>
                      </a>
                      <a
                        href=""
                        class="text-dark hover:bg-primary hover:border-primary mr-3 flex h-8 w-8 items-center justify-center rounded-full border border-[#E5E5E5] hover:text-white sm:mr-4 lg:mr-3 xl:mr-4"
                      >
                        <svg
                          width="16"
                          height="12"
                          viewBox="0 0 16 12"
                          class="fill-current"
                        >
                          <path
                            d="M14.2194 2.06654L15.2 0.939335C15.4839 0.634051 15.5613 0.399217 15.5871 0.2818C14.8129 0.704501 14.0903 0.845401 13.6258 0.845401H13.4452L13.3419 0.751468C12.7226 0.258317 11.9484 0 11.1226 0C9.31613 0 7.89677 1.36204 7.89677 2.93542C7.89677 3.02935 7.89677 3.17025 7.92258 3.26419L8 3.73386L7.45806 3.71037C4.15484 3.61644 1.44516 1.03327 1.00645 0.587084C0.283871 1.76125 0.696774 2.88845 1.13548 3.59296L2.0129 4.90802L0.619355 4.20352C0.645161 5.18982 1.05806 5.96477 1.85806 6.52838L2.55484 6.99804L1.85806 7.25636C2.29677 8.45401 3.27742 8.94716 4 9.13503L4.95484 9.36986L4.05161 9.93346C2.60645 10.8728 0.8 10.8024 0 10.7319C1.62581 11.7652 3.56129 12 4.90323 12C5.90968 12 6.65806 11.9061 6.83871 11.8356C14.0645 10.2857 14.4 4.41487 14.4 3.2407V3.07632L14.5548 2.98239C15.4323 2.23092 15.7935 1.8317 16 1.59687C15.9226 1.62035 15.8194 1.66732 15.7161 1.6908L14.2194 2.06654Z"
                          />
                        </svg>
                      </a>
                      <a
                        href=""
                        class="text-dark hover:bg-primary hover:border-primary mr-3 flex h-8 w-8 items-center justify-center rounded-full border border-[#E5E5E5] hover:text-white sm:mr-4 lg:mr-3 xl:mr-4"
                      >
                        <svg
                          width="16"
                          height="12"
                          viewBox="0 0 16 12"
                          class="fill-current"
                        >
                          <path
                            d="M15.6645 1.88018C15.4839 1.13364 14.9419 0.552995 14.2452 0.359447C13.0065 6.59222e-08 8 0 8 0C8 0 2.99355 6.59222e-08 1.75484 0.359447C1.05806 0.552995 0.516129 1.13364 0.335484 1.88018C0 3.23502 0 6 0 6C0 6 0 8.79263 0.335484 10.1198C0.516129 10.8664 1.05806 11.447 1.75484 11.6406C2.99355 12 8 12 8 12C8 12 13.0065 12 14.2452 11.6406C14.9419 11.447 15.4839 10.8664 15.6645 10.1198C16 8.79263 16 6 16 6C16 6 16 3.23502 15.6645 1.88018ZM6.4 8.57143V3.42857L10.5548 6L6.4 8.57143Z"
                          />
                        </svg>
                      </a>
                      <a
                        href=""
                        class="text-dark hover:bg-primary hover:border-primary mr-3 flex h-8 w-8 items-center justify-center rounded-full border border-[#E5E5E5] hover:text-white sm:mr-4 lg:mr-3 xl:mr-4"
                      >
                        <svg
                          width="14"
                          height="14"
                          viewBox="0 0 14 14"
                          class="fill-current"
                        >
                          <path
                            d="M13.0214 0H1.02084C0.453707 0 0 0.451613 0 1.01613V12.9839C0 13.5258 0.453707 14 1.02084 14H12.976C13.5432 14 13.9969 13.5484 13.9969 12.9839V0.993548C14.0422 0.451613 13.5885 0 13.0214 0ZM4.15142 11.9H2.08705V5.23871H4.15142V11.9ZM3.10789 4.3129C2.42733 4.3129 1.90557 3.77097 1.90557 3.11613C1.90557 2.46129 2.45002 1.91935 3.10789 1.91935C3.76577 1.91935 4.31022 2.46129 4.31022 3.11613C4.31022 3.77097 3.81114 4.3129 3.10789 4.3129ZM11.9779 11.9H9.9135V8.67097C9.9135 7.90323 9.89082 6.8871 8.82461 6.8871C7.73571 6.8871 7.57691 7.74516 7.57691 8.60323V11.9H5.51254V5.23871H7.53154V6.16452H7.55423C7.84914 5.62258 8.50701 5.08065 9.52785 5.08065C11.6376 5.08065 12.0232 6.43548 12.0232 8.2871V11.9H11.9779Z"
                          />
                        </svg>
                      </a>
                    </div>
                    <p class="text-body-color text-base text-center">&copy; 2023 Sora</p>
                  </div>
                </div>
              </div>
            </footer>
          </div>

  <!-- ====== Footer Section End -->
</template>
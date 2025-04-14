<template>
  <div class="relative w-screen min-h-screen overflow-x-hidden flex flex-col items-center justify-start pt-10 pb-24">
    <div class="floating-shapes">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
    </div>

    <div class="p-6 z-10">

      <vueper-slides
        ref="main"
        :visible-slides="1"
        :bullets="false"
        :arrows="true"
        :touchable="false"
        fixed-height="999px"
        class="rounded-2xl shadow-md w-[999px] mx-auto"
        @slide="$refs.thumbs.goToSlide($event.currentSlide.index, { emit: false })"
      >
        <vueper-slide
          v-for="(project, index) in projects"
          :key="index"
        >
          <template #content>
            <div class="flex flex-col items-center justify-center h-full px-7 text-center">
              <h3 class="text-white text-5xl font-bold mb-10">{{ project.title }}</h3>
              <img
                :src="project.image"
                alt="Project image"
                class="w-[400px] h-[400px] min-w-[400px] min-h-[400px] rounded-lg mb-4 object-cover"
              />
              <p class="text-gray-350 text-2xl mt-10">{{ project.description }}</p>
              <div class="mt-6 flex space-x-4">
                <a :href="project.viewLink" target="_blank">
                  <button class="bg-blue-700 hover:bg-blue-800 text-white rounded-lg text-lg font-semibold px-8 py-4">
                    View
                  </button>
                </a>
                <a :href="project.sourceLink" target="_blank">
                  <button class="bg-gray-700 hover:bg-gray-800 text-white rounded-lg text-lg font-semibold px-8 py-4">
                    Source
                  </button>
                </a>
              </div>
            </div>
          </template>
        </vueper-slide>
      </vueper-slides>

      <vueper-slides
        class="no-shadow thumbnails mt-4"
        ref="thumbs"
        @slide="$refs.main.goToSlide($event.currentSlide.index, { emit: false })"
        :visible-slides="projects.length"
        fixed-height="90px"
        :bullets="false"
        :touchable="false"
        :gap="2.5"
        :arrows="false"
      >
        <vueper-slide
          v-for="(project, i) in projects"
          :key="'thumb-' + i"
          :image="project.image"
          @click.native="$refs.main.goToSlide(i)"
        />
      </vueper-slides>
    </div>
  </div>
</template>

<script setup>
import { VueperSlides, VueperSlide } from 'vueperslides'

const projects = [
  {
    title: 'Bolton Cup',
    description: 'Website for the annual Bolton Cup hockey tournament. It holds game results, player statistics, player profiles, etc., providing fans and participants with up-to-date tournament information and highlights.',
    image: 'https://iiedqecnfyojvubvugmy.supabase.co/storage/v1/object/public/logos/boltoncup.png',
    viewLink: 'https://boltoncup.ca/',  
    sourceLink: 'https://github.com/bolst/BoltonCup'  
  },
  {
    title: 'Exo Explorer',
    description: 'Web app allowing users to freely navigate and explore discovered exoplanets. It allows users to click on planets/exoplanets to access detailed information about each one.',
    image: 'https://xuiksercgzfjbujbeupm.supabase.co/storage/v1/object/public/logos//exoexplorer.jpeg',
    viewLink: 'https://bolst.github.io/ExoExplorer/', 
    sourceLink: 'https://github.com/chrisbolton18/ExoExplorer'
  },
  {
    title: 'Proto Plastics',
    description: 'Custom modern website for a plastic injection molding manufacturing company using C#. Features a responsive UI and includes dedicated pages for About, Machine Specifications, and Contact.',
    image: 'https://protoplastics.ca/proto-logo-white.png',
    viewLink: 'https://protoplastics.ca/',
    sourceLink: 'https://github.com/bolst/Proto-Plastics'
  },
  {
    title: 'Data Structures & Algorithms Tutor',
    description: 'Web app designed to help users visualize and understand various data structures and algorithms. It provides a user-friendly interface for exploring concepts such as arrays, linked lists, and more.',
    image: 'https://xuiksercgzfjbujbeupm.supabase.co/storage/v1/object/public/logos//DSA.jpeg',
    viewLink: 'https://chrisbolton18.github.io/DSA_Visualizer/', 
    sourceLink: 'https://github.com/chrisbolton18/DSA_Visualizer'
  }
]
</script>

<style scoped>
.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
  overflow: hidden;
}

.floating-shapes span {
  position: absolute;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 50%;
  opacity: 0.8;
  animation: float-random 10s infinite alternate ease-in-out;
}

.floating-shapes span:nth-child(1) { width: 80px; height: 80px; left: 5%; top: 10%; animation-duration: 12s; animation-delay: -2s; }
.floating-shapes span:nth-child(2) { width: 100px; height: 100px; left: 40%; top: 50%; animation-duration: 14s; animation-delay: -4s; }
.floating-shapes span:nth-child(3) { width: 60px; height: 60px; left: 70%; top: 30%; animation-duration: 16s; animation-delay: -6s; }
.floating-shapes span:nth-child(4) { width: 90px; height: 90px; left: 25%; top: 75%; animation-duration: 18s; animation-delay: -1s; }
.floating-shapes span:nth-child(5) { width: 70px; height: 70px; left: 85%; top: 80%; animation-duration: 20s; animation-delay: -3s; }
.floating-shapes span:nth-child(6) { width: 50px; height: 50px; left: 15%; top: 40%; animation-duration: 22s; animation-delay: -5s; }
.floating-shapes span:nth-child(7) { width: 120px; height: 120px; left: 60%; top: 10%; animation-duration: 15s; animation-delay: -2.5s; }
.floating-shapes span:nth-child(8) { width: 110px; height: 110px; left: 80%; top: 60%; animation-duration: 17s; animation-delay: -3.5s; }
.floating-shapes span:nth-child(9) { width: 90px; height: 90px; left: 35%; top: 85%; animation-duration: 19s; animation-delay: -1.5s; }
.floating-shapes span:nth-child(10) { width: 130px; height: 130px; left: 50%; top: 90%; animation-duration: 21s; animation-delay: -2.8s; }

@keyframes float-random {
  0% { transform: translateY(0) translateX(0) scale(1); }
  25% { transform: translateY(-40px) translateX(30px) scale(1.1); }
  50% { transform: translateY(40px) translateX(-30px) scale(1); }
  75% { transform: translateY(-20px) translateX(20px) scale(1.2); }
  100% { transform: translateY(20px) translateX(-20px) scale(0.9); }
}

.thumbnails {
  margin: auto;
  max-width: 300px;
}

.thumbnails .vueperslide {
  box-sizing: border-box;
  border: 5px solid #fff;
  transition: 0.3s ease-in-out;
  opacity: 0.7;
  cursor: pointer;
  border-radius: 50%;
  overflow: hidden;
  width: 70px !important;
  height: 70px !important;
}

.thumbnails .vueperslide--active {
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.3);
  opacity: 1;
  border-color: #60a5fa;
}

.thumbnails .vueperslide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

</style>

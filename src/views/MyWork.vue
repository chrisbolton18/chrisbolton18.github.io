<script setup>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

const projects = [
  { 
    title: 'Bolton Cup', 
    image: 'https://iiedqecnfyojvubvugmy.supabase.co/storage/v1/object/public/logos/boltoncup.png', 
    description: 'Website for the annual Bolton Cup hockey tournament. It holds game results, player statistics, player profiles, etc., providing fans and participants with up-to-date tournament information and highlights.', 
    link1: 'https://boltoncup.ca/',  
    link2: 'https://github.com/bolst/BoltonCup' 
  },
  { 
    title: 'Exo Explorer', 
    image: 'img/ExoExplorer.jpeg', 
    description: 'Interactive web app that showcases the planets that the Habitable Worlds Observatory has discovered. Includes an adjusting telescope, planet and exoplanet descriptions, and real-time planet updates.', 
    link1: 'https://bolst.github.io/ExoExplorer/',
    link2: 'https://github.com/chrisbolton18/ExoExplorer'
  },
  { 
    title: 'Data Structures & Algorithms Tutor',
    image: 'img/DSA.jpeg', 
    description: 'Web app designed to help users visualize and understand various data structures and algorithms. It provides a user-friendly interface for exploring concepts such as arrays, linked lists, and more.', 
    link1: 'https://chrisbolton18.github.io/DSA_Visualizer/',
    link2: 'https://github.com/chrisbolton18/DSA_Visualizer'
  }
]
</script>

<template>
  <div class="relative w-screen min-h-screen flex flex-col justify-center items-center text-white px-8 py-16 overflow-hidden animate-fade-in">
    
    <!-- Floating Animated Background -->
    <div class="floating-shapes">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
    </div>

    <vueper-slides class="w-full max-w-6xl h-[800px] flex items-center justify-center bg-red-500" arrows :dragging="false" :touchable="false">
  <vueper-slide v-for="(project, index) in projects" 
    :key="index"
    :title="project.title">
    
    <template #content>
      <div class="flex flex-col items-center text-center h-full w-full px-8 bg-green-500">
        
        <!-- DEBUG TEXT -->
        <p class="text-4xl text-white">TEST CONTENT</p>

        <!-- Project Image -->
        <img :src="project.image" alt="Project Image" class="w-full max-w-lg h-[300px] object-contain rounded-lg shadow-lg">
        
        <!-- Title -->
        <h3 class="text-3xl font-bold mt-6">{{ project.title }}</h3>

        <!-- Description -->
        <p class="text-lg text-gray-300 mt-4 leading-relaxed max-w-2xl">
          {{ project.description }}
        </p>

        <!-- Buttons -->
        <div class="flex gap-6 mt-6">
          <a 
            :href="project.link1"
            target="_blank"
            class="px-5 py-2 bg-blue-500 hover:bg-blue-600 text-white font-semibold text-lg rounded-lg shadow-md transition">
            View
          </a>
          <a 
            :href="project.link2"
            target="_blank"
            class="px-5 py-2 bg-gray-600 hover:bg-gray-700 text-white font-semibold text-lg rounded-lg shadow-md transition">
            Source
          </a>
        </div>

      </div>
    </template>

  </vueper-slide>
</vueper-slides>





  </div>
</template>

<style>
/* Fade-in animation when entering */
.animate-fade-in {
  animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Floating Circles Animation */
.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  min-height: 100vh;
  z-index: -1;
  overflow: hidden;
  pointer-events: none;
}

.floating-shapes span {
  position: absolute;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 50%;
  animation: float-random 5s infinite alternate ease-in-out;
}

/* More Floating Shapes */
.floating-shapes span:nth-child(1) { width: 60px; height: 60px; left: 5%; top: 15%; animation-duration: 6s; }
.floating-shapes span:nth-child(2) { width: 80px; height: 80px; left: 50%; top: 50%; animation-duration: 7s; }
.floating-shapes span:nth-child(3) { width: 50px; height: 50px; left: 80%; top: 25%; animation-duration: 5s; }
.floating-shapes span:nth-child(4) { width: 70px; height: 70px; left: 20%; top: 85%; animation-duration: 9s; }
.floating-shapes span:nth-child(5) { width: 90px; height: 90px; left: 85%; top: 90%; animation-duration: 8s; }
.floating-shapes span:nth-child(6) { width: 50px; height: 50px; left: 30%; top: 40%; animation-duration: 6s; }
.floating-shapes span:nth-child(7) { width: 100px; height: 100px; left: 70%; top: 70%; animation-duration: 7s; }
.floating-shapes span:nth-child(8) { width: 60px; height: 60px; left: 15%; top: 55%; animation-duration: 5s; }
.floating-shapes span:nth-child(9) { width: 75px; height: 75px; left: 90%; top: 10%; animation-duration: 10s; }
.floating-shapes span:nth-child(10) { width: 65px; height: 65px; left: 40%; top: 10%; animation-duration: 8s; }

@keyframes float-random {
  0% { transform: translateY(0) translateX(0) scale(1); opacity: 0.7; }
  50% { transform: translateY(20px) translateX(-20px) scale(1.1); opacity: 0.9; }
  100% { transform: translateY(-20px) translateX(20px) scale(0.9); opacity: 0.6; }
}
</style>

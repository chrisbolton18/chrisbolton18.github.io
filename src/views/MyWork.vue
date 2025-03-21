<script setup>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

const projects = [
  { 
    title: 'Bolton Cup', 
    image: 'https://iiedqecnfyojvubvugmy.supabase.co/storage/v1/object/public/logos/boltoncup.png', 
    description: 'Website for the annual Bolton Cup hockey tournament.', 
    link1: 'https://boltoncup.ca/',  
    link2: 'https://github.com/bolst/BoltonCup' 
  },
  { 
    title: 'Exo Explorer', 
    image: '/img/ExoExplorer.jpeg', 
    description: 'Interactive web app for exoplanets.', 
    link1: 'https://bolst.github.io/ExoExplorer/',
    link2: 'https://github.com/chrisbolton18/ExoExplorer'
  },
  { 
    title: 'Project 3', 
    image: 'https://via.placeholder.com/600x400', 
    description: 'Yet another great project.', 
    link1: 'https://project3.com',
    link2: 'https://example.com/more-info-project3'
  }
]
</script>

<template>
  <div class="w-screen min-h-screen flex flex-col justify-center items-center text-white px-8 pt-12 pb-24">
    <h1 class="text-3xl font-bold mb-12">🔥 My Projects</h1>
    
    <!-- VueperSlides with enforced height -->
    <vueper-slides class="w-full max-w-4xl h-[600px] mx-auto flex items-center justify-center" arrows :dragging="false" :touchable="false">
      <vueper-slide v-for="(project, i) in projects" :key="i">
        <template #content>
          <div class="bg-gray-800 p-8 rounded-lg w-full h-full flex flex-col items-center">
            <h2 class="text-2xl font-bold text-white mb-4">{{ project.title }}</h2>
            <img :src="project.image" :alt="project.title" class="max-w-md h-auto mb-4">
            <p class="text-white mb-4">{{ project.description }}</p>
            <div class="flex space-x-4">
              <a :href="project.link1" target="_blank" class="btn btn-primary">View</a>
              <a :href="project.link2" target="_blank" class="btn btn-secondary">Source</a>
            </div>
          </div>
        </template>
      </vueper-slide>
    </vueper-slides>
  </div>
</template>

<style>
/* 🌟 Fix Slide Height */
.vueperslides {
  min-height: 600px !important;
  max-height: 600px !important;
  height: 600px !important;
  overflow: hidden !important;
}

.vueperslides__track {
  min-height: 600px !important;
  height: 600px !important;
}

.vueperslide {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: transparent !important;
}

/* 🟢 Fix Navigation Arrows */
.vueperslides__arrow {
  background-color: rgba(255, 255, 255, 0.3) !important;
  width: 44px !important;
  height: 44px !important;
  border-radius: 50% !important;
}

.vueperslides__arrow:hover {
  background-color: rgba(255, 255, 255, 0.6) !important;
}

/* 🔵 Fix Bullet Indicators */
.vueperslides__bullets {
  display: flex;
  justify-content: center;
  margin-top: 20px !important;
}

.vueperslides__bullet {
  margin: 0 5px !important;
  padding: 12px !important;
  background-color: rgba(255, 255, 255, 0.2) !important;
}

.vueperslides__bullet--active {
  background-color: rgba(37, 99, 235, 0.8) !important;
}

/* 🔥 Button Styling */
.btn {
  display: inline-block;
  min-width: 120px;
  text-align: center;
  padding: 10px 16px;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 8px;
  transition: 0.3s ease-in-out;
  text-decoration: none;
}

.btn-primary {
  background-color: #2563eb;
  color: white;
}

.btn-primary:hover {
  background-color: #1d4ed8;
}

.btn-secondary {
  background-color: #6b7280;
  color: white;
}

.btn-secondary:hover {
  background-color: #4b5563;
}
</style>

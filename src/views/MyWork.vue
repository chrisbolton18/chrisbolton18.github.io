<script setup>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

// ✅ Confirm the data is correct
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

// 🔥 Log the data in the console
console.log("🔍 Projects Data Loaded:", projects)
</script>

<template>
  <div class="w-screen max-w-8xl min-h-screen flex flex-col justify-center items-center text-white px-8 pt-12 pb-24">
    <!-- 🔥 Debugging Header -->
    <h1 class="text-3xl font-bold">🔥 VueperSlides Debug</h1>

    <vueper-slides class="w-full max-w-8xl h-auto mx-auto justify-center items-center" arrows :dragging="false" :touchable="false">
      <vueper-slide v-for="(project, index) in projects" :key="index" :title="project.title">
        <template #content>
          <div class="flex flex-col items-center text-center p-6">
            <p class="text-4xl text-white">🔥 Content is here!</p>

            <p class="text-lg text-white mt-4">Title: {{ project?.title || '❌ No Title' }}</p>
            <p class="text-lg text-white">Description: {{ project?.description || '❌ No Description' }}</p>

            <img :src="project?.image" 
                alt="Project Image" 
                class="w-full max-w-[700px] h-auto object-contain rounded-lg shadow-lg mt-4">

            <!-- ✅ Adjusted Dots & Buttons Container -->
            <div class="w-full flex flex-col items-center justify-center mt-6 gap-6">
              <div class="vueperslides__bullets"></div> <!-- Dots -->
              
              <div class="flex gap-6">
                <a 
                  :href="project?.link1 || '#'"
                  target="_blank"
                  class="btn btn-primary">
                  View
                </a>
                <a 
                  :href="project?.link2 || '#'"
                  target="_blank"
                  class="btn btn-secondary">
                  Source
                </a>
              </div>
            </div>
          </div>
        </template>
      </vueper-slide>
    </vueper-slides>
  </div>
</template>

<style>
/* 🎨 Animations */
.animate-fade-in {
  animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* 🌐 Floating Background */
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

/* More Floating Circles */
.floating-shapes span:nth-child(1) { width: 60px; height: 60px; left: 5%; top: 15%; animation-duration: 6s; }
.floating-shapes span:nth-child(2) { width: 80px; height: 80px; left: 50%; top: 50%; animation-duration: 7s; }
.floating-shapes span:nth-child(3) { width: 50px; height: 50px; left: 80%; top: 25%; animation-duration: 5s; }
.floating-shapes span:nth-child(4) { width: 70px; height: 70px; left: 20%; top: 85%; animation-duration: 9s; }
.floating-shapes span:nth-child(5) { width: 90px; height: 90px; left: 85%; top: 90%; animation-duration: 8s; }

/* 🎯 Vueper Slides Styles */
.vueperslide {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  height: 100% !important;
  background: transparent !important;
}

.vueperslides__track {
  height: 100% !important;
}

/* 🎯 Fixed Dots Placement */
.vueperslides__bullets {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  margin-bottom: 10px;
}

/* 🎯 Buttons Styling */
.btn {
  display: inline-block;
  min-width: 120px;
  text-align: center;
  padding: 10px 15px;
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

/* 🎯 Spacing Fix */
.vueperslide .flex.gap-6 {
  margin-top: 15px;
  justify-content: center;
  align-items: center;
}
</style>

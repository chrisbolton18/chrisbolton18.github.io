<script setup>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

// ✅ Debugging: Check if component is loaded
console.log("🔥 VueperSlides Component Loaded");

// ✅ Corrected Image URLs
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
    image: 'https://via.placeholder.com/600x400?text=Placeholder+Image',  // ✅ Using a proper placeholder
    description: 'Interactive web app for exoplanets.', 
    link1: 'https://bolst.github.io/ExoExplorer/',
    link2: 'https://github.com/chrisbolton18/ExoExplorer'
  },
  { 
    title: 'Project 3', 
    image: 'https://via.placeholder.com/600x400?text=Placeholder+Image', // ✅ Another valid placeholder
    description: 'Yet another great project.', 
    link1: 'https://project3.com',
    link2: 'https://example.com/more-info-project3'
  }
];

// 🔥 Debug: Log each project and image URL
projects.forEach((project, index) => {
  console.log(`🖼️ Project ${index + 1}:`, project);
  console.log(`🔗 Image URL: ${project.image}`);
});
</script>

<template>
  <div class="w-screen min-h-screen flex flex-col justify-center items-center text-white px-8 pt-12 pb-24">
    <h1 class="text-3xl font-bold mb-12">🔥 My Projects (Debug Mode)</h1>
    
    <!-- VueperSlides set to maximum height (100vh) -->
    <vueper-slides 
      class="w-full max-w-6xl h-screen mx-auto flex items-center justify-center"
      :dragging="false"
      :touchable="false"
      :arrows="false"
      :bullets="true">
      
      <vueper-slide v-for="(project, i) in projects" :key="i">
        <template #content>
          <div class="bg-gray-800 p-8 rounded-lg w-full h-full flex flex-col items-center justify-center">
            <!-- Debug log inside template -->
            <p class="text-white text-sm mb-2">✅ Rendering: {{ project.title }}</p>

            <h2 class="text-2xl font-bold text-white mb-4">{{ project.title }}</h2>

            <!-- Debug: Show image URL -->
            <p class="text-gray-400 text-sm">🔗 {{ project.image }}</p>

            <!-- Debug: Try loading the image -->
            <img :src="project.image" 
                 :alt="project.title"
                 class="max-w-[90%] max-h-[80vh] object-contain rounded-lg shadow-lg mt-4"
                 @error="console.error(`❌ Image failed to load:`, project.image)"
                 @load="console.log(`✅ Image loaded successfully:`, project.image)">

            <p class="text-white mt-4">{{ project.description }}</p>

            <div class="flex space-x-4 mt-4">
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
/* 🌟 Force max height */
.vueperslides {
  height: 90vh !important;
  max-height: 90vh !important;
}

.vueperslides__track {
  height: 100% !important;
}

.vueperslide img {
  max-height: 75vh !important;
}


/* 🎯 Remove Arrows */
.vueperslides__arrow {
  display: none !important;
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

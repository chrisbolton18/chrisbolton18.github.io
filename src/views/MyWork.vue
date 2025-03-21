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

// For debugging
console.log("Projects data loaded:", projects)
</script>

<template>
  <div class="w-screen max-w-8xl min-h-screen flex flex-col justify-center items-center text-white px-8 pt-12 pb-24">
    <h1 class="text-3xl font-bold mb-12">My Projects</h1>
    
    <div class="slider-container w-full max-w-5xl mx-auto relative">
      <vueper-slides
        class="w-full"
        :visible-slides="1"
        :gap="0"
        :bullets="true"
        :arrows="true"
        :dragging-distance="70"
        fixed-height="500px"
        :touchable="true"
        fade
        :autoplay="false">
        
        <vueper-slide 
          v-for="(project, index) in projects" 
          :key="index">
          <template #content>
            <div class="slide-content w-full h-full flex flex-col items-center justify-center px-8 py-12">
              <h2 class="text-3xl font-bold mb-4">{{ project.title }}</h2>
              
              <img 
                :src="project.image" 
                :alt="`${project.title} screenshot`" 
                class="w-full max-w-md h-auto object-contain rounded-lg shadow-lg mb-6"
                @error="$event.target.src = 'https://via.placeholder.com/500x300?text=Image+Not+Found'"
              />
              
              <p class="text-lg mb-8 text-center max-w-2xl">{{ project.description }}</p>
              
              <div class="flex gap-6">
                <a 
                  :href="project.link1" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="btn btn-primary">
                  View Project
                </a>
                <a 
                  :href="project.link2" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="btn btn-secondary">
                  View Source
                </a>
              </div>
            </div>
          </template>
        </vueper-slide>
      </vueper-slides>
    </div>
  </div>
</template>

<style>
/* Reset for VueperSlides */
.vueperslides, .vueperslide {
  overflow: visible !important;
}

/* Base styles */
body {
  background-color: #111827;
}

/* Slider container */
.slider-container {
  position: relative;
}

/* VueperSlides core overrides */
.vueperslides {
  background: transparent !important;
}

.vueperslides__track {
  height: 100% !important;
}

.vueperslide {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background-color: rgba(17, 24, 39, 0.8) !important;
  border-radius: 12px;
  backdrop-filter: blur(8px);
}

/* Slide content */
.slide-content {
  max-width: 100%;
  transition: all 0.3s ease;
}

/* Navigation controls */
.vueperslides__arrow {
  color: white !important;
  background-color: rgba(37, 99, 235, 0.5) !important;
  width: 44px !important;
  height: 44px !important;
  border-radius: 50% !important;
  z-index: 10 !important;
  transition: background-color 0.3s ease !important;
}

.vueperslides__arrow:hover {
  background-color: rgba(37, 99, 235, 0.8) !important;
}

.vueperslides__arrow--prev {
  left: -22px !important;
}

.vueperslides__arrow--next {
  right: -22px !important;
}

/* Bullets */
.vueperslides__bullets {
  position: relative !important;
  margin-top: 20px !important;
  justify-content: center !important;
}

.vueperslides__bullet {
  margin: 0 5px !important;
  padding: 12px !important;
  background-color: rgba(255, 255, 255, 0.2) !important;
  border: none !important;
  transition: background-color 0.3s ease !important;
}

.vueperslides__bullet--active {
  background-color: rgba(37, 99, 235, 0.8) !important;
}

/* Button styles */
.btn {
  display: inline-block;
  min-width: 150px;
  text-align: center;
  padding: 12px 20px;
  font-weight: bold;
  border-radius: 8px;
  transition: all 0.3s ease;
  text-decoration: none;
  letter-spacing: 0.5px;
}

.btn-primary {
  background-color: #2563eb;
  color: white;
}

.btn-primary:hover {
  background-color: #1d4ed8;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.btn-secondary {
  background-color: rgba(107, 114, 128, 0.8);
  color: white;
}

.btn-secondary:hover {
  background-color: #4b5563;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(75, 85, 99, 0.3);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .vueperslides__arrow {
    transform: scale(0.8);
  }
  
  .vueperslides__arrow--prev {
    left: -12px !important;
  }

  .vueperslides__arrow--next {
    right: -12px !important;
  }
  
  .btn {
    min-width: 120px;
    padding: 10px 16px;
  }
}
</style>
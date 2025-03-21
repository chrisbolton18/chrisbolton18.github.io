<template>
  <div class="p-6 flex flex-col items-center mt-40">
    <vueper-slides
      :visible-slides="1"
      :bullets="true"
      :arrows="true"
      :touchable="false"
      fixed-height="999px"
      class="rounded-2xl shadow-md w-[999px] mx-auto"
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
              class="w-[600px] h-[550px] min-w-[600px] min-h-[550px] rounded-lg mb-4 object-cover"
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
    title: 'Data Structures & Algorithms Tutor',
    description: 'Web app designed to help users visualize and understand various data structures and algorithms. It provides a user-friendly interface for exploring concepts such as arrays, linked lists, and more.',
    image: 'https://xuiksercgzfjbujbeupm.supabase.co/storage/v1/object/public/logos//DSA.jpeg',
    viewLink: 'https://chrisbolton18.github.io/DSA_Visualizer/', 
    sourceLink: 'https://github.com/chrisbolton18/DSA_Visualizer'
  }
]

</script>

<style scoped>
</style>


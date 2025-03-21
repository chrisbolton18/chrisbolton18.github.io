<script setup>
import Navbar from './components/Navbar.vue';
</script>

<template>
  <div>
    <Navbar />
    <transition name="fade" mode="out-in">
      <router-view />
    </transition>
  </div>
</template>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.6s ease-in-out, transform 0.6s ease-in-out;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
</style>



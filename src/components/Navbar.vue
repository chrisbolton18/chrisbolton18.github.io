<template>
  <nav class="fixed top-5 left-1/2 transform -translate-x-1/2 w-[70%] bg-transparent backdrop-blur-lg bg-opacity-50 text-white py-6 px-16 flex justify-center items-center rounded-full shadow-lg border border-gray-600">
    <ul class="flex space-x-16 text-2xl font-semibold tracking-wide">
      <li>
        <router-link to="/" class="nav-link">Home</router-link>
      </li>
      <li>
        <router-link to="/about" class="nav-link">About</router-link>
      </li>
      <li>
        <router-link to="/mywork" class="nav-link">My Work</router-link>
      </li>
      <li>
        <router-link to="/contact" class="nav-link">Contact</router-link>
      </li>
    </ul>
  </nav>
</template>

<style>

nav {
  z-index: 50;
  transition: all 0.3s ease-in-out;
}


.nav-link {
  position: relative;
  padding-bottom: 4px;
  transition: color 0.3s ease-in-out;
}


.nav-link::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -4px;
  width: 100%;
  height: 3px;
  background-color: #60a5fa; 
  transform: scaleX(0);
  transition: transform 0.3s ease-in-out;
}

.nav-link:hover {
  color: #60a5fa;
}

.nav-link:hover::after {
  transform: scaleX(1);
}
</style>

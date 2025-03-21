<template>
  <div class="relative w-screen h-screen overflow-hidden">

    <div class="floating-shapes">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
    </div>


    <div class="absolute inset-0 flex flex-col justify-center items-center text-center text-white px-6">
      <h1 class="text-8xl font-extrabold animate-fade-in">Chris Bolton</h1>
      <p class="text-3xl mt-4 text-gray-400 animate-fade-in delay-200">
        Full-Stack Developer || Student at the University of Windsor
      </p>
    </div>
  </div>
</template>


<style>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 1s ease-out forwards;
}


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
  0% {
    transform: translateY(0) translateX(0) scale(1);
  }
  25% {
    transform: translateY(-40px) translateX(30px) scale(1.1);
  }
  50% {
    transform: translateY(40px) translateX(-30px) scale(1);
  }
  75% {
    transform: translateY(-20px) translateX(20px) scale(1.2);
  }
  100% {
    transform: translateY(20px) translateX(-20px) scale(0.9);
  }
}
</style>

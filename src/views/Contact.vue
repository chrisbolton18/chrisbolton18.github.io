<template>
  <div class="relative w-screen min-h-screen flex flex-col justify-center items-center px-4 py-20 text-white overflow-hidden animate-fade-in">
    
    <!-- Floating background (optional) -->
    <div class="floating-shapes">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
    </div>

    <div class="w-full max-w-2xl text-center relative z-10">
      <h2 class="text-5xl font-bold text-blue-400 mb-6">Get In Touch</h2>


      <form class="space-y-6">
        <input 
          type="text" 
          placeholder="Your Name" 
          class="w-full p-4 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500" 
        />
        <input 
          type="email" 
          placeholder="Your Email" 
          class="w-full p-4 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500" 
        />
        <textarea 
          placeholder="Your Message" 
          rows="5"
          class="w-full p-4 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
        ></textarea>
        <button 
          type="submit"
          class="w-full py-3 bg-blue-500 hover:bg-blue-600 text-lg font-semibold rounded-lg transition shadow-md"
        >
          Send Message
        </button>
      </form>
    </div>
  </div>
</template>

<style>
/* Reuse the same fade-in and floating shape styles */
.animate-fade-in {
  animation: fadeIn 1s ease-in-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

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

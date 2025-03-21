<template>
  <div class="relative w-screen min-h-screen flex flex-col justify-center items-center text-white px-8 py-24 lg:py-40 overflow-hidden animate-fade-in">
    
    <!-- Floating Animated Background -->
    <div class="floating-shapes">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
    </div>

    <div class="w-11/12 max-w-6xl text-center space-y-16 relative z-10 mt-5 mb-20">  
      <h2 class="text-5xl font-bold text-blue-400 animate-fade-in">About Me</h2>
      <p class="text-2xl leading-relaxed text-gray-300 animate-fade-in delay-200">
        I am in my third year of studying Computer Science at the University of Windsor,
        where I have learned fundamental topics like data structures and algorithms,
        web development, and database design.
      </p>

      <h2 class="text-5xl font-bold text-blue-400 animate-fade-in">Tech Stack</h2>

      <div class="grid grid-cols-4 gap-10 text-left animate-fade-in delay-800 relative z-10">
        <div class="space-y-20 flex flex-col justify-center">
          <h4 class="text-2xl font-bold text-gray-300">Front-end</h4>
          <h4 class="text-2xl font-bold text-gray-300">Back-end</h4>
          <h4 class="text-2xl font-bold text-gray-300">Tools</h4>
        </div>
        <div class="col-span-3 space-y-16">
          <div class="flex flex-wrap justify-center gap-8">
            <div class="tech-icon"><img src="/icons/html.svg" alt="HTML5" /><p>HTML5</p></div>
            <div class="tech-icon"><img src="/icons/css.svg" alt="CSS3" /><p>CSS3</p></div>
            <div class="tech-icon"><img src="/icons/javascript.svg" alt="JavaScript" /><p>JavaScript</p></div>
            <div class="tech-icon"><img src="/icons/react.svg" alt="React.js" /><p>React.js</p></div>
            <div class="tech-icon"><img src="/icons/vue.svg" alt="Vue.js" /><p>Vue.js</p></div>
            <div class="tech-icon"><img src="/icons/tailwind.svg" alt="TailwindCSS" /><p>TailwindCSS</p></div>
            <div class="tech-icon"><img src="/icons/typescript.svg" alt="TypeScript" /><p>TypeScript</p></div>
          </div>
          <div class="flex flex-wrap justify-center gap-8">
            <div class="tech-icon"><img src="/icons/python.svg" alt="Python" /><p>Python</p></div>
            <div class="tech-icon"><img src="/icons/cpp.svg" alt="C++" /><p>C++</p></div>
            <div class="tech-icon"><img src="/icons/java.svg" alt="Java" /><p>Java</p></div>
            <div class="tech-icon"><img src="/icons/nodejs.svg" alt="Node.js" /><p>Node.js</p></div>
            <div class="tech-icon"><img src="/icons/dotnet.svg" alt=".NET" /><p>.NET</p></div>
            <div class="tech-icon"><img src="/icons/php.svg" alt="PHP" /><p>PHP</p></div>
            <div class="tech-icon"><img src="/icons/mysql.svg" alt="MySQL" /><p>MySQL</p></div>
          </div>
          <div class="flex flex-wrap justify-center gap-8">
            <div class="tech-icon"><img src="/icons/git.svg" alt="Git" /><p>Git</p></div>
            <div class="tech-icon"><img src="/icons/github.svg" alt="GitHub" /><p>GitHub</p></div>
            <div class="tech-icon"><img src="/icons/figma.svg" alt="Figma" /><p>Figma</p></div>
            <div class="tech-icon"><img src="/icons/uml.svg" alt="UML" /><p>UML</p></div>
            <div class="tech-icon"><img src="/icons/docker.svg" alt="Docker" /><p>Docker</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Fix vertical alignment */
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

/* Floating Circles Positions */
.floating-shapes span:nth-child(1) { width: 60px; height: 60px; left: 5%; top: 15%; animation-duration: 6s; }
.floating-shapes span:nth-child(2) { width: 80px; height: 80px; left: 50%; top: 50%; animation-duration: 7s; }
.floating-shapes span:nth-child(3) { width: 50px; height: 50px; left: 80%; top: 25%; animation-duration: 5s; }
.floating-shapes span:nth-child(4) { width: 70px; height: 70px; left: 20%; top: 85%; animation-duration: 9s; }
.floating-shapes span:nth-child(5) { width: 90px; height: 90px; left: 85%; top: 90%; animation-duration: 8s; }

@keyframes float-random {
  0% { transform: translateY(0) translateX(0) scale(1); opacity: 0.7; }
  50% { transform: translateY(20px) translateX(-20px) scale(1.1); opacity: 0.9; }
  100% { transform: translateY(-20px) translateX(20px) scale(0.9); opacity: 0.6; }
}

/* Fix icon alignment */
.tech-icon {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s ease-in-out;
  width: 90px;
}
.tech-icon img {
  width: 50px;
  height: 50px;
  filter: brightness(0) invert(1);
}
.tech-icon p {
  margin-top: 8px;
  font-size: 1rem;
  color: #ffffff;
  opacity: 0.8;
  text-align: center;
}
</style>

<template>
  <div class="relative w-screen min-h-screen flex flex-col justify-center items-center text-white px-8 py-16 overflow-hidden">
    
    <div class="floating-shapes">
      <span></span><span></span><span></span><span></span><span></span>
      <span></span><span></span><span></span><span></span><span></span>
    </div>

      


    <div class="w-11/12 max-w-6xl text-center space-y-8 relative z-10">  
      <br>
      <br>
      <br>
      <br>
      <h2 class="text-5xl font-bold text-blue-400 animate-fade-in mb-6">About Me</h2>
      <br>
      <p class="text-2xl leading-relaxed text-gray-300 animate-fade-in delay-200 mb-6">
        I am in my third year of studying Computer Science at the University of Windsor,
        where I have learned fundamental topics like data structures and algorithms,
        web development, and database design.
      </p>

      <br>
      <br>
      <br>
      <br>

      <h2 class="text-5xl font-bold text-blue-400 animate-fade-in mb-6">Tech Stack</h2>

      <br>
      <br>

      <div class="grid grid-cols-4 gap-10 text-left mt-8 animate-fade-in delay-800 relative z-10">
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
            <div class="tech-icon"><img src="/icons/dotnet.svg" alt="Dotnet" /><p>.Net</p></div>
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
  background: rgba(255, 255, 255, 0.08);
  border-radius: 50%;
  animation: float-random 3s infinite alternate ease-in-out;
}

.floating-shapes span:nth-child(1) { width: 60px; height: 60px; left: 5%; top: 15%; animation-duration: 6s; }
.floating-shapes span:nth-child(2) { width: 80px; height: 80px; left: 50%; top: 50%; animation-duration: 7s; }
.floating-shapes span:nth-child(3) { width: 50px; height: 50px; left: 80%; top: 25%; animation-duration: 5s; }
.floating-shapes span:nth-child(4) { width: 70px; height: 70px; left: 20%; top: 85%; animation-duration: 9s; }
.floating-shapes span:nth-child(5) { width: 90px; height: 90px; left: 85%; top: 90%; animation-duration: 8s; }

@keyframes float-random {
  0% { transform: translateY(0) translateX(0) scale(1); }
  50% { transform: translateY(20px) translateX(-20px) scale(1.1); }
  100% { transform: translateY(-20px) translateX(20px) scale(0.9); }
}



@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in { animation: fade-in 1s ease-out forwards; }

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}

.animate-float {
  animation: float 6s infinite ease-in-out;
}

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

.tech-icon:hover {
  transform: scale(1.1);
}
</style>

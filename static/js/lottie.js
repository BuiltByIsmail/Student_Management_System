document.addEventListener("DOMContentLoaded", function () {
  particlesJS("particles-js", {
    particles: {
      number: { value: 120, density: { enable: true, value_area: 1000 } },
      color: { value: ["#00ffea", "#ff00c8", "#00ff73"] }, // neon colors
      shape: { type: "circle" },
      opacity: { value: 0.8, random: true },
      size: { value: 4, random: true },
      line_linked: {
        enable: true,
        distance: 150,
        color: "#ffffff",
        opacity: 0.3,
        width: 1
      },
      move: {
        enable: true,
        speed: 2,
        direction: "none",
        random: true,
        straight: false,
        out_mode: "out"
      }
    },
    interactivity: {
      detect_on: "canvas",
      events: {
        onhover: { enable: true, mode: "grab" }, // connect particles on hover
        onclick: { enable: true, mode: "push" },
        resize: true
      },
      modes: {
        grab: { distance: 200, line_linked: { opacity: 0.6 } },
        push: { particles_nb: 5 }
      }
    },
    retina_detect: true
  });
});
// Lottie Animation Setup
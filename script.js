const root = document.documentElement;

// Gradient scroll
window.addEventListener("scroll", () => {
  const max = document.body.scrollHeight - window.innerHeight;
  const progress = window.scrollY / max;

  const c1 = 210 + progress * 60;
  const c2 = 260 + progress * 80;

  root.style.setProperty("--c1", c1.toFixed(1));
  root.style.setProperty("--c2", c2.toFixed(1));
});

// Scroll-trigger cards
const cards = document.querySelectorAll(".card");

const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);

cards.forEach(card => observer.observe(card));

// Roulette text
const rouletteTexts = ["Flexible", "Convenient", "Thoughtful"];
const rouletteSpan = document.querySelector(".roulette-text");
let idx = 0;

setInterval(() => {
  idx = (idx + 1) % rouletteTexts.length;
  rouletteSpan.style.opacity = 0;
  setTimeout(() => {
    rouletteSpan.textContent = rouletteTexts[idx];
    rouletteSpan.style.opacity = 1;
  }, 400); // matches CSS transition
}, 1000);

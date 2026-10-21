import './languages.js';
import './sizes.js';
import './reader.css';
import './pageturn.css';

const edition = window.EDITIONS.find(item => item.lang === document.documentElement.lang);
const story = document.createElement('script');
story.src = edition?.story || 'story-it.js';
story.onload = () => import('./reader.js');
story.onerror = () => {
  const desk = document.querySelector('.desk');
  desk.classList.add('drawn');
  desk.textContent = 'Impossibile caricare il libro. Ricarica la pagina per riprovare.';
};
document.head.append(story);

const form = document.getElementById('contactForm');
const note = document.getElementById('formNote');

form.addEventListener('submit', event => {
  event.preventDefault();
  note.className = 'form-note';
  note.replaceChildren('L’invio non è attivo su questa versione italiana. Per contattare gli autori, usa ');
  const original = document.createElement('a');
  original.href = 'https://www.frogandtoad.ai/contact.html';
  original.target = '_blank';
  original.rel = 'noopener noreferrer';
  original.textContent = 'il modulo del sito originale';
  note.append(original, '.');
});

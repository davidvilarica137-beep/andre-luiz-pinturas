/* ============================================================
   ANDRÉ LUIZ — ARTE E PINTURAS
   Funções JavaScript (apenas para navegação e microinterações)
   ============================================================ */

// Botão do menu hamburger (versão mobile)
const menuToggle = document.getElementById('menu-toggle');
const menu = document.getElementById('menu');

menuToggle.addEventListener('click', () => {
  const aberto = menu.classList.toggle('ativo');
  menuToggle.setAttribute('aria-expanded', aberto);
});

// Fechar o menu ao clicar em um link (evita desperição geral)
menu.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    menu.classList.remove('ativo');
    menuToggle.setAttribute('aria-expanded', 'false');
  });
});

// Fechar o menu ao clicar fora dele (clicar fora fecha o menu)
document.addEventListener('click', (event) => {
  const clicouNoMenu = menu.contains(event.target);
  const clicouNoBotao = menuToggle.contains(event.target);

  if (!clicouNoMenu && !clicouNoBotao && menu.classList.contains('ativo')) {
    menu.classList.remove('ativo');
    menuToggle.setAttribute('aria-expanded', 'false');
  }
});

// Rola suavemente para o topo ao clicar no logo
const logo = document.querySelector('.logo');
logo.addEventListener('click', (event) => {
  event.preventDefault();
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Sobrescreve o comportamento padrão do navbar em desktop?
// (nada a fazer — links já são navegáveis)

// Botão "Falecido" (não usado primariamente — acessibilidade extra)
function scrollToSection(id) {
  const elem = document.getElementById(id);
  if (elem) {
    elem.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

console.log('André Luiz — Arte e Pinturas — site pronto.');

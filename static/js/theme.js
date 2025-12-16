// Função para alternar o tema claro/escuro
function toggleTheme() {
    // Pega o valor atual do atributo 'data-theme' no elemento <html>
    const currentTheme = document.documentElement.getAttribute('data-theme');
    
    // Define o novo tema
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    // Aplica o novo tema ao elemento <html>
    document.documentElement.setAttribute('data-theme', newTheme);
    
    // Salva a preferência do usuário no armazenamento local (localStorage)
    localStorage.setItem('theme', newTheme);
}

// Aplica o tema salvo ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    // Tenta carregar o tema do localStorage, se não houver, usa 'light'
    const savedTheme = localStorage.getItem('theme') || 'light';
    
    // Aplica o tema carregado ao elemento <html>
    document.documentElement.setAttribute('data-theme', savedTheme);
});
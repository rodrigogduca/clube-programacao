# 🚀 Portal do Clube de Programação - SENAI CIMATEC

> Uma plataforma web moderna e interativa desenvolvida para conectar estudantes e entusiastas de tecnologia.

![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-5.0+-green)

## 📖 Sobre o Projeto

Este projeto consiste em um sistema web desenvolvido com **Django** (Python) focado na apresentação e gestão do **Clube de Programação do SENAI CIMATEC**. 

O objetivo foi criar uma Landing Page de alto impacto visual, com design responsivo, animações modernas e um sistema de temas (Dark/Light Mode), servindo como porta de entrada para novos membros e divulgação de trilhas de aprendizado.

## ✨ Funcionalidades Principais

* **🎨 UI/UX Moderna:** Design responsivo com CSS Grid e Flexbox, adaptável para mobile e desktop.
* **🌗 Dark/Light Mode:** Sistema de troca de tema com persistência de dados (salva a preferência do usuário).
* **✨ Scroll Reveal:** Animações suaves de aparecimento de elementos ao rolar a página.
* **🐍 Backend Robusto:** Estrutura MVC (Model-View-Template) utilizando o framework Django.
* **📱 Componentes Interativos:** Menu mobile, cards informativos e botões com feedback visual.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3 (Variáveis CSS, Grid, Flexbox), JavaScript (Vanilla)
* **Ferramentas:** VS Code, Git
* **Design:** Ícones via Google Material Symbols

## 📸 Capturas de Tela (Screenshots)

*(Aqui você pode colocar um print da sua tela. Sugestão: Tire um print do site e cole aqui ou salve na pasta do projeto)*

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o projeto na sua máquina:

### Pré-requisitos
* Python instalado
* Git instalado

### Passo a passo

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/SEU-USUARIO/site_clube.git](https://github.com/SEU-USUARIO/site_clube.git)
    cd site_clube
    ```

2.  **Crie e ative um ambiente virtual**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install django
    ```

4.  **Execute as migrações**
    ```bash
    cd sistema
    python manage.py migrate
    ```

5.  **Inicie o servidor local**
    ```bash
    python manage.py runserver
    ```

6.  **Acesse o projeto**
    Abra o navegador e visite: `http://127.0.0.1:8000/`

## 📚 Aprendizados

Este projeto faz parte da minha jornada de aprendizado em desenvolvimento Fullstack, onde explorei:
* Configuração de ambiente Django do zero.
* Gerenciamento de Arquivos Estáticos (CSS/JS) no Django.
* Manipulação do DOM com JavaScript.
* Boas práticas de organização de pastas e estrutura MVT.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---
Desenvolvido com 💙 por Rodrigo Gandarela

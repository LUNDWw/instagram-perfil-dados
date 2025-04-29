# Instagram OSINT

Este projeto é uma ferramenta de coleta de informações (OSINT) focada no Instagram, utilizando duas abordagens diferentes: `instaloader` e `selenium`. O usuário pode escolher entre os métodos para obter dados públicos de perfis, como biografia, links e estatísticas (seguidores, seguindo e número de publicações).

## Funcionalidades

- Coleta de nome completo, biografia, número de seguidores, seguindo e publicações (via Instaloader)
- Extração de links da biografia e verificação se estão ativos
- Acesso ao perfil pelo navegador Brave (via Selenium)
- Coleta visual dos dados do perfil mesmo se privado (limitado a informações públicas visíveis sem login)

---

## 📦 Requisitos

Antes de tudo, tenha certeza que você tem o Python instalado (recomendado Python 3.8+).

### Instale as bibliotecas necessárias:

```bash
pip install instaloader selenium requests webdriver-manager
```

### Instale o Brave Browser:

Você precisa ter o Brave instalado. Faça o download aqui:  
[https://brave.com/pt-br/download/](https://brave.com/pt-br/download/)

### Instale o Visual C++ (Windows somente):

Caso esteja no Windows e ocorra erro na instalação do Selenium, instale o Build Tools:  
[https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

---

## ▶️ Como usar

1. Abra o terminal (ou o VSCode)
2. Execute o script com `python nome_do_arquivo.py`
3. Digite o nome de usuário do Instagram quando solicitado
4. Escolha o método de coleta (1 = Instaloader, 2 = Selenium)
5. Visualize os dados retornados

---

## ⚠️ Observações

- Perfis privados só mostrarão a biografia e dados visíveis sem login (no método Selenium).
- A extração de e-mails e dados privados não é possível sem autenticação...ainda
- Esse projeto é apenas para fins educacionais. Respeite a privacidade dos usuários.

---

## 💻 Compatibilidade

- Windows: ✅
- Linux/Mac: ✅ (ajustando o caminho do Brave no script)
  - Exemplo de caminho do Brave no Linux: `/usr/bin/brave-browser`
  - Você pode alterar isso na linha:

```python
options.binary_location = 'CAMINHO_PARA_O_BRAVE'
```

---

## 📂 Créditos

Criado por um estudante de Sistema de informação explorando a prática de OSINT com Python 

# Instruções para Subir o Projeto para o GitHub

Olá! Aqui estão as instruções para colocar seu projeto de análise de dados de hospedagem de Seattle no seu perfil do GitHub. Isso é ótimo para criar um portfólio!

Existem duas situações principais:

1.  **Você ainda NÃO tem um repositório criado no GitHub para este projeto.**
2.  **Você JÁ tem um repositório criado e quer apenas atualizar os arquivos.**

Siga os passos correspondentes à sua situação.

## Situação 1: Criando um Novo Repositório no GitHub

Se você ainda não tem um lugar no GitHub para este projeto, siga estes passos:

1.  **Acesse o GitHub:** Faça login na sua conta em [github.com](https://github.com).
2.  **Crie um Novo Repositório:**
    *   No canto superior direito, clique no sinal de `+` e selecione "New repository".
    *   **Nome do Repositório:** Escolha um nome (ex: `seattle-lodging-analysis` ou `projeto-hospedagem-seattle`).
    *   **Descrição (Opcional):** Adicione uma breve descrição do projeto.
    *   **Público/Privado:** Escolha se o repositório será público (visível para todos) ou privado.
    *   **Inicializar (Importante):** **NÃO** marque as opções "Add a README file", "Add .gitignore" ou "Choose a license" por enquanto. Vamos adicionar os arquivos que já preparamos.
    *   Clique em "Create repository".
3.  **Prepare seus Arquivos Localmente:**
    *   Certifique-se de que você tem a pasta `seattle-lodging` com todos os arquivos organizados (dados, notebooks, README.md, environment.yml) e também o arquivo `analise_notebook.md` que preparei para você.
4.  **Faça o Upload dos Arquivos (Método Simples - Upload via Web):**
    *   Na página do seu repositório recém-criado no GitHub, você verá algumas opções. Clique no link "uploading an existing file".
    *   Arraste a pasta `seattle-lodging` inteira e o arquivo `analise_notebook.md` para a área de upload do GitHub.
    *   **Alternativa:** Se arrastar a pasta não funcionar bem, entre na pasta `seattle-lodging` no seu computador. No GitHub, clique em "Add file" > "Upload files". Arraste os arquivos `README.md` e `environment.yml` para lá. Depois, clique em "Add file" > "Create new file", digite `data/` no nome do arquivo (isso cria a pasta) e então faça o upload do `dados_hospedagem.json` para dentro dela. Repita o processo para `notebooks/` e faça upload dos arquivos `.ipynb` lá dentro. Por fim, faça upload do `analise_notebook.md` na raiz.
    *   Aguarde o upload terminar.
    *   **Commit:** Na parte de baixo da página, escreva uma mensagem curta descrevendo o que você está fazendo (ex: "Adiciona arquivos iniciais do projeto de análise de hospedagem").
    *   Clique em "Commit changes".
5.  **Pronto!** Seus arquivos estarão no GitHub.

**(Método Avançado - Usando Git no Terminal - Opcional)**

Se você tem o Git instalado e prefere usar a linha de comando:

1.  Abra o terminal ou prompt de comando.
2.  Navegue até a pasta que contém a pasta `seattle-lodging` e o arquivo `analise_notebook.md`.
3.  Copie a pasta `seattle-lodging` e o arquivo `analise_notebook.md` para um novo diretório que será seu repositório local (ex: `meu-projeto-github`).
4.  Entre nesse novo diretório: `cd meu-projeto-github`
5.  Inicialize o Git: `git init`
6.  Adicione os arquivos: `git add .`
7.  Faça o commit: `git commit -m "Commit inicial do projeto de análise de hospedagem"`
8.  Conecte seu repositório local ao repositório remoto do GitHub (substitua `<seu-usuario>` e `<nome-repositorio>` pelos seus dados - você encontra o link na página do GitHub após criar o repositório):
    `git remote add origin https://github.com/<seu-usuario>/<nome-repositorio>.git`
9.  Defina o branch principal (geralmente `main`):
    `git branch -M main`
10. Envie os arquivos para o GitHub:
    `git push -u origin main`

## Situação 2: Atualizando um Repositório Existente

Se você já tem um repositório no GitHub para este projeto:

1.  **Faça o Download (Clone) do seu Repositório (se ainda não tiver localmente):**
    *   Vá para a página do seu repositório no GitHub.
    *   Clique no botão verde "<> Code".
    *   Copie a URL HTTPS.
    *   No terminal, use: `git clone <URL_copiada>`
2.  **Substitua/Adicione os Arquivos:**
    *   Copie os arquivos da pasta `seattle-lodging` que preparei (e o `analise_notebook.md`) para dentro da pasta do seu repositório local que você clonou, substituindo os arquivos antigos se necessário.
3.  **Use o Git para Atualizar (Terminal):**
    *   Abra o terminal na pasta do seu repositório local.
    *   Verifique o status: `git status` (mostrará os arquivos modificados/adicionados).
    *   Adicione as mudanças: `git add .`
    *   Faça o commit: `git commit -m "Atualiza projeto com análise e notebook revisado"` (ou outra mensagem descritiva).
    *   Envie as mudanças para o GitHub: `git push`
4.  **Alternativa (Upload via Web):**
    *   Navegue até os arquivos no seu repositório no GitHub.
    *   Para cada arquivo que mudou, clique nele, depois clique no ícone de lápis (editar) ou nos três pontinhos e "Upload new version". Faça o upload do arquivo atualizado.
    *   Para arquivos novos (como `analise_notebook.md`), use "Add file" > "Upload files".

---

Espero que estas instruções ajudem! Ter seus projetos no GitHub é um passo importante na carreira de ciência de dados. Se tiver qualquer dúvida, pode perguntar.

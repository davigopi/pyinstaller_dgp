
---------------------------------------------------------
# CÓDIGO pyinstaller_dgp
---------------------------------------------------------
Script de automação interativa para compilação e empacotamento de aplicações Python em executáveis (.exe) utilizando PyInstaller.

### Problema de Negócio
A criação manual de executáveis via PyInstaller exige a digitação repetitiva de comandos complexos no terminal, além da inclusão manual de pastas de recursos, ícones e parâmetros de diretório, gerando margem para erros de configuração e lentidão no fluxo de build.

### Tecnologias Utilizadas
- **Linguagem:** Python
- **Frameworks/Libs:** PyInstaller / Subprocess / OS / Sys
- **Banco de Dados:** N/A

### Funcionalidades Principais
- [x] Verificação e instalação automática do PyInstaller via pip caso não esteja presente no ambiente
- [x] Mapeamento inteligente do diretório local para detecção de script principal, assets/pastas e arquivos de ícone (.ico/.png)
- [x] Interface CLI interativa para personalização do nome do executável, modo de compilação (--onefile / --onedir) e exibição do terminal (--console / --noconsole)
- [x] Organização estruturada dos diretórios de saída (dist, build e spec) dentro de uma pasta isolada com prefixo do projeto

---------------------------------------------------------
## 📋 Sumário
---------------------------------------------------------
1. [ESTRUTURA DA PASTA DO PROJETO LOCAL](#1-ESTRUTURA-DA-PASTA-DO-PROJETO-LOCAL)
2. [PUBLICAR NO GITHUB](#2-PUBLICAR-NO-GITHUB)
3. [INSTALAR E ATUALIZAÇÕES](#3-INSTALAR-E-ATUALIZAÇÕES)
4. [COMO USAR NOS SEUS PROJETOS](#4-COMO-USAR-NOS-SEUS-PROJETOS)
5. [EXEMPLOS DE CÓDIGO DE COMO UTILIZAR](#5-EXEMPLOS-DE-CÓDIGO-DE-COMO-UTILIZAR)

---------------------------------------------------------
## 1. ESTRUTURA DA PASTA DO PROJETO LOCAL
---------------------------------------------------------
Crie uma pasta com o nome pyinstaller_dgp e coloque os dois arquivos dentro dela:
```
pyinstaller_dgp/
    ├── pyinstaller_dgp.py
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE (Opcional)
    ├── .gitignore
    ├── .editorconfig
    ├── requirements-dev.txt
    └── CHANGELOG.md
```
---------------------------------------------------------
## 2. PUBLICAR NO GITHUB
---------------------------------------------------------
Repositório público ou privado no GitHub com o nome pyinstaller_dgp.

URL do repositório: https://github.com/davigopi/pyinstaller_dgp

---------------------------------------------------------
## 3. INSTALAR E ATUALIZAÇÕES
---------------------------------------------------------

Abra o terminal do seu computador, ative o ambiente virtual e, no diretório do repositório pyinstaller_dgp, execute

### A) INSTALAR A FERRAMENTA NO COMPUTADOR
```bash
pip install git+https://github.com/davigopi/pyinstaller_dgp.git
```

### B) ATUALIZAR A FERRAMENTA NO FUTURO

Alterado a version em pyproject.toml:
```bash
pip install --upgrade git+https://github.com/davigopi/pyinstaller_dgp.git
```
Força a atualização:
```bash
pip install --force-reinstall git+https://github.com/davigopi/pyinstaller_dgp.git
```
```bash
pip install --upgrade --no-cache-dir git+https://github.com/davigopi/pyinstaller_dgp.git
```

### C) INSTALAR REQUIREMENTS APENAS SE ERROS

```bash
pip install -r venv\Lib\site-packages\pyinstaller_dgp\requirements.txt
```
---------------------------------------------------------
## 4. COMO USAR NOS SEUS PROJETOS
---------------------------------------------------------
- Via terminal (em qualquer pasta de projeto React Native, Python, etc.):
  Basta abrir o terminal na pasta desejada e digitar:
```bash
python -m pyinstaller_dgp
```


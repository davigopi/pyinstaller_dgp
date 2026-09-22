# flake8: noqa
import os
import subprocess
import sys
from typing import List, Optional, Tuple


def instalar_pyinstaller() -> None:
    """Garante que o PyInstaller está instalado no ambiente em execução."""
    print(f"{50*'='}\n[1/5] Verificando / Instalando PyInstaller \n{50*'='}\n{40*' '}SAIR ( X )")
    try:
        import PyInstaller  # type: ignore # noqa: F401

        print("-> PyInstaller já está instalado.")
    except ImportError:
        print("-> PyInstaller não encontrado. Instalando via pip...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "pyinstaller"]
        )
        print("-> PyInstaller instalado com sucesso!")


def mapear_pastas_e_arquivos(
    diretorio_atual: str,
) -> Tuple[str, List[str], Optional[str]]:
    """Analisa a pasta local e identifica pastas, arquivo .py principal e ícone."""
    print(f"\n{50*'='}\n[2/5] Analisando o diretório: {diretorio_atual} \n{50*'='}\n{40*' '}SAIR ( X )")

    pastas_ignoradas = {
        "build",
        "dist",
        "__pycache__",
        ".git",
        ".vscode",
        "venv",
        "env",
        ".idea",
    }
    pastas_encontradas: List[str] = []
    arquivos_py: List[str] = []
    icone_encontrado: Optional[str] = None

    try:
        itens = os.listdir(diretorio_atual)
    except PermissionError as err:
        print(f"Erro de permissão ao ler diretório: {err}")
        sys.exit(1)

    for item in itens:
        caminho_completo = os.path.join(diretorio_atual, item)

        # Ignora arquivos de controle interno
        if item.startswith("_"):
            continue

        if os.path.isdir(caminho_completo) and item not in pastas_ignoradas:
            pastas_encontradas.append(item)

        elif os.path.isfile(caminho_completo):
            if item.endswith(".py"):
                arquivos_py.append(item)
            elif item.endswith(".ico") or item.endswith(".png"):
                if not icone_encontrado or item.endswith(".ico"):
                    icone_encontrado = caminho_completo

    # Identificação do script principal
    if "main.py" in arquivos_py:
        script_principal = "main.py"
    elif arquivos_py:
        script_principal = arquivos_py[0]
    else:
        while True:
            print("""Nenhum arquivo .py encontrado no escaneamento. 
                  Digite o nome do script principal (ex: app.py): """
            )
            input_strip = input('-> ').strip()
            if input_strip == "x":
                sys.exit()
            if input_strip and os.path.isfile(
                os.path.join(diretorio_atual, input_strip)
            ):
                script_principal = input_strip
                break
            print(
                f"Erro: O arquivo '{input_strip}' não foi encontrado no diretório atual. Tente novamente."
            )

    print(f"-> Script principal identificado: {script_principal}")
    print(f"-> Pastas mapeadas para include: {pastas_encontradas}")
    if icone_encontrado:
        print(f"-> Ícone detectado: {os.path.basename(icone_encontrado)}")

    return script_principal, pastas_encontradas, icone_encontrado


def obter_configuracoes_usuario(
    script_principal: str,
) -> Tuple[str, str, str]:
    """Interage com o usuário para obter preferências de compilação."""
    nome_padrao = os.path.splitext(script_principal)[0]

    print(f"\n{50*'='}\n[3/5] Nome do Executável \n{50*'='}\n{40*' '}SAIR ( X )")
    
    print(f"Deseja que o .exe se chame '{nome_padrao}'? [S/n]: ")
    input_strip = (
        input('-> ')
        .strip()
        .lower()
    )
    if input_strip == "x":
        sys.exit()
    elif input_strip in ["", "s", "sim"]:
        nome_exe = nome_padrao
    else:
        while True:
            print("Digite o nome desejado para o .exe: ")
            input_strip = input('-> ').strip()
            if input_strip == "x":
                sys.exit()
            # Remove caracteres inválidos comuns para nomes de arquivos
            nome_limpo = "".join(
                c for c in input_strip if c.isalnum() or c in ("-", "_")
            )
            if nome_limpo:
                nome_exe = nome_limpo
                break
            print("Nome inválido. Digite um nome válido sem caracteres especiais.")

    print(f"\n{50*'='}\n[4/5] Modo de Compilação \n{50*'='}\n{40*' '}SAIR ( X )")
    print("1 - Arquivo Único (--onefile)")
    print("2 - Pasta Separada (--onedir) [Recomendado para testes]")
    print("Escolha a opção (1 ou 2) [Padrão: 1]:")
    input_strip = input('-> ').strip()
    if input_strip == "x":
        sys.exit()
    modo = "--onefile" if input_strip != "2" else "--onedir"

    print(f"\nExibir janela de terminal (Console) ao executar?")
    print("1 - Ocultar terminal (--noconsole / GUI)")
    print("2 - Exibir terminal (--console)")
    print("Escolha a opção (1 ou 2) [Padrão: 2]:")
    input_strip = input('-> ').strip()
    if input_strip == "x":
        sys.exit()
    console = "--noconsole" if input_strip == "1" else "--console"

    return nome_exe, modo, console


def construir_comando(
    diretorio_atual: str,
    script_principal: str,
    pastas: List[str],
    icone: Optional[str],
    nome_exe: str,
    modo: str,
    console: str,
) -> Tuple[List[str], str]:
    """Mapeia os parâmetros no padrão desejado com suporte multiplataforma."""
    print(f"\n{50*'='}\n [5/5] Gerando Comando e Executando PyInstaller \n{50*'='}\n{40*' '}SAIR ( X )")

    pasta_build_base = os.path.join(diretorio_atual, f"__{nome_exe}")
    distpath = os.path.join(pasta_build_base, "dist")
    workpath = os.path.join(pasta_build_base, "build")
    specpath = pasta_build_base

    # Uso explicito do Python em execução para evitar quebras por variável PATH
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        f"--name={nome_exe}",
        modo,
        console,
        "--clean",
        "--log-level=INFO",
        f"--distpath={distpath}",
        f"--workpath={workpath}",
        f"--specpath={specpath}",
    ]

    # Ajuste de separador por sistema operacional (; para Windows, : para Linux/Mac)
    separador_add_data = os.pathsep

    for pasta in pastas:
        caminho_abs = os.path.join(diretorio_atual, pasta)
        cmd.append(f"--add-data={caminho_abs}{separador_add_data}{pasta}")

    if icone:
        cmd.append(f"--icon={icone}")

    cmd.append(os.path.join(diretorio_atual, script_principal))

    return cmd, distpath


def executar_compilacao(cmd: List[str], distpath: str) -> None:
    """Executa a compilação do projeto."""
    print("\nComando gerado:")
    print(" ".join(cmd))
    print("\nIniciando processo de build...\n" + "-" * 50)

    try:
        subprocess.run(cmd, check=True)
        print("\n" + "=" * 50)
        print(" COMPILAÇÃO CONCLUÍDA COM SUCESSO!")
        print(f" Executável gerado na pasta: {distpath}")
        print("=" * 50)
    except subprocess.CalledProcessError as e:
        print(f"\n Erro durante a compilação: {e}")
    except FileNotFoundError as e:
        print(f"\n Executável ou módulo não localizado: {e}")


def main() -> None:
    """Função principal que coordena o fluxo de execução."""
    diretorio_atual = os.getcwd()

    instalar_pyinstaller()

    script_principal, pastas, icone = mapear_pastas_e_arquivos(diretorio_atual)

    nome_exe, modo, console = obter_configuracoes_usuario(script_principal)

    comando, distpath = construir_comando(
        diretorio_atual,
        script_principal,
        pastas,
        icone,
        nome_exe,
        modo,
        console,
    )

    executar_compilacao(comando, distpath)


if __name__ == "__main__":
    main()
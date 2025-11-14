@echo off
echo Compilando e executando o projeto...
gcc cadastro.c -o cadastro.exe
if exist cadastro.exe (
    echo.
    echo --- Cadastro de Alunos ---
    cadastro.exe
    echo.
    echo --- Abrindo visualizacao em Python ---
    python visualiza.py
) else (
    echo Erro ao compilar o programa C. Verifique se o GCC esta instalado.
)
pause

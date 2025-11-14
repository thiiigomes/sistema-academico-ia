## 📚 Sistema Acadêmico Colaborativo com Apoio de Inteligência Artificial 🚀

Projeto Integrado Multidisciplinar (PIM) – UNIP • 2025

Este repositório contém o desenvolvimento completo de um Sistema Acadêmico Colaborativo, utilizando C e Python, com automação via .BAT e suporte conceitual de Inteligência Artificial.
O objetivo principal do projeto é criar uma solução simples, acessível e funcional para cadastro, análise e visualização do desempenho de alunos, integrando tecnologias básicas e conceitos de IA.

## 🧠 Descrição do Projeto

O sistema foi projetado para simular um ambiente acadêmico integrado, capaz de:

- Registrar alunos e suas notas (NP1, NP2, PIM)   
- Calcular médias automaticamente   
- Determinar status (Aprovado / Reprovado)
- Gerar visualizações gráficas
- Automatizar todo o fluxo com um único clique
- Preparar terreno para futuras aplicações de Inteligência Artificial

O projeto foi desenvolvido para compor o PIM – Projeto Integrado Multidisciplinar do 2° semestre do curso de Análise e Desenvolvimento de Sistemas – UNIP.

## 🚀 Tecnologias Utilizadas

| ETAPA                        | TECNOLOGIAS                      |  FUNÇÃO                          |
| ---------------------------- | -------------------------------- | -------------------------------- |
| Coleta de Dados              | **C**                            | Entrada de dados, geração de CSV |
| Processamento e Visualização | **Python (Tkinter, Matplotlib)** | Cálculos, interface e gráficos   |
| Armazenamento                | **dados.txt (CSV)**              | Estrutura simples e compatível   |
| Automação                    | **Script .BAT**                  | Compilação e execução            |
| Rede (conceitual)            | **Topologia Estrela + DHCP**     | Organização e comunicação        |
| Segurança                    | Práticas básica                  | Integridade dos arquivos         |

## 🗂️ Estrutura do Repositório

````md
```bash
/projeto_alunos

├── cadastro.c               # Programa em C para registrar alunos
├── visualiza.py             # Programa Python para análise e gráficos
├── compilar_e_executar.bat  # Automação da execução
├── dados.txt                # Arquivo gerado com os cadastros
└── README.md                # Documentação do projeto
````

## 🧩 Como Funciona o Sistema?

1️⃣ Cadastro de Alunos (C)

O arquivo cadastro.c coleta:

-  Nome do aluno
-  Nota NP1
-  Nota NP2
-  Nota PIM

Os dados são salvos automaticamente em dados.txt, em formato CSV.

2️⃣ Automação via Script .BAT

Ao executar compilar_e_executar.bat, ocorre:

- Compilação do C
- Execução do programa
- Geração do arquivo dados.txt
- Chamamento automático do script Python (opcional)

3️⃣ Análise e Visualização (Python)

O arquivo visualiza.py:
- Lê dados.txt
- Calcula médias

Aplica a regra:
- ✔️ Aprovado → média ≥ 7
- ❌ Reprovado → média < 7
- Abre uma interface gráfica via Tkinter
- Gera gráficos pelo Matplotlib

## 🛠️ Como Executar

✔️ Requisitos:
- Python 3+
- MinGW (GCC) instalado
- Windows

▶️ Passo a passo:

1. Abra a pasta projeto_alunos
2. Clique duas vezes em compilar_e_executar.bat
3. Siga as instruções na tela
4. Veja os dados e gráficos abrirem automaticamente

## 🔐 Segurança e Integridade

Embora simples, o projeto segue boas práticas como:
- Armazenamento local
- Leitura segura no Python

Base preparada para:
- Autenticação
- Criptografia
- Backup
- Logs
- Banco de dados SQL

## 📊 Visualizações

O sistema gera:
- Gráfico de barras (aluno x média), com cor indicando aprovação
- Interface com tabelas de alunos
- Opção para abrir o arquivo de dados

Possíveis expansões:
- Gráficos de pizza
- Boxplots
- PDF automático
- IA para recomendações pedagógicas

## 🧩 Diagramas (UML)

O trabalho inclui:
- Diagrama de Caso de Uso
- Diagrama de Classes
- Diagrama de Sequência
- Diagrama de Rede (Topologia estrela + DHCP)

Estes arquivos podem ser adicionados ao diretório /diagramas no GitHub.

## 🌐 Rede (Conceitual)

Configuração padrão usada no projeto:
- Servidor IA: 192.168.0.1
- Máscara: 255.255.255.0
- DHCP Range: 192.168.0.10 – 192.168.0.50

Funções do servidor:
- DHCP
- Banco de dados
- Processamento IA

## 🏁 Conclusão

O Sistema Acadêmico Colaborativo demonstra a integração eficiente entre:
- Linguagens de programação
- Tratamento de dados
- Visualização
- Estrutura de rede
- Conceitos de IA

É um projeto escalável, didático e ideal para demonstrar interdisciplinaridade no contexto acadêmico.

## 🧾 Autores
- Thiago Gomes Magalhães
- Jorge Conrado Kerssner Neto
- Lucas Henrique Ranolphi Pires
- Gabriel Carnovalle de Araújo

Universidade Paulista – UNIP
Curso: Análise e Desenvolvimento de Sistemas – 2025

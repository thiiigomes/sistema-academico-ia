#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *arquivo;
    int qtdAlunos;
    char nome[50];
    float np1, np2, pim;

    arquivo = fopen("dados.txt", "w");
    if (arquivo == NULL) {
        printf("Erro ao criar o arquivo!\n");
        return 1;
    }

    printf("Quantos alunos deseja cadastrar? ");
    scanf("%d", &qtdAlunos);

    for (int i = 0; i < qtdAlunos; i++) {
        printf("\n--- Aluno %d ---\n", i + 1);
        printf("Nome: ");
        scanf(" %[^\n]", nome);
        printf("Nota NP1: ");
        scanf("%f", &np1);
        printf("Nota NP2: ");
        scanf("%f", &np2);
        printf("Nota PIM: ");
        scanf("%f", &pim);
        fprintf(arquivo, "%s,%.2f,%.2f,%.2f\n", nome, np1, np2, pim);
    }

    fclose(arquivo);
    printf("\nCadastro concluído com sucesso! Dados salvos em 'dados.txt'.\n");
    return 0;
}

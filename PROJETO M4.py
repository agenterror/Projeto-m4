# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nb8UJPkEqQi6HxIrM4TCBSOLu9Y5D5dr
"""

import pandas as pd

"""#DADOS

##DADOS DOS FUNCIONARIOS
"""

dados = {
    'Nome do Funcionário': ['H', 'N', 'J'],
    'Horas Trabalhadas': [8, 7, 8],
    'Bugs Corrigidos': [5, 2, 7],
    'Tarefas Concluídas': [10, 8, 12],
}

dados

df = pd.DataFrame(dados)

"""##PRODUTIVIDADE DOS FUNCIONARIOS

"""

df['Produtividade Diária'] = df['Tarefas Concluídas'] / df['Horas Trabalhadas']

total_horas_trabalhadas = df['Horas Trabalhadas'].sum()

total_horas_trabalhadas

media_diaria_horas_trabalhadas = df['Horas Trabalhadas'].mean()
total_bugs_corrigidos = df['Bugs Corrigidos'].sum()
media_diaria_bugs_corrigidos = df['Bugs Corrigidos'].mean()
total_tarefas_concluidas = df['Tarefas Concluídas'].sum()
media_diaria_tarefas_concluidas = df['Tarefas Concluídas'].mean()
produtividade_diaria = df['Produtividade Diária'].mean()

"""##DATA DO RELATÓRIO"""

print("**Relatório de Progresso Diário**")
print(f"\n*Data:* [21/01/2005]]\n")

"""##RESULTADOS FINAIS"""

print("**Resumo Geral:**")
print(f"1. Total de Horas Trabalhadas: {total_horas_trabalhadas} horas")
print(f"2. Média Diária de Horas Trabalhadas: {media_diaria_horas_trabalhadas:.2f} horas")
print(f"3. Total de Bugs Corrigidos: {total_bugs_corrigidos}")
print(f"4. Média Diária de Bugs Corrigidos: {media_diaria_bugs_corrigidos:.2f}")
print(f"5. Total de Tarefas Concluídas: {total_tarefas_concluidas}")
print(f"6. Média Diária de Tarefas Concluídas: {media_diaria_tarefas_concluidas:.2f}")
print(f"7. Produtividade Diária (Tarefas Concluídas por Hora): {produtividade_diaria:.2f}\n")
print("Observações e Comentários:")
print("- [Inserir comentários específicos sobre o desempenho notável, desafios enfrentados, ou quaisquer eventos relevantes.]")
print("\nMetas e Objetivos para o Próximo Dia:")
print("- [Listar metas específicas para o próximo dia, se aplicável.]")
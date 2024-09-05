import matplotlib.pyplot as plt

provas = ['Prova 1', 'Prova 2', 'Prova 3', 'Prova 4', 'Prova 5']
notas_aluno_a = [7.5, 8.0, 7.0, 8.5, 9.0]
notas_aluno_b = [8.0, 7.5, 7.8, 8.2, 8.5]

plt.plot(provas, notas_aluno_a, marker='o', label='Aluno A')
plt.plot(provas, notas_aluno_b, marker='o', label='Aluno B')

plt.title('Comparação de Desempenho Acadêmico')
plt.xlabel('Prova')
plt.ylabel('Nota')
plt.legend()

plt.show()
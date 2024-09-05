import matplotlib.pyplot as plt

dias = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7', 'Dia 8', 'Dia 9', 'Dia 10']
acao_x = [100, 102, 101, 103, 105, 106, 108, 107, 109, 110]
acao_y = [95, 96, 97, 98, 99, 100, 101, 102, 103, 104]

plt.plot(dias, acao_x, marker='o', label='Ação X')
plt.plot(dias, acao_y, marker='o', label='Ação Y')

plt.title('Evolução de Preços de Ações')
plt.xlabel('Dia')
plt.ylabel('Preço de Fechamento (R$)')
plt.legend()

plt.show()
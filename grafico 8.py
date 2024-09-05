import matplotlib.pyplot as plt

dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
semana_1 = [120, 130, 125, 140, 135]
semana_2 = [110, 115, 120, 130, 125]

plt.plot(dias_semana, semana_1, marker='o', label='Semana 1')
plt.plot(dias_semana, semana_2, marker='o', label='Semana 2')

plt.title('Variação da Produtividade Semanal')
plt.xlabel('Dia da Semana')
plt.ylabel('Unidades Produzidas')
plt.legend()

plt.show()
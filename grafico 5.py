import matplotlib.pyplot as plt

dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
temperaturas = [32, 34, 33, 31, 30, 29, 28]

plt.plot(dias_semana, temperaturas, marker='o')

plt.title('Variação da Temperatura Diária ao Longo de Uma Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Temperatura (°C)')

plt.show()
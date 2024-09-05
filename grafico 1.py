import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
temperaturas = [25, 27, 30, 28, 24, 22]

plt.plot(meses, temperaturas, marker='o')

plt.title('Variação de Temperatura ao Longo do Ano')
plt.xlabel('Mês')
plt.ylabel('Temperatura (°C)')

plt.show()

import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
precipitacao = [120, 85, 95, 70, 50, 40]

plt.plot(meses, precipitacao, marker='o')

plt.title('Variação de Precipitação ao Longo do Ano')
plt.xlabel('Mês')
plt.ylabel('Precipitação (mm)')

plt.show()
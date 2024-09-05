import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
produto_x = [200, 210, 180, 220, 230, 240]
produto_y = [150, 170, 160, 190, 200, 210]

plt.plot(meses, produto_x, marker='o', label='Produto X')
plt.plot(meses, produto_y, marker='o', label='Produto Y')

plt.title('Evolução das Vendas de Dois Produtos')
plt.xlabel('Mês')
plt.ylabel('Vendas (unidades)')
plt.legend()

plt.show()
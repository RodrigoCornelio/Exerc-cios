import matplotlib.pyplot as plt

anos = [2020, 2021, 2022, 2023, 2024]
cidade_a = [500, 520, 540, 560, 580]
cidade_b = [450, 460, 470, 490, 510]

plt.plot(anos, cidade_a, marker='o', label='Cidade A')
plt.plot(anos, cidade_b, marker='o', label='Cidade B')

plt.title('Crescimento Populacional em Duas Cidades')
plt.xlabel('Ano')
plt.ylabel('População (milhares)')
plt.legend()

plt.show()
import matplotlib.pyplot as plt

anos = [2019, 2020, 2021, 2022, 2023]
economia_a = [2.5, 1.8, 2.0, 2.2, 2.4]
economia_b = [3.0, 2.5, 2.8, 3.1, 3.2]

plt.plot(anos, economia_a, marker='o', label='Economia A')
plt.plot(anos, economia_b, marker='o', label='Economia B')

plt.title('Comparação de Taxas de Crescimento Anual')
plt.xlabel('Ano')
plt.ylabel('Crescimento Anual (%)')
plt.legend()

plt.show()
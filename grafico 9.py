import matplotlib.pyplot as plt

horarios = ['00:00', '06:00', '12:00', '18:00', '21:00', '23:59']
consumo = [0.5, 1.2, 2.0, 2.5, 1.8, 1.0]

plt.plot(horarios, consumo, marker='o')

plt.title('Consumo de Energia ao Longo do Dia')
plt.xlabel('Horário')
plt.ylabel('Consumo (kWh)')

plt.show()
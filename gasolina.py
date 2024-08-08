import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

sns.set(style='whitegrid')


plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='dia', y='venda', marker='o', color='blue')
plt.title('Preço Médio de Venda da Gasolina em São Paulo - Julho 2021')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')
plt.grid(True)

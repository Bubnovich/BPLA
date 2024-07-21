import matplotlib.pyplot as plt
import seaborn as sns

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temperature_value = [-20, -25, -15, 8, 15, 25, 32, 25, 15, 3, -15, -25]

plt.figure(figsize=(20, 10))
sns.lineplot(x=months, y=temperature_value)
plt.xlabel("Месяцы")
plt.ylabel("Температура")
plt.title("Температура по месяцам года")
plt.savefig("homework_1_3_result.png")


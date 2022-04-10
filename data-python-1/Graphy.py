import matplotlib.pyplot as plt
import numpy as np
import matplotlib
plt.style.use('_mpl-gallery')
print(matplotlib.__version__)

file = open("cupcakeInvoices.csv", "r")

total = 0
chocolate_profit = 0
vanilla_profit = 0
strawberry_profit = 0
for x in file:
    new_x = x.split(",")
    if new_x[2] == "Chocolate":
         chocolate_profit = chocolate_profit + (float(new_x[3]) * float(new_x[4])) - (float(new_x[3]) * float(new_x[5]))
    if new_x[2] == "Vanilla":
         vanilla_profit = vanilla_profit + (float(new_x[3]) * float(new_x[4])) - (float(new_x[3]) * float(new_x[5]))
    if new_x[2] == "Strawberry":
         strawberry_profit = strawberry_profit + (float(new_x[3]) * float(new_x[4])) - (float(new_x[3]) * float(new_x[5]))

cupcakes = ["Chocolate", "Vanilla", "Strawberry"]
profits = []
profits.append(chocolate_profit)
profits.append(vanilla_profit)
profits.append(strawberry_profit)

plt.bar(cupcakes, profits, color ='maroon',
        width = 0.4)
plt.xlabel("Cupcakes offered")
plt.ylabel("Amount of profits created from each Cupcake type")
plt.title("Profits")
plt.show()

file.close()

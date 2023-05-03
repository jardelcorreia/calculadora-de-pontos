import tkinter as tk

def calcular_pontos(apostas, resultados):
    pontos = 0
    for aposta, resultado in zip(apostas, resultados):
        if aposta == resultado:
            pontos += 3
        elif (aposta[0] > aposta[1] and resultado[0] > resultado[1]) or (aposta[0] < aposta[1] and resultado[0] < resultado[1]):
            pontos += 1
        elif aposta[0] == aposta[1] and resultado[0] == resultado[1]:
            pontos += 1
    return pontos

def calcular():
    apostas = []
    resultados = []
    for i in range(10):
        aposta_1 = apostas_entry[i][0].get()
        aposta_2 = apostas_entry[i][1].get()
        resultado_1 = resultados_entry[i][0].get()
        resultado_2 = resultados_entry[i][1].get()
        if aposta_1 and aposta_2 and resultado_1 and resultado_2:
            aposta = (int(aposta_1), int(aposta_2))
            resultado = (int(resultado_1), int(resultado_2))
            apostas.append(aposta)
            resultados.append(resultado)
    pontos = calcular_pontos(apostas, resultados)
    pontos_label.config(text=f"Total de pontos: {pontos}")

def limpar():
    # Limpar o campo de entrada
    for i in range(10):
        apostas_entry[i][0].delete(0, tk.END)
        apostas_entry[i][1].delete(0, tk.END)
    
root = tk.Tk()
root.title("Calculadora de Pontos")

apostas_label = tk.Label(root, text="Apostas")
apostas_label.grid(row=0, column=1, columnspan=2)

resultados_label = tk.Label(root, text="Resultados")
resultados_label.grid(row=0, column=3, columnspan=2)

jogos_label = tk.Label(root, text="Jogos")
jogos_label.grid(row=1, column=0)

apostas_entry = []
resultados_entry = []
for i in range(10):
    jogo_label = tk.Label(root, text=f"Jogo {i+1}")
    jogo_label.grid(row=i+2, column=0)
    aposta_entry_1 = tk.Entry(root, width=5)
    aposta_entry_2 = tk.Entry(root, width=5)
    resultado_entry_1 = tk.Entry(root, width=5)
    resultado_entry_2 = tk.Entry(root, width=5)
    aposta_entry_1.grid(row=i+2, column=1)
    aposta_entry_2.grid(row=i+2, column=2)
    resultado_entry_1.grid(row=i+2, column=3)
    resultado_entry_2.grid(row=i+2, column=4)
    apostas_entry.append((aposta_entry_1, aposta_entry_2))
    resultados_entry.append((resultado_entry_1, resultado_entry_2))

calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.grid(row=12, column=0, columnspan=5)

limpar_button = tk.Button(root, text="Limpar", command=limpar)
limpar_button.grid(row=12, column=3, columnspan=5)



pontos_label = tk.Label(root, text="Total de pontos: 0")
pontos_label.grid(row=13, column=0, columnspan=5)

root.mainloop()
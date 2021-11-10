import tkinter as tk

window = tk.Tk()
window.title("Dextroit")
window.configure(background="#15224F",width=500,height=400)
##construção de entries e labels de concentração

variaveis = [0,0,0,0,0,0,0]
identidade_entries = []
contador = 0

def salvar_valores():
    global variaveis
    concentracoes_inicias = []
    contador = 0
    while contador < len(variaveis):
        try:
            concentracoes_inicias.append(float(variaveis[contador].get()))
        except:
            concentracoes_inicias.append(0.0)
        contador += 1
    print(concentracoes_inicias)
    return



while contador < len(variaveis):
    variaveis[contador] = tk.StringVar(window)
    concentracao = tk.Entry(textvariable = variaveis[contador])  # botao de iniciar ativ
    concentracao.config(width=15)
    identidade_entries.append(concentracao)
    textos = tk.Label(text="Concentração G" + str(contador+1), fg="white", bg="#1B1F49", width=35, height=3)
    textos.grid(row=contador+1,column=1)
    concentracao.grid(row=contador + 1, column=2)
    contador += 1

botao_enviar = tk.Button(window, width=15, text="Enviar!", bg="#aff587", command=salvar_valores)
botao_enviar.grid(row=10, column=1)

window.mainloop()

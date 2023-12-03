import tkinter as tk
import numpy as np
import statsmodels.api as sm

def run_statistical_test():
    num_inputs = int(input_field_num_points.get())

    numerador_array = np.array([])
    denominador_array = np.array([])

    for i in range(num_inputs):
        user_numerador_input = float(input_numerador_fields[i].get())
        user_denominador_input = float(input_denominador_fields[i].get())
        numerador_array = np.append(numerador_array, user_numerador_input)
        denominador_array = np.append(denominador_array, user_denominador_input)

    numerators = numerador_array  # Numeradores
    denominators = denominador_array  # Denominadores

    table = sm.stats.Table(np.column_stack((numerators, denominators - numerators)))
    trend_test = table.test_nominal_association()

    resultado_chi2 = trend_test.statistic
    valor_p = trend_test.pvalue

    if valor_p < 0.001:
        valor_p_final = '<.001'
    else:
        valor_p_final = round(float(valor_p), 3)

    output_area.config(state=tk.NORMAL)  # Enable editability
    output_area.delete("1.0", tk.END)    # Clear previous output
    output_area.insert(tk.END, f"Chi-square statistic: {resultado_chi2}\nP-value: {valor_p_final}")  # Insert new output
    output_area.config(state=tk.DISABLED)  # Disable editability

def exit_window():
    window.destroy()

window = tk.Tk()
window.title("Teste qui-quadrado de tendência - SCIENTIA TOOLS")
window.geometry('500x700')

input_label_num_points = tk.Label(window, text="Número de pontos na série:")
input_label_num_points.pack()
input_field_num_points = tk.Entry(window)
input_field_num_points.pack()

input_numerador_fields = []
input_denominador_fields = []

def create_input_fields():
    try:
        num_points = int(input_field_num_points.get())
    except ValueError:
        output_area.config(state=tk.NORMAL)  # Enable editability
        output_area.delete("1.0", tk.END)    # Clear previous output
        output_area.insert(tk.END, f"Valor inválido")  # Insert new output
        output_area.config(state=tk.DISABLED)  # Disable editability  
   
    else:
        for i in range(num_points):
            lbl_numerador = tk.Label(window, text=f"Numerador for point {i+1}:")
            lbl_numerador.pack()
            entry_numerador = tk.Entry(window)
            entry_numerador.pack()
            input_numerador_fields.append(entry_numerador)

            lbl_denominador = tk.Label(window, text=f"Denominador for point {i+1}:")
            lbl_denominador.pack()
            entry_denominador = tk.Entry(window)
            entry_denominador.pack()
            input_denominador_fields.append(entry_denominador)

create_input_fields_button = tk.Button(window, text="Entrar com os valores da série", command=create_input_fields)
create_input_fields_button.pack()

run_test_button = tk.Button(window, text="Rodar o teste estatístico", command=run_statistical_test)
run_test_button.pack()

output_label = tk.Label(window, text="Saída:")
output_label.pack()
output_area = tk.Text(window, height=10, width=40, state=tk.DISABLED)
output_area.pack()

exit_button = tk.Button(window, text="Sair", command=exit_window)
exit_button.pack()

window.mainloop()

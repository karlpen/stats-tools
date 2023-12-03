import numpy as np
import statsmodels.api as sm

# Pergunta o número de pontos na série a ser analisada
num_inputs = int(input("Insira o número de pontos na série: "))

# Cria uma NumPy array para salvar os numeradores e outra para os denominadores
numerador_array = np.array([])
denominador_array = np.array([])


# Loop para pegar os numeradores e denominadores e adicionar as arrays
for i in range(num_inputs):
    user_numerador_input = float(input("Entre o numerador para o ponto {}: ".format(i + 1)))
    user_denominador_input = float(input("Entre o denominador para o ponto {}: ".format(i + 1)))
    numerador_array = np.append(numerador_array, user_numerador_input)
    denominador_array = np.append(denominador_array, user_denominador_input)    
    
# coloca os dados do usário dentro das arrays a serem analisadas
numerators = numerador_array  # Numeradores
denominators = denominador_array  # Denominadores

# realiza o teste Cochran-Armitage (qui-quadrado de tendência)
table = sm.stats.Table(np.column_stack((numerators, denominators - numerators)))
trend_test = table.test_nominal_association()

resultado_chi2 = trend_test.statistic
valor_p = trend_test.pvalue

if valor_p < 0.001:
    valor_p_final = str('<.001')
else:
    valor_p_final = float (valor_p)

print("Chi-square statistic:", resultado_chi2)
print("P-value:", valor_p_final)



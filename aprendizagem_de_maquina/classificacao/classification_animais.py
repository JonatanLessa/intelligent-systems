# Exemplo para classificação de animais, considerando três características

# Duas classes: cachorro ou porco

# C1: Perna longa?
# C2: Gordo?
# C3: Late?

# O classificador multinomial Naïve Bayes é um dos modelos mais populares 
# no aprendizado de máquina. Tomando como premissa a suposição de independência 
# entre as variáveis do problema, o modelo de Naïve Bayes realiza uma 
# classificação probabilística de observações, caracterizando-as 
# em classes pré-definidas.

# Aplicado para características com valores discretos: quando o conjunto de 
# resultados possíveis é finito ou enumerável (número inteiros).

from sklearn.naive_bayes import MultinomialNB

pork_1 = [0, 1, 0]
pork_2 = [1, 1, 0]
pork_3 = [1, 1, 0]

dog_1 = [1, 1, 1]
dog_2 = [0, 1, 1]
dog_3 = [0, 1, 1]

animals = [pork_1, pork_2, pork_3, dog_1, dog_2, dog_3]
categories = [0, 0, 0, 1, 1, 1]
categories_names = ['Pork', 'Dog']

model = MultinomialNB()
model.fit(animals, categories)

# Novos animais (instâncias) para predição
animals_for_classification = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
animals_for_classification_categories = [0, 1, 1]


# Imprimindo o resultado da predição
result = model.predict(animals_for_classification)
print('Resultado: ' + str(result))


# Calculando a taxa de acerto
error = result - animals_for_classification_categories

correct = [r for r in error if r == 0]

correct_total = len(correct)
total = len(animals_for_classification)

correct_rate = 100.0 * correct_total / total

print(f"Taxa de acerto: {correct_rate}")
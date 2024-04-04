#!/usr/bin/env python
# coding: utf-8

# 2. O número de chamadas para o help-desk de uma empresa tem uma distribuição de Poisson com 60 chamadas por um período de 10 horas. Se C = a variável aleatória para o número de chamadas por hora, encontre:
# a. A probabilidade de que o suporte técnico não receba chamadas em uma determinada hora.
# b. a probabilidade de que o suporte técnico receba menos de oito 
# chamadas em uma determinada hora.
# c. O número médio de chamadas por hora E (C).
# d. A variância de C.
# e. O desvio padrão de C

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import math

# Função para calcular a probabilidade e Poisson
def poisson_prob(lambd, x):
    return math.exp(-lambd) * (lambd ** x) / math.factorial(x)

# Parâmetros do problema
lambd = 6  # Taxa média de chamadas por hora

# a. Probabilidade de que o suporte técnico não receba chamadas em uma determinada hora
prob_zero_calls = poisson_prob(lambd, 0)
print("a. Probabilidade de não receber chamadas por hora:", prob_zero_calls)

# b. Probabilidade de que o suporte técnico receba menos de oito chamadas em uma determinada hora
prob_less_than_eight_calls = sum(poisson_prob(lambd, x) for x in range(8))
print("b. Probabilidade de menos oito por hora:", prob_less_than_eight_calls)

# c. Número médio de chamadas por hora
mean_calls = lambd
print("c. Número médio de chamadas por hora:", mean_calls)

# d. Variância do número de chamadas por hora
var_calls = lambd
print("d. Variância do número de chamadas por hora:", var_calls)

# e. Desvio padrão do número de chamadas por hora
std_dev_calls = math.sqrt(var_calls)
print("e. Desvio padrão do número de chamadas por hora:", std_dev_calls)


# In[ ]:





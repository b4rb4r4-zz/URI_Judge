
# coding: utf-8

# In[14]:


salario = float(input())

if salario >= 0 and salario <= 400:
    ajuste = salario*0.15
    novo_salario = salario + ajuste
    percentual = 15
    
    print ("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:d} %".format(novo_salario, ajuste, percentual))

elif salario > 400 and salario<= 800:
    ajuste = salario*0.12
    novo_salario = salario + ajuste
    percentual = 12
    
    print ("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:d} %".format(novo_salario, ajuste, percentual))

elif salario>800 and salario<= 1200:
    ajuste = salario*0.10
    novo_salario = salario + ajuste
    percentual = 10
    
    print ("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:d} %".format(novo_salario, ajuste, percentual))

elif salario > 1200 and salario<= 2000:
    ajuste = salario*0.07
    novo_salario = salario + ajuste
    percentual = 7
    
    print ("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:d} %".format(novo_salario, ajuste, percentual))

elif salario > 2000:
    ajuste = salario*0.04
    novo_salario = salario + ajuste
    percentual = 4
    
    print ("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:d} %".format(novo_salario, ajuste, percentual))


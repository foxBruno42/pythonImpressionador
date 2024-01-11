#Recebe dados do usuário, imprime e compara se está correto
senha = input('Digite sua senha\n')
print('Senha digitada: '+senha)
if('foxBruno' in senha):
    print('Senha correta')
else:
    print ('Senha Incorreta')
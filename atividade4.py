#programa com nome e data de nascimento
primeironome = input("Digite seu primeiro nome: ")
print ("Digite sua data de nascimento ")
Dia =  input("Digite o Dia: ")
Mes =  input("Digite o Mês: ")
Ano =  input("Digite o Ano: ")
primeiraletra = primeironome[0:1].upper()
restantedonome = primeironome[1:].lower()
primeironomeformatado = primeiraletra + restantedonome

mensagem = " {} nasceu no dia {}/{}/{}." .format(primeironomeformatado, Dia, Mes, Ano)

print (mensagem)
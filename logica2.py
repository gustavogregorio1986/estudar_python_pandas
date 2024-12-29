nome = input("Digitwe o nome: ")
idade = int(input("Digite a idade: "))
sexo = input("Digite o sexo: ")

if idade >= 18 or sexo == "m":
    print(f"O {nome} pode se alistar no exercito")
else:
    print(f"O {nome} não pode se alistar no exercito")
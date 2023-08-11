print("---Exercicio 1---")
raio = int(input ("qual sera o raio do cilindro? "))
altura = int(input ("qual sera a altura do cilindro? "))
PI = 3.14
Áreabase = 2 * PI * raio * (raio + altura)
print(Áreabase)
volume = Áreabase * altura
print(volume)


print("---Exercicio 2---")
nome = str(input("digite o nome"))
print(f"seu nome é {nome}")


print("---Exercicio 3---")
primeiro_nome = str(input("fale seu primeiro nome"))
sobrenome = str(input("fale seu sobrenome"))
nome_completo = (f"{primeiro_nome} {sobrenome}")
print(f"seu nome completo é {nome_completo}")
print("/n")

print("---Exercicio 4---")
a = int(input("qual valor inteiro de a?"))
b = int(input("qual valor inteiro de b?"))
print(f"{a},{b}")
c = a
a = b
b = c
print(f"{a},{b}")







#variaveis (n, a, p)
nome = 'arthur'
peso = 90.5
altura = 1.63
print(nome)
print(peso)
print(altura)
#tipos
print(type(nome))
print(type(peso))
print(type(altura))

#operações (p / a * a)
imc = peso / (altura * altura)
print("{:.2f}".format(imc))

#condições

if imc < 20:
    print("MAGRO")
elif imc > 20 and imc < 30:
    print("GORDIN")
if imc > 30:
    print("GORDO")

#dicionario
dict_renato = {'nome':'renato','altura':1.72,'peso':78}
dict_arthur = {'nome':'arthur','altura':1.63,'peso':90}

print(dict_arthur, dict_renato)

#funções
def get_imc(dict_x):

    imc = dict_x['peso'] / (dict_x['altura'] * dict_x['altura']) 
    ret = ''

    if imc < 20:
        ret = "MAGRO"
    elif imc > 20 and imc < 30:
        ret = "GORDIN"
    if imc > 30:
        ret = "GORDO"
    
    return ret


print(get_imc(dict_renato))
print(get_imc(dict_arthur))

#vetores
a = [1,2,3,4,5]

print(a)
a = [dict_renato, dict_arthur]

#laços de repetição
for i in a:
    print(get_imc(i))
    
#expressões regulares

texto = """
13 3333 9999
RENATO COBEL DE SOUZA
EDUARDO
EWERTON
THIAGO FERAUCHE
RENATA CLARA PIMENTA
SAMU?
"""
import re

tel = re.findall(r'\d{2} \d{4} \d{4}', texto, re.MULTILINE)
print(tel)

nomes = re.findall(r'(RENATO|EDUARDO|EWERTON|THIAGO.*|RENATA)', texto, re.MULTILINE)
print(nomes)



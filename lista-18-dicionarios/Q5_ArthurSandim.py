#Arthur Vinicius Gouvêa Sandim
#21204602
#https://www.beecrowd.com.br/judge/pt/problems/view/1430

notas = {'W':1,'H':1/2,'Q':1/4,'E':1/8,'S':1/16,'T':1/32,'X':1/64}

def soma(dicio,lista):
    cont = 0
    for e in lista:
        summ = 0
        for j in e:
            if j.upper() in dicio.keys():
                summ += dicio[j]
        if summ == 1:
            cont+=1  
    return cont    

while True:
    compassos = input('Digite os compassos separados por "/": ').upper().split('/')
    if compassos == ['*']:
        print('Fim da execução do programa.')
        break
    for element in compassos:
        if element == '':
            compassos.remove(element)
    print(f'Número de compassos com duração correta: {soma(notas, compassos)}')
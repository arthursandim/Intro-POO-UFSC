#Arthur Vinicius Gouvea Sandim
#21204602
#Questão - https://www.beecrowd.com.br/judge/pt/problems/view/1763

felizNatal = {'brasil' : 'Feliz Natal!', 'alemanha' : 'Frohliche Weihnachten!', 'austria' : 'Frohe Weihnacht!', 'coreia' : 'Chuk Sung Tan!', 'espanha' : 'Feliz Navidad!', 'grecia' : 'Kala Christougena!', 'estados-unidos' : 'Merry Christmas!', 'inglaterra' : 'Merry Christmas!', 'australia' : 'Merry Christmas!', 'portugal' : 'Feliz Natal!', 'suecia' : 'God Jul!', 'turquia' : 'Mutlu Noeller', 'argentina' : 'Feliz Navidad!', 'chile' : 'Feliz Navidad!', 'mexico' : 'Feliz Navidad!', 'antardida' : 'Merry Christmas!', 'canada' : 'Merry Christmas!', 'irlanda' : 'Nollaig Shona Dhuit!', 'belgica' : 'Zalig Kerstfeest!', 'italia' : 'Buon Natale!', 'libia' : 'Buon Natale!', 'siria' : 'Milad Mubarak!', 'marrocos' : 'Milad Mubarak!', 'japao' : 'Merii Kurisumasu!'}

pais = input('Digite o país: ').lower()
if pais in felizNatal.keys():
    print(felizNatal[pais])
else:
    print('--- NOT FOUND ---')
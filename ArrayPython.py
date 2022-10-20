array = ['banana', 'melon', 'sandia', 'pera']

array.reverse() #revertim l'ordre
array.remove('melon') #eliminem melo
array.append('piña') #afegim piña

for fruta in array:
    if fruta.endswith('a'):
        print('La fruita ' + fruta)
        #es mostraran totes les fruites acabades amb a, com hem eliminat melo i afegit piña tambe es veura.
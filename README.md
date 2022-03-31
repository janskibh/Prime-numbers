# primenumb
Prime numbers finder

Ce script fonctionne sur la base du crible d'érathostène

Le code créé une liste avec tous les entiers entre 0 et un nombre donné (ex. 100000)

Il prend le premier nombre premier : 2
Il supprime tous ses multiples de la liste sauf 2 (4,6,8,10,12,14,16,18,20,...)
On reste avec 2,3,5,7,9,11,13,15 etc...

Il prend le prochain nombre de la liste : 3
Il supprime tous ses multiples de la liste sauf 3 (6,9,12,15,18,21,24,...)
On reste avec 2,3,5,7,11,13,17,19,23,25 etc...

Il prend le prochain nombre de la liste : 5
Il supprime tous ses multiples sauf 5 (10,15,20,25,30,35,40,45,...)
On reste avec 2,3,5,7,11,13,17,19,23,29 etc...

Et ainsi de suite...

Il y a plusieurs scripts et leur différence se trouve dans leur rapidité.

On peut commencer par faire une liste de tous les entiers mais cela prend beaucoup de temps et de mémoire
Comme ensuite, on supprime tous les multiples de 2 sauf 2, il reste tous les nombres impaires.

Le script2 commence directement avec les nombres impairs sauf 2 : 2,3,5,7,9,11 etc...
Cela permet d'économiser 1/2 de la mémoire et 1/3 du temps
Pour se faire il créée la liste avec une intervale de 2 entre chaque nombre

Le script3 commence directement sans les nombres pairs et les multiples de 3 : 2,3,5,7,11,13
Pour se faire il créée la liste avec des intervale entre les nombres : 2,4,2,4


Le script3 commence directement sans les nombres pairs, les multiples de 3 et les multiples de 5 : 2,3,5,7,11,13
Pour se faire il créée la liste avec des intervale entre les nombres : 4,2,4,2,4,6,4,6,4,2,4,2,4,6,4,6


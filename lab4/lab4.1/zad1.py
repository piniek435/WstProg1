Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
Lista=[1, 2, 3, 4]

print(Moja_lista[0], Moja_lista[-1] )
print(len(Moja_lista))
print(max(Moja_lista),min(Moja_lista))
print(sum(Moja_lista))
print(sorted(Moja_lista) )
Moja_lista.append(6)
print(Moja_lista)
i=1
Moja_lista.insert(i,5)
print(Moja_lista)
print(Moja_lista.pop() )
Moja_lista.reverse()
print(Moja_lista)
listaŁ = Moja_lista + Lista
listaM = Moja_lista*5
print(Moja_lista)
m=2
n=3
k=4
print(listaŁ[ :n],listaŁ[m: ],listaŁ[m:n:k],listaŁ[::-1])

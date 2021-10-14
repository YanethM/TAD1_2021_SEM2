import math
from DLL import DoubleLinkedLinkd
inst_DLL = DoubleLinkedLinkd()
inst_DLL.append('1')
inst_DLL.append('3')
inst_DLL.append('4')
inst_DLL.append('16')
inst_DLL.append('23')
inst_DLL.append('101')
inst_DLL.append('43')

#inst_DLL.shift()
print("\nLista obtenida")
inst_DLL.show_elements_list()
print("\nModificando el valor de la posición 1 por 1144")
inst_DLL.set(1, '1144')
inst_DLL.show_elements_list()
print("\nInsertar el valor 22 en la posición 6")
inst_DLL.insert(6,'22')
inst_DLL.show_elements_list()
print("\nInvirtiendo la lista")
inst_DLL.reverse()
inst_DLL.show_elements_list()





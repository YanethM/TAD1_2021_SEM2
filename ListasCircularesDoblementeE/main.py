from DLL import Circular_Double_Linked_List
inst_DLL = Circular_Double_Linked_List()
inst_DLL.prepend(5)
inst_DLL.prepend(6)
inst_DLL.prepend(7)
inst_DLL.prepend(10)
inst_DLL.append(4)
inst_DLL.append(3)
inst_DLL.prepend(11)
inst_DLL.pop()
inst_DLL.shift()
inst_DLL.show_circular_list()
print('Valor nodo posición 4')
inst_DLL.get(2)
inst_DLL.update(2, 23)
inst_DLL.insert(2,8)
inst_DLL.show_circular_list()







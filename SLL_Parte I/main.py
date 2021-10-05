from ActivityI_SLL import Ativity_SLL
inst_activity = Ativity_SLL()
inst_activity.append()
''' Punto 1 '''
search_node = int(input('       Ingresa el indice: '))
inst_activity.get(search_node)
print('Eliminando el nodo')
inst_activity.remove(search_node)
inst_activity.show_elements()
print('Creando nuevo nodo al cuadrado')
inst_activity.new_node_pow()



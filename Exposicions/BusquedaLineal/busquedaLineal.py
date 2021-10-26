class BusquedaLineal:
  def __init__(self):
    self.list_values = [101,364,3,65,908,540]
  
  def linealSearch(self, lista, tam, value):
    
    for item_list in range(tam):
      if lista[item_list] == value:
        return item_list
    return -1

  def encontrar_valor(self):
    while True:
      try:
        value_to_search = int(input('   Ingresa valor a buscar: '))
        position = self.linealSearch(self.list_values, len(self.list_values), value_to_search)
        if position == -1:
          return print('No se encontro el valor')
          break
        else:
          return print('Se encontro el valor en la posicion ', position)
          break
      except ValueError:
        print('Se esperaba un valor númerico')


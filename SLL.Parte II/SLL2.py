import math
class SLL_ActivityII:

  class Node:
    #Creamojs el método inicializador de la clasr nodo
    def __init__(self,value):
      self.value = value
      self.next = None
  #Creamos el méotod inicializador de la clase Single_Linked_List
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self):
    while True:
      try:
        cant_node = int(input('       Cantidad de nodos a crear: '))
        for node_item in range(cant_node):
          value = input('         Ingresa el valor del nodo: ')
          new_node = self.Node(value)
          if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
          else:
            self.tail.next = new_node
            self.tail = new_node
          self.length +=1
        self.show_elements()
        menu_options = int(input('        Selecciona una opción del menú\n        1. Añadir nodo con raiz cuadrada\n        2. Eliminar nodo y añadirlo al final elevado al cuadrado\n        3. Invertir la lista\n        >>>'))
        while True:
          if menu_options !=1 and menu_options!= 2 and menu_options!= 3:
            menu_options = int(input('        Opciones disponibles:\n        1. Añadir nodo con raiz cuadrada\n        2. Eliminar nodo y añadirlo al final elevado al cuadrado\n        3. Invertir la lista\n        >>>'))
          elif menu_options ==1:
            self.punto1()
            self.show_elements()
            break
          elif menu_options ==2:
            self.punto2()
            self.show_elements()
            break
          else:
            self.punto_3()
            self.show_elements()

            break
        break
      except ValueError:
        print('           ERROR, se esperaba un valor númerico')


  #Mostrar los elementos que conforman nuestra lista
  def show_elements(self):
    array= []
    current_node = self.head
    while current_node != None:
      #Mientras si exista un elemento en la cabeza de la lista, el valor se añade a la lista array
      array.append(current_node.value)
      current_node = current_node.next
    return print(array)

  def get(self, index):
    if index == self.length -1:
      return self.tail
    if index == 0:
      return self.head
    elif not(index >= self.length or index <0):
      current_node = self.head
      visit_node_count = 0
      while visit_node_count != index:
        current_node = current_node.next
        visit_node_count += 1
      return current_node
    else:
      return None

  def punto1(self):
    index = int(input('       Ingresa el indice: '))
    new_node = self.get(index - 1)
    node_sqrt = math.sqrt(int(new_node.value))
    node_n =self.Node(node_sqrt)
    if self.head == None and self.tail == None:
      self.head = node_n
      self.tail = node_n
    else:
      node_n.next = self.head
      self.head = node_n
    self.length += 1

  def shift(self):
    if self.length == 0:
      self.head = None
      self.tail = None
    else:
      delete_node = self.head
      self.head = delete_node.next
      delete_node.next = None
      self.length -= 1
      return print(delete_node.value)
    self.show_elements()
  #Método 5: Eliminar el último elemento de la linkedList
  def pop(self):
    if self.length == 0:
      self.head = None
      self.tail = None
    else:
      #Recorremos toda la lista para identificar el último elemento
      current_node = self.head
      new_tail = current_node
      while current_node.next != None:
        new_tail = current_node
        current_node = current_node.next
      self.tail = new_tail
      self.tail.next = None
      self.length -= 1
      return print(current_node.value)
    self.show_elements()

  def punto2(self):
    index = int(input('       Ingresa el indice: '))
    if index == 0:
      return self.shift()
    elif index == self.length -1:
      return self.pop()
    elif not index>=self.length or index < 0:
      preview_node = self.get(index-1)
      delete_node = preview_node.next
      preview_node.next = delete_node.next
      delete_node.next = None
      self.new_node_pow(delete_node)
      self.length -= 1
    else:
      return None
  
  def new_node_pow(self, delete_node):
    node_pow = math.pow(int(delete_node.value),2)
    node_n =self.Node(node_pow)
    if self.head == None and self.tail == None:
      self.head = node_n
      self.tail = node_n
    else:
      self.tail.next = node_n
      self.tail = node_n
    self.length +=1

  def punto_3(self):
    reverse_nodes = None
    current_node= self.head
    self.tail = current_node
    while current_node != None:
      next = current_node.next
      current_node.next = reverse_nodes
      reverse_nodes = current_node
      current_node = next
    self.head = reverse_nodes
    return self.head


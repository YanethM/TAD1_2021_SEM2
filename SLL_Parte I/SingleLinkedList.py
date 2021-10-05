class Single_Linked_List:
  class Node:
    #Creamojs el método inicializador de la clasr nodo
    def __init__(self,value):
      self.value = value
      self.next = None
  #Creamos el méotod inicializador de la clase Single_Linked_List
  def __init__(self):
    self.head = None
    self.tail = None
    self.lenght = 0
  #Mostrar los elementos que conforman nuestra lista
  def show_elements(self):
    array= []
    current_node = self.head
    while current_node != None:
      #Mientras si exista un elemento en la cabeza de la lista, el valor se añade a la lista array
      array.append(current_node.value)
      current_node = current_node.next
    return print(array)

  #Método 2: Agregar un elemento al inicio de la Single_Linked_List
  def prepend(self,value):
    new_node = self.Node(value)
    #Si la lista no contiene elementos, la cabeza y cola pasan a valor lo mismo
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    #Actualizamos el tamaño de la lista
    self.lenght += 1
  
  #Método 3: Agregar elemento al final de la lista
  def append(self, value):
    new_node = self.Node(value)
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.lenght +=1
  #Método 4: Eliminar el primer elemento de la linkedList
  def shift(self):
    if self.lenght == 0:
      self.head = None
      self.tail = None
    else:
      delete_node = self.head
      self.head = delete_node.next
      delete_node.next = None
      self.lenght -= 1
      return print(delete_node.value)
  #Método 5: Eliminar el último elemento de la linkedList
  def pop(self):
    if self.lenght == 0:
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
      self.lenght -= 1
      return print(current_node.value)
  #Método 6: Consultar valor de un nodo a partir del indice que ingrese User
  def get(self, index):
    if index == self.lenght -1:
      print(self.tail.value)
      return self.tail
    if index == 0:
      print(self.head.value)
      return self.head
    elif not(index >= self.lenght or index <0):
      current_node = self.head
      visit_node_count = 0
      while visit_node_count != index:
        current_node = current_node.next
        visit_node_count += 1
      print(current_node.value)
      return current_node
    else:
      return None
  
  #Método 7: Actualizar el valor que contiene el nodo consultado
  def update(self, index, value):
    update_node = self.get(index)
    #Validamos si si encontramos el nodo
    if update_node != None:
      update_node.value = value
    #De lo contrario, no se encontro el nodo
    else:
      return None

  #Método 8: Insertar nodo en determinada posición
  def insert(self, index, value):
    if index == self.lenght -1:
      #Se añadira el elemento al final de la linkedlist
      return self.append(value)
    elif not index >= self.lenght or index < 0:
      new_node = self.Node(value)
      preview_node = self.get(index)
      next_node = preview_node.next
      preview_node.next = new_node
      new_node.next = next_node
      self.lenght += 1
    else:
      return None
  
  #Método 9:Eliminar un elemento determinado
  def remove(self, index):
    if index == 0:
      return self.shift()
    elif index == self.lenght -1:
      return self.pop()
    elif not index>=self.lenght or index < 0:
      preview_node = self.get(index - 1)
      delete_node = preview_node.next
      preview_node.next = delete_node.next
      delete_node.next = None
      self.lenght -= 1
      return delete_node
    else:
      return None

      


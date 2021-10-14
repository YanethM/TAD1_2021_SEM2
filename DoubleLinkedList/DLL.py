class DoubleLinkedLinkd:
  class Nodo:
    #Constructor de la clase nodo
    def __init__(self, value):
      self.value = value
      self.previous_node = None
      self.next_node = None
  #Constructor de la clase DoubleLinkeLis
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  def show_elements_list(self):
    array=[]
    current_node = self.head
    #Mientras si exista al menos un nodo entonces
    while(current_node != None):
      array.append(current_node.value)
      current_node = current_node.next_node
    return print(array)

  def append(self, value):
    new_node = self.Nodo(value)
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next_node = new_node
      new_node.previous_node = self.tail
      self.tail = new_node
    self.length += 1
    return print(new_node.value)

  def unshift(self, value):
    new_node = self.Nodo(value)
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = self.head
    else:
      self.head.previous_node = new_node
      new_node.next_node = self.head
      self.head = new_node
    self.length +=1
    return print(new_node.value)

  def pop(self):
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      remove_node = self.tail
      self.tail = remove_node.previous_node
      self.tail.next_node = None
      remove_node.previous_node = None
      self.length -= 1
      return remove_node.value
  
  def shift(self):
    if self.length == 1:
      self.head = None
      self.tail = None
    elif self.head != None:
      remove_node = self.head
      self.head = remove_node.next_node
      remove_node.previous_node = None
      self.length -= 1
      return remove_node.value
    else:
      return None
  
  def get(self, index):
    cont_posicion = 1
    if index == self.length-1:
      print(self.tail.value)
      return self.tail
    elif index == 1:
      print(self.head.value)
      return self.head
    elif not (index < 1 or index > self.length):
      current_node = self.head
      while cont_posicion != index:
        current_node = current_node.next_node
        cont_posicion += 1
      print(current_node.value)
      return current_node
    else:
      return None

  def set(self, index, value):
    update_node = self.get(index)
    if update_node != None:
      update_node.value = value
    else:
      return None


  def insert(self, index, value):
        # Agrega un elemento en donde sea en la linkedlist dado el index
        if index == self.length - 1:
            return self.append(value)
        elif not (index >= self.length or index < 0):
            new_node = self._Nodo(value)
            ant_nodes = self.get(index)
            sig_node = ant_nodes.next_node
            ant_nodes.next_node = new_node
            new_node.nodo_anterior = ant_nodes
            new_node.next_node = sig_node
            sig_node.nodo_anterior = new_node
            self.length += 1
        else:
            return None
  def remove(self, index):
      # Saca un elemento de donde sea de la linkedlist dado un indice
      if index == 0:
          return self.shift()
      elif index == self.length - 1:
          return self.pop()
      elif not (index >= self.length or index < 0):
          delete_node = self.get(index)
          ant_nodes = delete_node.previous_node
          sig_node = delete_node.next_node
          ant_nodes.next_node = sig_node
          sig_node.previous_node  = ant_nodes
          delete_node.previous_node = None
          delete_node.next_node = None
          self.length -= 1
          return delete_node
      else:
          return None

  def reverse(self):
      # Revierte los nodos de la linkedlist
      linkes_list_reverse = None
      current_node = self.head
      self.tail = current_node
      while current_node != None:
          linkes_list_reverse = current_node.previous_node
          current_node.previous_node = current_node.next_node
          current_node.next_node = linkes_list_reverse
          current_node = current_node.previous_node
      self.head = linkes_list_reverse.previous_node



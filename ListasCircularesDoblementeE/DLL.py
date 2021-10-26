class Circular_Double_Linked_List:
  class _Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.previous_node = None
        self.next_node = None

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def show_circular_list(self):
    # Muestra los elementos de la linkedlist
    array = []
    current_node = self.head
    pivote = True
    contador = self.length
    while contador != 0:
      #Hay más de un nodo en la lista
        if pivote != False or current_node != self.head:
            array.append(current_node.valor)
            current_node = current_node.next_node
            pivote = False
            #Disminuimos el contador debido a que son menos nodos por visitar en la linkedlIST 
            contador -=1 
        else:
            break
    return print(array)
      
  def prepend(self, valor):
    # Agrega un elemento al principio de la linkedlist
    nuevo_nodo = self._Nodo(valor)
    if self.head == None and self.tail == None:
        self.head = nuevo_nodo
        self.tail = nuevo_nodo
    else:
        self.head.previous_node = nuevo_nodo
        nuevo_nodo.next_node = self.head
        self.tail.next_node = nuevo_nodo
        nuevo_nodo.previous_node = self.tail
        self.head = nuevo_nodo
    self.length += 1
  def append(self, valor):
      # Agrega un elemento al final de la linkedlist
      nuevo_nodo = self._Nodo(valor)
      if self.head == None and self.tail == None:
          self.head = nuevo_nodo
          self.tail = nuevo_nodo
      else:
          self.tail.next_node = nuevo_nodo
          nuevo_nodo.previous_node = self.tail
          nuevo_nodo.next_node = self.head 
          self.head.previous_node = nuevo_nodo
          self.tail = nuevo_nodo
      self.length += 1
  def shift(self):
      # Saca el primer elemento de la linkedlist
      if self.length == 0:
          self.head = None
          self.tail = None
      else:
          nodo_eliminado = self.head
          self.head = nodo_eliminado.next_node
          self.head.previous_node = self.tail
          self.tail.next_node = self.head
          nodo_eliminado.previous_node = None
          nodo_eliminado.next_node = None
          self.length -= 1
          return print(nodo_eliminado.valor)
  def pop(self):
      # Saca el ultimo elemento de la linkedlist
      if self.length == 0:
          self.head = None
          self.tail = None
      else:
          nodo_eliminado = self.tail
          self.tail = nodo_eliminado.previous_node
          self.tail.next_node = self.head
          self.head.previous_node = self.tail
          nodo_eliminado.previous_node = None
          nodo_eliminado.next_node = None
          self.length -= 1
          return print(nodo_eliminado.valor)
  def get(self, indice):
      # Obtiene un nodo dado un indice
      if indice == self.length-1:
          print(self.tail.valor)
          return self.tail
      elif indice == 0:
          print(self.head.valor)
          return self.head
      elif not (indice >= self.length or indice < 0):
          indice_balanceado = int(self.length / 2)
          if indice <= indice_balanceado:
              current_node = self.head
              contador = 0
              while contador != indice:
                  current_node = current_node.next_node
                  contador += 1
              print(current_node.valor)
              return current_node
          else:
              current_node = self.tail
              contador = self.length - 1
              while contador != indice:
                  current_node = current_node.previous_node
                  contador -= 1
              print(current_node.valor)
              return current_node
      else:
          return None
  def update(self, indice, valor):
      # Cambia el valor de un nodo dado el indice
      nodo_objetivo = self.get(indice)
      if nodo_objetivo != None:
          nodo_objetivo.valor = valor
      else:
          return None

  def insert(self, indice, valor):
      # Agrega un elemento en donde sea en la linkedlist dado el indice
      if indice == self.length - 1:
        return self.append(valor)
      elif indice == 0:
        return self.prepend(valor)
      elif not (indice >= self.length or indice < 0):
        nuevo_nodo = self._Nodo(valor)
        nodos_anteriores = self.get(indice-1)
        nodos_siguientes = nodos_anteriores.next_node
        nodos_anteriores.next_node = nuevo_nodo
        nuevo_nodo.previous_node = nodos_anteriores
        nuevo_nodo.next_node = nodos_siguientes
        nodos_siguientes.previous_node = nuevo_nodo
        self.length += 1
      else:
          return None


  def remove(self, indice):
      # Saca un elemento de donde sea de la linkedlist dado un indice
      if indice == 0:
          return self.shift()
      elif indice == self.length - 1:
          return self.pop()
      elif not (indice >= self.length or indice < 0):
          nodo_removido = self.get(indice-1)
          nodos_anteriores = nodo_removido.previous_node
          nodos_siguientes = nodo_removido.next_node
          nodos_anteriores.next_node = nodos_siguientes
          nodos_siguientes.previous_node  = nodos_anteriores
          nodo_removido.previous_node = None
          nodo_removido.next_node = None
          self.length -= 1
          return nodo_removido
      else:
          return None
  def reverse(self):
      # Revierte los nodos de la linkedlist
      nodos_revertidos = None
      self.head.previous_node = None
      self.tail.next_node = None
     current_node  = self.head
      self.tail = current_node
      while current_node != None:
          nodos_revertidos = current_node.previous_node
          current_node.previous_node = current_node.next_node
          current_node.next_node = nodos_revertidos
          current_node = current_node.previous_node
      self.head = nodos_revertidos.previous_node
      self.head.previous_node = self.tail
      self.tail.next_node = self.head
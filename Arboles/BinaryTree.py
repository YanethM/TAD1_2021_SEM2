class BinaryTree:

  class NodeTree:
    def __init__(self, value):
      self.value = value
      self.branch_left = None
      self.branch_right = None

  def __init__(self):
    self.root = None
    self.length = 0

  def insert_node(self, value):
    new_node = self.NodeTree(value)
    if self.root == None:
      self.root = new_node
    else:
      def tree_route(value, node):
        #Si el valor es igual que el del padre, no se debe insertar el nodo
        if value == node.value:
          return "El nodo ya existe"
        #Si el valor es menor que el del padre, debemos insertarlo al lado izq
        elif value < node.value:
          if node.branch_left == None:
            node.branch_left = new_node
            return True
          else:
            return tree_route(value, node.branch_left)
        #Si el valor es mayor que el del padre, debemos insertarlo al lado der
        elif value > node.value:
          if node.branch_right == None:
            node.branch_right = new_node
            return True
          else:
            return tree_route(value, node.branch_right)
      tree_route(value, self.root)
  
  def find_node(self, value):
    def tree_route(value, node):
      if value == node.value:
        return node.value
      elif value < node.value:
        if node.branch_left == None:
          return "No se encontro el nodo indicado"
        else:
          return tree_route(value, node.branch_left)
      else:
        if node.branch_right == None:
          return "No se encontro el nodo indicado"
        else:
          return tree_route(value, node.branch_right)
    find_node = tree_route(value, self.root)
    return print(find_node)
  
  def remove_node(self,value):
    def tree_route(value, node, previous_node):
      if value == node.value:
        if node.branch_left == None and  node.branch_right == None:
          if previous_node.branch_left != None:
            if previous_node.branch_left.value == node.value:
              previous_node.branch_left = None
          if previous_node.branch_right != None:
            if previous_node.branch_right.value == node.value:
              previous_node.branch_right = None
          node = None
        elif node.branch_left == None and node.branch_right != None:
          if previous_node.branch_left != None:
            if previous_node.branch_left.value == node.value:
              previous_node.branch_left = node.branch_right
          if previous_node.branch_right != None:
            if previous_node.branch_right.value == node.value:
              previous_node.branch_right = node.branch_right
        elif node.branch_right == None and node.branch_left != None:
          if previous_node.branch_left != None:
            if previous_node.branch_left.value == node.value:
              previous_node.branch_left = node.branch_left
          if previous_node.branch_right != None:
            if previous_node.branch_right.value == node.value:
              previous_node.branch_right = node.branch_left
        else:
          node_aux = None
          previous_node = node
          node =  node.branch_right
          if node.branch_left == None and node.branch_right != None:
            previous_node.value = node.value
            previous_node.branch_right = node.branch_right









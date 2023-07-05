class Evaluator:
  def __init__(self):
    self.env = {}
  
  def eval(self, node):
    if node.type == 'NUMBER':
      return node.value
    elif node.type == 'SYMBOL':
      return self.env[node.value]
    elif node.type == 'LIST':
      return self.eval_list(node)
    else:
      raise SyntaxError('Invalid AST node type')
  
  def evaluate_number(self, node):
    return node.value
  
  def evaluate_symbol(self, node):
    symbol = node.value
    if symbol not in self.env:
      raise ValueError('Undefined symbol: ' + symbol)
    return self.env[symbol]
  
  def evaluate_list(self, node):
    if not node.value:
      raise ValueError('Empty list')
    
    operator = node.value[0]
    arguments = node.value[1:]

    if operator.type == 'SYMBOL':
      if operator.value == 'defun':
        return self.evaluate_defun(arguments)
      else:
        return self.evaluate_function(operator, arguments)
    else:
      raise SyntaxError('Invalid operator')
    
  
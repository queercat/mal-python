class ASTNode:
  def __init__(self, type=None, value=None):
    self.type = type
    self.value = value

def parse_number(tokens):
  token_type, token_value = tokens.pop(0)
  if token_type != 'NUMBER':
    raise ValueError('Expected a number')
  return ASTNode('NUMBER', value=int(token_value))

def parse_symbol(tokens):
  token_type, token_value = tokens.pop(0)
  if token_type != 'SYMBOL':
    raise ValueError('Expected a symbol')
  return ASTNode('SYMBOL', value=token_value)

def parse_expression(tokens):
  token_type, _ = tokens[0]

  if token_type == 'NUMBER':
    return parse_number(tokens)
  elif token_type == 'SYMBOL':
    return parse_symbol(tokens)
  elif token_type == 'LPAREN':
    return parse_list(tokens)
  else:
    raise SyntaxError('Invalid expression')
  
def parse_list(tokens):
  token_type, _ = tokens.pop(0)
  if token_type != 'LPAREN':
    raise ValueError('Expected an opening parenthesis')
  
  elements = []
  while tokens[0][0] != 'RPAREN':
    elements.append(parse_expression(tokens))

  token_type, _ = tokens.pop(0)
  if token_type != 'RPAREN':
    raise ValueError('Expected a closing parenthesis')

  return ASTNode(type='LIST', value=elements)
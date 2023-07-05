import re

def tokenize(code):
  patterns = [
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'[+-]?\d+', 'NUMBER'),
    (r'[a-zA-Z_+\-*/=<>?!@#$%^&~][\w+\-*/=<>?!@#$%^&~]*', 'SYMBOL'),
  ]

  # Split the code into tokens.
  tokens = []
  while code:
    match = None
    for pattern, tag in patterns:
      match = re.match(pattern, code)
      if match:
        tokens.append((tag, match.group()))
        code = code[match.end():]
        break
    if not match:
      if code[0] == ' ':
        code = code[1:]
      else:
        raise Exception('Unexpected character: ' + code[0])
    
  return tokens
from tokenizer import tokenize
import unittest

class TestTokenizer(unittest.TestCase):
    def test_tokenize_basic(self):
        code = "(defun square (x) (* x x)) (square 5)"
        expected_tokens = [
            ('LPAREN', '('),
            ('SYMBOL', 'defun'),
            ('SYMBOL', 'square'),
            ('LPAREN', '('),
            ('SYMBOL', 'x'),
            ('RPAREN', ')'),
            ('LPAREN', '('),
            ('SYMBOL', '*'),
            ('SYMBOL', 'x'),
            ('SYMBOL', 'x'),
            ('RPAREN', ')'),
            ('RPAREN', ')'),
            ('LPAREN', '('),
            ('SYMBOL', 'square'),
            ('NUMBER', '5'),
            ('RPAREN', ')')
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

    def test_tokenize_complex(self):
        code = "(+ 1 (- 5 2) (* 3 4) (/ 10 2))"
        expected_tokens = [
            ('LPAREN', '('),
            ('SYMBOL', '+'),
            ('NUMBER', '1'),
            ('LPAREN', '('),
            ('SYMBOL', '-'),
            ('NUMBER', '5'),
            ('NUMBER', '2'),
            ('RPAREN', ')'),
            ('LPAREN', '('),
            ('SYMBOL', '*'),
            ('NUMBER', '3'),
            ('NUMBER', '4'),
            ('RPAREN', ')'),
            ('LPAREN', '('),
            ('SYMBOL', '/'),
            ('NUMBER', '10'),
            ('NUMBER', '2'),
            ('RPAREN', ')'),
            ('RPAREN', ')')
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)
if __name__ == '__main__':
    unittest.main()
import re

class LexicalAnalyzer:
    def __init__(self):
        self.token_rules = [
            ('WHITESPACE', r'\s+'),
            ('KEYWORD', r'\b(if|while|int|return|for|else|elif|void|char|float)\b'),
            ('OPERATOR', r'(==|!=|<=|>=|\+=|\-=|\*=|\/=|[\+\-\*\/\%=])'),
            ('FLOAT', r'\b\d+\.\d+\b'),
            ('NUMBER', r'\b\d+\b'),
            ('DELIMITER', r'[;,\(\)\{\}\[\]]'),
            ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9_]*'),
            ('ERROR', r'.')
        ]
        master = '|'.join('(?P<' + name + '>' + pattern + ')' for name, pattern in self.token_rules)
        self.regex = re.compile(master)

    def tokenize(self, code):
        tokens = []
        line_num = 1
        line_start = 0

        for match in self.regex.finditer(code):
            token_type = match.lastgroup
            token_value = match.group()
            start_index = match.start()
            col_num = start_index - line_start + 1

            if '\n' in token_value:
                line_num += token_value.count('\n')
                last_nl = token_value.rfind('\n')
                line_start = start_index + last_nl + 1

            if token_type == 'WHITESPACE':
                continue

            tokens.append({
                'lexeme': token_value,
                'token_type': token_type,
                'line': line_num,
                'column': col_num
            })

        return tokens
if __name__ == "__main__":
    analyzer = LexicalAnalyzer()
    code = "int x = 5; float y = 3.14;"
    result = analyzer.tokenize(code)
    
    print("=" * 50)
    print("LEXICAL ANALYSIS RESULT")
    print("=" * 50)
    print("Lexeme    | Token Type | Line | Column")
    print("-" * 45)
    
    for token in result:
        lexeme = token['lexeme']
        token_type = token['token_type']
        line = token['line']
        col = token['column']
        print(lexeme + " " * (10 - len(lexeme)) + "| " + token_type + " " * (11 - len(token_type)) + "| " + str(line) + "    | " + str(col))
    
    print("=" * 50)
    print("Total Tokens: " + str(len(result)))
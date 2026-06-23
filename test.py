from lexer import LexicalAnalyzer

analyzer = LexicalAnalyzer()

print("=" * 50)
print("LEXICAL ANALYZER - TEST RESULT")
print("=" * 50)

code = "int x = 5; float y = 3.14;"
tokens = analyzer.tokenize(code)

print("\nLexeme    | Token Type | Line | Column")
print("-" * 45)
for t in tokens:
    lexeme = t['lexeme']
    token_type = t['token_type']
    line = t['line']
    col = t['column']
    print(lexeme + " " * (10 - len(lexeme)) + "| " + token_type + " " * (11 - len(token_type)) + "| " + str(line) + "    | " + str(col))
print("-" * 45)
print("Total Tokens: " + str(len(tokens)))
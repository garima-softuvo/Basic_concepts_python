#Understanding Lexers
from pygments import lexers
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# lexers splits the code into tokens (identifier, keyword, literal etc)

# lex = lexers.get_lexer_by_name("python")
# print(lex)
lex1 = list(get_all_lexers())
print(lex1)
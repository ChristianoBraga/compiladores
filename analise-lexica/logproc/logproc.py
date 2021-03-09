# ------------------------------------------------------------
# Processing a log file
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'TIMESTAMP',
    'PROC',
    'MESSAGE'
] 

def t_TIMESTAMP(t):
    r'(\d\d):(\d\d):(\d\d).(\d\d\d\d\d\d)\ \-0300'
    return t

def t_PROC(t):
    r'\t[a-zA-Z\- \±\:\[\]\.]+\t'
    t.value = t.value[1:len(t.value) - 1]
    return t

def t_MESSAGE(t):
    r'[ a-zA-Z0-9:\_\.\:\;\[\]\=\,\<\>\{\}\(\)\-\+\'(\n)*\|\"/!\#\?\@\%\±]+\n'
    t.value = t.value[:len(t.value) - 1]
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


class LogProcLexer:
    data = None
    lexer = None
    def __init__(self):
        fh = open("log", 'r')
        self.data = fh.read()
        fh.close()
        self.lexer = lex.lex()
        self.lexer.input(self.data)

    def tokenize(self):
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            print(tok)
        
    def collect_messages(self):
        messages = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            if tok.type == 'PROC':
                if tok.value == 'kernel':
                    tok = self.lexer.token()
                    messages.append(tok)
        return messages

if __name__ == '__main__':
    print(LogProcLexer().tokenize())
                

    

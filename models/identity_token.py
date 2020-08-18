from automata.fa.dfa import DFA


class Token:
    def __init__(self):
        self.__value_format = ""
        self.__vtokens = []
        self.__dfa_id = DFA(
            states={'q0', 'q1', 'q2'},
            input_symbols={'L', 'd'},
            transitions={
                'q0': {'L': 'q1', 'd': 'q2'},
                'q1': {'L': 'q1', 'd': 'q1'},
                'q2': {'L': 'q2', 'd': 'q2'}
            },
            initial_state='q0',
            final_states={'q1'}
        )

        self.__dfa_num = DFA(
            states={'q0', 'q1', 'q2', 'q3'},
            input_symbols={'d', '.'},
            transitions={
                'q0': {'d': 'q1', '.': 'q3'},
                'q1': {'d': 'q1', '.': 'q2'},
                'q2': {'d': 'q2', '.': 'q3'},
                'q3': {'d': 'q3', '.': 'q3'}
            },
            initial_state='q0',
            final_states={'q1', 'q2'}
        )
        self.__dfa_op_arit = DFA(
            states={'q0', 'q1', 'q2'},
            input_symbols={'+', '-', '*', '/'},
            transitions={
                'q0': {'+': 'q1', '-': 'q1', '*': 'q1', '/': 'q1'},
                'q1': {'+': 'q2', '-': 'q2', '*': 'q2', '/': 'q2'},
                'q2': {'+': 'q2', '-': 'q2', '*': 'q2', '/': 'q2'}
            },
            initial_state='q0',
            final_states={'q1'}
        )
        self.__dfa_op_asign = DFA(
            states={'q0', 'q1', 'q2'},
            input_symbols={'='},
            transitions={
                'q0': {'=': 'q1'},
                'q1': {'=': 'q2'},
                'q2': {'=': 'q2'}
            },
            initial_state='q0',
            final_states={'q1'}
        )


    @property
    def value_format(self):
        return self.__value_format

    @value_format.setter
    def value_format(self, value):
        self.__value_format = value

    #lista con cada token en formato value_format
    def vtokens(self):
        return self.__vtokens

    #retorna la lista de tokens en formato L,d,+-,...
    def vtokens(self, value):
        self.__vtokens = value

    @staticmethod
    def format_string(value: str):
        format_str = ""
        for s in value:
            if s.isalpha():
                s = "L"
            elif s.isdigit():
                s = "d"
            elif s in "+-*/":
                s = "op_arit"
            format_str += s
        return format_str

    #agrego al atributo lista vtokens correspondiente de la entrada en value_formato
    def split_add_vtokens(self, value: []):
        self.__vtokens = self.__value_format.split(" ")

    #verifico para cada tokens en __vtokens si es aceptado por los dfa y su despliege
    def verified_tokens(self, value: []):
        for token in self.__vtokens:
            if token.validate_token_id():
                print(str(token)+" : <id>")
            elif token.validate_token_num:
                print(str(token)+" : <num>")
            elif token.validate_token_op_arit:
                print(str(token) + " : <op_arit>")
            elif token.validate_token_op_asign:
                print(str(token) + " : <op_asign>")
            else:
                print(str(token) + ": <unknown>")

    def validate_token_id(self):
        return self.__dfa_id.accepts_input(self.value_format)

    def validate_token_num(self):
        return self.__dfa_num.accepts_input(self.value_format)

    def validate_token_op_arit(self):
        return self.__dfa_op_arit.accepts_input(self.value_format)

    def validate_token_op_asign(self):
        return self.__dfa_op_asign.accepts_input(self.value_format)

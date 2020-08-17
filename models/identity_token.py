from automata.fa.dfa import DFA


class Token:
    def __init__(self):
        self.__value_format = None
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
            states={},
            input_symbols={'d', '.'},
            transitions={},
            initial_state='q0',
            final_states={}
        )
        self.__dfa_op_arit = DFA(
            states={},
            input_symbols={'+', '-', '*', '/'},
            transitions={},
            initial_state='q0',
            final_states={}
        )
        self.__dfa_op_asign = DFA(
            states={},
            input_symbols={'='},
            transitions={},
            initial_state='q0',
            final_states={}
        )

    @property
    def value_format(self):
        return self.__value_format

    @value_format.setter
    def value_format(self, value):
        self.__value_format = value

    def format_string(self, value: str):
        for s in value:
            if s.isalpha():
                s = "L"
            elif s.isdigit():
                s = "d"
            elif s in "+-*/":
                s = "op_arit"
            self.value_format += s

    def validate_token_id(self):
        return self.__dfa_id.accepts_input(self.value_format)

    def validate_token_num(self, value: str):
        return self.__dfa_num.accepts_input(self.value_format)

    def validate_token_op_arit(self):
        return self.__dfa_op_arit.accepts_input(self.value_format)

    def validate_token_op_asign(self):
        return self.__dfa_op_asign.accepts_input(self.value_format)

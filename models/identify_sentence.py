from automata.fa.dfa import DFA
from .identity_token import Token


class Sentence(Token):

    def __init__(self):
        Token.__init__(self)
        self.__dfa_sentence = DFA(
            states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'},
            input_symbols={'L', 'd', '.', 'op_arit', '='},
            transitions={
                'q0': {'L': 'q1', 'd': 'q10', '.': 'q10', 'op_arit': 'q10', '=': 'q10'},
                'q1': {'L': 'q1', 'd': 'q1', '.': 'q10', 'op_arit': 'q10', '=': 'q2'},
                'q2': {'L': 'q3', 'd': 'q4', '.': 'q10', 'op_arit': 'q10', '=': 'q10'},
                'q3': {'L': 'q3', 'd': 'q3', '.': 'q10', 'op_arit': 'q6', '=': 'q10'},
                'q4': {'L': 'q10', 'd': 'q4', '.': 'q5', 'op_arit': 'q10', '=': 'q10'},
                'q5': {'L': 'q10', 'd': 'q5', '.': 'q10', 'op_arit': 'q6', '=': 'q10'},
                'q6': {'L': 'q7', 'd': 'q8', '.': 'q5', 'op_arit': 'q10', '=': 'q10'},
                'q7': {'L': 'q7', 'd': 'q7', '.': 'q10', 'op_arit': 'q10', '=': 'q10'},
                'q8': {'L': 'q10', 'd': 'q8', '.': 'q9', 'op_arit': 'q10', '=': 'q10'},
                'q9': {'L': 'q10', 'd': 'q9', '.': 'q10', 'op_arit': 'q10', '=': 'q10'},
                'q10': {'L': 'q10', 'd': 'q10', '.': 'q10', 'op_arit': 'q10', '=': 'q10'}
            },
            initial_state='q0',
            final_states={'q3', 'q4', 'q5', 'q7', 'q8', 'q9'}
        )

    def validate_sentence(self):
        return self.__dfa_sentence.accepts_input(self.value_format)

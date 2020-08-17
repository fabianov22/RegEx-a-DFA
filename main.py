from automata.fa.dfa import DFA
"""
dfa = DFA(

    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'},
    input_symbols={'L', 'd', '.', 'op_arit', '='},
    transitions={
        'q0': {'L': 'q1', 'd': 'q0', '.': 'q0', 'op_arit': 'q0', '=': 'q0'},
        'q1': {'L': 'q1', 'd': 'q1', '.': 'q0', 'op_arit': 'q0', '=': 'q2'},
        'q2': {'L': 'q3', 'd': 'q4', '.': 'q0', 'op_arit': 'q0', '=': 'q0'},
        'q3': {'L': 'q1', 'd': 'q0', '.': 'q0', 'op_arit': 'q0', '=': 'q0'},
        'q4': {'0': 'q2', '1': 'q1'},
        'q5': {'0': 'q2', '1': 'q1'},
        'q6': {'0': 'q2', '1': 'q1'},
        'q7': {'0': 'q2', '1': 'q1'},
        'q8': {'0': 'q2', '1': 'q1'},
        'q9': {'0': 'q2', '1': 'q1'},
        'q10': {'L': 'q10', 'd': 'q10', '.': 'q10', 'op_arit': 'q10', '=': 'q10'}
    },
    initial_state = 'q0',
    final_states = {'q3', 'q4', 'q5', 'q7', 'q8', 'q9'}
)
"""

new_string = ""
string = input("Ingrese la entrada: ")
for s in string:
    if s.isalpha():
        s = "L"
    elif s.isdigit():
        s = "d"
    elif s in "+-*/":
        s = "op_arit"
    else:
        s = "?"
    new_string += s

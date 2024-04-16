def generate_truth_table(operation):
    variables = set(operation)
    variables = sorted(variables)
    num_vars = len(variables)
    table = []

    for i in range(2 ** num_vars):
        row = []
        for j in range(num_vars):
            row.append((i // (2 ** (num_vars - 1 - j))) % 2)
        table.append(row)

    truth_values = []
    for row in table:
        value = eval(operation, dict(zip(variables, row)))
        truth_values.append(value)

    return variables, table, truth_values

def first_canonical_form(operation, truth_values):
    variables = set(operation)
    variables = sorted(variables)
    num_vars = len(variables)
    canonical_form = ''

    for i in range(len(truth_values)):
        if truth_values[i] == 1:
            term = ''
            for j in range(num_vars):
                if table[i][j] == 0:
                    term += variables[j] + "'"
                else:
                    term += variables[j]
            canonical_form += term + ' + '

    return canonical_form[:-3]

def second_canonical_form(variables, truth_values):
    num_vars = len(variables)
    canonical_form = ''
    for i in range(len(truth_values)):
        if truth_values[i] == 0:
            term = ''
            for j in range(num_vars):
                if table[i][j] == 1:
                    term += variables[j] + "'"
                else:
                    term += variables[j]
            canonical_form += '(' + term + ') * '

    return canonical_form[:-3]

operation = input("Entrez l'opération logique (en utilisant 'and', 'or', 'not', 'xor', etc.) : ")
variables, table, truth_values = generate_truth_table(operation)
print("Table de vérité :")
for row in table:
    print(row, '=', eval(operation, dict(zip(variables, row))))
print("Première forme canonique :", first_canonical_form(operation, truth_values))
print("Deuxième forme canonique :", second_canonical_form(variables, truth_values))

# dictionary data structure with list as value
# input key value pair
# output key value pair(but with one terminal or two non terminal symbols)
# Cases if one terminal symbol in production leave it
# if two terminal symbol represent each terminal symbol by non terminal symbol and such that we get two new entry into the grammar 
# if more then two symbols in RHS take the first two and represent it with arbitrary non terminal symbol hence new entry to the grammar

# grammar = {"S": ["NP", "VP"], "S": ["Aux", "NP", "VP"], "S": ["VP"], "NP": ["Pronoun"], "NP": ["Proper-Noun"], "NP":["Det Nominal"], "Nominal": ["Noun"], "Nominal": ["Nominal Noun"], "Nominal": ["Nominal PP"]}
# problems:
# dictionary data structure was not valid choice since it treats elements in the form of hash each key has its hash identification id 
# so any thing represented by hash will be replaced by upcoming one.

# Hence i will move to tuple of value and list pair
grammar = [["S", ["NP", "VP"]], ["S",["Aux", "NP", "VP"]], ["S", ["VP"]], ["NP", ["Pronoun"]], ["NP", ["Proper-Noun"]], ["NP",["Det Nominal"]], ["Nominal", ["Noun"]], ["Nominal", ["Nominal Noun"]], ["Nominal", ["Nominal PP"]]]

# also include which are terminal symbols and which are non terminal symbols
def TermNonTerm(itemList): # this functions take as input one grammar rule and returns the terminal and non terminal symbols list
    vocab = {"terminal":[], "non_terminal":[]} 
    for item in itemList:
        if item.isupper():
            vocab["non_terminal"].append(item)
        else:
            vocab["terminal"].append(item)
    return vocab
print(TermNonTerm(["NP", "VP", "He", "ZT"]))

u = [["S", ["Aux", "NP", "VP", "ZT", "KT", "ST"]], ["T", ["M", "Z", "V"]], ["V", ["k", "U"]]]

def CNF_conversion(rule, counter):
    i = len(rule[1])
    new_grammar = []
    while i > 2:
        new = [f"Z{counter}",rule[1][:2]]
        rule[1] = rule[1][2:]
        rule[1].insert(0, f"Z{counter}")
        i = len(rule[1])
        new_grammar.append((new))
        counter += 1
    new_grammar.append(rule)
    return new_grammar, counter
# print(CNF_conversion(u[0], 0))


def CNF_conversion_whole(grammar):
    counter = 0
    c = []
    for item in grammar:
        new_grammar , counter = CNF_conversion(item, counter)
        print(counter)
        c = [*c, *new_grammar]
        counter += 1
    return c

print("revised grammar",CNF_conversion_whole(u))


# print(new_grammar)
# print(new, rule)

# for i, (key, value) in enumerate(grammar):
#     if len(value) <= 2:

    

# CNFconverter(grammar)

# print(grammar)
# coding: utf-8
# numero_disciplinas
# Anderson Sales

def numero_disciplinas(grade, horarios, pagas):
    lista_horarios = []
    qtd = 0
    for e in grade:
        if set(grade[e]).issubset(set(pagas)) and e not in pagas:
            if horarios[e] not in lista_horarios:
                qtd += 1
            lista_horarios.append(horarios[e])
    return qtd
    
grade = {"p1": [],
       "lp1": [],
       "ic": [],
       "calc1": [],
       "p2": ["ic", "p1", "lp1"],
       "lp2": ["ic", "p1", "lp1"],
       "grafos": ["ic", "p1", "lp1"],
       "calc2": ["calc1"],
       "edados": ["ic", "p1", "lp1", "p2", "lp2", "grafos"],
       "leda": ["ic", "p1", "lp1", "p2", "lp2", "grafos"]}


horarios= {"p1": "s082",
       "lp1": "x082",
       "ic": "i142",
       "calc1": "q082",
       "p2": "t162",
       "lp2": "s082",
       "grafos": "q082",
       "calc2": "x162",
       "edados": "x162",
       "leda": "t102"}

assert numero_disciplinas(grade, horarios, []) == 4
assert numero_disciplinas(grade, horarios, ["ic", "p1", "lp1"]) == 3
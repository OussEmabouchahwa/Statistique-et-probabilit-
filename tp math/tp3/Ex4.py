import pulp

# Création du problème
prob = pulp.LpProblem("multinationale_de_bonbon", pulp.LpMaximize)

# Variables
X = pulp.LpVariable("type_A", lowBound=0)
Y = pulp.LpVariable("type_B", lowBound=0)
Z = pulp.LpVariable("type_C", lowBound=0)

# Fonction objectif
prob += 24*X + 40*Y + 9*Z, "profit_total"

# Contraintes
prob += 500*X + 200*Y + 1000*Z <= 500, "temps_machine"
prob += (1/25)*X + (1/10)*Y + (1/50)*Z <= 45, "temps_main_oeuvre"

# Résolution
prob.solve()

# Résultats
print("Status:", pulp.LpStatus[prob.status])
print("type A =", X.varValue)
print("type B =", Y.varValue)
print("type C =", Z.varValue)
print("profit total =", pulp.value(prob.objective))
import pulp

prob = pulp.LpProblem("exemple optimisation", pulp.LpMaximize)
X= pulp.LpVariable("grande voture", 0, None)
Y= pulp.LpVariable("petieVoiture", 0, None)
prob += 16000*X + 10000*Y, "profit total"
prob += 1*X + 1*Y <= 400, "caoutchouc"
prob += 2*X + 1*Y <= 600, "acier"
prob.solve()
print("Status:", pulp.LpStatus[prob.status])
print("grande voture = ", X.varValue)
print("petieVoiture = ", Y.varValue)
print("profit total = ", pulp.value(prob.objective))

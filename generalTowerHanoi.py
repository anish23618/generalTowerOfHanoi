from ortools.sat.python import cp_model

#######################################################################
# Algorithm to solve generalized Tower of Hanoi.
# Only variables are:
# - NO_PILLER: int          : number of pillar to consider,
# - NO_DISC: int            : number of disc to consider,
# - MAX_RUN_TIME : float    : maximum no. of seconds to run,
# At the beginning, all the discs are placed on first pillar.
# At the end, we want all the disc to be on the last pillar.
#######################################################################
# Example:
# for NO_PILLER = 4,NO_DISC = 4, the solution is
# [0 1 2 3][][][]
# [1 2 3][][][0]
# [2 3][][1][0]
# [3][2][1][0]
# [3][2][0 1][]
# [][2][0 1][3]
# [0][2][1][3]
# [0][][1][2 3]
# [0][][][1 2 3]
# [][][][0 1 2 3]
#
# Each bracket represts a pillar. 
# The number within them represent the disc, 
# where lower no. represts smaller diameter.
########################################################################

NO_PILLER = 4
NO_DISC = 4
MAX_RUN_TIME = 30.0
NO_STEPS = 2**NO_DISC

# initializing the cpsat model
model = cp_model.CpModel()


# variables for state 
state_vars = [[[model.NewBoolVar(f'state_{t}_{i}_{j}') for j in range(NO_PILLER)] for i in range(NO_DISC)] for t in range(NO_STEPS)]
state_change_bools = [[[model.NewBoolVar(f'state_{t}_{i}_{j}') for j in range(NO_PILLER)] for i in range(NO_DISC)] for t in range(NO_STEPS-1)]

# initializing 
for i in range(NO_DISC):
    model.Add(state_vars[0][i][0]==1)
    for j in range(1,NO_PILLER):
        model.Add(state_vars[0][i][j]==0)

# final
for i in range(NO_DISC):
    model.Add(state_vars[-1][i][-1]==1)
    for j in range(NO_PILLER-1):
        model.Add(state_vars[-1][i][j]==0)

# inductive step
for t in range(NO_STEPS):
    if t!=NO_STEPS-1:   #rule: at a time only two state can change.
        model.Add(sum(sum(x) for x in state_change_bools[t])<=2)
    for i in range(NO_DISC):
        model.Add(sum(state_vars[t][i])==1)     #rule: each disc must lie in one piller
        for j in range(NO_PILLER):
            if t!=NO_STEPS-1:
                # flagging when a state is changed
                model.Add(state_vars[t][i][j]!=state_vars[t+1][i][j]).OnlyEnforceIf(state_change_bools[t][i][j])
                model.Add(state_vars[t][i][j]==state_vars[t+1][i][j]).OnlyEnforceIf(state_change_bools[t][i][j].Not())
                ##################################
                #rule: only the smallest disc can be removed from a given piller, and a smaller disc can be added to a given piller.
                # both of these are encoded in same equation.
                model.Add(sum(x[j] for x in state_vars[t][:i])==0).OnlyEnforceIf(state_change_bools[t][i][j])

# minimizing total no. of moves
wt_total_moves = sum(0.95**i*sum(sum(y) for y in x) for i,x in enumerate(state_change_bools))
model.Minimize(wt_total_moves)


##################
solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = MAX_RUN_TIME    # gives best solution within 30 secs.


status = solver.Solve(model)
if status in [cp_model.OPTIMAL,cp_model.FEASIBLE]:
    print('sucess')
    state = [[[solver.Value(state_vars[t][i][j]) for j in range(NO_PILLER)] for i in range(NO_DISC)] for t in range(NO_STEPS)]
    #####################
    # printing the moves given by the solver
    tmp1 = ""
    for t in range(NO_STEPS):
        res = ""
        for i in range(NO_PILLER):
            res += "["+ " ".join([str(j) for j,x in enumerate(state[t]) if x[i]==1])+"]"
        if tmp1!=res:
            print(res)
            tmp1=res
    #####################
else:
    print('failed')

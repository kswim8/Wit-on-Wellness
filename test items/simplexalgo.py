# Keren Huang

# manually coding simplex algorithm for optimization of linear systems

def simplexAlgorithm(totalCost, totalFat, totalProtein):
    fooditem1name = 'Chick-fil-A® Chicken Biscuit'
    fooditem2name = 'Hash Browns'
    fooditem3name = 'Icedream® Cone'

    # CITATION: Food nutrition facts from https://www.fastfoodmenuprices.com/chick-fil-a-nutrition/
    # CITATION: Food prices from https://www.fastfoodmenuprices.com/chick-fil-a-prices/

    # food item        calories, fat, protein, cost
    fooditem1 =        [450,    -21,  -17,    -2.19]
    fooditem2 =        [240,    -16,  -2,     -0.99]
    fooditem3 =        [170,    -4,   -5,     -1.25]
    totalCalories =    0
    solution =         [0, 0, 0, totalCost, totalFat, totalProtein]

    # more simplified labels for slackForm system
    #                calories      fat           protein       cost
    a0, a1, a2, a3 = fooditem1[0], fooditem1[1], fooditem1[2], fooditem1[3] # 'Chick-fil-A® Chicken Biscuit' (a)
    b0, b1, b2, b3 = fooditem2[0], fooditem2[1], fooditem2[2], fooditem2[3] # 'Hash Browns'                  (b)
    c0, c1, c2, c3 = fooditem3[0], fooditem3[1], fooditem3[2], fooditem3[3] # 'Icedream® Cone'               (c)

    #             constant       a   b   c    d   e   f
    slackForm = [[totalCalories, a0, b0, c0,  0,  0,  0], # calories equation
                 [totalFat,      a1, b1, c1, -1,  0,  0], # fat equation
                 [totalProtein,  a2, b2, c2,  0, -1,  0], # protein equation
                 [totalCost,     a3, b3, c3,  0,  0, -1]] # cost equation

    # if coefficient of a is positive, maximum can still be achieved; thus, find biggest constraint on a
    if 5==0:
        for i in range(1, 4):
            if slackForm[0][i] >= 0:
                listOfConstraints = []
                listOfConstraints.append(-1 * slackForm[1][0] / slackForm[1][i]) # slackForm[1][1]
                listOfConstraints.append(-1 * slackForm[2][0] / slackForm[2][i]) # slackForm[2][1]
                listOfConstraints.append(-1 * slackForm[3][0] / slackForm[3][i]) # slackForm[3][1]
                tightestConstraint = min(listOfConstraints)
                print("List of constraints:", listOfConstraints) # fat, protein, cost
                print("The tightest constraint is:", tightestConstraint) 

                # find the equation where the tighest constraint was found
                tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
                print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 

                slackForm[tightestConstraintEquation][1] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
                # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
                newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][i], # constant
                            1,                                                                                   # a
                            slackForm[tightestConstraintEquation][2] / slackForm[tightestConstraintEquation][i], # b
                            slackForm[tightestConstraintEquation][3] / slackForm[tightestConstraintEquation][i], # c
                            slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][i], # d
                            slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][i], # e 
                            slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][i]] # f
                print(newEquation) # this is the rearranged equation
                solution[0] = newEquation[0] # we need to store the current solution for a that achieves a max
                print(solution) 
                slackForm2 = [  [totalCalories + slackForm[0][i] * newEquation[0], 0, b0 + slackForm[0][i] * newEquation[2], c0 + slackForm[0][i] * newEquation[3],  0 + slackForm[0][1] * newEquation[4],  0 + slackForm[0][1] * newEquation[5],  0 + slackForm[0][1] * newEquation[6]], # calories equation
                                [totalFat + slackForm[1][i] * newEquation[0],      0, b1 + slackForm[1][i] * newEquation[2], c1 + slackForm[1][i] * newEquation[3], -1 + slackForm[1][1] * newEquation[4],  0 + slackForm[1][1] * newEquation[5],  0 + slackForm[1][1] * newEquation[6]], # fat equation
                                [totalProtein + slackForm[2][i] * newEquation[0],  0, b2 + slackForm[2][i] * newEquation[2], c2 + slackForm[2][i] * newEquation[3],  0 + slackForm[2][1] * newEquation[4], -1 + slackForm[2][1] * newEquation[5],  0 + slackForm[2][1] * newEquation[6]], # protein equation
                                [totalCost + slackForm[3][i] * newEquation[0],     0, b3 + slackForm[3][i] * newEquation[2], c3 + slackForm[3][i] * newEquation[3],  0 + slackForm[3][1] * newEquation[4],  0 + slackForm[3][1] * newEquation[5], -1 + slackForm[3][1] * newEquation[6]]] # cost equation

                slackForm2[tightestConstraintEquation][i] = 1
                slackForm2[tightestConstraintEquation] = newEquation

                print(slackForm2[0])
                print(slackForm2[1])
                print(slackForm2[2])
                print(slackForm2[3])
                slackForm = slackForm2

    if a0 >= 0:
        
        # finding tightest constraint
        listOfConstraints = []
        listOfConstraints.append(-1 * slackForm[1][0] / slackForm[1][1]) # slackForm[1][1]
        listOfConstraints.append(-1 * slackForm[2][0] / slackForm[2][1]) # slackForm[2][1]
        listOfConstraints.append(-1 * slackForm[3][0] / slackForm[3][1]) # slackForm[3][1]
        tightestConstraint = min(listOfConstraints)
        print("List of constraints:", listOfConstraints) # fat, protein, cost
        print("The tightest constraint is:", tightestConstraint) 

        # find the equation where the tighest constraint was found
        tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
        print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 

        slackForm[tightestConstraintEquation][1] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
        # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
        newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][1], # constant
                       1,                                                                                   # a
                       slackForm[tightestConstraintEquation][2] / slackForm[tightestConstraintEquation][1], # b
                       slackForm[tightestConstraintEquation][3] / slackForm[tightestConstraintEquation][1], # c
                       slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][1], # d
                       slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][1], # e 
                       slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][1]] # f
        print("The rearranged equation is:", newEquation) # this is the rearranged equation
        solution[0] = newEquation[0] # we need to store the current solution for a that achieves a max
        
        print("Current solution is:", solution) 

        slackForm2 = [  [slackForm[0][0] + slackForm[0][1] * newEquation[0], 0, slackForm[0][2] + slackForm[0][1] * newEquation[2], slackForm[0][3] + slackForm[0][1] * newEquation[3],  slackForm[0][4] + slackForm[0][1] * newEquation[4],  slackForm[0][5] + slackForm[0][1] * newEquation[5],  slackForm[0][6] + slackForm[0][1] * newEquation[6]], # calories equation
                        [slackForm[1][0] + slackForm[1][1] * newEquation[0], 0, slackForm[1][2] + slackForm[1][1] * newEquation[2], slackForm[1][3] + slackForm[1][1] * newEquation[3],  slackForm[1][4] + slackForm[1][1] * newEquation[4],  slackForm[1][5] + slackForm[1][1] * newEquation[5],  slackForm[1][6] + slackForm[1][1] * newEquation[6]], # fat equation
                        [slackForm[2][0] + slackForm[2][1] * newEquation[0], 0, slackForm[2][2] + slackForm[2][1] * newEquation[2], slackForm[2][3] + slackForm[2][1] * newEquation[3],  slackForm[2][4] + slackForm[2][1] * newEquation[4],  slackForm[2][5] + slackForm[2][1] * newEquation[5],  slackForm[2][6] + slackForm[2][1] * newEquation[6]], # protein equation
                        [slackForm[3][0] + slackForm[3][1] * newEquation[0], 0, slackForm[3][2] + slackForm[3][1] * newEquation[2], slackForm[3][3] + slackForm[3][1] * newEquation[3],  slackForm[3][4] + slackForm[3][1] * newEquation[4],  slackForm[3][5] + slackForm[3][1] * newEquation[5],  slackForm[3][6] + slackForm[3][1] * newEquation[6]]] # cost equation

        slackForm2[tightestConstraintEquation] = newEquation
        slackForm2[tightestConstraintEquation][1] = -1

        print(slackForm2[0])
        print(slackForm2[1])
        print(slackForm2[2])
        print(slackForm2[3])
        slackForm = slackForm2
        # print(slackForm)

    # if coefficient of b is positive, maximum can still be achieved; thus, find biggest constraint on b
    if b0 >= 0:
        # finding tightest constraint
        listOfConstraints = []
        listOfConstraints.append(-1 * slackForm[1][0] / slackForm[1][2]) # slackForm[1][1]
        listOfConstraints.append(-1 * slackForm[2][0] / slackForm[2][2]) # slackForm[2][1]
        listOfConstraints.append(-1 * slackForm[3][0] / slackForm[3][2]) # slackForm[3][1] 
        tightestConstraint = min(listOfConstraints)
        print("List of constraints:",listOfConstraints) # fat, protein, cost
        print("The tightest constraint is:",tightestConstraint) 

        # find the equation where the tighest constraint was found
        tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
        print("The equation with the tightest constraint is:",tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 

        slackForm[tightestConstraintEquation][1] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
        # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
        newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][2], # constant
                       slackForm[tightestConstraintEquation][1] / slackForm[tightestConstraintEquation][2], # a   
                       1,                                                                                   # b
                       slackForm[tightestConstraintEquation][3] / slackForm[tightestConstraintEquation][2], # c
                       slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][2], # d
                       slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][2], # e 
                       slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][2]] # f
        print("The rearranged equation is:", newEquation) # this is the rearranged equation
        solution[1] = newEquation[0] # we need to store the current solution for a that achieves a max
        print("Current solution is:", solution) 
        slackForm2 = [  [totalCalories + slackForm[0][1] * newEquation[0], 0, b0 + a0 * newEquation[2], c0 + a0 * newEquation[3],  0 + a0 * newEquation[4],  0 + a0 * newEquation[5],  0 + a0 * newEquation[6]], # calories equation
                        [totalFat + slackForm[1][1] * newEquation[0],      0, b1 + slackForm[1][1] * newEquation[2], c1 + slackForm[1][1] * newEquation[3], -1 + slackForm[1][1] * newEquation[4],  0 + slackForm[1][1] * newEquation[5],  0 + slackForm[1][1] * newEquation[6]], # fat equation
                        [totalProtein + slackForm[2][1] * newEquation[0],  0, b2 + slackForm[2][1] * newEquation[2], c2 + slackForm[2][1] * newEquation[3],  0 + slackForm[2][1] * newEquation[4], -1 + slackForm[2][1] * newEquation[5],  0 + slackForm[2][1] * newEquation[6]], # protein equation
                        [totalCost + slackForm[3][1] * newEquation[0],     0, b3 + slackForm[3][1] * newEquation[2], c3 + slackForm[3][1] * newEquation[3],  0 + slackForm[3][1] * newEquation[4],  0 + slackForm[3][1] * newEquation[5], -1 + slackForm[3][1] * newEquation[6]]] # cost equation
        slackForm2[tightestConstraintEquation][1] = 1
        slackForm2[tightestConstraintEquation] = newEquation

        # print(slackForm2[0])
        # print(slackForm2[1])
        # print(slackForm2[2])
        # print(slackForm2[3])
        slackForm = slackForm2
        # print(slackForm)

    # if coefficient of c is positive, maximum can still be achieved; thus, find biggest constraint on c
    if c0 >= 0:
        pass


simplexAlgorithm(20, 50, 30)
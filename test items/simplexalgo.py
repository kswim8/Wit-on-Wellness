# Keren Huang

# manually coding simplex algorithm for optimization of linear systems

# CITATION: Video at https://www.youtube.com/watch?v=RO5477EKlXE&ab_channel=OllieCrow, used only for learning conceptual simplex algorithm

def simplexAlgorithm(totalFat, totalProtein, totalCost):
    # these are the food items to be used in the puzzle menus
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
    solution =         [0, 0, 0, totalFat, totalProtein, totalCost]

    tightestConstraintA = tightestConstraintB = tightestConstraintC = None

    # more simplified labels for slackForm system
    #                calories      fat           protein       cost
    a0, a1, a2, a3 = fooditem1[0], fooditem1[1], fooditem1[2], fooditem1[3] # 'Chick-fil-A® Chicken Biscuit' (a)
    b0, b1, b2, b3 = fooditem2[0], fooditem2[1], fooditem2[2], fooditem2[3] # 'Hash Browns'                  (b)
    c0, c1, c2, c3 = fooditem3[0], fooditem3[1], fooditem3[2], fooditem3[3] # 'Icedream® Cone'               (c)

    # slackForm linear system, objective function is slackForm[0], to be maximized
    #             constant       a   b   c    d   e   f
    slackForm = [[totalCalories, a0, b0, c0,  0,  0,  0], # calories equation
                 [totalFat,      a1, b1, c1, -1,  0,  0], # fat equation
                 [totalProtein,  a2, b2, c2,  0, -1,  0], # protein equation
                 [totalCost,     a3, b3, c3,  0,  0, -1]] # cost equation

    # if coefficient of a is positive, maximum can still be achieved; thus, find biggest constraint on a
    if slackForm[0][1] >= 0:
        
        # finding tightest constraint
        listOfConstraints = []
        listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][1])) # slackForm[1][1]
        listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][1])) # slackForm[2][1]
        listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][1])) # slackForm[3][1]
        tightestConstraint = min(listOfConstraints)
        print("List of constraints:", listOfConstraints) # fat, protein, cost
        print("The tightest constraint is:", tightestConstraint) 

        # find the equation where the tightest constraint was found
        tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
        print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
        tightestConstraintA = tightestConstraintEquation

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
        solution[0] = slackForm[tightestConstraintEquation][0]
        print("Current solution is:", solution)
        # print(slackForm)
    
    # if coefficient of b is positive, maximum can still be achieved; thus, find biggest constraint on b
    if slackForm[0][2] >= 0:

        # finding tightest constraint
        listOfConstraints = []
        listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][2])) # slackForm[1][1]
        listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][2])) # slackForm[2][1]
        listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][2])) # slackForm[3][1]
        tightestConstraint = min(listOfConstraints)
        print("List of constraints:", listOfConstraints) # fat, protein, cost
        print("The tightest constraint is:", tightestConstraint) 

        # find the equation where the tighest constraint was found
        tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
        print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
        tightestConstraintB = tightestConstraintEquation

        slackForm[tightestConstraintEquation][2] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
        # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
        newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][2], # constant
                    slackForm[tightestConstraintEquation][1] / slackForm[tightestConstraintEquation][2], # a
                    1,                                                                                   # b
                    slackForm[tightestConstraintEquation][3] / slackForm[tightestConstraintEquation][2], # c
                    slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][2], # d
                    slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][2], # e 
                    slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][2]] # f
        print("The rearranged equation is:", newEquation) # this is the rearranged equation

        slackForm2 = [  [slackForm[0][0] + slackForm[0][2] * newEquation[0], slackForm[0][1] + slackForm[0][2] * newEquation[1], 0, slackForm[0][3] + slackForm[0][2] * newEquation[3],  slackForm[0][4] + slackForm[0][2] * newEquation[4],  slackForm[0][5] + slackForm[0][2] * newEquation[5],  slackForm[0][6] + slackForm[0][2] * newEquation[6]], # calories equation
                        [slackForm[1][0] + slackForm[1][2] * newEquation[0], slackForm[1][1] + slackForm[1][2] * newEquation[1], 0, slackForm[1][3] + slackForm[1][2] * newEquation[3],  slackForm[1][4] + slackForm[1][2] * newEquation[4],  slackForm[1][5] + slackForm[1][2] * newEquation[5],  slackForm[1][6] + slackForm[1][2] * newEquation[6]], # fat equation
                        [slackForm[2][0] + slackForm[2][2] * newEquation[0], slackForm[2][1] + slackForm[2][2] * newEquation[1], 0, slackForm[2][3] + slackForm[2][2] * newEquation[3],  slackForm[2][4] + slackForm[2][2] * newEquation[4],  slackForm[2][5] + slackForm[2][2] * newEquation[5],  slackForm[2][6] + slackForm[2][2] * newEquation[6]], # protein equation
                        [slackForm[3][0] + slackForm[3][2] * newEquation[0], slackForm[3][1] + slackForm[3][2] * newEquation[1], 0, slackForm[3][3] + slackForm[3][2] * newEquation[3],  slackForm[3][4] + slackForm[3][2] * newEquation[4],  slackForm[3][5] + slackForm[3][2] * newEquation[5],  slackForm[3][6] + slackForm[3][2] * newEquation[6]]] # cost equation

        slackForm2[tightestConstraintEquation] = newEquation
        slackForm2[tightestConstraintEquation][2] = -1
        

        print(slackForm2[0])
        print(slackForm2[1])
        print(slackForm2[2])
        print(slackForm2[3])
        
        slackForm = slackForm2
        solution[0] = slackForm[tightestConstraintA][0]
        solution[1] = slackForm[tightestConstraintEquation][0]
        tightestConstraintB = tightestConstraintEquation
        # print(slackForm)
        if tightestConstraintB == tightestConstraintA: solution[0] = 0

    # if coefficient of c is positive, maximum can still be achieved; thus, find biggest constraint on c
    if slackForm[0][3] >= 0:

        # finding tightest constraint
        listOfConstraints = []
        listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][3])) # slackForm[1][1]
        listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][3])) # slackForm[2][1]
        listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][3])) # slackForm[3][1]
        tightestConstraint = min(listOfConstraints)
        print("List of constraints:", listOfConstraints) # fat, protein, cost
        print("The tightest constraint is:", tightestConstraint) 

        # find the equation where the tighest constraint was found
        tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
        print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
        tightestConstraintC = tightestConstraintEquation

        slackForm[tightestConstraintEquation][3] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
        # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
        newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][3], # constant
                    slackForm[tightestConstraintEquation][1] / slackForm[tightestConstraintEquation][3], # a
                    slackForm[tightestConstraintEquation][2] / slackForm[tightestConstraintEquation][3], # b
                    1,                                                                                   # c
                    slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][3], # d
                    slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][3], # e 
                    slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][3]] # f
        print("The rearranged equation is:", newEquation) # this is the rearranged equation

        slackForm2 = [  [slackForm[0][0] + slackForm[0][3] * newEquation[0], slackForm[0][1] + slackForm[0][3] * newEquation[1], slackForm[0][3] + slackForm[0][3] * newEquation[2], 0,  slackForm[0][4] + slackForm[0][3] * newEquation[4],  slackForm[0][5] + slackForm[0][3] * newEquation[5],  slackForm[0][6] + slackForm[0][3] * newEquation[6]], # calories equation
                        [slackForm[1][0] + slackForm[1][3] * newEquation[0], slackForm[1][1] + slackForm[1][3] * newEquation[1], slackForm[1][3] + slackForm[1][3] * newEquation[2], 0,  slackForm[1][4] + slackForm[1][3] * newEquation[4],  slackForm[1][5] + slackForm[1][3] * newEquation[5],  slackForm[1][6] + slackForm[1][3] * newEquation[6]], # fat equation
                        [slackForm[2][0] + slackForm[2][3] * newEquation[0], slackForm[2][1] + slackForm[2][3] * newEquation[1], slackForm[2][3] + slackForm[2][3] * newEquation[2], 0,  slackForm[2][4] + slackForm[2][3] * newEquation[4],  slackForm[2][5] + slackForm[2][3] * newEquation[5],  slackForm[2][6] + slackForm[2][3] * newEquation[6]], # protein equation
                        [slackForm[3][0] + slackForm[3][3] * newEquation[0], slackForm[3][1] + slackForm[3][3] * newEquation[1], slackForm[3][3] + slackForm[3][3] * newEquation[2], 0,  slackForm[3][4] + slackForm[3][3] * newEquation[4],  slackForm[3][5] + slackForm[3][3] * newEquation[5],  slackForm[3][6] + slackForm[3][3] * newEquation[6]]] # cost equation

        slackForm2[tightestConstraintEquation] = newEquation
        slackForm2[tightestConstraintEquation][3] = -1

        print(slackForm2[0])
        print(slackForm2[1])
        print(slackForm2[2])
        print(slackForm2[3])
        slackForm = slackForm2
        solution[0] = slackForm[tightestConstraintA][0]
        solution[1] = slackForm[tightestConstraintB][0]
        solution[2] = slackForm[tightestConstraintEquation][0]
        # print(slackForm)
        if tightestConstraintC == tightestConstraintA: solution[0] = 0
        if tightestConstraintC == tightestConstraintB: solution[1] = 0

    
    totalCalories = slackForm[0][0]
    print("FINAL SOLUTION:", solution)
    print("TOTAL CALORIES:", totalCalories)

simplexAlgorithm(50, 30, 20)
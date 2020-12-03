# Keren Huang

# manually coding simplex algorithm for optimization of linear systems

def simplexAlgorithm(totalCost, totalFat, totalProtein):
    fooditem1name = 'Chick-fil-A® Chicken Biscuit'
    fooditem2name = 'Hash Browns'
    fooditem3name = 'Icedream® Cone'
    # food item        calories, fat, protein, cost
    fooditem1 =        [450,    -21,  -17,    -2.19]
    fooditem2 =        [240,    -16,  -2,     -0.99]
    fooditem3 =        [170,    -4,   -5,     -1.25]
    totalCalories =    0
    solution =         [0, 0, 0, totalCost, totalFat, totalProtein]

    a0, a1, a2, a3 = fooditem1[0], fooditem1[1], fooditem1[2], fooditem1[3]
    b0, b1, b2, b3 = fooditem2[0], fooditem2[1], fooditem2[2], fooditem2[3]
    c0, c1, c2, c3 = fooditem3[0], fooditem3[1], fooditem3[2], fooditem3[3]

    #             constant       a   b   c   d  e  f
    slackForm = [[totalCalories, a0, b0, c0, 0, 0, 0], # calories equation
                 [totalFat,      a1, b1, c1, 1, 0, 0], # fat equation
                 [totalProtein,  a2, b2, c2, 0, 1, 0], # protein equation
                 [totalCost,     a3, b3, c3, 0, 0, 1]] # cost equation

    if fooditem1[0] >= 0:
        # finding tightest constraint
        listOfConstraints = []
        listOfConstraints.append(-1 * totalFat / fooditem1[1])
        listOfConstraints.append(-1 * totalProtein / fooditem1[2])
        listOfConstraints.append(-1 * totalCost / fooditem1[3]) 
        tighestConstraint = min(listOfConstraints)
        print(listOfConstraints) # fat, protein, cost
        print(tighestConstraint)

        # rearrange the equation where the tighest constraint was found
        tighestConstraintEquation = listOfConstraints.index(tighestConstraint)
        print(tighestConstraintEquation)
        # since the tighest constraint here was protein, 30/17 = 1.7647, we rearrange f and fooditem1[2]
        newEquation = [1, -1 * totalProtein / fooditem1[2], fooditem2[2] / fooditem1[2], fooditem3[2] / fooditem1[2], 1 / fooditem1[2]]
        print(slackForm)

    if fooditem2[0] >= 0:
        pass

    if fooditem3[0] >= 0:
        pass


simplexAlgorithm(20, 50, 30)
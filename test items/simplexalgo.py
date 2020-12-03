def simplexAlgorithm(totalCost):
    chickfila_chicken_biscuit = [450, -21,  -17,    -2.19]
    hash_browns =               [240, -16,  -2,     -0.99]
    icedream_cone =             [170, -4,   -5,     -1.25]
    totalCalories =             0
    totalFat =                  50
    totalProtein =              30
    Z =                         0
    d = e = f =                 None
    solution =                  [0, 0, 0, totalCost, 50, 30]
    #                                                   a                      b                c
    slackForm = [[Z,       totalCalories, chickfila_chicken_biscuit[0], hash_browns[0], icedream_cone[0], 0, 0, 0],
                 [d,       totalCost,     chickfila_chicken_biscuit[3], hash_browns[3], icedream_cone[3], 0, 0, 0],
                 [e,       totalFat,      chickfila_chicken_biscuit[1], hash_browns[1], icedream_cone[1], 0, 0, 0],
                 [f,       totalProtein,  chickfila_chicken_biscuit[2], hash_browns[2], icedream_cone[2], 0, 0, 0]  ]

    while True:
        if chickfila_chicken_biscuit[0] >= 0 and hash_browns[0] >= 0 and icedream_cone[0] >= 0:
            # finding tightest constraint
            listOfConstraints = []
            listOfConstraints.append(-1 * totalCost / chickfila_chicken_biscuit[3]) 
            listOfConstraints.append(-1 * totalFat / chickfila_chicken_biscuit[1])
            listOfConstraints.append(-1 * totalProtein / chickfila_chicken_biscuit[2])
            tighestConstraint = min(listOfConstraints)
            print(tighestConstraint)

            # rearrange the equation where the tighest constraint was found
            tighestConstraintEquation = listOfConstraints.index(tighestConstraint)
            # since the tighest constraint here was protein, 30/17 = 1.7647, we rearrange f and chickfila_chicken_biscuit[2]
            newEquation = [1, -1 * totalProtein / chickfila_chicken_biscuit[2], hash_browns[2] / chickfila_chicken_biscuit[2], icedream_cone[2] / chickfila_chicken_biscuit[2], f / chickfila_chicken_biscuit[2]]

            

        else:
            break

def findTighestConstraint(slackForm):
    listOfConstraints = []
    listOfConstraints.append(totalCost / chickfila_chicken_biscuit[3]) 
    listOfConstraints.append(totalFat / chickfila_chicken_biscuit[1])
    listOfConstraints.append(totalProtein / chickfila_chicken_biscuit[2])
    tighestConstraint = min(listOfConstraints)
    print(tighestConstraint)



simplexAlgorithm(20)
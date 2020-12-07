import random

def flexibleSimplexAlgo():
    num_vars = random.choice([2, 3, 4])
    print("Number of variables:", num_vars)
    totalCalories = 0
    totalFat = random.randrange(80, 120, 5)
    totalCarbs = random.randrange(80, 120, 5)
    totalProtein = random.randrange(40, 80, 5)
    totalCost = random.randrange(10, 20, 1)

    # CITATION: https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#creating2dLists
    # generating a matrix
    def make2dList(rows, cols):
        return [ ([0] * cols) for row in range(rows) ]

    rows = num_vars + 1                 # number of equations
    cols = num_vars + 4                 # the non basic, basic variables, keeping the number of foods constant

    slackForm = make2dList(rows, cols)  # generate matrix / slack form system
    
    solution = [0, 0, 0]                # the quantities for each food, constant at 3

    tightestConstraints = [None, None, None] # tightest constraint equations

    # print("Slack Form:", slackForm)
    # print("Solution:", solution)
    # print("Tightest Constraints:", tightestConstraints) 

    # CITATION: https://www.fastfoodmenuprices.com/chick-fil-a-nutrition/
    # CITATION: https://www.fastfoodmenuprices.com/chick-fil-a-prices/
    chickfila_menu       = {   'Hash Browns': [240, -0.99, -16, -23, -2,  'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0009_%5BFeed%5D_0000s_0028_Breakfast_Hashbrowns_2.png'],
                                'Icedream® Cone': [170, -1.25, -4, -31, -5, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Drinks/Drinks%20PDP/_0000s_0027_%5BFeed%5D_0006s_0013_Drinks_Ice-Dream.png'],
                                'Grilled Nuggets': [140, -3.75, -3.5, -2, -25, 'https://www.cfacdn.com/img/order/menu/Online/Entrees/grilledNuggets_8ct_PDP.png'],
                                '1% White Milk': [90, -1.19, -2, -11, -7, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Drinks/Drinks%20PDP/_0000s_0020_%5BFeed%5D_0006s_0019_Drinks_Milk.png'],
                                'Chick-fil-A® Chicken Biscuit': [450, -2.19, -21, -50, -17, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20Desktop/_0000s_0000_Stack620_0000_CFA_1605_60_Biscuit_Chicken_PROD_2155_1240px.png'],
                                'Chick-n-Strips™': [350, -3.05, -17, -22, -28, 'https://www.cfacdn.com/img/order/menu/Online/Entrees/strips_3ct_PDP.png'],
                                'Cobb Salad': [510, -7.19, -27, -28, -40, 'https://www.cfacdn.com/img/order/menu/Online/Salads%26wraps/cobbSalad_nug_pdp.png'],
                                'Bacon, Egg & Cheese Biscuit': [420, -2.59, -21, -41, -15, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20Desktop/_0000s_0008_Bacon-Egg-Cheese-Biscuit_620_PDP.png'] }

    # Food Name = name
    # Food Info = dict[name][0], dict[name][1], dict[name][2], dict[name][3]
    foodList = []
    while len(foodList) < 3:
        newFood = random.choice(list(chickfila_menu))

        if newFood not in foodList: 
            foodList.append(newFood)

    print(foodList)
    #               [ first column is constant/total ] [second column is food1 ] [ third column is food2 ] [ fourth column is food3  ]             
    # slackForm --> [ first row is calories ] []
    #               [ second row is fat     ] []
    #               [ third row is carbs    ] []
    #               [ fourth row is protein ] []
    #               [ fifth row is cost     ] []

    # import the food data and assign them into the 2d list 
    for i in range(1, 4):
        slackForm[0][i] = chickfila_menu[foodList[i - 1]][0]

    # fat, carbs, protein, cost
    for num_eq in range(1, rows):
        foodnum = 0
        for variable in range(1, cols - num_vars):
            slackForm[num_eq][variable] = chickfila_menu[foodList[foodnum]][num_eq]
            foodnum += 1
    listOfVariables = [totalCalories, totalCost, totalFat, totalCarbs, totalProtein]
    i = 0
    for row in range(rows):
        for constraints in range(1):
            slackForm[row][0] = listOfVariables[i]
        i += 1
    print("FINAL SLACK FORM:", slackForm)

    # loop through the 3 foods
    for i in range(1, 4):
        # loop through the coefficients of the foods' calories in eq 1 (objective)
        if slackForm[0][i] >= 0:
            # create a list of constraints to find the minimum
            listOfConstraints = []
            for num_eq in range(1, rows):
                listOfConstraints.append(abs(slackForm[num_eq][0] / slackForm[num_eq][i])) 
            # finding the minimum
            tightestConstraint = min(listOfConstraints)
            print(tightestConstraint)
            tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1 # looking for the equation that is constrained
            tightestConstraints[i-1] = tightestConstraintEquation # adding the index of the equation for later to check commonality
            print(tightestConstraints)
            # checking for commonality; in the case where one needs to pivot on an already rearranged equation
            if tightestConstraints[i-1] in tightestConstraints[:i-1] or tightestConstraints[i-1] in tightestConstraints[i:]:
                # set the coefficeint in the solution equal to 0
                print("there is a commonality")
            slackForm[tightestConstraintEquation][i] *= -1




flexibleSimplexAlgo()
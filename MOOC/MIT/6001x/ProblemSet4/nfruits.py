def nfruits(quantity, fruits_eaten):
    '''
    quantity:A non-empty dictionary containing type of fruit \
        and its quantity initially with Python when he leaves home (length < 10)
    fruits_eaten:A string pattern of the fruits eaten by Python \
        on his journey as observed by Cobra.
    return: maximum of the quantities of eaten fruits.
    '''
    #deal except the last eaten fruit
    for each in fruits_eaten[:-1]:
        quantity[each] -=2
        for key in quantity.keys():
            quantity[key] += 1
    #eat the last one and will not buy
    quantity[fruits_eaten[-1]] -=1
    #maximum of the quantities of the fruits
    return max(quantity.values())
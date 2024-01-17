def calculateNetIncome(gross, state):
    """
    Calculate the net income after federal and state tax
    :param gross: Gross Income
    :param state: State Name
    :return: Net Income
    """
    state_tax = {'CA': 10, 'NY': 8, 'TX': 0, 'NJ':6}

    # Calculate net income after federal tax
    net = gross - (gross * .10)

    # Calculate net income after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net income after all the heavy taxes is: " + str(net))
        return net
    else:
        print("State not in the list")
        return None
    
# Plug in your state from the dictionary key variable "state_tax" below and adjust your gross income accordingly
calculateNetIncome(98000, 'NY')

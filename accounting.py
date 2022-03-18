MELON_COST = 1.00

def calculate_expected_total(item_amount, cost):
    """Take item amount and cost as inputs and return an expected total.

    """
    expected_total = item_amount * cost

    return expected_total

def return_first_name(name):
    """Returns first name of a name."""
    #remove left whitespace
    name = name.lstrip()
    #create new string
    first_name = ""

    #loop through name
    for char in name:
        #if it isn't a space, add to string
        if char != " ":
            first_name += char
        #if it is a space, return first name
        else:
            return first_name


def print_payment_status(file):

    #open file
    the_file = open(file)
    #loop through each line
    for line in the_file:
        #tokenize each line; list = [customer id, name, melons delivered, payment]
        tokens = line.split("|")

        #isolate first name
        name = return_first_name(tokens[1])
        #convert index 2 into a int
        melons = int(tokens[2])
        #convert into money format
        actual_payments = float(tokens[3])
        expected_payments = calculate_expected_total(melons, MELON_COST)

        #if expected payment doesn't match actual payment
        if expected_payments != actual_payments:
            #print discrepancy message
            print(f"{name.title()} paid ${actual_payments},",
                  f"expected ${expected_payments:.2f}"
                  )

    the_file.close()
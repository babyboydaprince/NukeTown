from random import choice


# Add sugar to data
def addSugar(message, sugar):
    # Vars
    cData = ''
    sugar = list(sugar)
    sugarChars = []

    # Add sugar chars to list
    for char in message:
        if char not in sugarChars:
            sugarChars.append(char)

    # Add sugar to message
    for index, secretChar in enumerate(message):
        for _ in range(int(sugar[index])):
            cData += choice(sugarChars)
        cData += secretChar

    return cData


# Remove sugar from data
def removeSugar(message, sugar):
    # Vars
    p = 0
    dData = ''

    # Remove sugar characters from string
    for secrerSugar in sugar:
        message = message[int(secrerSugar) + p:]
        # If not data - break
        if not message:
            break

        dData += message[0]
        p = 1

    return dData

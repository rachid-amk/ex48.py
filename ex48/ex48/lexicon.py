
def scan(direction):
    #direction is the parameter we given, we split it in the next line
    words = direction.split()
    #list is somthing you should know by now
    direction_words = ['north', 'east', 'south']
    verb_words = ['go', 'kill', 'eat']
    stops_words = ['the', 'in', 'of']
    nouns_words = ['bear', 'princess']
    # result is what will be retuned at the end
    result = []
    # now we try to convert string to number
    try:
        #if direction(parameter) is int than we do the code down here
        for i in words:
            inte = int(i)
            result.append(('number', inte))
        return result
    except ValueError:
        # we catch the error and do the code down here
        for i in words:
            if i in direction_words:
                result.append(('direction', i))
            elif i in verb_words:
                result.append(('verb', i))
            elif i in stops_words:
                result.append(('stop', i))
            elif i in nouns_words:
                result.append(('noun', i))
            else:
                result.append(('error', i))
        return result

# remove the commant to test the code by youself 
#print('write somthing?')
#user_input = input("> ")
#print(scan(user_input))

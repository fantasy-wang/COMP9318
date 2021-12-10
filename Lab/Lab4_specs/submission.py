## import modules here 

################# Question 1 #################

def multinomial_nb(training_data, sms):
    
    # prevent x not in training_data
    smooth = 1
    voc = set()
    num = {'ham': 0, 'spam': 0}
    prior = {'ham': 0, 'spam': 0}
    sentence = {'spam':{},'ham':{}}
    
    for data in training_data:
        prior[data[1]] += 1
        for index in data[0]:
            num[data[1]] += data[0][index]
            voc.add(index)
            if index in sentence[data[1]]:
                sentence[data[1]][index] += data[0][index]
            else:
                sentence[data[1]][index] = data[0][index]
    # probability of 'ham'
    prob0 = prior['ham'] / len(training_data)
    # probability of 'spam'
    prob1 = prior['spam'] / len(training_data)
    result = {'ham': prob0, 'spam': prob1}
    

    for token in sms:
        if token in voc:
            for key in sentence:
                if token in sentence[key]:
                    conditional_prob = (sentence[key][token] + smooth) / (num[key] + len(voc))
                else:
                    conditional_prob = ( smooth) / (num[key] + len(voc))
                result[key] *= conditional_prob
    return result['spam'] / result['ham']
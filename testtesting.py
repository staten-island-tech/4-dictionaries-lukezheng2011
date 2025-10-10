

def mc(x):
    correct = 0
    questions = x[0]

    for i in range(questions+1):
        if x[i] == x[(i+questions)]:
            correct = correct + 1
    
    return(correct)
    print(correct)
mc(input("PUT IN INPUT"))

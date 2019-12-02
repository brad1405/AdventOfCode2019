control = 0

for noun in range(0,99):
    for verb in range(0,99):
        input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,1,13,23,27,1,6,27,31,2,31,13,35,1,9,35,39,2,39,13,43,1,43,10,47,1,47,13,51,2,13,51,55,1,55,9,59,1,59,5,63,1,6,63,67,1,13,67,71,2,71,10,75,1,6,75,79,1,79,10,83,1,5,83,87,2,10,87,91,1,6,91,95,1,9,95,99,1,99,9,103,2,103,10,107,1,5,107,111,1,9,111,115,2,13,115,119,1,119,10,123,1,123,10,127,2,127,10,131,1,5,131,135,1,10,135,139,1,139,2,143,1,6,143,0,99,2,14,0,0]
        count = -4
        input[1] = noun
        input[2] = verb

        for num in input:
            count = count + 4
            if count < len(input):
                if input[count] == 1:
                    Num1 = input[count+1]
                    Num2 = input[count+2]
                    Num3 = input[count+3]
                    output = input[Num1] + input[Num2]
                    input[Num3] = output
                elif input[count] == 2:
                    Num1 = input[count+1]
                    Num2 = input[count+2]
                    Num3 = input[count+3]
                    output = input[Num1] * input[Num2]
                    input[Num3] = output
                elif input[count] == 99:
                    control + 1 #just for reference
                    #print(input)
                elif input[0] == 19690720:
                    print(noun)
                    print(verb)


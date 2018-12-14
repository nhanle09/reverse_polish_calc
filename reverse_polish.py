#open file input_RPN_EC.txt for reading, read each line and iterate through them
input_file = open("input_RPN_EC.txt", "r")
read_file = input_file.readlines()
for line in read_file:
    # split each character by space and strip the null terminator from the last character
    line = line.split(" ")
    line[-1] = line[-1].strip()
    # declare list for RPN outputs and list for operator
    main_stack = []
    op_stack = []
    # iterate through each character in algebraic expression
    for i in range(len(line)):
        # digits get store into main list
        if line[i].isdigit():
            main_stack.append( line[i] )
        # operator get store into operator list and get put into main list under
        # condition of () or when * and / are on top and next operator is + or -
        elif line[i] == '+' or line[i] == '-' or line[i] == '*' or line[i] == '/' or line[i] == '^':
            if len(op_stack) > 0 and op_stack[-1] != '(' and (op_stack[-1] == '*' or op_stack[-1] == '/' or op_stack[-1] == '^'):
                main_stack.append(op_stack.pop())
            op_stack.append(line[i])
        # store ( into operator and pop all operator into main until (
        elif line[i] == '(':
            op_stack.append(line[i])
        elif line[i] == ')':
            op_stack.remove('(')
            for j in range(len(op_stack)) :
                main_stack.append(op_stack.pop())
    # store the remainder operator into main list
    for i in range(len(op_stack)) :
        main_stack.append(op_stack.pop())
    # begin solving RPN
    num_stack = [] # store final result
    for i in range(len(main_stack)):
        # store digit into final list
        if main_stack[i].isdigit():
            num_stack.append( int(main_stack[i]) )
        # pop digits, add/subtract/multiply/divide and push final result back into final list
        elif main_stack[i] == '+':
            num_stack.append( int(num_stack.pop() + num_stack.pop()) )
        elif main_stack[i] == '*':
            num_stack.append( int(num_stack.pop() * num_stack.pop()) )
        elif main_stack[i] == '-':
            temp_n = num_stack.pop()
            temp_m = num_stack.pop()
            num_stack.append( int(temp_m - temp_n) )  
        elif main_stack[i] == '/':
            temp_n = num_stack.pop()
            temp_m = num_stack.pop()
            num_stack.append( int(temp_m / temp_n) )
        elif main_stack[i] == '^': 
            temp_n = num_stack.pop()
            temp_m = num_stack.pop()
            num_stack.append( int(temp_m ** temp_n) )
    # displaying final results
    print("Original Algebraic Form: ", end = '')
    for i in line:
        print(i, end= ' ')
    print("\nReverse Polish Notation: ", end = '')
    for i in main_stack:
        print (i, end= ' ')
    print("\nOutput: %s\n" % num_stack[0])
#Analizador lexico (Scanner)

def scanner(input):
    lex = ''
    digits = []
    count = 0
    while count < len(input):
        if input[count] == " ":
            count += 1
        if input[count] == "+":
            if input[count + 1] == "+":
                lex = lex + '<incremento,++>'
                count += 1
            elif input[count + 1] != "+":
                lex = lex + '<suma,+>'
        elif input[count] != " " and input[count] != "+" and input[count] != "E" and input[count] != "." and input[count] != "-" and input[count] != "*" and input[count] != "e":
            digits.append(input[count]) # 1
            count += 1 # 2
            if count == len(input):
                lex = lex + '<entero,' + ''.join(digits) + '>'
                digits.clear()
                return lex
            while input[count] != " " and input[count] != "+" and input[count] != "E" and input[count] != "." and input[count] != "*":
                digits.append(input[count]) # 2
                count += 1 # .
                if count == len(input):
                    lex = lex + '<entero,' + ''.join(digits) + '>'
                    digits.clear()
                    return lex
            if input[count] == ".":
                digits.append(input[count]) # .
                count += 1 # 5
                if input[count] != " " and input[count] != "+" and input[count] != "E" and input[count] != ".":
                    digits.append(input[count]) # 2
                    count += 1 # 5
                    if count == len(input):
                        lex = lex + '<flotante,' + ''.join(digits) + '>'
                        digits.clear()
                        return lex
                    while input[count] != " " and input[count] != "+" and input[count] != "." and input[count] != "E":
                        digits.append(input[count]) # 5
                        count += 1 # +
                        if count == len(input):
                            lex = lex + '<flotante,' + ''.join(digits) + '>'
                            digits.clear()
                            return lex
                    if input[count] == "E":
                        digits.append(input[count])
                        count += 1
                        if input[count] == "+" or input[count] == "-":
                            digits.append(input[count])
                            count += 1
                            if input[count] != " " and input[count] != "+" and input[count] != "E" and input[count] != ".":
                                while input[count] != " " and input[count] != "+" and input[count] != "E" and input[count] != ".":
                                    digits.append(input[count])
                                    count += 1
                                    if count == len(input):
                                        lex = lex + '<exponente,' + ''.join(digits) + '>'
                                        digits.clear()
                                        return lex
                                if input[count] == "E" and input[count] == " " and input[count] == "+" and input[count] == ".":
                                    lex = lex + '<exponente,' + ''.join(digits) + '>'
                                    digits.clear()
                            else:
                                lex = lex + '<error,' + ''.join(digits) + '>'
                                digits.clear()  
                        else:
                            digits.append(input[count])
                            lex = lex + '<error,' + ''.join(digits) + '>'
                            digits.clear()    
                    elif input[count] == "." or input[count] == " " or input[count] == "+":
                        lex = lex + '<flotante,' + ''.join(digits) + '>'
                        digits.clear()
                        count -= 1
                else:
                    lex = lex + '<error,' + ''.join(digits) + '>'
                    digits.clear()
            elif input[count] == "E" or input[count] == " " or input[count] == "+" or input[count] == "*":
                lex = lex + '<entero,' + ''.join(digits) + '>'
                digits.clear()
                count -= 1
        elif input[count] != " " and input[count] != "+" or input[count] == "-" or input[count] == "*":
            digits.append(input[count])
            lex = lex + '<error,' + ''.join(digits) + '>'
            digits.clear()
        count += 1
    return lex
        
print(scanner("5.25+23*325Ee12.5"))
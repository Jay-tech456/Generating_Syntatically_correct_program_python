from re import search
import string
import secrets


def stats(syntax):
    prod= search('<[A-Za-z_]*>', syntax).group()
    if prod == '<cmpd_stat>':
        b = '{<stat_list>}'
        return syntax.replace(prod, b)

    elif prod == '<iter_stat>':
        List = ['\nwhile (<exp>) \n\t<stat>', '\nwhile(<exp>) \n\t<cmpd_stat>']
        index = secrets.SystemRandom().choice(range(len(List)))
        List = List[index]
        return syntax.replace(prod, List)

    elif prod == '<assgn_stat>':
        b = "<id>=<exp>;\n"
        return syntax.replace(prod, b)

    elif prod == '<decl_stat>':
        List = ["<type><id>;", "<type><assgn_stat>"]
        Index = secrets.SystemRandom().choice(range(len(List)))
        List = List[Index]
        return syntax.replace(prod, List)

    elif prod == '<if_stat>':
        List = ['\nif (<exp>) \n<stat>', '\nif ( <exp>) \n<cmpd_stat>\n',
                  '\nif (<exp>) \n<stat> \nelse \n<stat>',
                  '\nif (<exp>) \n<cmpd_stat> \nelse \n<stat>'
                  '\nif (<exp>) \n<stat> \nelse \n\t<cmpd_stat>\n',
                  '\nif (<exp>) \n<cmpd_stat> \nelse \n<cmpd_stat>\n']
        Index = secrets.SystemRandom().choice(range(len(List)))
        List = List[Index]
        return syntax.replace(prod, List)
    else:
        return

def expansion(syntax):
    prod = search('<[A-Za-z_]*>', syntax).group()

    if prod == '<stat_list>':
        List = ['<stat><stat_list>', '<stat>']
        index = secrets.SystemRandom().choice(range(len(List)))
        List = List[index]
        return syntax.replace(prod, List)

    elif prod == '<stat>':
        List = ['<cmpd_stat>', '<if_stat>',
                    '<iter_stat>', '<assgn_stat>',
                    '<decl_stat>']
        Index = secrets.SystemRandom().choice(range(len(List)))
        return syntax.replace(prod, List[Index])

    elif prod == '<prog>':
        a = "int main()\n{ \n<stat_list> \nreturn 0; \n}"
        return syntax.replace(prod, a)

    else:
        return

def type_op_ex(syntax):
    production = search('<[A-Za-z_]*>', syntax).group()

    if production == '<exp>':
       List = ['<id>', '<exp><op><exp>']
       index = secrets.SystemRandom().choice(range(len(List)))
       List = List[index]
       return syntax.replace(production, List)
    elif production == '<op>':
        List = [' = ', ' + ', ' * ', ' / ']
        index = secrets.SystemRandom().choice(range(len(List)))
        List = List[index]
        return syntax.replace(production, List)

    elif production == '<type>':
        List = ["\nint ", '\ndouble ']
        index = secrets.SystemRandom().choice(range(len(List)))
        List = List[index]
        return syntax.replace(production, List)

    elif production == '<id>':
        new = '<char><char_digit_seq>'
        return syntax.replace(production, new)

    elif production == '<char_digit_seq>':
        List = ['[empty]', '<char><char_digit_seq>', '<digit><char_digit_seq>']
        index = secrets.SystemRandom().choice(range(len(List)))
        List = List[index]
        return syntax.replace(production, List)

    elif '<const>':
        new = "<digit><digit_seq>"
        return syntax.replace(production, new)
    else:
        return

def constants(syntax):
    prod = search('<[A-Za-z_]*>', syntax).group()
    if prod == '<char>':
        character = secrets.SystemRandom().choice(string.ascii_letters)
        return syntax.replace(prod, character)
    elif '<digit>':
        List = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        index = secrets.SystemRandom().choice(range(len(List)))
        List = List[index]
        return syntax.replace(prod, List)

syntax = "<prog>"
while search('<' and '>', syntax):
    production = search('<[A-Za-z_]*>', syntax).group()

    if production == '<prog>':
        syntax = expansion(syntax)

    elif production == '<stat>':
        syntax = expansion(syntax)

    elif production == '<stat_list>':
        syntax = expansion(syntax)

    elif production == '<if_stat>':
        syntax = stats(syntax)

    elif production == '<cmpd_stat>':
        syntax = stats(syntax)

    elif production == '<iter_stat>':
        syntax = stats(syntax)

    elif production == '<assgn_stat>':
        syntax = stats(syntax)

    elif production == '<decl_stat>':
        syntax = stats(syntax)

    elif production == '<exp>':
        syntax = type_op_ex(syntax)

    elif production == '<id>':
        syntax = type_op_ex(syntax)

    elif production == '<type>':
        syntax = type_op_ex(syntax)

    elif production == '<op>':
        syntax = type_op_ex(syntax)

    elif production == '<const>':
        syntax = type_op_ex(syntax)

    elif production == '<char_digit_seq>':
        syntax = type_op_ex(syntax)

    elif production == '<digit_seq>':
        syntax = type_op_ex(syntax)

    elif production == '<char>':
        syntax = constants(syntax)

    elif production == '<digit>':
        syntax = constants(syntax)

    else:
        break

# Printing the value into the console
print(syntax)

# printing the value to a .cpp file
saveFile = open("output.cpp", 'w')
saveFile.write(syntax)
saveFile.close()

# saving output to a .txt file
saveFile = open("output.txt", 'w')
saveFile.write(syntax)
saveFile.close()

# Python swapping 


def swap(lit,na1,na2):
    lit[na1],lit[na2]=lit[na2],lit[na1]

    return lit

lit =['sam','vam']
na1 = 0
na2 = 1

print(swap(lit,na1,na2))

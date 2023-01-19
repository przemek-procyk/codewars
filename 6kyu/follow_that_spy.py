def find_routes(routes):
    test = dict(routes)
    dupa = [i for i in test.keys() if i not in test.values()]
    for i in range(len(routes)):
        dupa.append(test[dupa[i]])
    return ", ".join(dupa)





    #
    # lista = []
    # for i in range(len(routes)):
    #     for j in range(len(routes)):
    #         if routes[i][1] == routes[j][0]:
    #             lista.append(routes[i])
    # return lista
    #



#print(find_routes([('Calgary','Fargo'), ('Spokane','Toronto'), ('Winnipeg','Montreal'), ('Toronto','Calgary'), ('Fargo','Winnipeg')]))


#print(find_routes([('MNL','TAG'), ('CEB','TAC'), ('TAG','CEB'), ('TAC','BOR')]))

print(find_routes([('ITA','GER'), ('GER','BEL'), ('BEL','CAN')]))

for i in range(1000):
    find_routes(
        [('Calgary', 'Fargo'), ('Spokane', 'Toronto'), ('Winnipeg', 'Montreal'),
         ('Toronto', 'Calgary'), ('Fargo', 'Winnipeg')])

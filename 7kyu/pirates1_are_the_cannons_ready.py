def cannons_ready(gunners):
    for gunner in gunners.values():
        if gunner == "nay":
            return "Shiver me timbers!"
    return "Fire!"


a = {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'}
b = {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'}

print(cannons_ready(a))

# for i in b.values():
#     print(i)

def cannons_ready(gunners):
    for gunner in gunners.values():
        if gunner == "nay":
            return "Shiver me timbers!"
    return "Fire!"
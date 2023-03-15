def to_time(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600 / 60))
    return f"{hours} hour(s) and {minutes} minute(s)"

print((to_time(3660)))
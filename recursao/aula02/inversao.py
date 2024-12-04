def inverter(x):
    x = str(x)

    if len(x) == 1:
        return x[0]
    else:
        return f"{x[-1]}{inverter(x[:-1])}"

print(inverter(62593))
def trans(Height, Width, BoxHeight, BoxWidth, *args):  # преобразование для интерпретатора из удобной
    x0 = args[0][0]
    y0 = args[0][1]
    return int(Width + x0 - BoxWidth / 2), int(Height - BoxHeight / 2 - y0)
# def untrans(Height, Width, x1, y1):    #преобразование в удобную
#   return [x1 - Width/2, Height/2 - y1]

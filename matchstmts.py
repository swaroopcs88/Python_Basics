def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not found"
        case 418:
            return "I'am a teapot"

        case _:
            return "Something's wrong with the internet"

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
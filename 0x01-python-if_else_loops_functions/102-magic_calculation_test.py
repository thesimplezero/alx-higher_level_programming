import dis

def magic_calculation(a, b, c):
    return c if a < b else ((a + b) if c > b else (a * b - c))

dis.dis(magic_calculation)

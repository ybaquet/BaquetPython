def print_type(n):
    print(n, " est de type ", type(n))
    
def my_var():
    a = 42
    b = "42"
    c = "quarante deux"
    d = 42.0
    e = True
    f = [42]
    g = {42: 42}
    h = (42,)
    i = set()
    print_type(a)
    print_type(b)
    print_type(c)
    print_type(d)
    print_type(e)
    print_type(f)
    print_type(g)
    print_type(h)
    print_type(i)

if __name__ == '__main__':
    my_var()

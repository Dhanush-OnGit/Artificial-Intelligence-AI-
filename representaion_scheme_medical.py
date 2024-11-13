def measles(a,b,c,d,e):
    if a == 'y' and b == 'y' and c == 'y' and d == 'y' and e == 'y':
        return "measles" 
    else:
        return None
def flu(a,b,c,d,e,f,g,h):
    if a == 'y' and b == 'y' and c == 'y' and d == 'y' and e == 'y' and f == 'y' and g == 'y' and h == 'y':
        return "flu"
    else:
        return None
def cold(c,b,a,h,d):
    if c == 'y' and b == 'y' and a == 'y' and h == 'y' and d == 'y':
        return "cold"
    else:
        return None
def chikenbox(a,h,g,b):
    if a == 'y' and h == 'y' and g == 'y' and b == 'y':
        return "chikenbox"
    else:
        return None
def run_diagosis():
    name = input("enter your name : ").lower()
    a = input("do you have fever (y/n):").lower()
    b = input("do you have rashes(y/n):").lower()
    c = input("do you have headache(y/n):").lower()
    d = input("do you have running nose(y/n):").lower()
    e = input("do you have conjactives(y/n):").lower()
    f = input("do you have cough(y/n):").lower()
    g = input("do you have ache(y/n):").lower()
    h = input("do you have chills(y/n):").lower()
    
    diagosis = []
    result = measles(a, b, c, d, e)
    if result:
        diagosis.append(result)
    result = flu(a,b,c,d,e,f,g,h)
    if result:
        diagosis.append(result)
    result = cold(c, b, a, h, d)
    if result:
        diagosis.append(result)
    result = chikenbox(a, h, g, b)
    if result:
        diagosis.append(result)
    if len(diagosis) > 0:
        print(f"{name} you have based on {','.join(diagosis)}.")
    else:
        print(f"{name} you are alright")
run_diagosis()
        
def multi_list(lst):
    mullst = 1

    for i in lst:
        mullst = mullst * i
    return mullst

def max(lst):
    maxa = 0
    for i in lst:
        if maxa < i:
            maxa = i

    return maxa

def main():
    lst = [5, 15, 20, 40, 6]

    sumlst = 0
    """
    sumlst = sumlst + lst[0]
    sumlst = sumlst + lst[1]
    sumlst = sumlst + lst[2]
    sumlst = sumlst + lst[3]
    """
    for i in lst:
        sumlst = sumlst + i

    print(sumlst)
    mult = multi_list(lst)
    print(mult)

    max_el = max(lst)
    print(max_el)

if __name__ == "__main__":
    main()

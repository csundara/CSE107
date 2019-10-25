# note: feb. 20, 2019 learning how to sort lists
# also convaying the concept of pseudo code
# mentions slicing (array[start:end-1] where start is the index fo the first
# one whishes to access and end is the element after the element you wish to end on)

#import
def smallest_index(l):
    small = 0
    for i in range(1, len(l)):
        if l[i] < l[small]:
            small = i
    return small
"""
def main():
    original = [5, 3, 7, 8, 2]
    sorted = []

    while original != []:
        i = smallest_index(original)
        sorted. append(original[i])
        del original[i]

    print(sorted)
"""
def main():
    original = [5, 3, 7, 8, 2]
    for i in range(len(original - 1)):
        s = smallest_index(original))
        tmp = original[i]
        original[i] = original[s]
        original[s] = tmp

if __name__ == "__main__":
    main()


def main():
    list = {
    1:[2, 5],
    2:[1, 3],
    3:[3, 5],
    4:[5],
    5:[1, 3, 4],
    }

    for node, adj in list.items():
        print(node)
        print(adj)


if __name__ == "__main__":
    main()

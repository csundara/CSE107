import matplotlib.pyplot as plt


def main():
    xs = range(-5, 15)
    ys = [-(x - 2) ** 2 for x in xs]

    plt.plot(xs, ys, 'y--')
    plt.annotate(s='Max', xy=(2.5, -5), xytext=(2,-25),
                 arrowprops={'color': 'black', 'width': 2})
    plt.title('Plot of $-(x - 2)^2$')

    plt.show()


if __name__ == "__main__":
    main()

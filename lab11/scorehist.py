import readscores
import matplotlib.pyplot as plt


def new_func():
    """ additional functions """


def main():
    averages = readscores.test()
    avg_scr = []

    # print(averages[1])
    for avg in averages:
        avg_scr.append(avg['act_average_score'])
    plt.hist(avg_scr, bins=10, color='lightblue', edgecolor='blue')
    plt.title('Histogram of ACT scores', fontdict=None, loc='center', pad=None)
    plt.ylabel('scores out of 36', fontdict=None, labelpad=None)
    plt.xlabel('Number of states', fontdict=None, labelpad=None)
    # plt.xticks(range(18, 36))
    # plt.xticks(len(avg_scr), )
    plt.show()


if __name__ == "__main__":
    main()

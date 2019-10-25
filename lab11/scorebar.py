import readscores
import matplotlib.pyplot as plt


def sat_calc(scr):
    """ takes in elements of an sat score and calculates the total score """
    sat = float(scr['sat_average_math'])
    sat = sat + float(scr['sat_average_reading'])
    sat = sat + float(scr['sat_average_writing'])
    return sat


def main():
    scores = readscores.test()
    state = []
    act_scores = []
    sat_scores = []

    for scr in scores:
        actp = int(scr['act_percent_taking'])
        satp = int(scr['sat_percent_taking'])
        if actp < 50 and satp > 50:
            act_scores.append(float(scr['act_average_score']) / 36)
            sat = sat_calc(scr)
            sat = sat * -1 / 2400
            sat_scores.append(sat)
            state.append(scr['state'])

    # fig, ax = plt.subplots()
    plt.bar(state, act_scores, color='yellow', edgecolor='gray')
    plt.bar(state, sat_scores, color='white', edgecolor='gray')
    plt.ylim(-1, 1)
    plt.title('ACT and SAT scores', fontdict=None, loc='center', pad=None)
    plt.ylabel('scores', fontdict=None, labelpad=None)
    plt.xlabel('States', fontdict=None, labelpad=None)
    plt.show()


if __name__ == "__main__":
    main()

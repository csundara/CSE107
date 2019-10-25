import matplotlib.pyplot as plt
import country_data


def parse_data(country):
    """ additional functions """
    data = []
    if country.get('gdp') == None:
        country['gdp'] = 10
    data.append(country['gdp'])

    if country.get('expectancy') == None:
        country['expectancy'] = 10
    data.append(country['expectancy'])

    if country.get('population') == None:
        country['population'] = 10
    data.append(country.get('population'))
    return data


def mean(values):
    """  """
    total = 0
    for v in values:
        total = total + v
    return total / len(values)


def main():
    x_income = []
    y_life = []
    pop = []
    country = []
    arrow = ['China', 'Russia', 'United States', 'Afghanistan']

    for cntr in country_data.data1960:
        if cntr.get('country') in arrow:
            country.append(cntr)
        info = parse_data(cntr)
        x_income.append(info[0])
        y_life.append(info[1])
        pop.append(info[2])
    scaled_pop = [800 * p / max(pop) for p in pop]

    x = range(0, round(max(x_income)))
    y = [mean(y_life) for x in x]
    plt.plot(x, y, 'r--')
    ymax = [max(y_life) for x in x]
    plt.plot(x, ymax, 'r--')
    plt.xlabel('Income')
    plt.ylabel('Life expectancy')
    plt.title('Year 1960')
    plt.scatter(x_income, y_life, s=scaled_pop, alpha=0.8)
    for c in country:
        income = c.get('gdp')
        life = c.get('expectancy')
        plt.annotate(s=c.get('country'), xy=(income, life), xytext=(income + 2, life + 2),
                 arrowprops={'arrowstyle': 'wedge,tail_width=0.25', 'color': 'black'})
    plt.show()

    x_income.clear()
    y_life.clear()
    pop.clear()
    country.clear()
    for cntr in country_data.data2010:
        if cntr.get('country') in arrow:
            country.append(cntr)
        info = parse_data(cntr)
        x_income.append(info[0])
        y_life.append(info[1])
        pop.append(info[2])
    scaled_pop = [800 * p / max(pop) for p in pop]

    x = range(0, round(max(x_income)))
    y = [mean(y_life) for x in x]
    plt.plot(x, y, 'r--')
    ymax = [max(y_life) for x in x]
    plt.plot(x, ymax, 'r--')
    plt.xlabel('Income')
    plt.ylabel('Life expectancy')
    plt.title('Year 2010')
    plt.scatter(x_income, y_life, s=scaled_pop, alpha=0.8)
    for c in country:
        income = c.get('gdp')
        life = c.get('expectancy')
        plt.annotate(s=c.get('country'), xy=(income, life), xytext=(income + 2, life + 2),
                 arrowprops={'arrowstyle': 'wedge,tail_width=0.25', 'color': 'black'})
    plt.show()


if __name__ == "__main__":
    main()

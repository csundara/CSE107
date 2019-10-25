import math


def reduce(frac):
    """ Take in parameter frac, which is a tuple that contains a fractions
    denominator and numerator and returns a tuple with a reduced version of
    the fraction """
    commond = math.gcd(frac[0], frac[1])
    new_num = frac[0] / commond
    new_den = frac[1] / commond

    return (int(new_num), int(new_den))


def add(frac1, frac2):
    """ given 2 fractions (frac1 and frac2) add them together """
    num = frac1[0] * frac2[1] + frac1[1] * frac2[0]
    den = frac1[1] * frac2[1]
    sum = (int(num), int(den))

    return reduce(sum)


def multiply(frac1, frac2):
    """ Takes 2 frations (frac1 and frac2) and multiplys them together """
    num = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    mult = (int(num), int(den))

    return reduce(mult)


def divide(frac1, frac2):
    """ Takes 2 fractions (frac1 and frac2) and divides them """
    num = frac1[0] * frac2[1]
    den = frac1[1] * frac2[0]
    div = (int(num), int(den))

    return reduce(div)


def main():
    frac_in = input('Enter a fraction >>> ')
    num, den = frac_in.split('/')
    frac1 = (int(num), int(den))

    frac_in = input('Enter a fraction >>> ')
    num, den = frac_in.split('/')
    frac2 = (int(num), int(den))

    redu1 = reduce(frac1)
    redu2 = reduce(frac2)
    print('Reduced fractions to {}/{} and {}/{}.\
    '.format(redu1[0], redu1[1], redu2[0], redu2[1]))
    sum = add(frac1, frac2)
    print('Sum of the fractions: {}/{}.'.format(sum[0], sum[1]))
    mult = multiply(frac1, frac2)
    print('Multiplication of the fractions: {}/{}.'.format(mult[0], mult[1]))
    div = divide(frac1, frac2)
    print('Division of the first by the second: {}/{}.'.format(div[0], div[1]))


if __name__ == "__main__":
    main()

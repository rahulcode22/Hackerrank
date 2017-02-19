def product(fracs):
    t = Fraction(reduce(lambda x,y:Fraction(x*y),fracs))
    return t.numerator, t.denominator

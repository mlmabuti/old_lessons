import sympy as sp
from IPython.display import display, Math


def main():
    display(Math(sp.latex(sp.integrate('3*x'))))


if __name__ == '__main__':
    main()

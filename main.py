from burger import Burger


if __name__ == '__main__':
    burgerBuilder = Burger.builder()
    burgerBuilder.bun(True).patty(True).cheese(True)
    myBurger = burgerBuilder.build()
    print(myBurger)
    
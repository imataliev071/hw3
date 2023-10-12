class Bank:
    def __init__(self, name, balanse):
        self.__name = name
        self.__balanse = balanse

    def moneyX(self):
        sum = int(input('Введите сумму: '))
        self.__balanse += sum
        print(f'Ваш баланс: {self.__balanse}')


    def printB(self):
        print(self.__name, self.__balanse)

    def _kill(self):
        self.__balanse = 0
        print(f'Ваш баланс: {self.__balanse}')

    def __jackpot(self):
        self.__balanse *= 10
        print(self.__balanse)

    def _bankk(self, balance1):
        self.balanse1 = balance1
        self.__balanse += self.balanse1
        print(self.__balanse)


bank = Bank('Аббас', 100)
bank._bankk(100)


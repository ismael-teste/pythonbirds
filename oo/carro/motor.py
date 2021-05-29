class Motor:

    def __init__(self):
        self.velocidade = 0


    def acelerar(self):
        self.velocidade +=1


    def frear(self):
        if self.velocidade <= 1:
            self.velocidade = 0
        else:
            self.velocidade -= 2


if __name__ == "__main__":
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    motor.frear()
    motor.frear()
    motor.frear()
    print(motor.velocidade)

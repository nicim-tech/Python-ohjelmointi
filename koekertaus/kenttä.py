import random
import time
class Field:
    def __init__(self, max_points):
        self.max_points = max_points
        self.current_points = 0
    def play(self):
        while self.current_points != self.max_points:
            print(f"Needed points {self.max_points}")
            print(f"Current points {self.current_points}")
            self.guess_number()
    def guess_number(self):
        number = random.randint(1, 5)
        guess = int(input("Arvaus: "))
        while guess != number:
            if guess > number:
                print("Too high")
            else:
                print("Too low")

            guess = int(input("Guess: "))
        else:
            self.current_points += 1
            print("Correct! 1 point")

class TimedField(Field):
    def __init__(self, max_points, timelimit):
        super().__init__(max_points)
        self.timelimit = timelimit

    def play(self):
        starting_time = time.time()
        while self.current_points != self.max_points:
                print(f"Needed points {self.max_points}")
                print(f"Current points {self.current_points}")
                game_duration = time.time() - starting_time
                if game_duration >= self.timelimit:
                    print(f"Times out!")
                    break
                super().guess_number()

    field = TimedField(3, 60)
    field.play()

        #niin kauan kun pelaajalla ei ole riittävästi pisteitä
        #katsoa onko aikaraja täynnä
        #times out game ends


        #guess number
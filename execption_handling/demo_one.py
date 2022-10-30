class Test:
    def test1(self):
        print("1st program is started")
        try:
            print(10 / 0)  # zeroDivisionError

        except ZeroDivisionError:
            print("Entered in to except block - Handled exception")
        print("1st program is completed")

    def test2(self):
        print("2nd program is started")
        try:
            print(10 / 5)

        except ZeroDivisionError:
            print("Entered in to except block - Handled exception")
        print("2nd program is completed")

print("1st program is started")
try:
    print(10 / 0)  # zeroDivisionError

except TypeError:
    print("Entered in to except block - Handled TypeError exception")
except ZeroDivisionError:
    print("Entered in to except block - Handled ZeroDivisionError exception ")
else:
    print("Entered in to else block....")
finally:
    print("Entered in to else block....")
print("1st program is completed")

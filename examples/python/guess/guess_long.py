response1 = input("the guess is 3, is it [C] correct, [L] low, or [H] high? ")

if response1 == "C":
  print("the number is 3")
  
elif response1 == "H":

    response2 = input("the guess is 2, is it [C] correct or [H] high? ")

    if response2 == "H":
      print("the number is 1")

    elif response2 == "C":
      print("the number is 2")

elif response1 == "L":

    response2 = input("the guess is 4, is it [C] correct or [L] low? ")

    if response2 == "C":
      print("the number is 4")

    elif response2 == "L":
      print("the number is 5")

$ python3 guess_number.py
the guess is 3, is it [C] correct, [L] low, or [H] high? H
the guess is 2, is it [C] correct or [H] high? H
the number is 1

$ python3 guess_number.py
the guess is 3, is it [C] correct, [L] low, or [H] high? H
the guess is 2, is it [C] correct or [H] high? C
the number is 2

$ python3 guess_number.py
the guess is 3, is it [C] correct, [L] low, or [H] high? C
the number is 3

$ python3 guess_number.py
the guess is 3, is it [C] correct, [L] low, or [H] high? L
the guess is 4, is it [C] correct or [L] low? C
the number is 4

$ python3 guess_number.py
the guess is 3, is it [C] correct, [L] low, or [H] high? L
the guess is 4, is it [C] correct or [L] low? L
the number is 5
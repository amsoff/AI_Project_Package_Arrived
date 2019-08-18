import os


AMOUNT = 1500
TYPE = "optimistic"
HEURISTIC = "sum"


def run():
  """
  play with parameters at the beginning of the file to run the game
  """
  os.system("python3 run_script.py {} {} {} {}".format(AMOUNT, TYPE, HEURISTIC))


if __name__ == "__main__":
    os.system("pip3 install numpy")
    os.system("pip3 install pandas")
    os.system("pip3 install colorama")
    run()

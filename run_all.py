import os


def run():
    for type in ["optimistic"]: #, "average"]:
        for heuristic in ["sum", "max"]:
            for gen_flag in range(2, 3):
                gen = "gen_%d" % gen_flag
                for amnt in range(0, 2201, 200):
                    x = 0
                    os.system("python run_script.py {} {} {} {}".format(amnt, type, heuristic, gen_flag))
                    print("###########################################################")
                    print("FINISHED ROUND %d: type       - %s\n"
                          "                   heuristic - %s\n"
                          "                   gen       - %s\n"
                          "                   amount    - %d" % (x, type, heuristic, gen, amnt))
                    print("###########################################################")
                    x += 1


if __name__ == "__main__":
    run()

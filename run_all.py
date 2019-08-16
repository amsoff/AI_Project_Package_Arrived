import os


def run():
    for type in ["average"]: #, "average"]:
        for heuristic in ["sum"]:
            for gen_flag in range(1, 4):
                gen = "gen_%d" % gen_flag
                for amnt in [1500,300]:
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

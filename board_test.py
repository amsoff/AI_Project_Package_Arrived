import board
import dice

dice = dice.Dice()
board_dict = board.Board().transition_dict

for tile1 in board_dict:
    for d in dice.values:
        for tile2 in board_dict[tile1][d]:
            if tile1 not in board_dict[tile2][d]:
                print(tile1, tile2, d)







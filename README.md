# AI PROJECT - THE PACKAGE ARRIVED #

Submitted by:\
Reut Rabenou - 312416621 - reut\
Erez Kaufman - 305605255 - erez\
Nitzan Wagner - 205872963 - nitzan.wagner1



###############################################################################
#                                 HOW TO RUN                                  #
###############################################################################

For your convenience, we made a file named demo.py
you can simply run it, or play with the magic numbers at the beginning of the
file and then run it.

###############################################################################
#                              BRIEF EXPLANATION                              #
###############################################################################

This project is made out of 3 parts:

1. Graphplan from ex3 + Search from ex1

2. The domain and problem creators 

3. The game itself

###############################################################################
#                             DOMAIN AND PROBLEM                              #
###############################################################################

The domain file is created once. The file that creates it is domain_create.py 
It creates all of the propositions and actions, and they are all explained
within the file.

The problem is created each turn (unless it uses the previous plan - explained
in the report). Therefore, the player creates the problem file according to 
its current state (how much money it has, what cell it is in, etc.)
This is created in the file player.py

###############################################################################
#                                  THE GAME                                   #
###############################################################################

The game itself is constructed by many different classes:
1. game.py - The engine of the game.
2. board.py - The hardcoded board of the game.
2. player.py - Represents a player, holds the player's current
		       state and creates the problem file mentioned earlier.
3. dice.py - Represents the dice in the game. Can be a generator that 
		     uses a list that was randomly generated (we used it for 
		     comparing the results) or purely random.
4. certificates.py - Enum class of all of the certificates you can receive in 
		     the game.
5. surprise.py - Represents the surprises in the game. Can be a generator 
		     that uses a list that was randomly generated (we used it
		     for comparing the results) or purely random.
6. constants.py	- Contains all of the constants throughout the game to keep
		     the code organized.

###############################################################################
#                                   RESULTS                                   #
###############################################################################

In order to test and compare different heuristics, agents, starting values of
money, etc. we needed the other elements to be constant throughout each run of
the game. Therefore, we created generators in the die and surprise classes.
(so the difference won't be based on pure luck).

We created files to run the game with the different values. They are:
run_script.py and run_all.py. run_all.py runs all the 3 generated games
on all the initial amounts of money from 0 to 2200, for both players and both heuristics.

To run run_script.py: Enter the following parameters:
Player type ("optimistic"/"average"), goal cell, start cell, initial money.

To run run_all.py: Simply press play.

We also created a file that parses the results of the runs and creates 
graphs: graphs.py

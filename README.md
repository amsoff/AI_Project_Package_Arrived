#AI PROJECT - THE PACKAGE ARRIVED#

submitted by:
Reut Rabenou - 312416621 - reut



###############################################################################
#                                 HOW TO RUN                                  #
###############################################################################

for your conveniece, we made a file named demo.py
you can simply run it, or play with the magic numbers and the beginning of the
file and then run it.

###############################################################################
#                              BRIEF EXPLANATION                              #
###############################################################################

this project is constructed by 3 parts:

1. graphplan from ex3 + search from ex1

2. the domain and problem creators 

3. the game itself

###############################################################################
#                             DOMAIN AND PROBLEM                              #
###############################################################################

the domain is created once. the file that creates it is domain_create.py 
it creates all of the propositions and actions, and they are all explained
within the file.

the problem is created each turn (unless it uses the previous plan - explained
in the report). therefore, the player creates the problem file according to 
its current state (how much money it has, what cell it is at, etc)
it is created in the file player.py

###############################################################################
#                                  THE GAME                                   #
###############################################################################

the game itself is constructed by many different classes:
1. game.py 		   - it is the engine of the game.
2. player.py       - class that represents a player, holds the player's current
		     state and creates the problem file mentioned earlier.
3. dice.py         - represents the dice in the game. can be a generator that 
		     uses a list that was randomly generated (we used it for 
		     comparing the results) or purely random.
4. certificates.py - enum class of all of the certificates you can receive in 
		     the game.
5. surprise.py     - represents the surprises in the game. can be a generator 
		     that uses a list that was randomly generated (we used it
		     for comparing the results) or purely random.
6. constants.py	   - contains all of the constants throughout the game to keep
		     the code organized.

###############################################################################
#                                   RESULTS                                   #
###############################################################################

in order to test and compare different heuristics, agents, starting values of
money, etc. we needed the other elements to be constant throughout each run of
the game, therefore we created generators in the dice and surprise classes.
(so the difference wouldn't be based on pure luck)

we created files to run the game with the different values. they are:
run_script.py and run_all.py

and we also created a file that parses the results of the runs and creates 
graphs: graph.py

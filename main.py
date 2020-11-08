import argparse
import game_loop
from colors import Colors

parser = argparse.ArgumentParser(description='A game based on the Game of Life')
parser.add_argument('--night-mode', dest='night_mode', action='store_true', help="Changes the colors to accomodate the eyes")
parser.add_argument('--no-ui', dest='ui', action='store_false', help="Makes the game run without a ui. Use it with --synchronous to speed up the game by a lot")
parser.add_argument('--synchronous', dest='synchronous', action='store_true', help="Does not wait the set amount of time to run next step, only wait for the players")
parser.add_argument('--nb-moves', dest='nb_moves', help="The max number of move for each player", default=250)
parser.add_argument('--density', dest='density', help="The proportion of alive cells at the start of the game, between 0 and 1", default=0.2)
parser.add_argument('--nb-games', dest='nb_games', help="Runs several games and returns stats for both players", default=1)
parser.add_argument('--p1', dest="p1", help="The location of your player 1", default="AIs/player.py")
parser.add_argument('--p2', dest="p2", help="The location of your player 2", default="AIs/player.py")

args = parser.parse_args()

col = Colors()
if args.night_mode:
    col.night_mode()

res = []

for game in range(int(args.nb_games)):
    res.append(game_loop.game(args.p1.replace('/', '.')[:-3], args.p2.replace('/', '.')[:-3], col, args.ui, args.synchronous, int(args.nb_moves), float(args.density)))

print(res)

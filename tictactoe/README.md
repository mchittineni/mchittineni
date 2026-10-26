# 🎮 Community Tic-Tac-Toe

A game of tic-tac-toe that anyone can play from my [GitHub profile](https://github.com/mchittineni).
Everyone shares one board: ❌ and ⭕ take turns, and any visitor can make the next move.

## How to play

1. Go to the [profile page](https://github.com/mchittineni#-community-tic-tac-toe) and click an empty square.
2. GitHub opens a new issue with the move already filled in. Press **Submit new issue** without changing the title.
3. About 30 seconds later the board updates and the bot replies on your issue and closes it.

Can't wait for someone else? Use **Let the bot play** under the board. The bot plays perfectly, so beating it is
not an option. The best you can do is a draw.

## Rules

- ❌ and ⭕ alternate. The team that didn't open the last game opens the next one.
- You can't play two moves in a row. Let someone else take the next turn, or ask the bot to play it.
- When a game is won or drawn, the result is recorded and a fresh board starts straight away.
- The leaderboard counts **game-winning moves**: whoever places the final mark of a winning line gets the credit.

## Behind the scenes

| Piece | What it does |
| ----- | ------------ |
| Square links | Open an issue titled `ttt\|move\|<team>\|<square>` (squares 1–9, left to right, top to bottom), or `ttt\|move\|<team>\|bot` |
| [`tictactoe.yaml`](../.github/workflows/tictactoe.yaml) | Runs on every new issue whose title starts with `ttt\|`, plays the move, commits the board, replies, and closes the issue |
| [`game.py`](game.py) | Validates the move, runs the minimax bot, updates [`state.json`](state.json), and rewrites the README section between the `TICTACTOE` markers |
| [`state.json`](state.json) | The board, whose turn it is, stats, the last five moves, and the leaderboard |

If two people move at the same time, the workflow replays the later move on the newest board before saving it,
so no move is lost. A move that's no longer valid (the square was taken, or it's the other team's turn) gets a
reply explaining why, and its issue is closed as *not planned*.

### Running it locally

```bash
python3 -m unittest discover -s tictactoe            # tests
ISSUE_TITLE='ttt|move|x|5' ISSUE_USER=you python3 tictactoe/game.py   # play a move
python3 tictactoe/game.py --render                   # redraw the README from state.json
```

Inspired by [JonathanGin52's community Connect Four](https://github.com/JonathanGin52/JonathanGin52).

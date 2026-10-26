"""Tests for the tic-tac-toe engine. Run with: python -m unittest discover tictactoe"""

import random
import unittest

import game


def state_with(board: str, turn: str = "x") -> dict:
    """Build a state from a 9-char board string, e.g. 'xo.x.o...' ('.' = empty)."""
    state = game.new_state()
    state["board"] = ["" if ch == "." else ch for ch in board]
    state["turn"] = turn
    return state


class OutcomeTest(unittest.TestCase):
    def test_rows_columns_and_diagonals(self):
        self.assertEqual(game.outcome(state_with("xxxoo....")["board"]), "x")
        self.assertEqual(game.outcome(state_with("ox.ox.o..")["board"]), "o")
        self.assertEqual(game.outcome(state_with("xo.ox...x")["board"]), "x")

    def test_draw_and_open(self):
        self.assertEqual(game.outcome(state_with("xoxxoooxx")["board"]), "draw")
        self.assertIsNone(game.outcome(state_with(".........")["board"]))


class BotTest(unittest.TestCase):
    def test_takes_the_win(self):
        board = state_with("oo.xx....", "o")["board"]
        self.assertEqual(game.best_move(board, "o"), 2)

    def test_blocks_the_loss(self):
        board = state_with("xx..o....", "o")["board"]
        self.assertEqual(game.best_move(board, "o"), 2)

    def test_never_loses_to_random_play(self):
        rng = random.Random(7)
        for _ in range(200):
            board, player = [""] * 9, "x"
            while game.outcome(board) is None:
                if player == "o":
                    board[game.best_move(board, "o", rng)] = "o"
                else:
                    board[rng.choice([i for i, c in enumerate(board) if not c])] = "x"
                player = game.other(player)
            self.assertNotEqual(game.outcome(board), "x")


class PlayTest(unittest.TestCase):
    def test_valid_move_updates_state(self):
        state = game.new_state()
        message = game.play(state, "ttt|move|x|5", "alice")
        self.assertEqual(state["board"][4], "x")
        self.assertEqual(state["turn"], "o")
        self.assertEqual(state["stats"]["moves"], 1)
        self.assertEqual(state["players"], ["alice"])
        self.assertIn("square 5", message)

    def test_rejects_bad_title_wrong_turn_taken_square_and_repeat_player(self):
        state = game.new_state()
        for title in ("ttt|move|x|0", "ttt|move|x|10", "hello", "ttt|move|z|1"):
            with self.assertRaises(game.MoveError):
                game.play(state, title, "alice")
        with self.assertRaises(game.MoveError):
            game.play(state, "ttt|move|o|1", "alice")
        game.play(state, "ttt|move|x|1", "alice")
        with self.assertRaises(game.MoveError):
            game.play(state, "ttt|move|o|1", "bob")
        with self.assertRaises(game.MoveError):
            game.play(state, "ttt|move|o|2", "alice")
        self.assertEqual(state["stats"]["moves"], 1)

    def test_bot_move_is_credited_to_bot(self):
        state = game.new_state()
        game.play(state, "ttt|move|x|1", "alice")
        game.play(state, "ttt|move|o|bot", "alice", random.Random(1))
        self.assertEqual(state["last_mover"], game.BOT)
        self.assertTrue(state["recent"][0]["bot"])
        self.assertEqual(state["board"].count("o"), 1)

    def test_win_records_result_and_starts_new_game(self):
        state = state_with("xx.oo....", "x")
        state["last_mover"] = "bob"
        message = game.play(state, "ttt|move|x|3", "alice")
        self.assertIn("won", message)
        self.assertEqual(state["stats"]["games"], 1)
        self.assertEqual(state["stats"]["x_wins"], 1)
        self.assertEqual(state["leaderboard"], {"alice": 1})
        self.assertEqual(state["board"], [""] * 9)
        self.assertEqual(state["turn"], "o")  # the other team opens the next game
        self.assertIsNone(state["last_mover"])

    def test_draw(self):
        state = state_with("xoxoox.xo", "x")
        game.play(state, "ttt|move|x|7", "alice")
        self.assertEqual(state["stats"]["draws"], 1)
        self.assertEqual(state["leaderboard"], {})


class RenderTest(unittest.TestCase):
    def test_render_has_markers_links_and_tables(self):
        state = game.new_state()
        game.play(state, "ttt|move|x|5", "alice")
        out = game.render(state)
        self.assertTrue(out.startswith(game.START) and out.endswith(game.END))
        self.assertIn("ttt%7Cmove%7Co%7C1", out)  # empty squares link to o's moves
        self.assertNotIn("ttt%7Cmove%7Co%7C5", out)  # taken square has no link
        self.assertIn("assets/tictactoe/x.svg", out)
        self.assertIn("[@alice](https://github.com/alice)", out)


if __name__ == "__main__":
    unittest.main()

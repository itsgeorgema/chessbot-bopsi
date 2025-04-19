import time
import random
from data.classes.Board import Board

class Bot:
    def __init__(self):
        self.start_time = None

    def evaluate_piece(self, piece):
        values = {
            '': 1,
            'N': 3,
            'B': 3,
            'R': 5,
            'Q': 9,
            'K': 100,
            'S': 4,
            'J': 10
        }
        return values.get(piece[1], 0)

    def evaluate_board(self, board_state, side):
        score = 0
        for row in board_state:
            for piece in row:
                if piece:
                    value = self.evaluate_piece(piece)
                    score += value if piece[0] == side[0] else -value
        return score

    def simulate_move(self, board, start_pos, end_pos):
        new_board = Board(board.width, board.height)
        board_state = board.get_board_state()
        for square in new_board.squares:
            square.occupying_piece = None

        for y in range(len(board_state)):
            for x in range(len(board_state[y])):
                piece = board_state[y][x]
                if piece:
                    square = new_board.get_square_from_pos((x, y))
                    new_board.config[y][x] = piece

        new_board.setup_board()
        new_board.handle_move(start_pos, end_pos)
        return new_board

    def get_opponent(self, side):
        return "white" if side == "black" else "black"

    def minimax(self, board, depth, maximizing, side):
        if time.time() - self.start_time > 0.09 or depth == 0:
            return self.evaluate_board(board.get_board_state(), side)

        valid_moves = board.get_all_valid_moves(side if maximizing else self.get_opponent(side))
        if not valid_moves:
            return self.evaluate_board(board.get_board_state(), side)

        if maximizing:
            max_eval = float('-inf')
            for move in valid_moves:
                sim_board = self.simulate_move(board, move[0], move[1])
                eval = self.minimax(sim_board, depth - 1, False, side)
                max_eval = max(max_eval, eval)
                if time.time() - self.start_time > 0.09:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in valid_moves:
                sim_board = self.simulate_move(board, move[0], move[1])
                eval = self.minimax(sim_board, depth - 1, True, side)
                min_eval = min(min_eval, eval)
                if time.time() - self.start_time > 0.09:
                    break
            return min_eval

    def move(self, side, board):
        self.start_time = time.time()
        valid_moves = board.get_all_valid_moves(side)
        if not valid_moves:
            return None

        best_score = float('-inf')
        best_move = random.choice(valid_moves)

        for move in valid_moves:
            sim_board = self.simulate_move(board, move[0], move[1])
            score = self.minimax(sim_board, depth=2, maximizing=False, side=side)
            if score > best_score:
                best_score = score
                best_move = move
            if time.time() - self.start_time > 0.09:
                break

        return best_move

## Rule

This is a simplified chess with a different board and slightly different rules. Please check [`rules.md`](rules.md).

## Setup
clone the repository

To setup the virtual environment:

```bash
python -m venv venv
# For MacOS/Linux:
source venv/bin/activate  
# On Windows (use command line if powershell gives any issues): 
venv\Scripts\activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

- Random Bot: The bot chooses random move.
- Single Step Optimized Bot: The bot chooses the best move among the all possible moves at the moment. It does not consider the consequences of later moves.
- Minimax Bot: The bot is implemented with minimax algorithm but with a time cutoff at .1 seconds regardless of recursive depth

## Packages

Please check [`requirements.py`](requirements.txt).

## About This Fork

This fork highlights my personal contributions to the AI Chess Bot project originally developed collaboratively.

### 🔍 My Focus:
- Built multiple AI bots using random, greedy, minimax, and time-constrained strategies
- Developed a modular Pygame interface for both autonomous and manual play
- Integrated a heuristic fallback into the time-aware minimax agent to ensure sub-0.1s move selection
- Achieved an 80% win rate against baseline bots and a 9–2 record in competitive bot tournaments

See [`CONTRIBUTIONS.md`](./CONTRIBUTIONS.md) for a full breakdown of my work.

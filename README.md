# 8 Queens Problem Solver - Backtracking Algorithm

---

<div align="center">
  <img src="img/8queens_gif.gif" alt="Your GIF" width="400">
</div>


## N Queens Game

The N Queens Game is a classic chess puzzle that involves placing N queens on an N x N chessboard, such that no two queens threaten each other. A queen can move horizontally, vertically, or diagonally. The challenge is to find a configuration where all the queens are safe and do not attack each other.

In this repository, we provide a Python implementation of the 8 Queens Game. The game has two modes:

1. Manual Mode (queens.py): In this mode, you can run the `queens.py` script, which creates an 8x8 chessboard. You can manually place the queens on the board and see if you can solve the puzzle by positioning all the queens safely.

2. Automatic Mode (queens_backtracking.py): In this mode, you can run the `queens_backtracking.py` script, which automatically solves the 8 Queens problem using the backtracking algorithm.

## How to Play

### Manual Mode:

1. Make sure you have Python and Pygame installed on your system.

2. Clone this repository to your local machine.

3. Open a terminal or command prompt and navigate to the repository's directory.

4. Run the `queens.py` script:
   ```bash
   python queens.py
   ```

5. A window with an 8x8 chessboard will appear.

6. To place a queen on the board, click on the desired cell. A queen will be placed if the move is valid.

7. To delete a queen from the board, click on a cell with an already placed queen. The queen will be removed from that cell.

8. Try to position all the queens safely so that no two queens threaten each other.

### Automatic Mode:

1. Make sure you have Python installed on your system.

2. Clone this repository to your local machine.

3. Open a terminal or command prompt and navigate to the repository's directory.

4. Run the `queens_backtracking.py` script:
   ```bash
   python queens_backtracking.py
   ```

5. Sit back and enjoy the visualization of how the backtracking algorithm works to solve the 8 Queens problem. The script will display each step of the backtracking algorithm until a valid solution is found.

## What is Backtracking?

Backtracking is a systematic algorithm for finding solutions to problems by incrementally building candidates and discarding those that fail to satisfy the conditions of the problem. It is a depth-first search algorithm that works through all possible configurations of a problem until a solution is found or all options are exhausted.

In the context of the N Queens Game, backtracking is used to find a valid arrangement of queens on the chessboard without any queen attacking each other. The algorithm starts with an empty board and tries placing queens one by one in different columns, backtracking when it encounters a situation where a queen threatens another. It continues this process until all queens are placed correctly or exhausts all possibilities.

Backtracking is particularly useful when searching for a solution in a large search space where a naive brute-force approach would be impractical. It efficiently prunes branches that lead to invalid solutions, significantly reducing the search space and improving the time complexity.

## Contributing

Feel free to contribute to this repository by submitting bug reports, feature requests, or pull requests. We welcome any improvements or new features that enhance the N Queens Game implementation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Happy Problem Solving!** 🚀
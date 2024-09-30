class Game:
    """
    This class renders the board and contains main
    game logic.
    """
    def __init__(self, rows: int, cols: int) -> None:
        """
        Set up the board arguements

        Args:
            rows (int): The rows for the board
            cols (int): The columns for the board
        """
        self.rows: int = rows
        self.cols: int = cols

    def board_matrix(self) -> list[list[str]]:
        """
        This function builds the board matrix

        Returns:
            list[list[str]]: The board object
        """
        return [[' ' for col in range(self.cols)] for row in range(self.rows)]

    def render(self) -> None:
        """
        This function renders the board
        """
        board = self.board_matrix()
        print('+' + self.cols * '-' + '+')
        for row in board:
            print('|' + ''.join(row) + '|')
        print('+' + self.cols * '-' + '+')

if __name__ == "__main__":
    game = Game(5,6)
    game.render()

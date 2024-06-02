class Tablero_Consola:
    
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[" " for _ in range(width)] for _ in range(height)]

    def draw_board(self):
        top_bottom = "=" * self.width
        print(top_bottom)
        for row in self.board:
            print("=" + "".join(row) + "=")
        print(top_bottom)

    def place_pacman(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.board[y][x] = 'P'

    def clear_position(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.board[y][x] = ' '

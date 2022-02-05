class Matrix():
    def __init__(self, rows, columns, default_character = '@'):
        self.rows = rows
        self.columns = columns
        self.grid = [[default_character] * columns for _ in  range(rows)]
    def print_matrix(self):
        for row in self.grid:
            print(''.join(row))

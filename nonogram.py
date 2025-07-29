import random

class Puzzle:
    def __init__(self, size=5):
        self.size = size
        self.solution = self.generate_solution()
        self.clues = self.generate_clues()
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
    
    def generate_solution(self):
        """Генерирует случайное решение"""
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]
    
    def generate_clues(self):
        """Генерирует подсказки для строк и столбцов"""
        row_clues = []
        for row in self.solution:
            clues = []
            count = 0
            for cell in row:
                if cell == 1:
                    count += 1
                elif count > 0:
                    clues.append(count)
                    count = 0
            if count > 0:
                clues.append(count)
            row_clues.append(clues if clues else [0])
        
        col_clues = []
        for j in range(self.size):
            clues = []
            count = 0
            for i in range(self.size):
                if self.solution[i][j] == 1:
                    count += 1
                elif count > 0:
                    clues.append(count)
                    count = 0
            if count > 0:
                clues.append(count)
            col_clues.append(clues if clues else [0])
        
        return {
            "rows": row_clues,
            "columns": col_clues
        }
    
    def display(self):
        """Отображает текущее состояние головоломки"""
        # Отображение подсказок для столбцов
        max_col_clues = max(len(c) for c in self.clues["columns"])
        for i in range(max_col_clues):
            print(" " * (self.size * 2 + 1), end="")
            for j in range(self.size):
                clues = self.clues["columns"][j]
                idx = i - (max_col_clues - len(clues))
                print(f"{clues[idx] if idx >= 0 else ' '} ", end="")
            print()
        
        # Отображение сетки и подсказок для строк
        print("+" + "-" * (self.size * 2) + "+")
        for i in range(self.size):
            # Подсказки для строк
            clues_str = " ".join(str(c) for c in self.clues["rows"][i])
            print(f"|{clues_str.ljust(self.size * 2 - 1)}|", end="")
            
            # Сетка
            for j in range(self.size):
                cell = self.grid[i][j]
                symbol = " " if cell == 0 else "X" if cell == 1 else "?"
                print(f"{symbol} ", end="")
            print("|")
        print("+" + "-" * (self.size * 2) + "+")
    
    def toggle_cell(self, row, col):
        """Переключает состояние ячейки"""
        if 0 <= row < self.size and 0 <= col < self.size:
            self.grid[row][col] = (self.grid[row][col] + 1) % 3
            return True
        return False
    
    def is_solved(self):
        """Проверяет, решена ли головоломка"""
        for i in range(self.size):
            for j in range(self.size):
                # Проверяем только закрашенные ячейки (1)
                if self.grid[i][j] == 1 and self.solution[i][j] != 1:
                    return False
                elif self.grid[i][j] != 1 and self.solution[i][j] == 1:
                    return False
        return True
import random

class Puzzle:
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty
        self.elements = self.generate_elements()
        self.solution = self.generate_solution()
        self.player_solution = {}
        
    def generate_elements(self):
        elements = {
            "easy": [("H", 1), ("O", 8), ("C", 6), ("N", 7)],
            "medium": [("H", 1), ("O", 8), ("C", 6), ("N", 7), ("Na", 11), ("Cl", 17)],
            "hard": [("H", 1), ("O", 8), ("C", 6), ("N", 7), ("Na", 11), ("Cl", 17), ("Fe", 26), ("Ag", 47)]
        }
        return elements[self.difficulty]
    
    def generate_solution(self):
        # Формула воды
        if self.difficulty == "easy":
            return {"H": 2, "O": 1}
        
        # Формула соли
        if self.difficulty == "medium":
            return {"Na": 1, "Cl": 1}
        
        # Формула аммиака
        return {"N": 1, "H": 3}
    
    def display(self):
        print("Составьте химическую формулу:")
        print("Доступные элементы:")
        for i, (element, number) in enumerate(self.elements):
            print(f"{i+1}. {element} (атомный номер {number})")
        
        print("\nВведите элемент и количество атомов (например: H 2):")
        print("Введите 'готово', когда закончите")
    
    def handle_input(self, input_str):
        if input_str.lower() == "готово":
            return self.check_solution()
        
        try:
            parts = input_str.split()
            if len(parts) != 2:
                return False
                
            element_idx = int(parts[0]) - 1
            count = int(parts[1])
            
            if 0 <= element_idx < len(self.elements):
                element = self.elements[element_idx][0]
                self.player_solution[element] = count
                print(f"Добавлено: {element} x {count}")
                return True
        except:
            pass
        return False
    
    def check_solution(self):
        return self.player_solution == self.solution
    
    def is_solved(self):
        return self.check_solution()
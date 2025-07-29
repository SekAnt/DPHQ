import random

class Puzzle:
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty
        self.circuit = self.generate_circuit()
        self.solution = self.calculate_solution()
        self.inputs = [random.choice([0, 1]) for _ in range(3)]
    
    def generate_circuit(self):
        # Генерируем случайную схему в зависимости от сложности
        gates = {
            "easy": ["AND", "OR"],
            "medium": ["AND", "OR", "XOR"],
            "hard": ["AND", "OR", "XOR", "NAND", "NOR"]
        }[self.difficulty]
        
        circuit = []
        for i in range(3 if self.difficulty == "easy" else 5):
            gate = random.choice(gates)
            inputs = [random.randint(0, 1), random.randint(0, 1)]
            circuit.append((gate, inputs))
        
        return circuit
    
    def calculate_solution(self):
        # Вычисляем ожидаемый результат
        result = 0
        for gate, inputs in self.circuit:
            a, b = inputs
            if gate == "AND":
                res = a and b
            elif gate == "OR":
                res = a or b
            elif gate == "XOR":
                res = a ^ b
            elif gate == "NAND":
                res = not (a and b)
            elif gate == "NOR":
                res = not (a or b)
            result = int(res) if isinstance(res, bool) else res
        return result
    
    def display(self):
        print("Логическая схема:")
        for i, (gate, inputs) in enumerate(self.circuit):
            print(f"Этап {i+1}: {gate}({inputs[0]}, {inputs[1]})")
        
        print("\nВаши входные данные:")
        for i, val in enumerate(self.inputs):
            print(f"Вход {i+1}: {val}")
        
        print("\nИзмените входные данные так, чтобы результат был равен 1")
        print("Введите номера входов для изменения (например: 1 3):")
    
    def handle_input(self, input_str):
        try:
            # Обрабатываем ввод пользователя
            inputs_to_change = [int(i) for i in input_str.split()]
            for idx in inputs_to_change:
                if 1 <= idx <= len(self.inputs):
                    self.inputs[idx-1] = 1 - self.inputs[idx-1]  # Инвертируем значение
            
            # Пересчитываем результат
            current_result = self.calculate_current()
            print(f"Текущий результат: {current_result}")
            return current_result == 1
        except:
            return False
    
    def calculate_current(self):
        # Вычисляем текущий результат с учетом пользовательских входов
        values = self.inputs.copy()
        for gate, _ in self.circuit:
            a, b = values[0], values[1]
            if gate == "AND":
                res = a and b
            elif gate == "OR":
                res = a or b
            elif gate == "XOR":
                res = a ^ b
            elif gate == "NAND":
                res = not (a and b)
            elif gate == "NOR":
                res = not (a or b)
            values = [int(res) if isinstance(res, bool) else res] + values[2:]
        return values[0]
    
    def is_solved(self):
        return self.calculate_current() == 1
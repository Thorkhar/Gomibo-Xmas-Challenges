# Chocolate milk

class ChocolateMilk:
    def __init__(self, value:int) -> None:
        self.value = value
        self.history = [self.value]
        self.snd_history = []
        with open('input4.txt', 'r') as file:
            self.instructions = file.read().split('\n')
        self.current_instruction = 0 # Index of current instruction
        self.registers = {}

    def create_registers(self):
        for command_line in self.instructions:
            cmd = command_line.split()
            if cmd[1] not in self.registers:
                self.registers[cmd[1]] = 0
    
    def choose_method_for_instr(self, instr_idx: int):
        instruction_line = self.instructions[instr_idx].split()
        print(instruction_line)
        cmd = instruction_line[0]

    def santa_snd(self):
        print(self.value)

    def santa_set(self, y:int):
        self.value = y
        self.history.append(y)

    def santa_add(self, y:int):
        self.santa_set(self.value + y)

    def santa_mul(self, y:int):
        self.santa_set(self.value * y)

    def santa_mod(self, y:int):
        self.santa_set(self.value % y)
    
    def santa_rcv(self):
        if self.value != 0:
            idx = len(self.snd_history) - 1
            self.santa_set(self.snd_history[idx])
    
    def santa_jgz(self, y:int):
        if self.value > 0:
            pass

x = ChocolateMilk(0)
x.create_registers()
print(x.registers)
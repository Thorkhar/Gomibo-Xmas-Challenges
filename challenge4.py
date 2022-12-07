# Chocolate milk

class ChocolateMilk:
    def __init__(self) -> None:
        self.history = {}
        self.snd_history = []
        with open('input4.txt', 'r') as file:
            self.instructions = file.read().split('\n')
        self.current_instruction = 0 # Index of current instruction
        self.registers = {}
        self.create_registers()

    def create_registers(self):
        for command_line in self.instructions:
            cmd = command_line.split()
            if cmd[1] not in self.registers and cmd[1] != '1':
                self.registers[cmd[1]] = 0
                self.history[cmd[1]] = [0]
    
    def find_freq(self):
        while self.current_instruction in range(len(self.instructions)):
            self.ecex_instr(self.current_instruction)
            self.current_instruction += 1

    def ecex_instr(self, instr_idx: int):
        instr = self.instructions[instr_idx].split()
        print(instr)
        cmd = instr[0]
        if cmd == 'snd':
            self.santa_snd(instr[1])
        elif cmd == 'set':
            if instr[2] in self.registers:
                y = self.registers[instr[2]]
            else:
                y = int(instr[2])
            self.santa_set(instr[1], y)
        elif cmd == 'add':
            if instr[2] in self.registers:
                y = self.registers[instr[2]]
            else:
                y = int(instr[2])
            self.santa_add(instr[1], y)
        elif cmd == 'mul':
            if instr[2] in self.registers:
                y = self.registers[instr[2]]
            else:
                y = int(instr[2])
            self.santa_mul(instr[1], y)
        elif cmd == 'mod':
            if instr[2] in self.registers:
                y = self.registers[instr[2]]
            else:
                y = int(instr[2])
            self.santa_mod(instr[1], y)
        elif cmd == 'rcv':
            self.santa_rcv(instr[1])
        elif cmd == 'jgz':
            if instr[1] == '1':
                x = 1
            else:
                x = instr[1]

            if instr[2] in self.registers:
                y = self.registers[instr[2]]
            else:
                y = int(instr[2])
            self.santa_jgz(x, y)

    def santa_snd(self, x):
        print(self.registers[x])
        self.snd_history.append([x, self.registers[x]])

    def santa_set(self, x: str, y:int):
        if x in self.registers:
            self.registers[x] = y
            self.history[x].append(y)

    def santa_add(self, x: str, y:int):
        self.santa_set(x, self.registers[x] + y)

    def santa_mul(self, x: str, y:int):
        self.santa_set(x, self.registers[x] * y)

    def santa_mod(self, x, y:int):
        self.santa_set(x, self.registers[x] % y)
    
    def santa_rcv(self, x:str):
        if self.registers[x] != 0:
            idx = len(self.snd_history) - 1
            self.santa_set(x, self.snd_history[idx][1])
    
    def santa_jgz(self, x:str, y:int):
        if type(x) == int:
            x_prime = x
        else:
            x_prime = self.registers[x]
        if x_prime > 0:
            self.current_instruction -= (y + 1)

x = ChocolateMilk()
x.find_freq()
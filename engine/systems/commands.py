from dataclasses import dataclass

@dataclass
class CommandCode:
    opcode: str
    operands: str


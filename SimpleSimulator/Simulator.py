import os
import sys

# ----------------------- Register Initialization -----------------------

reg_add_val = [
    ["zero", "00000", 0],
    ["ra", "00001", 0],
    ["sp", "00010", 380],
    ["gp", "00011", 0],
    ["tp", "00100", 0],
    ["t0", "00101", 0],
    ["t1", "00110", 0],
    ["t2", "00111", 0],
    ["s0", "01000", 0],
    ["s1", "01001", 0],
    ["a0", "01010", 0],
    ["a1", "01011", 0],
    ["a2", "01100", 0],
    ["a3", "01101", 0],
    ["a4", "01110", 0],
    ["a5", "01111", 0],
    ["a6", "10000", 0],
    ["a7", "10001", 0],
    ["s2", "10010", 0],
    ["s3", "10011", 0],
    ["s4", "10100", 0],
    ["s5", "10101", 0],
    ["s6", "10110", 0],
    ["s7", "10111", 0],
    ["s8", "11000", 0],
    ["s9", "11001", 0],
    ["s10", "11010", 0],
    ["s11", "11011", 0],
    ["t3", "11100", 0],
    ["t4", "11101", 0],
    ["t5", "11110", 0],
    ["t6", "11111", 0],
]

# ----------------------- Memory Initialization -----------------------

data_memory  = {
    "0x00010000": "0b00000000000000000000000000000000",
    "0x00010004": "0b00000000000000000000000000000000",
    "0x00010008": "0b00000000000000000000000000000000",
    "0x0001000c": "0b00000000000000000000000000000000",
    "0x00010010": "0b00000000000000000000000000000000",
    "0x00010014": "0b00000000000000000000000000000000",
    "0x00010018": "0b00000000000000000000000000000000",
    "0x0001001c": "0b00000000000000000000000000000000",
    "0x00010020": "0b00000000000000000000000000000000",
    "0x00010024": "0b00000000000000000000000000000000",
    "0x00010028": "0b00000000000000000000000000000000",
    "0x0001002c": "0b00000000000000000000000000000000",
    "0x00010030": "0b00000000000000000000000000000000",
    "0x00010034": "0b00000000000000000000000000000000",
    "0x00010038": "0b00000000000000000000000000000000",
    "0x0001003c": "0b00000000000000000000000000000000",
    "0x00010040": "0b00000000000000000000000000000000",
    "0x00010044": "0b00000000000000000000000000000000",
    "0x00010048": "0b00000000000000000000000000000000",
    "0x0001004c": "0b00000000000000000000000000000000",
    "0x00010050": "0b00000000000000000000000000000000",
    "0x00010054": "0b00000000000000000000000000000000",
    "0x00010058": "0b00000000000000000000000000000000",
    "0x0001005c": "0b00000000000000000000000000000000",
    "0x00010060": "0b00000000000000000000000000000000",
    "0x00010064": "0b00000000000000000000000000000000",
    "0x00010068": "0b00000000000000000000000000000000",
    "0x0001006c": "0b00000000000000000000000000000000",
    "0x00010070": "0b00000000000000000000000000000000",
    "0x00010074": "0b00000000000000000000000000000000",
    "0x00010078": "0b00000000000000000000000000000000",
    "0x0001007c": "0b00000000000000000000000000000000",
}

stack_memory  = {
    "0x0000017c": "0b00000000000000000000000000000000",
    "0x00000178": "0b00000000000000000000000000000000",
    "0x00000174": "0b00000000000000000000000000000000",
    "0x00000170": "0b00000000000000000000000000000000",
    "0x0000016c": "0b00000000000000000000000000000000",
    "0x00000168": "0b00000000000000000000000000000000",
    "0x00000164": "0b00000000000000000000000000000000",
    "0x00000160": "0b00000000000000000000000000000000",
    "0x0000015c": "0b00000000000000000000000000000000",
    "0x00000158": "0b00000000000000000000000000000000",
    "0x00000154": "0b00000000000000000000000000000000",
    "0x00000150": "0b00000000000000000000000000000000",
    "0x0000014c": "0b00000000000000000000000000000000",
    "0x00000148": "0b00000000000000000000000000000000",
    "0x00000144": "0b00000000000000000000000000000000",
    "0x00000140": "0b00000000000000000000000000000000",
    "0x0000013c": "0b00000000000000000000000000000000",
    "0x00000138": "0b00000000000000000000000000000000",
    "0x00000134": "0b00000000000000000000000000000000",
    "0x00000130": "0b00000000000000000000000000000000",
    "0x0000012c": "0b00000000000000000000000000000000",
    "0x00000128": "0b00000000000000000000000000000000",
    "0x00000124": "0b00000000000000000000000000000000",
    "0x00000120": "0b00000000000000000000000000000000",
    "0x0000011c": "0b00000000000000000000000000000000",
    "0x00000118": "0b00000000000000000000000000000000",
    "0x00000114": "0b00000000000000000000000000000000",
    "0x00000110": "0b00000000000000000000000000000000",
    "0x0000010c": "0b00000000000000000000000000000000",
    "0x00000108": "0b00000000000000000000000000000000",
    "0x00000104": "0b00000000000000000000000000000000",
    "0x00000100": "0b00000000000000000000000000000000",
}

# ----------------------- Utility Functions -----------------------

def decimal_binary(decimal, num_bits=32, type_of_bit="signed"):
    if type_of_bit == "unsigned" or decimal >= 0:
        bin_no = ""
        temp = decimal
        while temp > 0:
            bin_no = str(temp % 2) + bin_no
            temp = temp // 2
        return bin_no.zfill(num_bits)
    else:
        bin_no = ""
        temp = abs(decimal)
        while temp > 0:
            bin_no = str(temp % 2) + bin_no
            temp = temp // 2
        bin_no = bin_no.zfill(num_bits)
        bin_no = twos_complement(bin_no)
        return bin_no

def twos_complement(value):
    inverted = "".join("1" if b == "0" else "0" for b in value)
    result = (int(inverted, 2) + 1) & 0xFFFFFFFF
    return format(result, "032b")

def binary_decimal(binary, type_of_bit="signed"):
    if type_of_bit == "unsigned" or binary[0] == "0":
        return int(binary, 2)
    else:
        return -int(twos_complement(binary), 2)

def decimal_to_hexadecimal(decimal):
    return format(decimal, "08x")

def find_reg(binary):
    return int(binary, 2)


# ----------------------- Instruction Handlers -----------------------

def R_Type(prog_memory, opern, reg_add_val):
    global prog_counter
    rd, rs1, rs2 = prog_memory[20:25], prog_memory[12:17], prog_memory[7:12]
    if find_reg(rd) == 0:
        prog_counter += 1
        return
    if opern == "add":
        result = reg_add_val[find_reg(rs1)][2] + reg_add_val[find_reg(rs2)][2]
    elif opern == "sub":
        result = reg_add_val[find_reg(rs1)][2] - reg_add_val[find_reg(rs2)][2]
    elif opern == "srl":
        result = rshift(rs1, rs2)
    elif opern == "slt":
        result = set_less_than(rs1, rs2)
    elif opern == "or":
        result = reg_add_val[find_reg(rs1)][2] | reg_add_val[find_reg(rs2)][2]
    elif opern == "and":
        result = reg_add_val[find_reg(rs1)][2] & reg_add_val[find_reg(rs2)][2]
    else:
        print("Unknown Operation:", opern)
        result = 0

    reg_add_val[find_reg(rd)][2] = result
    prog_counter += 1

def I_Type(prog_memory, opern, reg_add_val):
    global prog_counter
    imm, rs1, rd = prog_memory[0:12], prog_memory[12:17], prog_memory[20:25]
    switch_case = {
        "addi": handle_addi,
        "lw": handle_lw,
        "jalr": handle_jalr
    }
    if opern in switch_case:
        switch_case[opern](reg_add_val, rd, rs1, imm)

def S_Type(prog_memory, opern, reg_add_val):
    global prog_counter
    rs2, rs1, imm = prog_memory[7:12], prog_memory[12:17], prog_memory[0:7] + prog_memory[20:25]
    if opern == "sw":
        sw(rs1, rs2, imm, reg_add_val)
    prog_counter += 1

def B_Type(prog_memory, opern, reg_add_val):
    global prog_counter
    rs2, rs1 = prog_memory[7:12], prog_memory[12:17]
    imm = prog_memory[0] + prog_memory[24] + prog_memory[1:7] + prog_memory[20:24] + "0"
    immval = binary_decimal(imm, "2s") // 4
    jump_table = {"beq": beq, "bne": bne, "blt": blt}
    prog_counter = jump_table[opern](rs1, rs2, immval) if opern in jump_table else prog_counter + 1

def J_Type(prog_memory, opern, reg_add_val):
    global prog_counter
    rd = prog_memory[20:25]
    imm = prog_memory[0] + prog_memory[12:20] + prog_memory[11] + prog_memory[1:11] + "0"
    immval = binary_decimal(imm, "2s") // 4
    if find_reg(rd) != 0:
        reg_add_val[find_reg(rd)][2] = (prog_counter + 1) * 4
    prog_counter += immval

def bonus(prog_memory, opern, reg_add_val):
    global prog_counter
    if opern == "rst":
        reset_reg_add_val(reg_add_val)
        prog_counter += 1
    if opern == "virtual_halt":
        pass

# ----------------------- Instruction Subfunctions -----------------------

def rshift(rs1, rs2):
    shift_amount = int(decimal_binary(reg_add_val[find_reg(rs2)][2])[27:], 2)
    return reg_add_val[find_reg(rs1)][2] >> shift_amount

def set_less_than(rs1, rs2):
    return int(reg_add_val[find_reg(rs1)][2] < reg_add_val[find_reg(rs2)][2])

def sw(rs1, rs2, imm, reg_add_val):
    base = reg_add_val[find_reg(rs1)][2]
    offset = binary_decimal(imm, "2s")
    address = base + offset
    key = f"0x{address:08x}"
    val = "0b" + decimal_binary(reg_add_val[find_reg(rs2)][2], 32, "2s")
    (data_memory if key in data_memory else stack_memory)[key] = val

def handle_addi(reg_add_val, rd, rs1, imm):
    global prog_counter
    if find_reg(rd) != 0:
        reg_add_val[find_reg(rd)][2] = reg_add_val[find_reg(rs1)][2] + binary_decimal(imm, "2s")
    prog_counter += 1

def handle_lw(reg_add_val, rd, rs1, imm):
    global prog_counter
    if find_reg(rd) == 0:
        prog_counter += 1
        return
    base = reg_add_val[find_reg(rs1)][2]
    offset = binary_decimal(imm, "2s")
    key = f"0x{(base + offset):08x}"
    val = (data_memory if key in data_memory else stack_memory).get(key, "0b0")[2:]
    reg_add_val[find_reg(rd)][2] = binary_decimal(val, "2s")
    prog_counter += 1

def handle_jalr(reg_add_val, rd, rs1, imm):
    global prog_counter
    if find_reg(rd) != 0:
        reg_add_val[find_reg(rd)][2] = (prog_counter + 1) * 4
    prog_counter = (reg_add_val[find_reg(rs1)][2] + binary_decimal(imm, "2s")) & ~1
    prog_counter //= 4

def beq(rs1, rs2, immval):
    return prog_counter + immval if reg_add_val[find_reg(rs1)][2] == reg_add_val[find_reg(rs2)][2] else prog_counter + 1

def bne(rs1, rs2, immval):
    return prog_counter + immval if reg_add_val[find_reg(rs1)][2] != reg_add_val[find_reg(rs2)][2] else prog_counter + 1

def blt(rs1, rs2, immval):
    return prog_counter + immval if reg_add_val[find_reg(rs1)][2] < reg_add_val[find_reg(rs2)][2] else prog_counter + 1

def reset_reg_add_val(reg_add_val):
    for i in range(32):
        reg_add_val[i][2] = 0
# ----------------------- Output Functions -----------------------

def output(reg_add_val):
    binary_representations = []
    for value in reg_add_val:
        is_negative = value[2] < 0
        binary = bin(value[2] & 0xFFFFFFFF)[2:] if is_negative else bin(value[2])[2:].zfill(32)
        binary_representations.append("0b" + binary + " ")
    return "".join(binary_representations)

def output_decimal(reg_add_val):
    return " ".join([str(reg[2]) for reg in reg_add_val])

def output_mem():
    global data_memory
    prog_memorys = []
    for i in range(32):
        address = 0x00010000 + (i * 4)
        key_upper = f"0x{address:08X}"
        key_lookup = key_upper.lower()
        value = data_memory.get(key_lookup, "0b00000000000000000000000000000000")
        prog_memorys.append(f"{key_upper}:{value}")
    return "\n".join(prog_memorys)

def output_mem_decimal():
    global data_memory
    prog_memorys = []
    for i in range(32):
        address = 0x00010000 + (i * 4)
        key = f"0x{address:08x}"
        val = data_memory.get(key, "0b00000000000000000000000000000000").replace("0b", "")
        prog_memorys.append(f"{key}:{int(val, 2)}")
    return "\n".join(prog_memorys)

# ----------------------- File Reading -----------------------

def read_input_file(file_path):
    with open(file_path, "r") as f:
        prog_memorys = f.read().splitlines()
    operns = []
    for prog_memory in prog_memorys:
        prog_memory = prog_memory.strip()
        if not prog_memory:
            continue
        if prog_memory.startswith("0x"):
            break
        for token in prog_memory.split():
            if token.startswith("0b"):
                token = token[2:]
            if len(token) == 32 and all(c in "01" for c in token):
                operns.append(token)
    return operns

# ----------------------- Instruction Decoding -----------------------

def instrn_type(instrn):
    if instrn == "00000000000000000000000001100011":
        return ["virtual_halt", "bonus"]
    if instrn == "00000000000000000000000000000000":
        return ["rst", "bonus"]

    opcode = instrn[25:32]
    if opcode == "0110011":
        funct3 = instrn[17:20]
        funct7 = instrn[:7]
        if funct3 == "000":
            return ["add", "r"] if funct7 == "0000000" else ["sub", "r"]
        elif funct3 == "010":
            return ["slt", "r"]
        elif funct3 == "101":
            return ["srl", "r"]
        elif funct3 == "110":
            return ["or", "r"]
        elif funct3 == "111":
            return ["and", "r"]
    elif opcode == "0000011":
        return ["lw", "i"]
    elif opcode == "0010011":
        return ["addi", "i"]
    elif opcode == "1100111":
        return ["jalr", "i"]
    elif opcode == "0100011":
        return ["sw", "s"]
    elif opcode == "1100011":
        funct3 = instrn[17:20]
        if funct3 == "000":
            return ["beq", "b"]
        elif funct3 == "001":
            return ["bne", "b"]
        elif funct3 == "100":
            return ["blt", "b"]
    elif opcode == "1101111":
        return ["jal", "j"]
    return None

# ----------------------- Execution Driver -----------------------

def Exec_Program(prog_memory, dir_path_output):
    global prog_counter
    outdata_binary, outdata_decimal = [], []
    decimal_output_file = dir_path_output.replace(".txt", "_r.txt")

    prog_counter = 0
    while prog_counter < len(prog_memory):
        find_typ_opn = instrn_type(prog_memory[prog_counter])
        instruction = prog_memory[prog_counter]
        operation_type = find_typ_opn[0]
        instruction_type = find_typ_opn[1]
        if not find_typ_opn:
            print(f"Invalid opern at instruction {prog_counter}: {instruction}")
            break
        if instruction_type == "bonus":
            bonus(instruction, operation_type, reg_add_val)
            if operation_type == "virtual_halt":
                reg_add_val[0][2] = 0
                outdata_binary.append("0b" + decimal_binary(prog_counter * 4) + " " + output(reg_add_val))
                outdata_decimal.append(f"{prog_counter * 4} " + output_decimal(reg_add_val))
                break

        if instruction_type == "r":
            R_Type(instruction, operation_type, reg_add_val)
        elif instruction_type == "i":
            I_Type(instruction, operation_type, reg_add_val)
        elif instruction_type == "s":
            S_Type(instruction, operation_type, reg_add_val)
        elif instruction_type == "b":
            B_Type(instruction, operation_type, reg_add_val)
        elif instruction_type == "j":
            J_Type(instruction, operation_type, reg_add_val)

        reg_add_val[0][2] = 0
        outdata_binary.append("0b" + decimal_binary(prog_counter * 4) + " " + output(reg_add_val))
        outdata_decimal.append(f"{prog_counter * 4} " + output_decimal(reg_add_val))

    with open(dir_path_output, "w") as f:
        f.write("\n".join(outdata_binary) + "\n" + output_mem() + "\n")

    with open(decimal_output_file, "w") as f:
        f.write("\n".join(outdata_decimal) + "\n" + output_mem_decimal() + "\n")

# ----------------------- Main Call -----------------------

inp_file = sys.argv[1]
out_file = sys.argv[2]

def inp():
    prog_memory = read_input_file(inp_file)
    if prog_memory and prog_memory[-1] == "":
        prog_memory.pop()
    Exec_Program(prog_memory, out_file)

inp()

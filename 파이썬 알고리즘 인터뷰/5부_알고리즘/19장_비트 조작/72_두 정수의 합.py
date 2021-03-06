# 풀이 1. 전가산기 구현
def getSum_1(self, a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF
    
    a_bin = bin(a & MASK)[2:].zfill(32)
    b_bin = bin(b & MASK)[2:].zfill(32)
    
    result = []
    carry = 0
    sum = 0
    for i in range(32):
        A = int(a_bin[31 - i])
        B = int(b_bin[31 - i])
        
        # 전가산기 구현
        Q1 = A & B
        Q2 = A ^ B
        Q3 = Q2 & carry
        sum = carry ^ Q2
        carry = Q1 | Q3
        
        result.append(str(sum))
    
    if carry == 1:
        result.append('1')
        
    # 초과 자릿수 처리
    result = int(''.join(result[::-1]), 2) & MASK
    # 음수 처리
    if result > INT_MAX:
        result = ~(result ^ MASK)
    
    return result


# 풀이 2. 좀 더 간소한 구현
def getSum_2(self, a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF
    # 합, 자릿수 처리
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    
    # 음수 처리
    if a > INT_MAX:
        a = ~(a ^ MASK)
        
    return a

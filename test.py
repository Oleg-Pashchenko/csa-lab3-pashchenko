a, b = 0, 1
total = 0
c = 1
while True:
    a = b
    b = c
    c += a
    print(a, b, c, total)
    if b > 4000000:
        break
    if b % 2 == 0:
        total += b

print(total)

"""
MOV R1 1 ; A
MOV R2 1 ; B
MOV R3 2 ; C
MOV R4 0 ; COMPARE RESULT

MOV R10 0; RESULT
MOV R11 4000000; END
MOV R12 2; COMPARE ELEMENT
MOV R9 0; COMPARE ELEMENT #2
.LOOP:
    MOV R1 R2
    MOV R2 R3
    CMP R3 R11
    JG .EXIT
    
    MOV R4 R2
    MOD R4 R12
    CMP R4 R9
    JE .INC

.INC
    ADD R4 R3

.EXIT
    HLT
"""
section .text
    global add, sub, mul, div

add:
    mov rax, rcx        ; first argument (a)
    add rax, rdx        ; second argument (b)
    ret

sub:
    mov rax, rcx
    sub rax, rdx
    ret

mul:
    mov rax, rcx
    imul rax, rdx
    ret

div:
    mov rax, rcx
    cqo
    idiv rdx
    ret

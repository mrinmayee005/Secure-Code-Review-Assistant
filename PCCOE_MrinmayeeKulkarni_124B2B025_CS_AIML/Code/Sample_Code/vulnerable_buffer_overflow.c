// Sample_Code/vulnerable_buffer_overflow.c
// Reference test input containing Buffer Overflow vulnerability (CWE-120)
#include <stdio.h>
#include <string.h>

void process_input() {
    char buffer[64];
    printf("Enter username: ");
    gets(buffer); // Insecure function: no boundary checks
}

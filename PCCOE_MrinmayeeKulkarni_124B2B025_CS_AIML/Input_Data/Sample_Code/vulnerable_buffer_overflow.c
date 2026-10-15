// Input_Data/Sample_Code/vulnerable_buffer_overflow.c
#include <stdio.h>
#include <string.h>

void process_input() {
    char buffer[64];
    printf("Enter username: ");
    gets(buffer); // Vulnerable to stack-based buffer overflow
}

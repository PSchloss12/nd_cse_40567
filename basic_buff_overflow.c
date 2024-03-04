#include <stdio.h>
#include <string.h>
// strcat assumes 
//  1. the dest is long enought to hold incoming string 
//  2. incoming string is properly terminated with "\0"
int main(void){
    char gender[8] = "female";
    char fullname [8] = "";
    char firstname [6] = "Alice";
    char lastname [6] = "Smith";
    printf("With printf:\n");
    strcat(fullname, firstname); 
    strcat (fullname," ");
    // before buffer overflow
    strcat(fullname, lastname);
    // after buffer overflow
    // printf will print until reaching a string termination character
    printf("Full name is: %s\n", fullname);
    printf("Gender is: %s\n", gender);
    // we can see that gender now actually holds the string "ith\0le\0\0"
    // because the first four characters were overwritten by the overflow
    int i;
    printf("\nActual fullname string: ");
    for (i=0;i<8; i++){
        printf("%c", fullname[i]);
    } printf("\n");
    printf("Actual gender string: ");
    for (i=0;i<8; i++){
        printf("%c", gender[i]);
    } printf("\n");
}
// NB: here we assume our compiler reads arguments right to left for func calls

/* Call stack main() before strcat calls
 ret address
 calling stack pointer
 gender = "female"
 fullname = ""
 firstname = "Alice"
 lastname = "Smith"
*/

/* Call stack main() after strcat calls
 ret address
 calling stack pointer
 gender = "ith\0le\0\0"
 fullname = "Alice Sm"
 firstname = "Alice"
 lastname = "Smith"
*/
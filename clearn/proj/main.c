#include <stdio.h>
#include <stdlib.h>
#include "exercise_1.h"

int main()
{
    char * c ="Hello world!\n";
    int len ;
    len = count_char(c);
    printf("%s",copy_printf(c));
    return 0;
}

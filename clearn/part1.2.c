#include <stdio.h>
/*print for fahr = 0, 20, ..., 300;*/
main()
{
    float fahr, celsius;
    float lower, upper, step;

    lower = 0;
    upper = 300;
    step  = 20;

    fahr = lower;

    /*exercise 1-3 */
    printf("FahrenheitCelsius table.\n");
    while(fahr <= upper)
        {
            celsius = (5.0 / 9.0) * (fahr - 32.0);
            printf("%3.0f %6.1f\n", fahr, celsius);
            fahr = fahr + step;
        }

}

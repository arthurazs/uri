#include <stdio.h>

int main() {

    int units1, units2;
    double price1, price2;
    scanf("%*i %i %lf", &units1, &price1);
    scanf("%*i %i %lf", &units2, &price2);

    double total = (units1 * price1) + (units2 * price2);

    printf("VALOR A PAGAR: R$ %.2lf\n", total);

    return 0;
}

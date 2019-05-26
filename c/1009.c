#include <stdio.h>

int main() {

    float salary, total;
    scanf("%s");
    scanf("%f", &salary);
    scanf("%f", &total);

    printf("TOTAL = R$ %.2f\n", salary + (total * .15));

    return 0;
}

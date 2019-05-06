#include <stdio.h>

// préférer un type int pour main que void
int main()
{
    // Colors:
    char __RED__[] = "\e[0;31m";
    char __GREEN__[] = "\e[0;32m";
    char __YELLOW__[] = "\e[0;33m";
    char __D_BLUE__[] = "\e[0;34m";
    char __PURPLE__[] = "\e[0;35m";
    char __L_BLUE__[] = "\e[0;36m";

    int i = 0;
    int toggle = 0;

    char my_string[] = "Hello World !";

    for (i = 0; i < sizeof(my_string); i++) {

        if (my_string[i] == ' ') {
            printf(" ");
            continue;
        }

        switch (toggle % 6) {
            case 0:
                printf("%s%c", __RED__, my_string[i]);
                break;
            case 1:
                printf("%s%c", __GREEN__, my_string[i]);
                break;
            case 2:
                printf("%s%c", __YELLOW__, my_string[i]);
                break;
            case 3:
                printf("%s%c", __D_BLUE__, my_string[i]);
                break;
            case 4:
                printf("%s%c", __PURPLE__, my_string[i]);
                break;
            case 5:
                printf("%s%c", __L_BLUE__, my_string[i]);
                break;
            default:
                printf("ERROR\n");
                return -1;
        }

        toggle = toggle + 1;
    }

    printf("\n");

    return 0;
}



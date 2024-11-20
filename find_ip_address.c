#include <stdio.h>
#include <string.h>

void findIPClass(const char* ip) {
    int s[4], temp;
    int count = sscanf(ip, "%d.%d.%d.%d", &s[0], &s[1], &s[2], &s[3]);

    if (count == 4) {
        temp = s[0];
        if (temp >= 0 && temp <= 127)
            printf("This IP address belongs to Class A\n");
        else if (temp >= 128 && temp <= 191)
            printf("This IP address belongs to Class B\n");
        else if (temp >= 192 && temp <= 223)
            printf("This IP address belongs to Class C\n");
        else if (temp >= 224 && temp <= 239)
            printf("This IP address belongs to Class D\n");
        else if (temp >= 240 && temp <= 255)
            printf("This IP address belongs to Class E\n");
        else
            printf("This is an invalid IP address\n");
    } else {
        printf("This is an invalid IP address\n");
    }
}

int main() {
    char ip[20];
    printf("Enter IP address: ");
    scanf("%s", ip);
    findIPClass(ip);
    return 0;
}

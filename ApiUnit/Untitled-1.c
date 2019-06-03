#include <stdio.h>

int main()
{
    char szS[32];
    int i = 0;
    int j = 0;
    char c = 'A';
    
    j = 'Q' - 'A'; 
    i++;
    j++;
    c += j - 2;
    szS[i] = c;
    c -= 12;
    szS[--i] = c;
    i++;
    szS[++i] = 0;
    
    printf("%s", szS);
    
    return 0;
}

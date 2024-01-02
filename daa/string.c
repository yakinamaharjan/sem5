#include <stdio.h>
#include <string.h>

int min(int x, int y, int z)
{
    return x < y ? (x < z ? x : z) : (y < z ? y : z);
}

int editDist(char *str1, char *str2, int m, int n)
{
    if (m == 0)
        return n;

    if (n == 0)
        return m;

    if (str1[m - 1] == str2[n - 1])
        return editDist(str1, str2, m - 1, n - 1);

    return 1 + min(
        editDist(str1, str2, m, n - 1),
        editDist(str1, str2, m - 1, n),
        editDist(str1, str2, m - 1, n - 1));
}

int main()
{
    char str1[20];
    char str2[20];

    printf("Enter two strings:\n");
    scanf("%s %s", str1, str2);
    int m = strlen(str1);
    int n = strlen(str2);

    printf("String edit distance: %d", editDist(str1, str2, m, n));

    return 0;
}

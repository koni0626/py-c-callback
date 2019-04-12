#include <stdio.h>

int g_num = 0;

void myfunc1()
{
    printf("%d\n", g_num);
    g_num++;
}

void myfunc2()
{
    printf("%d\n",g_num);
}

void myfunc3(char *pStr)
{
    printf("%s\n", pStr);
}

void call_back(void(*cb)(const char *))
{
    cb("callback!!");
}

# py-c-callback
C言語の関数をpythonから呼び出して、C言語の関数でpythonの関数をコールバックするサンプル
Cをビルドするときは
gcc -fPIC -shared main.c -o libtest.so

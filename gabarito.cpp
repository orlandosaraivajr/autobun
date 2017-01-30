/*
Crie um programa que receba dois números inteiros (num1 e num2) 
e realize a soma dos dois números.
Imprimir a soma dos dois números no final.

Saída Esperada
==============
Lendo o primeiro número...: 12

Lendo o segundo número....: 13
25

*/

#include <iostream>
using namespace std;
int main() {
  int num1;
  int num2;
  int soma;
  cout << "Lendo o primeiro número...: ";
  cin >> num1;
  cout << endl;
  cout << "Lendo o segundo número....: ";
  cin >> num2;
  soma = num1 + num2;
  cout << soma << endl;
  return 0;
}

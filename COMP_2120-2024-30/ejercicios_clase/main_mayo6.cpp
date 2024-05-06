#include <iostream>
#include <string.h>
using namespace std;
int main() {
    cout<<"Hola Mundo\n";
    cout<<"Hola Mundo\n";
    cout<<"Hola Mundo\n";
    cout<<"Hola Mundo\n";
    cout<<"Hola Mundo\n";
    int a;
    float x;
    char m;
    string letra;
    a = 3;
    x = 1.0;
    m = 'a';
    letra = "casa";
    cout<< a<<"\n"<<x<<"\n"<<m<<"\n"<<letra<<endl;
    cout<<"\nIngrese su nombre: ";
    cin>>letra;
    cout<<endl<<"Bienvenido "<<letra<<"."<<endl;
    for(a=1;a<=10;a=a+1){
        cout<<a<<"\t";
    }
    return 0;
}

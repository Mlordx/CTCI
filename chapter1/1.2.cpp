#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

char* flip(char* str){
  size_t len = strlen(str);

  if(len <= 1) return str;

  char* start = str;
  char* end = str + len - 1;
  char* tmp;
  while(start < end){
    swap(*start,*end);
    start++;
    end--;
  }
  cout << str << endl;
  return str;
}


int main(){
  char a[] = "Mateus Barros Rodrigues";
  char b[] = "Arara";
  char c[] = "Oi eu sou a xuxa";
  flip(a);
  flip(b);
  flip(c);
  
  return 0;
}

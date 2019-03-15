#include <string>
#include <iostream>

using namespace std;

string& replace(string& str){
  int whitespaces = 0;
  for(size_t i = 0; i < str.size(); i++)
    if(str[i] == ' ')
      whitespaces++;

  size_t j = str.size();
  str.resize(str.size() + 2*whitespaces);
  size_t i = str.size();

  for(;j > 0; j--){
    if(str[j-1] == ' '){
      str[i-1] = '0';
      str[i-2] = '2';
      str[i-3] = '%';
      i -= 3;
    }else{
      str[i-1] = str[j-1];
      i--;
    }
  }
  return str;
}

int main(){
  string a = "A B C D E";
  
  cout << replace(a) << endl;
  return EXIT_SUCCESS;
}

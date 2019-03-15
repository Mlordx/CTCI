#include <string>
#include <iostream>

using namespace std;

string& remove_duplicates(string& str){
  size_t len = str.size();

  if(len <= 1) return str;

  bool seen[128] = {false};

  size_t i = 1;

  seen[str[0]] = true;

  for(size_t j = 1; j < len; j++){
    if(seen[str[j]] == false){
      seen[str[j]] = true;
      str[i] = str[j];
      i++;
    }
  }

  str.resize(i);
  str.shrink_to_fit();
  return str;
}

int main(){
  string a = "abacada";

  cout << remove_duplicates(a) << endl;
  
  return EXIT_SUCCESS;
}

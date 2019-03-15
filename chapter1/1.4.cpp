#include <string>
#include <iostream>

using namespace std;

bool isAnagram(string& a, string& b){
  int A[128] = {0};
  int B[128] = {0};

  for(size_t i = 0; i < a.size(); i++) A[a[i]]++;
  for(size_t i = 0; i < b.size(); i++) B[b[i]]++;
  
  for(size_t i = 0; i < 128; i++)
    if(A[i] != B[i]) return false;
  
  return true;
}

int main(){
  string a = "Batata";
  string b = "atataB";

  cout << "is it anagram?: " << isAnagram(a,b) << endl;

  
  return EXIT_SUCCESS;
}

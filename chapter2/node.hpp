#ifndef __LIST_HPP__
#define __LIST_HPP__

template<typename T>
class List{
private:
  struct node{
    T value;
    node* next = nullptr;
  };

  node* head = nullptr;
  size_t size = 0;

public:
  ~List(){
    node* position = head;

    while(position != nullptr){
      node* toDelete = position;
      position = position->next;
      delete toDelete;
    }
  }

  void insert(const& T value){
    node* old = head;
    head = new node;
    head->value = value;
    head->next = old;
    size++;
  }

  size_t size() const{
    return size;
  }
};

#endif /* __LIST_HPP__ */

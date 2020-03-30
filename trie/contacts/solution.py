#!/bin/python3

import os

class TrieNode:
    def __init(self):
      self.__children = {}
      self.__is_complete_word = False

    def __init__(self, value, is_complete_word):
      self.__init()
      self.__value = value
      self.__is_complete_word = is_complete_word

    def __hash__(self):
        return hash(self.__value)
    
    def find_all_children_complete_words(self):
        words = []        
        for c in self.__children.values():
            children = c.find_all_children_complete_words()
            if children:
                words = words + children        
        
        if self.__is_complete_word:            
            words.append(self)

        return words
        
    def add_children(self, letter, is_complete_word):
        self.__children[letter] = TrieNode(letter, is_complete_word)        

    def find(self, value):
      if (value in self.__children):
        return self.__children[value]
      else:
        return False


class Trie:
    def __init__(self):        
        self.__root = TrieNode("*", False)
          
    def __str__(self):
      return str(self.__root)   

    def find_partial(self, word):
        current = self.__root

        for c in word:            
            if current:
              current = current.find(c)
            else: return []

        if current:
            return current.find_all_children_complete_words()

        return []
        
    def add(self, word):
        current = self.__root

        for c in word[:-1]:
            next_node = current.find(c)
            if (not next_node):
                current.add_children(c, False)
                next_node = current.find(c)
            current = next_node

        current.add_children(word[-1], True)                    
 
#
# Complete the contacts function below.
#
def contacts(queries):
    trie = Trie()
    resultList = []
    for q in queries:
        op, op_value = q
        if op == 'add':
            trie.add(op_value)
        elif op == 'find':
            resultList.append(len(trie.find_partial(op_value)))
    return resultList

def process_input():
  queries = []

  input_file = open("input02.txt", 'r')
  queries_rows = int(input_file.readline())
  for _ in range(queries_rows):
    queries.append(input_file.readline().rstrip().split())
  input_file.close()
  
  return queries


if __name__ == '__main__':    
    result = contacts(process_input())

    fptr = open("saci.txt", 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()  
# YOUR CODE AND HEADING HERE
import ctypes
class DynamicArray:
  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)
   #display array  
  def __str__(self):
    if self.__n == 0:
        return "[]"

    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
    return out[:-2] + ']'
  
  #add elements to array  
  def append(self,item):
    if self.__n == self.__capacity:
      self.__resize()
    self.__A[self.__n] = item
    self.__n += 1
       
  
  #increasing array size when at max
  def __resize(self):
    self.__capacity = self.__capacity * 2
    temp = self.__make_array(self.__capacity)
    for i in range(len(self.__A)):
      temp[i] = self.__A[i]
    self.__A = temp  



    return self.__capacity    
  
  #get the max capacity of the array
  def get_cap(self):
    return self.__capacity
  
  #generates a new array
  def __make_array(self, c):
      """return new array with capacity c"""
      return (c * ctypes.py_object)()
  #allows indexing of the array
  def __getitem__(self, index):
    """return element at index"""
    if k <= 0 or k >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[index]
  #returns size of array
  def __len__(self):
    return self.__n



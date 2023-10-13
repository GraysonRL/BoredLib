__version__ = '0.1.0'


class Math: 
  def iseven(self, n, ignore=0):
    if type(n) != 'int' and ignore==0:
      raise TypeError(f"TypeError: you entered an object of type '{type(n)}' when an object of type int is needed. If you want the function to convert a non-int to an int, add the ignore paramater and set to 1.")
    if n**2 == 0:
      return True
    else:
       return False
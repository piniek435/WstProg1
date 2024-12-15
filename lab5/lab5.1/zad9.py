import math
import keyword

funkcje_math = [elem for elem in dir(math) if not elem.startswith("__")]
print(funkcje_math)

funkcje_keyword = [elem for elem in dir(keyword) if not elem.startswith("__")]
print(funkcje_keyword)

funkcje_tuple = [elem for elem in dir(tuple) if not elem.startswith("__")]
print(funkcje_tuple)

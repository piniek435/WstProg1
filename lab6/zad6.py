import numpy as np

macierzA = np.zeros((3, 3), dtype=int)
macierzA[2, 0] = 1
macierzA[2, 1] = 1
macierzA[2, 2] = 1

macierzB = np.zeros((3, 3), dtype=int)
macierzB[1, 1] = 1
macierzB[2, 1] = 1

macierzC = np.zeros((3, 3), dtype=int)
macierzC[2, 0] = 1
macierzC[2, 1] = 1
macierzC[2, 2] = 1
macierzC[1, 0] = 1
macierzC[1, 1] = 1
macierzC[1, 2] = 1

macierzD = np.zeros((3, 3), dtype=int)
macierzD[0, 0] = 1
macierzD[0, 2] = 1
macierzD[1, 0] = 1
macierzD[1, 2] = 1

macierzE = np.zeros((3, 3), dtype=int)
macierzE[1, 1] = 1
macierzE[1, 2] = 1
macierzE[2, 1] = 1
macierzE[2, 2] = 1

print(macierzA, "\n""\n", macierzB, "\n""\n", macierzC, "\n""\n", macierzD, "\n""\n", macierzE)
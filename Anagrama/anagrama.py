def anagrama(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    word1_array = list(word1)
    word2_array = list(word2)

    word1_array.sort()
    word2_array.sort()

    word1_sorted = "".join(word1_array)
    word2_sorted = "".join(word2_array)

    return word1_sorted == word2_sorted

palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

es_anagrama = anagrama(palabra1, palabra2)

if es_anagrama:
    print("Ambas palabras son anagramas.")
else:
    print("Lo siento, las palabras no son anagramas.")
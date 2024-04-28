class TransformadorInserio:
    def transformador_segun_vocales(s):
        print(
            "Este transformador retorna tu mayor deseo segun un intenso analisis psicologico atraves de la aleatoridad de tu texto")
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for char in s:
            if char in vowels:
                vowels[char] += 1
        max_vowel = max(vowels, key=vowels.get)
        if max_vowel == 'a':
            return 'tu mayor deseo es que el cancer sea contagioso'
        elif max_vowel == 'e':
            return 'tu mayor deseo es ser invisible'
        elif max_vowel == 'i':
            return 'tu mayor deseo es poder teleportarte'
        elif max_vowel == 'o':
            return 'tu mayor deseo es cometer crimenes de odio en israel'
        elif max_vowel == 'u':
            return 'Tu mayor deseo es la mayor aberracion jamas pensada por un humano,estas tan mal de la cabeza que incluso el diablo duda de que seas una creacion de dios'
        else:
            return "Tu mayor deseo es desaparecer de la existencia"

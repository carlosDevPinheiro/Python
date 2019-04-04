def busca_letra():
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    contador6 = 0
    contador7 = 0
    contador8 = 0
    contador9 = 0
    contador10 = 0
    contador11 = 0
    contador12 = 0
    contador13 = 0
    contador14 = 0
    contador15 = 0
    contador16 = 0
    contador17 = 0
    contador18 = 0
    contador19 = 0
    contador20 = 0
    contador21 = 0
    contador22 = 0
    contador23 = 0
    contador24 = 0
    contador25 = 0
    contador26 = 0
    letra1 = len(palavra)
    
    for letra in palavra:
        if letra == 'a':
            contador1 += 1
        if letra == 'b':
            contador2 += 1
        if letra == 'c':
            contador3 += 1
        if letra == 'd':
            contador4 += 1
        if letra == 'e':
            contador5 += 1
        if letra == 'f':
            contador6 += 1
        if letra == 'g':
            contador7 += 1
        if letra == 'h':
            contador8 += 1
        if letra == 'i':
            contador9 += 1
        if letra == 'j':
            contador10 += 1
        if letra == 'k':
            contador11 += 1
        if letra == 'l':
            contador12 += 1
        if letra == 'm':
            contador13 += 1
        if letra == 'n':
            contador14 += 1
        if letra == 'o':
            contador15 += 1
        if letra == 'p':
            contador16 += 1
        if letra == 'q':
            contador17 += 1
        if letra == 'r':
            contador18 += 1
        if letra == 's':
            contador19 += 1
        if letra == 't':
            contador20 += 1
        if letra == 'u':
            contador21 += 1
        if letra == 'v':
            contador22 += 1
        if letra == 'w':
            contador23 += 1
        if letra == 'x':
            contador24 += 1
        if letra == 'y':
            contador25 += 1
        if letra == 'z':
            contador26 += 1
    print "Na palavra",palavra,"existem: \n"
    print contador1,'ocorrencias da letra a'
    print contador2,'ocorrencias da letra b'
    print contador3,'ocorrencias da letra c'
    print contador4,'ocorrencias da letra d'
    print contador5,'ocorrencias da letra e'
    print contador6,'ocorrencias da letra f'
    print contador7,'ocorrencias da letra g'
    print contador8,'ocorrencias da letra h'
    print contador9,'ocorrencias da letra i'
    print contador10,'ocorrencias da letra j'
    print contador11,'ocorrencias da letra k'
    print contador12,'ocorrencias da letra l'
    print contador13,'ocorrencias da letra m'
    print contador14,'ocorrencias da letra n'
    print contador15,'ocorrencias da letra o'
    print contador16,'ocorrencias da letra p'
    print contador17,'ocorrencias da letra q'
    print contador18,'ocorrencias da letra r'
    print contador19,'ocorrencias da letra s'
    print contador20,'ocorrencias da letra t'
    print contador21,'ocorrencias da letra u'
    print contador22,'ocorrencias da letra v'
    print contador23,'ocorrencias da letra w'
    print contador24,'ocorrencias da letra x'
    print contador25,'ocorrencias da letra y'
    print contador26,'ocorrencias da letra z'

    print "A mensagem tem",letra1,"letras \n"

    ika = float(contador1 * (contador1 - 1)) / (letra1 * (letra1 -1))
    ikb = float(contador2 * (contador2 - 1)) / (letra1 * (letra1 -1))
    ikc = float(contador3 * (contador3 - 1)) / (letra1 * (letra1 -1))
    ikd = float(contador4 * (contador4 - 1)) / (letra1 * (letra1 -1))
    ike = float(contador5 * (contador5 - 1)) / (letra1 * (letra1 -1))
    ikf = float(contador6 * (contador6 - 1)) / (letra1 * (letra1 -1))
    ikg = float(contador7 * (contador7 - 1)) / (letra1 * (letra1 -1))
    ikh = float(contador8 * (contador8 - 1)) / (letra1 * (letra1 -1))
    iki = float(contador9 * (contador9 - 1)) / (letra1 * (letra1 -1))
    ikj = float(contador10 * (contador10 - 1)) / (letra1 * (letra1 -1))
    ikk = float(contador11 * (contador11 - 1)) / (letra1 * (letra1 -1))
    ikl = float(contador12 * (contador12 - 1)) / (letra1 * (letra1 -1))
    ikm = float(contador13 * (contador13 - 1)) / (letra1 * (letra1 -1))
    ikn = float(contador14 * (contador14 - 1)) / (letra1 * (letra1 -1))
    iko = float(contador15 * (contador15 - 1)) / (letra1 * (letra1 -1))
    ikp = float(contador16 * (contador16 - 1)) / (letra1 * (letra1 -1))
    ikq = float(contador17 * (contador17 - 1)) / (letra1 * (letra1 -1))
    ikr = float(contador18 * (contador18 - 1)) / (letra1 * (letra1 -1))
    iks = float(contador19 * (contador19 - 1)) / (letra1 * (letra1 -1))
    ikt = float(contador20 * (contador20 - 1)) / (letra1 * (letra1 -1))
    iku = float(contador21 * (contador21 - 1)) / (letra1 * (letra1 -1))
    ikv = float(contador22 * (contador22 - 1)) / (letra1 * (letra1 -1))
    ikw = float(contador23 * (contador23 - 1)) / (letra1 * (letra1 -1))
    ikx = float(contador24 * (contador24 - 1)) / (letra1 * (letra1 -1))
    iky = float(contador25 * (contador25 - 1)) / (letra1 * (letra1 -1))
    ikz = float(contador26 * (contador26 - 1)) / (letra1 * (letra1 -1))

    ikappa = ika+ikb+ikc+ikd+ike+ikf+ikg+ikh+iki+ikj+ikk+ikl+ikm+ikn+iko+ikp+ikq+ikr+iks+ikt+iku+ikv+ikw+ikx+iky+ikz
    IC = ikappa / 0.0385
    print "Indice Kappa = ", ikappa
    print "IC = ", IC

palavra = raw_input("Digite a mensagem criptografada: ")
busca_letra()
#Fonte: https://rosettacode.org/wiki/Vigen%C3%A8re_cipher/Cryptanalysis

from string import uppercase
from operator import itemgetter
 
def vigenere_decrypt(target_freqs, input):
    nchars = len(uppercase)
    ordA = ord('A')
    sorted_targets = sorted(target_freqs)
 
    def frequency(input):
        result = [[c, 0.0] for c in uppercase]
        for c in input:
            result[c - ordA][1] += 1
        return result
 
    def correlation(input):
        result = 0.0
        freq = frequency(input)
        freq.sort(key=itemgetter(1))
 
        for i, f in enumerate(freq):
            result += f[1] * sorted_targets[i]
        return result
 
    cleaned = [ord(c) for c in input.upper() if c.isupper()]
    best_len = 0
    best_corr = -100.0
 
    # Supondo que, se houver menos de 20 caracteres por coluna, entende-se que "chave muito longa para adivinhar"
    for i in xrange(2, len(cleaned) // 20):
        pieces = [[] for _ in xrange(i)]
        for j, c in enumerate(cleaned):
            pieces[j % i].append(c)
 
        # A correlacao parece aumentar para pedacos menores / chaves mais longas; aqui faz-se uma compensacao
        corr = -0.5 * i + sum(correlation(p) for p in pieces)
 
        if corr > best_corr:
            best_len = i
            best_corr = corr
 
    if best_len == 0:
        return ("Text is too short to analyze", "")
 
    pieces = [[] for _ in xrange(best_len)]
    for i, c in enumerate(cleaned):
        pieces[i % best_len].append(c)
 
    freqs = [frequency(p) for p in pieces]
 
    key = ""
    for fr in freqs:
        fr.sort(key=itemgetter(1), reverse=True)
 
        m = 0
        max_corr = 0.0
        for j in xrange(nchars):
            corr = 0.0
            c = ordA + j
            for frc in fr:
                d = (ord(frc[0]) - c + nchars) % nchars
                corr += frc[1] * target_freqs[d]
 
            if corr > max_corr:
                m = j
                max_corr = corr
 
        key += chr(m + ordA)
 
    r = (chr((c - ord(key[i % best_len]) + nchars) % nchars + ordA)
         for i, c in enumerate(cleaned))
    return (key, "".join(r))
 
 
def main():
    encoded = raw_input("Digite a mensagem a ser decodificada: ")
        
 
    english_frequences = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
 
    (key, decoded) = vigenere_decrypt(english_frequences, encoded)
    print "Chave:", key
    print "\nTexto decodificado:", decoded
 
main()
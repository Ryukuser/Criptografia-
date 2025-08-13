# Criptografia-
Exercícios de implementação com criptografia |  Elaborei  programas que possam cifrar e decifrar uma mensagem, permitindo utilizar a  cifra de cesar. Pra aumentar meu conhecimento. Elaborei um segundo programa para fazer a criptoanálise e decifrar um texto cifrado, usando análise de  frequências (em Português BR ou Inglês).  

Exemplo de uso em cesar.py:

Entradas: Processo (cifrar/decifrar), chave, texto claro/texto cifrado. Saída: texto cifrado/claro

Entrada: INTERNET OF THINGS

Processo: cifrar
Chave: 6
Texto: Entrada
Saída: OTZKTZ UL ZNOTMY

Entrada: BNQNMZ

Processo: decifrar
Chave: -1
Texto: Entrada
Saída: CORONA

Exemplo de uso em criptoanalise.py:


O programa de criptoanálise calculará a frequência de letras no texto cifrado e comparará com as frequências esperadas no português brasileiro (baseadas em STTMedia). Ele testará todas as chaves possíveis ( a ) e escolherá a que produzir o texto com distribuição de frequências mais próxima da esperada, usando a soma dos erros quadráticos como métrica.

texto exemplo: criptoanálise para decifrar o seguinte texto:

SquiqhsyfxuhCujxetydmxysxuqsxbujjuhydjxufbqydjunjyihufbqsutroqbujjuhiecuvynutdkcruh evfeiyjyeditemdjxuqbfxqrujJxucujxetyidqcutqvjuhZkbykiSquiqhmxekiutyjydxyifhylqjusehhu ifedtudsu

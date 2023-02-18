def escreva(msg):
    esp = len(msg) + 4
    print('~' * esp)
    print(f'{msg:^{esp}}')
    print('~' * esp)


# PROGRAMA PRINCIPAL
escreva('Luiz Felipe Cantanhede Cristino')
escreva('Curso em Vídeo')
escreva('CeV')

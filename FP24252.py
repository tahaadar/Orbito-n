# TAD DE POSICÕES

# Construtor
def cria_posicao(col, lin):
    """
    cria_posicao(col, lin) -> posicao
    
    Recebe um cadeia de caractere col correspondente à coluna (deve estar entre 'a' e 'j') e um inteiro lin correspondente à linha (deve estar entre 1 e 10),
    e devolve uma posição correspondente representada como um tuplo (col, lin). O construtor verifica se os argumentos são válidos.

    Levanta uma ValueError com a mensagem 'cria_posicao: argumentos invalidos' caso os argumentos não sejam válidos.
    """
    if not (type(col) == str and len(col) == 1 and type(lin) == int and ord("a") <= ord(col) <= ord("j") and 10 >= lin >= 1):
    # Esta linha de código valida se todos os argumentos estão na forma desejada;
    # Se um ou mais dos requisitos retornarem False, é levantada uma ValueError.
        raise ValueError("cria_posicao: argumentos invalidos")
    return (col, lin)
    # Retorna a representação interna da posição

# Seletores
def obtem_pos_col(p):
    """
    Obtém a coluna da posição fornecida.

    Argumento: p (posicao): A posição da qual se deseja obter a coluna.

    Retorna: str: A coluna correspondente da posição.
    """
    return p[0]
    # Acessa o elemento do índice associado à coluna na representação interna da posição.
def obtem_pos_lin(p):
    """
    Obtém a linha da posição fornecida.

    Argumento: p (posicao): A posição da qual se deseja obter a linha.

    Retorna: int: A linha correspondente da posição.
    """
    return p[1]
    #  Acessa o elemento do índice associado à linha na representação interna da posição.

# Reconhecedor
def eh_posicao(arg):
    """
    Verifica se o argumento fornecido é uma posição válida.

    Argumento: arg: Um argumento qualquer.

    Retorna: bool: True se o argumento for uma posição válida no TAD 'posicao', False caso contrário.
    """

    return (type(arg) == tuple and len(arg) == 2 and type(arg[0]) == str and len(arg[0]) == 1 and type(arg[1]) == int and
    ord("a") <= ord(arg[0]) <= ord("j") and 10 >= arg[1] >= 1)
    # Retorna True se o argumento estiver totalmente em conformidade com a representação interna das posições, 
    # False se uma ou mais partes não estiverem em conformidade.

# Teste
def posicoes_iguais(p1, p2):
    """
    Verifica se duas posições fornecidas são iguais.

    Argumentos:
    p1: Primeira posição a ser comparada.
    p2: Segunda posição a ser comparada.

    Retorna: bool: True se ambas as posições forem válidas e iguais, False caso contrário.
    """
    return (eh_posicao(p1) and eh_posicao(p2) and obtem_pos_col(p1) == obtem_pos_col(p2) and obtem_pos_lin(p1) == obtem_pos_lin(p2))
    # Retorna True se ambos os argumentos forem posições e suas colunas e linhas forem iguais, 
    # False se um ou mais dos requisitos não forem verdadeiros.

# Transformadores
def posicao_para_str(p):
    """
    Converte uma posição do tipo 'posicao' para uma string.

    Argumento: p (posicao): A posição a ser convertida.

    Retorna: str: A cadeia de caracteres que representa a posição, no formato 'coluna' seguida pelo 'número da linha'.
    """
    return f"{p[0]}{p[1]}"
    # Transforme a coluna da posição seguida pela linha da posição para em uma string na mesmo ordem
def str_para_posicao(s):
    """
    Converte uma string que representa uma posição para o tipo 'posicao'.

    Argumento: s (str): A string representando a posição.

    Retorna: posicao: A posição representada pelo argumento de entrada.
    """
    return (s[0], int(s[1::]))
    # Transforma o elemento do índice que representa uma coluna e o elemento do índice que representa uma linha na representação interna de posições.

# FUNÇÕES DE ALTO NÍVEL DE POSICÕES
def eh_posicao_valida(p, n):
    """
    Verifica se a posição `p` é válida dentro de um tabuleiro de Orbito-n.

    Argumentos:
    p (posicao): Posição a ser verificada.
    n (int): Número de órbitas do tabuleiro.

    Retorna: bool: Retorna True se `p` for uma posição válida dentro do tabuleiro, False caso contrário.
    """
    return ( eh_posicao(p) and 2 <= n <= 5 and 0 < obtem_pos_lin(p) <= n * 2 and
    ord("a") <= ord(obtem_pos_col(p)) < (ord("a") + n * 2))
    # Retorna True se o argumento 'p' for uma posição possível e se o argumento 'n' tiver um tamanho válido
    # e se o argumento 'p' for uma posição válida em um jogo de orbito-n de órbita 'n',
    # Retorna False se um ou mais desses requisitos não forem verdadeiros
def obtem_posicoes_adjacentes(p, n, d):
    """
    Obtém as posições adjacentes à posição `p` no tabuleiro de Orbito-n.

    Argumentos:
    p (posicao): Posição inicial para encontrar as adjacências.
    n (int): Número de órbitas do tabuleiro.
    d (bool): Se True, retorna todas as posições adjacentes (incluindo diagonais). 
              Se False, retorna apenas as posições adjacentes ortogonais.

    Retorna: tuple: Tupla contendo as posições adjacentes em sentido horário, começando pela posição acima de `p`.
    """
    col, lin = obtem_pos_col(p), obtem_pos_lin(p)

    def obtem_posicoes_ort(c):
        # Retorna as primeiras até quartas posições ortogonais adjacentes a 'p', determinadas pelo argumento 'c' que instrui a função a retornar qual delas.
        # As posições ortogonais são encontradas através dos limites do tabuleiro (determinados pelo número de órbitas 'n')
        # e pelos valores da coluna e linha da posição.
        if c == 1 and lin != 1:
            return (cria_posicao(col, lin-1))
        if c == 2 and ord(col) != ord("a") + n * 2 - 1:
            return (cria_posicao(chr(ord(col)+1), lin))
        if c == 3 and lin != n * 2:
            return (cria_posicao(col, lin+1))
        if c == 4 and ord(col) != ord("a"):
            return (cria_posicao(chr(ord(col)-1), lin))
    def obtem_posicoes_diag(c):
        # Retorna as primeiras até quartas posições diagonais adjacentes a 'p', determinadas pelo argumento 'c' que instrui a função a retornar qual delas.
        # As posições diagonais são encontradas através dos limites do tabuleiro (determinados pelo número de órbitas 'n')
        # e pelos valores da coluna e linha da posição.
        if c == 1 and lin != 1 and ord(col) != ord("a"):
            return (cria_posicao(chr(ord(col)-1), lin-1))
        if c == 2 and lin != 1 and ord(col) != ord("a") + n * 2 - 1:
            return (cria_posicao(chr(ord(col)+1), lin-1))
        if c == 3 and lin != n * 2 and ord(col) != ord("a") + n * 2 - 1:
            return (cria_posicao(chr(ord(col)+1), lin+1))
        if c == 4 and lin != n * 2 and ord(col) != ord("a"):
            return (cria_posicao(chr(ord(col)-1), lin+1))
    
    if d:
        return tuple(filter(None, (obtem_posicoes_ort(1), obtem_posicoes_diag(2), obtem_posicoes_ort(2),
        obtem_posicoes_diag(3), obtem_posicoes_ort(3), obtem_posicoes_diag(4), obtem_posicoes_ort(4), obtem_posicoes_diag(1))))
        # Se "d" for verdadeiro, retorna as posições adjacentes diagonais e ortogonais à posição 'p' em formato de tuplo, começando pela posição ortogonal acima de 'p', seguida em sentido horário. 
    else:
        return tuple(filter(None, (obtem_posicoes_ort(1), obtem_posicoes_ort(2), obtem_posicoes_ort(3), obtem_posicoes_ort(4))))
        # Se "d" for falso, retorna só as posições adjacentes ortogonais à posição 'p' em formato de tuplo, começando pela posição ortogonal acima de 'p', seguida em sentido horário. 
def obtem_orbito(col, lin, n):
    # Esta função auxiliar determina a órbita à qual uma posição pertence, recebendo a coluna 'col' e a linha 'lin' à qual pertence,
    # e o número de órbitas 'n' que a tabela possui. Faz isso utilizando os limites da tabela (determinados pelo inteiro 'n'), a string 'col' e o inteiro 'lin'.
    if n == 2:
        if (lin - 1 < 1 or lin + 1 > n * 2) or (ord(col) - 1 < ord("a") or ord(col) + 1 >= ord("a") + n * 2):
            return n
        if (lin - 1 == n-1 or lin + 1 == n * 2) or (ord(col) - 1 == ord("a") + n-2 or ord(col) + 1 < ord("a") + n * 2):
            return n - 1
    elif n == 3:
        if (lin - 1 < 1 or lin + 1 > n * 2) or (ord(col) - 1 < ord("a") or ord(col) + 1 >= ord("a") + n * 2):
            return n
        if (lin - 1 == n-2 or lin + 1 == n * 2) or (ord(col) - 1 == ord("a") + n-3 or ord(col) + 1 == ord("a") + n * 2 - 1):
            return n - 1
        if (lin - 1 == n-1 or lin + 1 == n * 2 - 1) or (ord(col) - 1 == ord("a") + n-2 or ord(col) + 1 == ord("a") + n * 2 - 2):
            return n - 2
    elif n == 4:
        if (lin - 1 < 1 or lin + 1 > n * 2) or (ord(col) - 1 < ord("a") or ord(col) + 1 >= ord("a") + n * 2):
            return n
        if (lin - 1 == n-3 or lin + 1 == n * 2) or (ord(col) - 1 == ord("a") + n-4 or ord(col) + 1 == ord("a") + n * 2 - 1):
            return n - 1
        if (lin - 1 == n-2 or lin + 1 == n * 2 - 1) or (ord(col) - 1 == ord("a") + n-3 or ord(col) + 1 == ord("a") + n * 2 - 2):
            return n - 2
        if (lin - 1 == n-1 or lin + 1 == n * 2 - 2) or (ord(col) - 1 == ord("a") + n-2 or ord(col) + 1 == ord("a") + n * 2 - 3):
            return n - 3
    else:
        if (lin - 1 < 1 or lin + 1 > n * 2) or (ord(col) - 1 < ord("a") or ord(col) + 1 >= ord("a") + n * 2):
            return n
        if (lin - 1 == n-4 or lin + 1 == n * 2) or (ord(col) - 1 == ord("a") + n-5 or ord(col) + 1 == ord("a") + n * 2 - 1):
            return n - 1
        if (lin - 1 == n-3 or lin + 1 == n * 2 - 1) or (ord(col) - 1 == ord("a") + n-4 or ord(col) + 1 == ord("a") + n * 2 - 2):
            return n - 2
        if (lin - 1 == n-2 or lin + 1 == n * 2 - 2) or (ord(col) - 1 == ord("a") + n-3 or ord(col) + 1 == ord("a") + n * 2 - 3):
            return n - 3
        if (lin - 1 == n-1 or lin + 1 == n * 2 - 3) or (ord(col) - 1 == ord("a") + n-2 or ord(col) + 1 == ord("a") + n * 2 - 4):
            return n - 4
def ordena_posicoes(t, n):
    """
    Ordena as posições de acordo com a ordem de leitura do tabuleiro de Orbito-n.

    Argumentos:
    t (tuplo): Tuplo de posições a serem ordenadas.
    n (int): Número de órbitas do tabuleiro.

    Retorna: tuplo: Um tuplo de posições ordenadas de acordo com a ordem de leitura do tabuleiro de Orbito-n.
    """
    def key_ordena(t):
        # Esta função de chave dá prioridade à órbita à qual a posição pertence (ordem de prioridade da mais interior para a mais exterior),
        # depois à linha (ordem de prioridade da mais alta para a mais baixa) e, em seguida, à coluna (ordem de prioridade da esquerda para a direita)."
        col, lin = obtem_pos_col(t), obtem_pos_lin(t)
        orbito = obtem_orbito(col, lin, n)
        return (orbito, lin, col)
    return sorted(t, key=key_ordena)
    # Devolve as posições ordenadas pela chave 'key_ordena'

# TAD DE PEDRAS

# Construtores
def cria_pedra_branca():
    """
    Cria uma pedra pertencente ao jogador branco.

    Retorna: pedra: Uma pedra branca representada pelo valor (-1,).
    """
    return (-1, )
    # Devolve a representação interna da pedra branca
def cria_pedra_preta():
    """
    Cria uma pedra pertencente ao jogador preto.

    Retorna: pedra: Uma pedra preta representada pelo valor (1,).
    """
    return (1, )
    # Devolve a representação interna da pedra preta
def cria_pedra_neutra():
    """
    Cria uma pedra neutra que não pertence a nenhum jogador.

    Retorna: pedra: Uma pedra neutra representada pelo valor (0,).
    """
    return (0, )
    # Devolve a representação interna da pedra neutra

# Reconhecedores
def eh_pedra(arg):
    """
    Verifica se o argumento fornecido é uma pedra válida do TAD 'pedra'.

    Argumento: arg: O argumento a ser verificado.

    Retorna: bool: True se o argumento for uma pedra válida (pedra branca, preta ou neutra), False caso contrário.
    """
    return (type(arg) == tuple and arg in [(-1, ), (1, ), (0, )])
    # Retorna verdadeiro se o argumento estiver em conformidade com a representação interna das pedras,
    # ou seja, se for um tuplo e for uma das seguintes pedras: ((-1, ), (1, ), (0, )). Se uma ou ambas as condições não forem verdadeiras, retorna falso.
def eh_pedra_branca(arg):
    """
    Verifica se a pedra fornecida pertence ao jogador branco.

    Argumento: arg: A pedra a ser verificada.

    Retorna: bool: True se a pedra for do jogador branco, False caso contrário.
    """
    return eh_pedra(arg) and arg == (-1, )
    # Retorna verdadeiro se o argumento estiver em conformidade com a representação interna da pedra branca,
    # ou seja, se for um pedra e for da seguinte pedra: (-1, ).
def eh_pedra_preta(arg):
    """
    Verifica se a pedra fornecida pertence ao jogador preto.

    Argumento: arg: A pedra a ser verificada.

    Retorna: bool: True se a pedra for do jogador preto, False caso contrário.
    """
    return eh_pedra(arg) and arg == (1, )
    # Retorna verdadeiro se o argumento estiver em conformidade com a representação interna da pedra preta,
    # ou seja, se for um pedra e for da seguinte pedra: (1, ).

# Teste
def pedras_iguais(p1, p2):
    """
    Verifica se duas pedras são iguais.

    Argumentos:
    p1 (pedra): A primeira pedra a ser comparada.
    p2 (pedra): A segunda pedra a ser comparada.

    Retorna: bool: Retorna True se ambas as pedras forem iguais e False caso contrário.
    """
    return (eh_pedra(p1) and eh_pedra(p2) and p1 == p2)
    # Retorna verdadeiro se 'p1' e 'p2' forem do tipo 'pedra' e forem iguais.

# Transformador
def pedra_para_str(p):
    """
    Converte uma pedra para a representação em string do jogador dono da pedra.

    Argumento: p (pedra): A pedra que será convertida.

    Retorna: str: A representação em string do jogador dono da pedra, sendo:
    - 'O' para a pedra do jogador branco
    - 'X' para a pedra do jogador preto
    - ' ' para a pedra neutra
    """
    if eh_pedra(p):
        if eh_pedra_branca(p):
            return 'O'
        if eh_pedra_preta(p):
            return 'X'
        return ' '
    # Retorna a cadeia de caracteres que representa o jogador dono da pedra: 'O' para branco, 'X' para preto. Ou a pedra ' ' para neutra.

# FUNÇÕES DE ALTO NÍVEL DE PEDRAS
def str_jog_para_pedra(s):
    # Retorna a pedra jogador que é representada pela cadeia de caractares 'O', 'X': 'O' para branco, 'X' para preto.
    if s == "O":
        return cria_pedra_branca()
    elif s == "X":
        return cria_pedra_preta()
    else:
        return False
def eh_pedra_jogador(p):
    """
    Verifica se a pedra fornecida pertence a um jogador (preto ou branco).

    Argumento: p (pedra): A pedra a ser verificada.

    Retorna: bool: True se a pedra pertence a um jogador (preto ou branco), False caso contrário.
    """
    return eh_pedra(p) and (eh_pedra_branca(p) or eh_pedra_preta(p))
    # Retorna True se 'p' é uma pedra e a pedra 'p' pertence ao jogador preto ou branco. Caso contrário, retorna False.
def pedra_para_int(p):
    """
    Converte uma pedra para seu valor inteiro correspondente.

    Argumento: p (pedra): A pedra que será convertida.

    Retorna: int: -1 para pedras do jogador branco, 1 para pedras do jogador preto e 0 para pedras neutras.
    """
    if eh_pedra(p):
        if eh_pedra_branca(p):
            return -1
        if eh_pedra_preta(p):
            return 1
        return 0
    # Retorna um valor inteiro que representa o tipo da pedra: -1 para branco, 1 para preto e 0 para neutra.

# TAD DE TABULEIRO

# Construtores
def cria_tabuleiro_vazio(n):
    """
    Cria um tabuleiro vazio do jogo Orbito com 'n' órbitas.

    Argumento: n (int): O número de órbitas do tabuleiro.

    Retorna: tabuleiro: Um tabuleiro de Orbito com 'n' órbitas sem posições ocupadas.

    Levanta um ValueError se 'n' não for um inteiro entre 2 e 5.
    """
    if not (type(n)==int and 2 <= n <= 5):
    # Verifica se 'n' é um inteiro válido entre 2 e 5.
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")
    return list([cria_pedra_neutra() for _ in range(n * 2)] for i in range(n*2))
    # Cria um tabuleiro com todas as posições contendo pedras neutras.
    # Cada linha do tabuleiro contém 'n*2' pedras neutras.
def cria_tabuleiro(n, tp, tb):
    """
    Cria um tabuleiro de Orbito com 'n' órbitas, ocupando posições conforme especificado pelos argumentos.

    Argumentos:
    n (int): Número de órbitas do tabuleiro.
    tp (tuplo): As posições ocupadas por pedras pretas.
    tb (tuplo): As posições ocupadas por pedras brancas.

    Retorna: tabuleiro: Um tabuleiro de Orbito com as posições de 'tp' ocupadas por pedras pretas e as de 'tb' ocupadas por pedras brancas.

    Levanta um ValueError se os argumentos não forem válidos (se 'n' não estiver entre 2 e 5, ou se as posições em 'tp' e 'tb' forem inválidas ou repetidas).
    """
    if not (type(n)==int and 2 <= n <= 5 and type(tp) == tuple and all(eh_posicao_valida(i, n) for i in tp) and len(tp) == len(set(tp)) \
    and type(tb) == tuple and all(eh_posicao_valida(i, n) for i in tb) and len(tb) == len(set(tb)) and not (set(tp) & set(tb))):
    # Verifica a validade de 'n', 'tp', e 'tb'. 'n' deve estar entre 2 e 5, e as posições em 'tp' e 'tb' não devem se repetir nem serem inválidas.
        raise ValueError("cria_tabuleiro: argumentos invalidos")
    tab = []
    # Inicializa a lista 'tab' que representará o tabuleiro.

    for i in range(n * 2):
        col = []
        # Cria a coluna do tabuleiro.
        for j in range(n * 2):
            posicao_atual = cria_posicao(chr(ord("a") + i), j + 1)
            # Cria uma posição do tabuleiro com base na coluna e na linha.
            if posicao_atual in tp:
            # Se a posição estiver em 'tp', insere uma pedra preta.
                col.append(cria_pedra_preta())
            elif posicao_atual in tb:
            # Se a posição estiver em 'tb', insere uma pedra branca.
                col.append(cria_pedra_branca())
            else:
            # Caso contrário, insere uma pedra neutra.
                col.append(cria_pedra_neutra())
        tab.append(col)
        # Adiciona a coluna ao tabuleiro.
    return tab
    # Retorna um tabuleiro com as posições ocupadas por pedras pretas e brancas, de acordo com 'tp' e 'tb'.
def cria_copia_tabuleiro(t):
    """
    Cria uma cópia do tabuleiro fornecido.

    Argumento: t (tabuleiro): O tabuleiro que será copiado.

    Retorna: tabuleiro: Uma cópia do tabuleiro fornecido como argumento.
    """
    copia = list(list(col) for col in t)
    # Cria uma cópia do tabuleiro 't', onde cada coluna é copiada individualmente.
    return copia
    # Retorna uma cópia do tabuleiro 't'. A cópia é criada para manter a imutabilidade do tabuleiro original.

# Seletores
def obtem_numero_orbitas(t):
    """
    Obtém o número de órbitas do tabuleiro.

    Argumento: t (tabuleiro): O tabuleiro do jogo Orbito.

    Retorna: int: O número de órbitas do tabuleiro.
    """
    return len(t) // 2
    # Divide o comprimento total do tabuleiro por 2, já que cada órbita ocupa duas colunas.        
def obtem_pedra(t, p):
    """
    Obtém a pedra na posição 'p' do tabuleiro 't'.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo Orbito.
    p (posicao): A posição do tabuleiro de onde obter a pedra.

    Retorna: pedra: A pedra na posição especificada, ou uma pedra neutra se a posição não estiver ocupada.
    """
    return t[(ord(obtem_pos_col(p))-ord("a"))][obtem_pos_lin(p)-1]    
    # Calcula o índice da coluna subtraindo o valor de 'a' do valor da coluna de 'p'.
    # Acessa a linha correta subtraindo 1 da linha de 'p' para corresponder ao índice da lista.
def obtem_linha_horizontal(t, p):
    """
    Obtém as posições e pedras da linha horizontal que passa pela posição 'p'.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo Orbito.
    p (posicao): A posição que determina a linha horizontal.

    Retorna: tuple: Tuplo de pares (posição, pedra) para cada posição da linha horizontal.
    """
    lin_idx = obtem_pos_lin(p)
    # Obtém o índice da linha da posição 'p'.
    return tuple((cria_posicao((chr(ord("a") + i)), lin_idx), t[i][lin_idx-1]) for i in range(len(t)))
    # Gera um tuplo contendo pares de posição e pedra para cada coluna da linha.
    # Retorna a linha horizontal correspondente, com as posições ordenadas da esquerda para a direita.
def obtem_linha_vertical(t, p):
    """
    Obtém as posições e pedras da linha vertical que passa pela posição 'p'.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo Orbito.
    p (posicao): A posição que determina a linha vertical.

    Retorna: tuple: Tuplo de pares (posição, pedra) para cada posição da linha vertical.
    """
    col_idx = ord(obtem_pos_col(p)) - ord("a")
    # Obtém o índice da coluna da posição 'p' convertendo o valor da coluna de 'p' em um índice.
    return tuple((cria_posicao(obtem_pos_col(p), 1 + i), t[col_idx][i]) for i in range(len(t[col_idx])))
    # Gera um tuplo contendo pares de posição e pedra para cada linha da coluna.
    # Retorna a linha vertical correspondente, com as posições ordenadas de cima para baixo.
def obtem_linhas_diagonais(t, p):
    """
    Obtém as posições e pedras das diagonais que passam pela posição 'p'.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo Orbito.
    p (posicao): A posição que determina as diagonais.

    Retorna: tuple: Dois tuplos formados por pares (posição, pedra) representando a diagonal e a antidiagonal que passam pela posição 'p'.
    """
    def obtem_diagonal(inicial_i, inicial_j, passo_lin, passo_col):
        diagonal = []
        # Inicializa uma lista vazia para armazenar a diagonal.

        i, j = inicial_i, inicial_j
        # Define os índices de linha e coluna iniciais.
        while 0 <= i < n and 0 <= j < n:
        # Enquanto os índices estiverem dentro dos limites do tabuleiro.
            diagonal.append((cria_posicao(chr(ord("a") + i), j + 1), t[i][j]))
            # Adiciona à diagonal a posição criada e a pedra correspondente no tabuleiro.
            i += passo_lin
            j += passo_col
            # Incrementa ou decrementa os índices de acordo com o passo especificado.
        return diagonal
        # Retorna a lista resultante da diagonal.

    col_idx = ord(obtem_pos_col(p)) - ord("a")
    # Obtém o índice da coluna da posição 'p'.
    lin_idx = obtem_pos_lin(p) - 1
    # Obtém o índice da linha da posição 'p'.
    n = len(t)
    # Define o tamanho do tabuleiro.


    inicial_i, inicial_j = col_idx, lin_idx
    # Calcula os índices iniciais para a diagonal descendente.
    while inicial_i > 0 and inicial_j > 0:
        inicial_i -= 1
        inicial_j -= 1
    # Chama a função auxiliar para obter a diagonal descendente.
    lin_diagonal = obtem_diagonal(inicial_i, inicial_j, 1, 1)

    inicial_i, inicial_j = col_idx, lin_idx
    # Calcula os índices iniciais para a antidiagonal ascendente.
    while inicial_i > 0 and inicial_j < n - 1:
        inicial_i -= 1
        inicial_j += 1
    lin_anti_diagonal = obtem_diagonal(inicial_i, inicial_j, 1, -1)
    # Chama a função auxiliar para obter a antidiagonal ascendente.

    return tuple(lin_diagonal), tuple(lin_anti_diagonal)
    # Retorna os dois tuplos correspondentes às diagonais.
def obtem_posicao_linha_elemento(e):
    return e[0]
def obtem_posicoes_pedra(t, j):
    """
    Obtém todas as posições do tabuleiro que estão ocupadas pela pedra 'j'.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo Orbito.
    j (pedra): A pedra específica (branca, preta ou neutra) a ser procurada.

    Retorna: tuple: Tuplo de posições ocupadas pela pedra 'j', ordenadas em ordem de leitura do tabuleiro.
    """
    posicoes_pedra = tuple(
        cria_posicao(chr(ord("a") + i), k + 1)
        for i in range(len(t))
        # Itera por todas as colunas do tabuleiro.
        for k in range(len(t[i]))
        # Itera por todas as linhas do tabuleiro.
        if t[i][k] == j
        # Verifica se a posição atual contém a pedra 'j'.

    )
    # Gera um tuplo com todas as posições do tabuleiro ocupadas pela pedra 'j'.

    return ordena_posicoes(posicoes_pedra, obtem_numero_orbitas(t))
    # Ordena as posições obtidas pela função ordena_posicoes.
    # Retorna o conjunto de posições ocupadas pela pedra 'j', organizadas pela ordem de leitura do tabuleiro.


# Modificadores
def coloca_pedra(t, p, j):
    """
    Modifica destrutivamente o tabuleiro, colocando a pedra 'j' na posição 'p'.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo Orbito.
    p (posicao): A posição onde a pedra deve ser colocada.
    j (pedra): A pedra a ser colocada (branca, preta ou neutra).

    Retorna: tabuleiro: O tabuleiro modificado com a pedra colocada na posição 'p'.
    """
    col, lin = ord(obtem_pos_col(p))-ord("a"), obtem_pos_lin(p)-1
    # Obtém o índice da coluna a partir da posição 'p'.
    # Obtém o índice da linha a partir da posição 'p'.

    t[col][lin] = j
    # Modifica a posição correspondente no tabuleiro, colocando a pedra 'j'.
    return t
    # Retorna o tabuleiro modificado.
    # Esta função altera o estado do tabuleiro de forma destrutiva, colocando a pedra especificada na posição fornecida.


def remove_pedra(t, p):
    """
    Modifica destrutivamente o tabuleiro, removendo a pedra da posição 'p'.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo Orbito.
    p (posicao): A posição de onde a pedra deve ser removida.

    Retorna: tabuleiro: O tabuleiro modificado com a pedra removida da posição 'p' e substituída por uma pedra neutra.
    """
    t[ord(obtem_pos_col(p))-ord("a")][obtem_pos_lin(p)-1] = cria_pedra_neutra()
    # Obtém o índice da coluna a partir da posição 'p'.
    # Obtém o índice da linha a partir da posição 'p'.
    # Substitui a pedra existente por uma pedra neutra na posição especificada.
    return t
    # Retorna o tabuleiro modificado.
    # Esta função altera destrutivamente o tabuleiro ao remover a pedra da posição especificada e substituí-la por uma pedra neutra.

# Reconhecedor
def eh_tabuleiro(arg):
    """
    Verifica se o argumento fornecido é um TAD 'tabuleiro' válido.

    Argumento: arg: O argumento a ser verificado.

    Retorna: bool: Retorna True se o argumento for um tabuleiro válido, e False caso contrário.
    """
    if type(arg) != list:
    # Verifica se o argumento é do tipo lista.
        return False
        # Retorna False se 'arg' não for uma lista, pois a representação interna de um tabuleiro deve ser uma lista de listas.

    n_orb = obtem_numero_orbitas(arg)
    # Obtém o número de órbitas do tabuleiro.
    n_orbx2 = n_orb * 2
    # Calcula o número total de elementos esperado para as órbitas.

    if not (2 <= n_orb <= 5 and len(arg) == n_orbx2):
    # Verifica se o número de órbitas está no intervalo de 2 a 5 e se o tamanho do tabuleiro corresponde ao valor esperado.
        return False
        # Retorna False se o número de órbitas não for válido ou se o tamanho da lista não corresponder ao número de elementos esperado.

    return all(type(col) == list and len(col) == n_orb * 2 and all(eh_pedra(lin) for lin in col) for col in arg)
    # Verifica se cada elemento da lista é uma lista válida e se todas as posições contêm pedras válidas.
    # Retorna True apenas se cada coluna for uma lista, tiver o tamanho esperado, e todas as posições contiverem uma pedra válida.

# Teste
def tabuleiros_iguais(t1, t2):
    """
    Verifica se dois tabuleiros são iguais.

    Argumentos:
    t1 (tabuleiro): O primeiro tabuleiro a ser comparado.
    t2 (tabuleiro): O segundo tabuleiro a ser comparado.

    Retorna: bool: Retorna True se t1 e t2 forem tabuleiros e forem iguais, False caso contrário.
    """
    if not (eh_tabuleiro(t1) and eh_tabuleiro(t2)) or obtem_numero_orbitas(t1) != obtem_numero_orbitas(t2):
    # Verifica se ambos os argumentos são tabuleiros válidos e se possuem o mesmo número de órbitas.
        return False
        # Retorna False se um dos argumentos não for um tabuleiro válido ou se o número de órbitas dos tabuleiros for diferente.

    return t1 == t2
    # Verifica se os tabuleiros são exatamente iguais.
    # Retorna True se os tabuleiros 't1' e 't2' forem idênticos em suas representações internas.

# Transformador
def tabuleiro_para_str(t):
    """
    Converte a representação interna do tabuleiro para uma string.

    Argumentos: t (tabuleiro): O tabuleiro a ser convertido.

    Retorna: str: Uma representação em string do tabuleiro no formato especificado pelos exemplos fornecidos.
    """
    n = obtem_numero_orbitas(t)
    # Obtém o número de órbitas do tabuleiro.
    caracteres_col = "    " + "   ".join(chr(ord('a') + i) for i in range(n * 2)) + "\n"
    # Gera o cabeçalho das colunas do tabuleiro, usando letras consecutivas para representar cada coluna.

    linhas = []
    for lin in range(n * 2):
        lin_num = f"{lin + 1:02d}"
        # Gera o número da linha, formatado para ter sempre dois dígitos.
        lin_conteudo = "-".join(f"[{pedra_para_str(t[col][lin])}]" for col in range(n * 2))
        # Gera o conteúdo da linha com as pedras correspondentes, utilizando "-" para separar as colunas.
        linhas.append(f"{lin_num} {lin_conteudo}")

        if lin < n * 2 - 1:
            linhas.append(" " + "   |" * (n * 2 - 1) + "   |")
            # Adiciona uma linha intermediária de barras verticais (|) para separar visualmente as linhas do tabuleiro.

    return caracteres_col + "\n".join(linhas)
    # Retorna a string completa do tabuleiro, contendo o cabeçalho das colunas e as linhas do tabuleiro.


# FUNÇÕES DE ALTO NÍVEL
def move_pedra(t, p1, p2):
    """
    Move uma pedra de uma posição para outra no tabuleiro.

    Argumentos:
    t (tabuleiro): O tabuleiro onde a pedra será movida.
    p1 (posicao): A posição original da pedra.
    p2 (posicao): A posição para onde a pedra será movida.

    Retorna: tabuleiro: O tabuleiro modificado após o movimento da pedra.
    """
    j = obtem_pedra(t, p1)
    # Obtém a pedra na posição original p1

    remove_pedra(t, p1)
    # Remove a pedra da posição original p1
    coloca_pedra(t, p2, j)
    # Coloca a pedra na nova posição p2
    return t
    # Retorna o tabuleiro atualizado
def obtem_posicao_seguinte(t, p, s):
    """
    Obtém a posição seguinte à posição p na mesma órbita.

    Argumentos:
    t (tabuleiro): O tabuleiro a ser considerado.
    p (posicao): A posição atual no tabuleiro.
    s (booleano): Determina a direção (True para horário, False para anti-horário).

    Retorna: posicao: A posição seguinte na mesma órbita, de acordo com a direção especificada.
    """
    n = obtem_numero_orbitas(t)
    # Obtém o número de órbitas do tabuleiro

    col, lin = obtem_pos_col(p), obtem_pos_lin(p)
    # Obtém a coluna e a linha da posição atual
    orbito = obtem_orbito(col, lin, n)
    # Determina o nível da órbita em que a posição p se encontra

    def obtem_posicoes_adjacentes_na_orbita(p):
        # Obtém as posições adjacentes na órbita da posição p
        posicoes = obtem_posicoes_adjacentes(p, n, False)
        return tuple(i for i in posicoes if obtem_orbito(obtem_pos_col(i), obtem_pos_lin(i), n) == orbito)

    posicoes_na_orbita = obtem_posicoes_adjacentes_na_orbita(p)
    # Obtém todas as posições na mesma órbita da posição p
    if s:
        if (obtem_pos_lin(p)-1 <= 0 or obtem_orbito(col, lin-1, n) == orbito+1) or \
        (obtem_orbito(chr(ord(col)-1), lin, n) == orbito+1 or ord(chr(ord(col)-1)) < ord("a")):
            return posicoes_na_orbita[0]
        else:
            return posicoes_na_orbita[1]
    else:
        if (obtem_pos_lin(p)-1 <= 0 or obtem_orbito(col, lin-1, n) == orbito+1) or \
        (obtem_orbito(chr(ord(col)-1), lin, n) == orbito+1 or ord(chr(ord(col)-1)) < ord("a")):
            return posicoes_na_orbita[1]
        else:
            return posicoes_na_orbita[0]
    # Determina a próxima posição com base no valor de s (True para horário, False para anti-horário)
def roda_tabuleiro(t):
    """
    Roda todas as pedras do tabuleiro em uma posição no sentido anti-horário.

    Argumentos:
    t (tabuleiro): O tabuleiro a ser rodado.

    Retorna: tabuleiro: O tabuleiro modificado após rodar todas as pedras.
    """
    n = obtem_numero_orbitas(t)
    # Obtém o número de órbitas no tabuleiro

    posicoes_pedra_branca = obtem_posicoes_pedra(t, cria_pedra_branca())
    posicoes_pedra_preta = obtem_posicoes_pedra(t, cria_pedra_preta())
    # Obtém as posições de todas as pedras brancas e pretas no tabuleiro

    movimentos = []

    if len(posicoes_pedra_branca) > 0:
        for jb in posicoes_pedra_branca:
            nova_pos = obtem_posicao_seguinte(t, jb, False)  
            pedra = obtem_pedra(t, jb)  
            movimentos.append((jb, nova_pos, pedra))
    if len(posicoes_pedra_preta) > 0:
        for jp in posicoes_pedra_preta:
            nova_pos = obtem_posicao_seguinte(t, jp, False)  
            pedra = obtem_pedra(t, jp)  
            movimentos.append((jp, nova_pos, pedra))
    # Calcula os movimentos para todas as pedras brancas e pretas no sentido anti-horário

    t_temp = cria_copia_tabuleiro(t)
    # Cria uma cópia do tabuleiro para armazenar o estado temporário

    for (pos_atual, _, _) in movimentos:
        remove_pedra(t_temp, pos_atual)
    # Remove todas as pedras das posições atuais no tabuleiro temporário
    for (_, nova_pos, pedra) in movimentos:
        coloca_pedra(t_temp, nova_pos, pedra)
    # Coloca todas as pedras nas novas posições no tabuleiro temporário

    for i in range(n*2):
        for j in range(n*2):
            posicao = cria_posicao(chr(ord("a") + i), j + 1)
            pedra = obtem_pedra(t_temp, posicao)
            remove_pedra(t, posicao)
            coloca_pedra(t, posicao, pedra)
    # Atualiza o tabuleiro original com os movimentos realizados no tabuleiro temporário

    return t
    # Retorna o tabuleiro atualizado
def verifica_linha_pedras(t, p, j, k):
    """
    Verifica se existe uma linha de pedras consecutivas do jogador com pelo menos k pedras.

    Argumentos:
    t (tabuleiro): O tabuleiro a ser considerado.
    p (posicao): A posição de partida.
    j (pedra): A pedra do jogador a ser verificada.
    k (int): Número mínimo de pedras consecutivas necessárias.

    Retorna: booleano: True se existe uma linha com k ou mais pedras consecutivas do jogador, False caso contrário.
    """
    def conta_consecutivas(lin):
        pos_index = -1
        for i in range(len(lin)):
            if obtem_posicao_linha_elemento(lin[i]) == p:
                pos_index = i
                break 
        # Encontra o índice da posição p na linha lin

        if obtem_pedra(t, p) != j:
            return False
        # Encontra o índice da posição p na linha lin

        conta = 1
        for i in range(pos_index + 1, len(lin)):
            if obtem_pedra(t, obtem_posicao_linha_elemento(lin[i])) == j:
                conta += 1
            else:
                break
        # Conta quantas pedras consecutivas existem após a posição p
        for i in range(pos_index - 1, -1, -1):
            if obtem_pedra(t, obtem_posicao_linha_elemento(lin[i])) == j:
                conta += 1
            else:
                break
        # Conta quantas pedras consecutivas existem antes da posição p

        return conta >= k
        # Retorna True se conta supera o 'k'
    
    diagonais = obtem_linhas_diagonais(t, p)
    linha = obtem_linha_horizontal(t, p)
    coluna = obtem_linha_vertical(t, p)
    # Verifica se existem k ou mais pedras consecutivas nas linhas, colunas ou diagonais

    return conta_consecutivas(linha) or conta_consecutivas(coluna) or any(conta_consecutivas(diagonal) for diagonal in diagonais)
    # Verifica se existem k ou mais pedras consecutivas em alguma linha, coluna ou diagonal que passe pela posição p.
    # A função retorna True se houver uma sequência válida em qualquer direção (horizontal, vertical ou diagonal).
 
# FUNÇÕES ADICIONAIS
def eh_vencedor(t, j):
    """
    Verifica se há um vencedor no tabuleiro.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo Orbito-n.
    j (pedra): A pedra do jogador ('O' ou 'X').

    Retorna: bool: True se existir uma linha completa no tabuleiro do jogador, False caso contrário.
    """
    posicoes_pedra = obtem_posicoes_pedra(t, j)
    # Obtém todas as posições do tabuleiro que estão ocupadas pela pedra do jogador.

    return any(verifica_linha_pedras(t, posicao, j, obtem_numero_orbitas(t)*2) for posicao in posicoes_pedra)
    # Verifica se em alguma das posições ocupadas há uma linha completa de pedras do jogador.
    # Se encontrar ao menos uma linha completa do jogador 'j', a função retorna True, indicando uma vitória.
    # Para cada posição ocupada por uma pedra do jogador 'j', verifica se há uma sequência completa de pedras do jogador
    # do tamanho correspondente ao número de órbitas (obtem_numero_orbitas(t) * 2).
    # Se ao menos uma posição tiver a sequência completa, retorna True indicando uma vitória do jogador.
    # Caso contrário, retorna False.

def eh_fim_jogo(t):
    """
    Verifica se o jogo já terminou.

    Argumento: t (tabuleiro): O tabuleiro do jogo Orbito-n.

    Retorna: bool: True se o jogo já terminou, seja porque não há mais posições livres ou porque um jogador venceu.
    """
    return (len(obtem_posicoes_pedra(t, cria_pedra_neutra())) == 0 or eh_vencedor(t, cria_pedra_branca()) or eh_vencedor(t, cria_pedra_preta()))
    # Esta linha verifica se não existem mais posições neutras no tabuleiro
    # ou se um dos jogadores (branco ou preto) é vencedor.
def escolhe_movimento_manual(t):
    """
    Permite ao jogador escolher manualmente uma posição livre no tabuleiro onde deseja colocar uma pedra.

    Argumento: t (tabuleiro): O tabuleiro do jogo.

    Retorna: posicao: A posição escolhida pelo jogador que está livre para receber uma pedra.
    
    A função mantém-se em execução até o jogador introduzir uma posição válida.
    """
    posicao = input("Escolha uma posicao livre:")
    # Solicita ao jogador que escolha uma posição livre.

    if type(posicao) == str and (len(posicao) == 2 or len(posicao) == 3) and ord("a") + obtem_numero_orbitas(t)*2 > ord(posicao[0]) >= ord("a") and f"{(obtem_numero_orbitas(t)*2)}" >= posicao[1::] >= "1":
    # Verifica se a entrada fornecida pelo jogador é uma string de comprimento 2 ou 3.
    # Além disso, verifica se a coluna fornecida está dentro dos limites do tabuleiro,
    # e se a linha fornecida está dentro dos valores válidos de "1" até ao dobro das órbitas.
        posicao_obj = str_para_posicao(posicao) 
        # Transforma a posição da string para o objeto posição.
        if posicao_obj in obtem_posicoes_pedra(t, cria_pedra_neutra()):
        # Verifica se a posição escolhida está livre (contém uma pedra neutra).
            return posicao_obj
            # Se a posiçao está livre, retorna a posição
    return escolhe_movimento_manual(t)
    # Caso a entrada não seja válida, a função é chamada recursivamente para pedir nova entrada.
def escolhe_movimento_auto(t, j, lvl):
    """
    Escolhe automaticamente uma posição no tabuleiro onde colocar a pedra 'j', de acordo com a estratégia indicada pelo nível 'lvl'.

    Argumentos:
    t (tabuleiro): O tabuleiro do jogo.
    j (pedra): A pedra do jogador (branca ou preta).
    lvl (str): Nível da estratégia a ser utilizada ("facil" ou "normal").

    Retorna: posicao: A posição escolhida automaticamente de acordo com a estratégia selecionada.

    A função faz uso das estratégias de nível 'facil' e 'normal' para decidir qual a melhor posição a ser ocupada.
    """
    n = obtem_numero_orbitas(t)
    t_copia = cria_copia_tabuleiro(t)
    t_rotacionado = cria_copia_tabuleiro(roda_tabuleiro(t_copia))
    t_rotacionado_copia = cria_copia_tabuleiro(t_rotacionado)
    t_rotacionado2 = cria_copia_tabuleiro(roda_tabuleiro(t_rotacionado_copia))

    def facil(j):
        posicoes_livres = obtem_posicoes_pedra(t_rotacionado, cria_pedra_neutra())
        # Obtém todas as posições livres (posições neutras).
        posicoes_adjacentes = [obtem_posicao_seguinte(t_rotacionado, pos, True) for pos in posicoes_livres if any(pos in obtem_posicoes_adjacentes(p, n, True) \
        for p in obtem_posicoes_pedra(t_rotacionado, j))]
        # Encontra posições adjacentes livres a uma pedra do jogador 'j'.
        posicoes_ordenadas = ordena_posicoes(posicoes_adjacentes if posicoes_adjacentes else posicoes_livres, n)
        return posicoes_ordenadas[0]
        # Ordena as posições, priorizando as adjacentes se houver.

    def normal(j):
        # Função auxiliar para encontrar as melhores posições com base na quantidade de pedras consecutivas.
        def encontrar_melhores_posicoes(posicoes_livres, t_rotacionado, j, n, pos_op):
            melhores_posicoes = []
            maior_l = -1

            for pos in posicoes_livres:
                t_temp = cria_copia_tabuleiro(t_rotacionado)
                coloca_pedra(t_temp, pos, j)

                l = max((i for i in range(n * 2, 1, -1) if verifica_linha_pedras(t_temp, pos, j, i)), default=0)
                # Calcula o maior número de pedras consecutivas a partir da posição.

                if l > maior_l:
                    melhores_posicoes = [pos]
                    maior_l = l
                elif l == maior_l:
                    melhores_posicoes.append(pos)
                # Atualiza as melhores posições com base na maior quantidade de pedras consecutivas encontradas.

            if pos_op:
                melhores_posicoes = (obtem_posicao_seguinte(t_rotacionado, obtem_posicao_seguinte(t_rotacionado2, pos, True), True) for pos in melhores_posicoes)
            else:
                melhores_posicoes = (obtem_posicao_seguinte(t_rotacionado, pos, True) for pos in melhores_posicoes)
            # Atualiza as posições conforme a estratégia do oponente ou do jogador.

            melhores_posicoes_ordenadas = ordena_posicoes(melhores_posicoes, n)
            # Ordena as melhores posições encontradas.

            return melhores_posicoes_ordenadas, maior_l
        
        posicoes_livres = obtem_posicoes_pedra(t_rotacionado, cria_pedra_neutra())
        posicoes_livres2 = obtem_posicoes_pedra(t_rotacionado2, cria_pedra_neutra())
        j_op = cria_pedra_preta() if eh_pedra_branca(j) else cria_pedra_branca()

        posicoes_pedra_j = obtem_posicoes_pedra(t_copia, j)
        if not posicoes_pedra_j:
            posicoes_ordenadas = ordena_posicoes(posicoes_livres, n)
            return obtem_posicao_seguinte(t_rotacionado, posicoes_ordenadas[0], True)

        melhores_posicoes_jog_ordenadas, maior_l_jog = encontrar_melhores_posicoes(posicoes_livres, t_rotacionado, j, n, False)
        melhores_posicoes_op_ordenadas, maior_l_op = encontrar_melhores_posicoes(posicoes_livres2, t_rotacionado2, j_op, n, True)
        # Encontra as melhores posições para o jogador e o oponente.


        if maior_l_jog >= maior_l_op:
            return melhores_posicoes_jog_ordenadas[0]
        elif maior_l_op > maior_l_jog:
            return melhores_posicoes_op_ordenadas[0]
        else:
            todas_posicoes_ordenadas = (pos for pos in ordena_posicoes(melhores_posicoes_jog_ordenadas + melhores_posicoes_op_ordenadas, n))
            todas_posicoes_ordenadas = ordena_posicoes(todas_posicoes_ordenadas, n)
            return todas_posicoes_ordenadas[0]
        # Retorna a posição com maior potencial para o jogador ou o oponente.


    if lvl == "facil":
        return facil(j)
    else:
        return normal(j)
    # Chama a função correta de acordo com o nível selecionado.

def orbito(n, modo, jog):
    """
    Função principal que executa o jogo completo de Orbito-n.

    Argumentos:
    n (int): O número de órbitas do tabuleiro (entre 2 e 5).
    modo (str): O modo de jogo - "facil", "normal", ou "2jogadores".
    jog (str): Representação externa da pedra do jogador - 'O' para pedra branca ou 'X' para pedra preta.

    Retorna: int: Retorna um inteiro que identifica o jogador vencedor (1 para o jogador de pedra preta, -1 para o jogador de pedra branca) ou 0 em caso de empate.

    A função começa sempre com o jogador de pedras pretas, e se desenvolve até ao fim do jogo, retornando o vencedor ou indicando empate.
    """
    if not (type(n) == int and 2 <= n <= 5 and modo in ["facil", "normal", "2jogadores"] and type(jog) == str and eh_pedra_jogador(str_jog_para_pedra(jog))):
    # Verifica a validade dos argumentos
        raise ValueError("orbito: argumentos invalidos")
    
    print(f"Bem-vindo ao ORBITO-{n}.")
    tabuleiro = cria_tabuleiro_vazio(n)
    # Cria um tabuleiro vazio
    jog_pedra = str_jog_para_pedra(jog)
    # Transforme a representação string das pedras jogadores para para tipo pedras

    def executa_turno(tabuleiro, movimento, jog_pedra):
        # Função auxiliar que executa o turno de um jogador.
        coloca_pedra(tabuleiro, movimento, jog_pedra)
        roda_tabuleiro(tabuleiro)
        print(tabuleiro_para_str(tabuleiro))
    
    if modo in ["facil", "normal"]:
    # Caso o modo de jogo seja contra o computador.
        cmp_pedra = cria_pedra_preta() if eh_pedra_branca(jog_pedra) else cria_pedra_branca()
        
        print(f"Jogo contra o computador ({modo}).")
        print(f"O jogador joga com '{jog}'.")
        print(tabuleiro_para_str(tabuleiro))
        
        jog = -(pedra_para_int(jog_pedra))
        # Jog alterna entre jogador e computador.
        while not eh_fim_jogo(tabuleiro):
            # O jogo continua enquanto não tiver terminado
            if jog == 1:
                print(f"Turno do computador ({modo}):")
                pedra_atual = cmp_pedra
                movimento = escolhe_movimento_auto(tabuleiro, cmp_pedra, modo)
            else:
                print("Turno do jogador.")
                pedra_atual = jog_pedra
                movimento = escolhe_movimento_manual(tabuleiro)
                
            executa_turno(tabuleiro, movimento, pedra_atual)
            # Executa o turno do jogador ou computador.
            jog = -jog

        if eh_vencedor(tabuleiro, jog_pedra) and not eh_vencedor(tabuleiro, cmp_pedra):
            print("VITORIA")
            return pedra_para_int(jog_pedra)
        elif eh_vencedor(tabuleiro, cmp_pedra) and not eh_vencedor(tabuleiro, jog_pedra):
            print("DERROTA")
            return pedra_para_int(cmp_pedra)
        else:
            print("EMPATE")
            return pedra_para_int(cria_pedra_neutra())
        # Verifica e imprime o resultado final do jogo.

    else:
    # Caso o modo de jogo seja para dois jogadores.
        print("Jogo para dois jogadores.")
        print(tabuleiro_para_str(tabuleiro))
        
        while not eh_fim_jogo(tabuleiro):
            print(f"Turno do jogador '{jog}'.")
            movimento = escolhe_movimento_manual(tabuleiro)
            executa_turno(tabuleiro, movimento, jog_pedra)
            
            jog_pedra = cria_pedra_preta() if eh_pedra_branca(jog_pedra) else cria_pedra_branca()
            jog = pedra_para_str(jog_pedra)
            # Alterna as pedras dos jogadores a cada turno.

        if eh_vencedor(tabuleiro, jog_pedra) and not eh_vencedor(tabuleiro, cria_pedra_preta() if eh_pedra_branca(jog_pedra) else cria_pedra_branca()):
            print(f"VITORIA DO JOGADOR '{jog}'")
            return pedra_para_int(jog_pedra)
        elif eh_vencedor(tabuleiro, cria_pedra_preta() if eh_pedra_branca(jog_pedra) else cria_pedra_branca()) and not eh_vencedor(tabuleiro, jog_pedra):
            print(f"VITORIA DO JOGADOR '{pedra_para_str(cria_pedra_preta() if eh_pedra_branca(jog_pedra) else cria_pedra_branca())}'")
            return pedra_para_int(cria_pedra_preta() if eh_pedra_branca(jog_pedra) else cria_pedra_branca())
        else:
            print("EMPATE")
            return pedra_para_int(cria_pedra_neutra())
        # Verifica e imprime o resultado final do jogo.
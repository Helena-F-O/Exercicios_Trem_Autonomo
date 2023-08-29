#Crie as historias de usuário e implemente o código:

#exercicio trem autonomo PARTE 1

#-um trem está localizado em um trilho numérico infinito, que pode ser representado pelo intervalo -M,...,-2,-1,0,1,2,...,N

#-o trem recebe uma lista de comandos para se mover em duas direções possiveis: esquerda ou direita. Inicialmente, o trem está na posição 0 e pode se mover uma unidade para direita(+1) ou para a esquerda (-1) com base nos comandos recebidos

#-O objetivo é executar a lista de comandos e determinar a posição final do trem

#Exemplos:

#-Comandos: [DIREITA, DIREITA]
#-Posião inicial: 0 -Posição final: 2

#-Comandos: [ESQUERDA]
#-Posião inicial: 0 -Posição final: -1

#-Comandos: [ESQUERDA, DIREITA, DIREITA, DIREITA, DIREITA, ESQUERDA]
#-Posião inicial: 0 -Posição final: 2

#-----------------------------------------------------------------------------------

#Histórias de Usuário:

#Como usuário, quero fornecer uma lista de comandos para o trem autônomo, de modo que ele possa se mover na direção especificada.

#Como usuário, desejo saber a posição final do trem após a execução de uma lista de comandos, para entender sua localização no trilho numérico.

#-----------------------------------------------------------------------------------

class AutonomousTrain:
    def __init__(self):
        self.position = 0
    
    def move(self, commands):
        for command in commands:
            if command == "DIREITA":
                self.position += 1
            elif command == "ESQUERDA":
                self.position -= 1
    
    def get_position(self):
        return self.position

# Exemplos de uso
if __name__ == "__main__":
    train = AutonomousTrain()

    commands1 = ["DIREITA", "DIREITA"]
    train.move(commands1)
    print("Posicao final apos comandos 1:", train.get_position())

    train.position = 0  # Reset position
    
    commands2 = ["ESQUERDA"]
    train.move(commands2)
    print("Posicao final apos comandos 2:", train.get_position())

    train.position = 0  # Reset position
    
    commands3 = ["ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]
    train.move(commands3)
    print("Posicao final apos comandos 3:", train.get_position())

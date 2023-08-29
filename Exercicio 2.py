#Crie as historias de usuário e implemente o código:

#exercicio trem autonomo PARTE 2

#-O mesmo trem roda em um trilho finito. Ele pode variar de -2 a +10
#-Ele nunca deve extrapolar os limites

#-Modifique/adicione as hitórias de usuário para suportar esta mudança
#-Implemente o código de modo que suporte as duas formas de trabalho (trilho infinito e finito)

#-----------------------------------------------------------------------------------

#Histórias de Usuário:

#Como usuário, quero fornecer uma lista de comandos para o trem autônomo em um trilho finito, de modo que ele possa se mover na direção especificada dentro dos limites definidos (-2 a +10).

#Como usuário, desejo que o trem autônomo respeite os limites do trilho finito, garantindo que nunca ultrapasse as posições -2 e +10.

#Como usuário, quero saber a posição final do trem após a execução de uma lista de comandos no trilho finito, para entender sua localização no contexto dos limites.

#-----------------------------------------------------------------------------------

class AutonomousTrain:
    def __init__(self, rail_start, rail_end):
        self.rail_start = rail_start
        self.rail_end = rail_end
        self.position = 0
    
    def move(self, commands):
        for command in commands:
            if command == "DIREITA":
                self.position = min(self.position + 1, self.rail_end)
            elif command == "ESQUERDA":
                self.position = max(self.position - 1, self.rail_start)
    
    def get_position(self):
        return self.position

# Exemplos de uso
if __name__ == "__main__":
    rail_start = -2
    rail_end = 10
    
    train = AutonomousTrain(rail_start, rail_end)

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

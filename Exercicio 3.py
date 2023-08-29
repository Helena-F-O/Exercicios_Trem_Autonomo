#Crie as historias de usuário e implemente o código:

#exercicio trem autonomo PARTE 3

#-O mesmo trem roda em um trilho finito. O usuario deve informar os limites do trilho.
#-A posição inicial deve ser informada pelo usuário
#-O usuario deve informar a lista de comandos completa e depois o trem deve executa-lá (A lista de comandos pode ter tamanho variado, entretando no maximo 30 comandos)
#-O trem nunca deve extrapolar os limites definidos.

#-Modifique/adicione as histórias de usuario para suportar esta mudança
#-Implemente o codigo de modo que suporte as duas formas de trabalho (trilho infinito e finito).

#-----------------------------------------------------------------------------------

#Histórias de Usuário:

#Como usuário, desejo informar os limites do trilho finito nos quais o trem autônomo pode se mover, garantindo que ele permaneça dentro desses limites durante a execução dos comandos.

#Como usuário, quero definir a posição inicial do trem no trilho, para que ele comece de onde eu especificar.

#Como usuário, quero fornecer uma lista de comandos (com no máximo 30 comandos) para o trem autônomo, a fim de instruí-lo sobre o movimento desejado ao longo do trilho.

#Como usuário, desejo que o trem autônomo execute a lista de comandos de acordo com as restrições do trilho finito, garantindo que nunca ultrapasse os limites especificados.

#Como usuário, quero saber a posição final do trem após a execução completa da lista de comandos no trilho finito, para entender sua localização final no contexto dos limites.

#-----------------------------------------------------------------------------------

class AutonomousTrain:
    def __init__(self, rail_start, rail_end, initial_position):
        self.rail_start = rail_start
        self.rail_end = rail_end
        self.position = initial_position
    
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
    rail_start = int(input("Informe o limite inferior do trilho: "))
    rail_end = int(input("Informe o limite superior do trilho: "))
    initial_position = int(input("Informe a posicao inicial do trem: "))
    
    if initial_position < rail_start or initial_position > rail_end:
        print("A posicao inicial está fora dos limites do trilho.")
    else:
        commands = input("Informe a lista de comandos separados por virgula: ").split(",")
        commands = [command.strip().upper() for command in commands]
        
        if len(commands) > 30:
            print("A lista de comandos nao pode ter mais do que 30 elementos.")
        else:
            train = AutonomousTrain(rail_start, rail_end, initial_position)
            train.move(commands)
            print("Posição final apos a execucao dos comandos:", train.get_position())

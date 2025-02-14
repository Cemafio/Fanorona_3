class Fanorona:
    def __init__(self,grille=None, joueur='X'):
        self.grille = grille or [[' ', ' ', ' '] for _ in range(3)]
        # self.valeur = valeur
        self.joueur = joueur #N: noire 

        

    def plein(self):
        # Vérifie que toutes les cases ne sont pas vides
        return all(cell != ' ' for row in self.grille for cell in row)
    
    def affiche(self):
        for i in range(3):
            print("|".join(self.grille[i*3 : (i+1) * 3]))
            if i<2:
                print("-" * 5)

    def coup_valide(self,index):
        return self.grille[index] == " "

    def gagnant(self):
        # Vérification des lignes
        for row in self.grille:
            if row[0] != ' ' and row[0] == row[1] == row[2]:
                return row[0]
        # Vérification des colonnes
        for col in range(3):
            if self.grille[0][col] != ' ' and self.grille[0][col] == self.grille[1][col] == self.grille[2][col]:
                return self.grille[0][col]

        # Vérification des diagonales
        if self.grille[0][0] != ' ' and self.grille[0][0] == self.grille[1][1] == self.grille[2][2]:
            return self.grille[0][0]
        if self.grille[0][2] != ' ' and self.grille[0][2] == self.grille[1][1] == self.grille[2][0]:
            return self.grille[0][2]

        return None

    def eval(self,us):
        if self.gagnant() == us:
            return 1
        elif self.gagnant() == None:
            return 0
        else:
            return -1
     
    
    def fin_de_partie(self):
        # Le jeu est terminé s'il y a un gagnant ou si le plateau est plein
        return self.gagnant() is not None or self.plein()

    def get_successors(self):
        if self.fin_de_partie():
            return []  # Aucun mouvement possible si le jeu est terminé
        
        # Détermination du prochain joueur
        next_player = 'O' if self.joueur == 'X' else 'X'

        for i in range(3):
            for j in range(3):
                if self.grille[i][j] == ' ':
                    # Copie profonde du plateau pour éviter les modifications
                    new_board = [row[:] for row in self.grille]
                    new_board[i][j] = self.joueur
                    yield Fanorona(new_board, next_player)

    def __str__(self):
        return '\n'.join('|'.join(row) for row in self.grille)
    
    def str_with_indent(self, indent):
        return '\n'.join(' ' * indent + '|'.join(row) for row in self.grille)
    
    def __repr__(self):
        return f"Fanorona(\n{str(self)}\n, {self.joueur})"



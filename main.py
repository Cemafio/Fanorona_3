# ----------------exec-----------------
# import tkinter as tk
# from tkinter import messagebox
from fanorona import Fanorona  
fanorona = Fanorona()

def aff_succ(root, indent= 0, profondeur=1):
    print(root.str_with_indent(indent))
    print()
    if profondeur > 1:
        for succ in root.get_successors():
            aff_succ(succ, indent + 4, profondeur - 1)

def minimax(node, profondeur,user="X"):
    if profondeur == 0 or node.fin_de_partie():
        return (node.eval(user), None)

    if node.joueur == user:
        maxEval = -1000
        best_move = None
        for child in node.get_successors():
            eval, _ = minimax(child, profondeur - 1, user)
            if eval > maxEval:
                maxEval = eval
                best_move = child            
        return (maxEval, best_move)                
    else:
        minEval = 1000
        best_move = None
        for child in node.get_successors():
            eval, _ = minimax(child, profondeur - 1, user)
            if eval < minEval:
                minEval = eval
                best_move = child
        return (minEval, best_move)

def alphabeta(node, profondeur, alpha, beta, user='X'):
    if profondeur == 0 or node.fin_de_partie():
        return (node.eval(user), None)
    if node.joueur == user:
        maxEval = -1000
        best_move = None
        for child in node.get_successors():
            eval, _ = alphabeta(child, profondeur - 1, alpha, beta, user)
            if eval > maxEval:
                maxEval = eval
                best_move = child
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return (maxEval, best_move)
    else:
        minEval = 1000
        best_move = None
        for child in node.get_successors():
            eval, _ = alphabeta(child, profondeur - 1, alpha, beta, user)
            if eval < minEval:
                minEval = eval
                best_move = child
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return (minEval, best_move)
    


aff_succ(fanorona, profondeur=4)
print("---------------Minimax-----------------")
print(minimax(fanorona, 1000))
print("---------------Alphabeta-----------------")
print(alphabeta(fanorona, 1000, -1000, 1000))

root = tk.Tk()
jeu = Fanorona(root)
root.mainloop()
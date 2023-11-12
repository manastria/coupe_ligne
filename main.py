import pyperclip
from cut_long_line import cut_long_line

# Récupère le contenu du presse-papier et le divise en une liste de lignes
clipboard_content = pyperclip.paste()
lines = clipboard_content.splitlines()

# Découpe chaque ligne avec la fonction cut_long_line et stocke le résultat dans une liste
cut_lines = [cut_long_line(line, max_length=80, cut_indicator='✂', indent_chars=[' '], align_chars=[]) for line in lines]

# Concatène les lignes découpées en une seule chaîne de caractères
cut_text = '\n'.join(cut_lines)

# Copie le résultat dans le presse-papier
pyperclip.copy(cut_text)

# Affiche un message de confirmation
print("Le texte a été découpé et copié dans le presse-papier avec succès !")

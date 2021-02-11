from rendu.local_dir.path import Path

def my_program():
    dir = Path('./mon_repertoire')
    if not dir.exists():
        dir.mkdir()
    file = Path('./mon_repertoire/mon_fichier')
    if not file.exists():
        file.touch()
        file.write_text("Ceci est la premiere ligne d'un texte\n")
        file.write_text("Ceci est la seconde ligne d'un texte", append=True)
    with open(str(file), "r") as f:
        for record in f:
            print(record.replace('\n',''))

if __name__ == '__main__':
    my_program()
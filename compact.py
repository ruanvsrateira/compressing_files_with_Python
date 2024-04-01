import zipfile

def create_example_archive():
  try:
    with open("archive_to_compact.txt", "x") as archive:
      archive.write("Este arquivo deve ser compactado.")
  except FileExistsError:
    print("Já um arquivo criado")
  except:
    print("Algo deu errado!")

def compact():
  try:
    with zipfile.ZipFile("final_compact_file.zip", "w") as archive:
      archive.write("archive_to_compact.txt")
      print("Arquivo compactado com sucesso!")
  except:
    print("Algo deu errado na etapa de compactação")

if __name__ == "__main__":
  create_example_archive()
  compact()

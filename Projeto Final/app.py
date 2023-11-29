import random
import time


def insercao_direta(vetor):
  n = len(vetor)
  for i in range(1, n):
      key = vetor[i]
      j = i - 1
      while j >= 0 and key < vetor[j]:
          vetor[j + 1] = vetor[j]
          j -= 1
      vetor[j + 1] = key
      print("Direct insert",vetor)


def selecao_direta(vetor):
  n = len(vetor)
  for i in range(n):
    indice_menor = i
    for j in range(i + 1, n):
      if vetor[j] < vetor[indice_menor]:
        indice_menor = j
    vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
    print("Direct select",vetor)


def bolha(vetor):
  n = len(vetor)
  for i in range(n):
    for j in range(0, n - i - 1):
      if vetor[j] > vetor[j + 1]:
        vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
        print("Buble",vetor)

def quick_sort(vetor):
  if len(vetor) <= 1:
    return vetor
    
  pivo = vetor[len(vetor) // 2]
  esq,mid,dir = [x for x in vetor if x < pivo], [x for x in vetor if x == pivo], [x for x in vetor if x > pivo]
  
  return quick_sort(esq) + mid + quick_sort(dir)


def criar_vetor(tamanho):
  return [random.randint(1, 1000) for _ in range(tamanho)]


def main():
  tamanho_vetor = int(input("Informe o tamanho do vetor: "))

  vetor_insercao = criar_vetor(tamanho_vetor)
  vetor_selecao = vetor_insercao.copy()
  vetor_bolha = vetor_insercao.copy()
  vetor_quick = vetor_insercao.copy()

  inicio = time.time()
  insercao_direta(vetor_insercao)
  tempo_insercao = time.time() - inicio

  inicio = time.time()
  selecao_direta(vetor_selecao)
  tempo_selecao = time.time() - inicio

  inicio = time.time()
  bolha(vetor_bolha)
  tempo_bolha = time.time() - inicio

  inicio = time.time()
  vetor_quick = quick_sort(vetor_quick)
  tempo_quick = time.time() - inicio
  

  print("Vetor ordenado por Inserção Direta:", vetor_insercao)
  print("Tempo gasto por Inserção Direta: {:.6f} segundos".format(
      tempo_insercao))

  print("\nVetor ordenado por Seleção Direta:", vetor_selecao)
  print(
      "Tempo gasto por Seleção Direta: {:.6f} segundos".format(tempo_selecao))

  print("\nVetor ordenado por Bolha:", vetor_bolha)
  print("Tempo gasto por Bolha: {:.6f} segundos".format(tempo_bolha))

  print("\nVetor ordenado por Quick Sort:", vetor_quick)
  print("Tempo gasto por Quick: {:.6f} segundos".format(tempo_quick))

if __name__ == "__main__":
  main()
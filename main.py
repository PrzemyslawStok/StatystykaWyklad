import numpy as np
from matplotlib import pyplot as plot
import timeit

#poniżej znajduje się funkcja generatora z przykładu z transparencji
def generator(size: int) -> np.ndarray:
    # tutaj wybieram przykładowe liczby z tabelki z prezentacji
    a: int = 16807
    b: int = 0
    m: int = 2 ** 31 - 1

    x_0 = 10  # tutaj możemy wybrać dowolną liczbę, przykładowo czas w milisekundach
    x_n = x_0

    array: np.ndarray = np.empty(size, dtype=float)
    #x_0 opuszczamy - to nie jest wartość otrzymana z generatora

    for i in range(size):
        x_n = (a * x_n + b) % m #to wzór z wykładu
        array[i] = x_n/m #jak podzielimy przez wartość maksymalną otrzymamy liczby z przedziału [0,1]

    return array

def plotHistorgram(array: np.ndarray, noBars: int):
    # funkcja przygotowuje histogram z macierzy
    # wartośći w odpowiednich przedziałach są grupowane w odpowiednich słupkach

    Y, X = np.histogram(array, noBars)

    # ilość słupków jest większa od 1 od liczby wartośći, trzeba jeden odjąć
    plot.bar(X[:-1], Y, width=0.5, color='#0504aa', alpha=0.7)
    plot.show()


def standardRandom(size: int, noBars: int)->float:
    startTime = timeit.default_timer()
    histogramArray: np.ndarray = np.random.random(size)
    endTime = timeit.default_timer()
    plotHistorgram(histogramArray, noBars)

    return endTime-startTime


def normalDistribution(size: int, noBars: int):
    # tworzymy tablicę dla rozkładu normalnego
    histogramArray: np.ndarray = np.random.normal(loc=0, scale=1, size=size)
    plotHistorgram(histogramArray, noBars)


def ownDistribution(size: int, noBars: int)->float:
    # tutaj proszę użyć własnej funkcji generującej dane
    startTime = timeit.default_timer()
    histogramArray: np.ndarray = generator(size)
    endTime = timeit.default_timer()

    plotHistorgram(histogramArray, noBars)
    return endTime-startTime

def printTime(time: float, name: str="generatora"):
    print(f"Czas działania {name}: {(time):0.5f}s")

if __name__ == '__main__':
    #np.random.seed(10)
    #wyświetlamy kilka liczb generowanych przez generator z wykłdu:
    print("Tablica wygenerowana przez przykładowy generator z wykładu: ")
    print(generator(5))

    # poniżej naryzowano histogram dla rozkładu z biblioteki numpy
    # generujemy pewną ilość liczb losowych
    # proszę sprawdzić jak zmienia się rozkład w zależności od ilości liczb
    # proszę zwrócić uwagę na ilość słupków z danymi - noBars

    #standardRandom(size=10, noBars=5)

    # rozkład normalny
    #normalDistribution(size=100, noBars=1000)

    #Zad 1 proszę uzupełnić funkcję i użyć przygotowanego generatora z wykładu
    #(f"Czas działania generatora: {(endTime - startTime):0.5f}s")

    printTime(standardRandom(size=1000_000, noBars=2), "generatora numpy")
    printTime(ownDistribution(size=1000_000, noBars=2),"zbudowanego generatora")



    # Zad 2 proszę utworzyć generator LFG - transarencja 6
    # ownDistribution1(size=100, noBars=10)

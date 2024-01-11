import os
import time
from ATDGraph import ATDGraph
from typing import List

def menu() -> int:
    '''
    Выводит меню пользователя и возвращает выбранный пункт.

    Возвращает:
    int : выбранный пункт меню
    '''
    menu = (
        "\n(1) Load network\n(2) Node operations"
        "\n(3) Edge operations\n(4) Display network"
        "\n(5) Individual Task\n(6) Save network\n(7) HomeWork 3 Task\n(0) Exit\n>> "
    )
    return input(menu)

def read_adjacency_list(file_name: str) -> ATDGraph:
    with open(file_name, 'r') as file:
        data = file.readlines()
        vertices = int(data[0].strip())
        graph = ATDGraph(vertices)
        for line in data[1:]:
            parts = line.split()
            u, v, weight = int(parts[0]), int(parts[1]), int(parts[2])
            graph.addEdge(u, v, weight)
    return graph

def read_adjacency_matrix_from_file(file_name:str)->List[List[int]]:
    '''
    Читает матрицу смежности из файла.

    Параметры:
    file_name (str) : имя файла

    Возвращает:
    List[List[int]] : матрица смежности
    '''
    with open(file_name, 'r', encoding='utf-8') as file:
        matrix = []
        for line in file:
            matrix.append(list(map(int, line.strip().split())))
    return matrix


def load_network(file: str) -> ATDGraph:
    '''
    Загружает сеть из файла.

    Параметры:
    file (str) : имя файла

    Возвращает:
    ATDGraph : граф, загруженный из файла
    '''
    adjacency_matrix = read_adjacency_matrix_from_file(file)
    num_vertices = len(adjacency_matrix)
    g = ATDGraph(num_vertices)
    cnt_l = 0
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adjacency_matrix[i][j] != 0:
                cnt_l += 1
                g.addEdge(i, j, adjacency_matrix[i][j])
    return g, cnt_l

def print_problem_and_wait(exception: str) -> None:
    '''
    Выводит ошибку и ждет 3 секунды.

    Параметры:
    exception (str) : сообщение об ошибке
    '''
    print("Возникла ошибка\nОшибка:\n", exception)
    time.sleep(3)
    os.system("cls||clear")


if __name__ == "__main__":
    g, cnt_lines = load_network("input.txt")
    g.visual()
    print("Число вершин в графе:", g.V)
    while True:
        try:
            choise = int(menu())
        except Exception as ex:
            print_problem_and_wait(ex)
        if choise == 1:
            try:
                file = input(
                    "Укажите файл с матрицей идентичности (включая формат файла): "
                )
                print("Загрузка графа из файла...")
                g, cnt_lines = load_network(file)
                #g = read_adjacency_list('output.txt')
                print("Загрузка графа из файла проведена успешно")
                time.sleep(3)
                os.system("cls||clear")
            except Exception as ex:
                print_problem_and_wait(ex)
        elif choise == 2:
            try:
                operation_number = int(
                    input("\t(1) Insert\n\t(2) Remove\n\t(3) First\n\t(4) Next\n\t>> ")
                )
                if operation_number == 1:
                    g.ADD_V(
                        "заглушка разрешенная преподавателем",
                        "заглушка разрешенная преподавателем",
                    )
                    print("Вершина добавлена! Добавьте ей ребро")
                    print("Число вершин в графе:", g.V)
                    g.visual()
                    time.sleep(3)
                    os.system("cls||clear")
                elif operation_number == 2:
                    number_to_delete = int(
                        input("Выберете номер вершины для удаления: ")
                    )
                    g.DEL_V(number_to_delete)
                    print("Число вершин в графе:", g.V)
                    g.visual()
                    time.sleep(3)
                    os.system("cls||clear")
                elif operation_number == 3:
                    number_to_print = int(
                        input("Выберете номер вершины для поиска смежной вершины: ")
                    )
                    output = g.FIRST(number_to_print)
                    print(output if output != "L" else "Вершина не найдена")
                    time.sleep(3)
                    os.system("cls||clear")
                elif operation_number == 4:
                    number_to_find = int(
                        input("Выберете номер вершины для поиска смежной вершины: ")
                    )
                    number_to_print = int(
                        input(
                            "Выберете минимальный номер вершины, которую вы можете вернуть (вершины с номером меньше показаны не будет): "
                        )
                    )
                    output = g.NEXT(number_to_find, number_to_print)
                    print(output if output != "L" else "Вершина не найдена")
                    time.sleep(3)
                    os.system("cls||clear")
            except Exception as ex:
                print_problem_and_wait(ex)
        elif choise == 3:
            try:
                operation_number = int(
                    input(
                        "\t(1) Insert\n\t(2) Remove\n\t(3) Edit\n\t(4) Find weight\n\t>> "
                    )
                )
                if operation_number == 1:
                    number_start = int(input("Выберете откуда идет ребро: "))
                    number_finish = int(input("Выберете в какую вершину идет ребро: "))
                    weight = int(input("Выберете вес ребра: "))
                    output = g.ADD_E(number_start, number_finish, weight)
                    print(
                        f"Ребро ({number_start},{number_finish} с весом {weight} добавлено!"
                    )
                    g.visual()
                    time.sleep(3)
                    os.system("cls||clear")
                elif operation_number == 2:
                    number_start = int(input("Выберете откуда идет ребро: "))
                    number_finish = int(input("Выберете в какую вершину идет ребро: "))
                    g.DEL_E(number_start, number_finish)
                    print(
                        f"Ребро ({number_start},{number_finish} с весом {weight} добавлено!"
                    )
                    g.visual()
                    time.sleep(3)
                    os.system("cls||clear")
                elif operation_number == 3:
                    number_start = int(input("Выберете откуда идет ребро: "))
                    number_finish = int(input("Выберете в какую вершину идет ребро: "))
                    weight = int(input("Выберете вес ребра: "))
                    output = g.EDIT_E(number_start, number_finish, weight)
                    print(
                        f"Ребро ({number_start},{number_finish} с весом {weight} изменено!"
                    )
                    time.sleep(3)
                    os.system("cls||clear")
                elif operation_number == 4:
                    number_start = int(input("Выберете откуда идет ребро: "))
                    number_finish = int(input("Выберете в какую вершину идет ребро: "))
                    output = g.VERTEX(number_start, number_finish)
                    print(
                        f"Вес ребра = {output}"
                        if output != 0
                        else "Данное ребро не существует"
                    )
                    time.sleep(3)
                    os.system("cls||clear")
            except Exception as ex:
                print_problem_and_wait(ex)
        elif choise == 4:
            try:
                operation_number = int(
                    input(
                        "\t(1) Display network with graph\n\t(2) Display matrix\n\t>> "
                    )
                )
                if operation_number == 1:
                    g.visual()
                    print("Граф выведен с помощью библиотеки matplotlib и networkx")
                    time.sleep(3)
                    os.system("cls||clear")
                elif operation_number == 2:
                    for i in g.graph:
                        print(i)
            except Exception as ex:
                print_problem_and_wait(ex)
        elif choise == 5:
            try:
                s = int(input("Введите вершину старта задания (поиск путей)"))
                d = int(input("Введите вершину конца задания (поиск путей)"))
                print("Все пути от вершины % d до % d :" % (s, d))
                g.printAllPaths(s, d)
            except Exception as ex:
                print_problem_and_wait(ex)
        elif choise == 6:
            try:
                filename = input("Введите имя файла для сохранения вместе с форматом: ")
                with open(filename, "w") as file:
                    for row in g.graph:
                        file.write(" ".join(map(str, row)) + "\n")
                print(f"Матрица идентичности графа сохранена в файл {filename}")
            except Exception as ex:
                print_problem_and_wait(ex)
        elif choise == 7:
            paths = []
            for i in range(g.V):
                for j in range(g.V):
                    if i!=j:
                        a = g.printAllPaths(i,j)
                        for p in a:
                            if len(p)==3:
                                paths.append(p)
            visit = []
            cnt = 0
            for _ in sorted(paths):
                if _[::-1] not in visit and _ not in visit:
                    cnt+=1
                    print(cnt, _)
                    visit.append(_)
                
        elif choise == 0:
            quit()

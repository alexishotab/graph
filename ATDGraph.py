import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import List, Union

class ATDGraph():
    def __init__(self, vertices:int)->None:
        '''
        Конструктор класса. Инициализирует граф с заданным количеством вершин.

        Параметры:
        vertices (int) : количество вершин в графе
        '''
        self.graph = [[0]*vertices for _ in range(vertices)]
        self.V = vertices

    def addEdge(self, u:int, v:int, weight:int=1)->None:
        '''
        Добавляет ребро в граф.

        Параметры:
        u (int) : начальная вершина
        v (int) : конечная вершина
        weight (int) : вес ребра (default = 1)
        '''
        self.graph[u][v] = weight

    def ADD_E(self, v:int, w:int, c:int)->None: 
        '''
        Добавляет дугу в граф.

        Параметры:
        v (int) : начальная вершина
        w (int) : конечная вершина
        c (int) : вес дуги
        '''
        self.addEdge(v,w,c)

    def EDIT_E(self, u:int, v:int, weight:int=1)->None:
        '''
        Изменяет вес ребра.

        Параметры:
        u (int) : начальная вершина
        v (int) : конечная вершина
        weight (int) : новый вес ребра (default = 1)
        '''
        self.addEdge(v,w,c)

    def ADD_V(self, name:str, mark:str)->None:
        '''
        Добавляет вершину в граф.

        Параметры:
        name (str) : имя вершины
        mark (str) : маркировка вершины
        '''
        self.V += 1
        self.graph.append([0]*self.V)
        for i in range(self.V):
            self.graph[i].append(0)

    def EDIT_E(self, v:int, w:int, new_weight:int)->None:
        '''
        Изменяет вес дуги.

        Параметры:
        v (int) : начальная вершина
        w (int) : конечная вершина
        new_weight (int) : новый вес дуги
        '''
        self.graph[v][w] = new_weight

    def FIRST(self, v:int)->Union[str, int]:
        '''
        Возвращает индекс первой вершины, смежной с заданной вершиной.

        Параметры:
        v (int) : индекс вершины

        Возвращает:
        Union[str, int] : индекс первой вершины или 'L', если вершина не имеет смежных вершин
        '''
        for first_vertex in range(self.V):
            if self.graph[v][first_vertex] != 0:
                return first_vertex
        return 'L'

    def NEXT(self, v:int, i:int)->Union[str, int]:
        '''
        Возвращает индекс первой вершины, смежной с заданной вершиной и индекс которой минимум =i.

        Параметры:
        v (int) : индекс вершины
        i (int) : индекс предыдущей смежной вершины

        Возвращает:
        Union[str, int] : индекс следующей вершины или 'L', если подходящая соседняя вершина не нашлась.
        '''
        for next_vertex in range(i + 1, self.V):
            if self.graph[v][next_vertex] != 0:
                return next_vertex
        return 'L'

    def VERTEX(self, v:int, i:int)->int:
        '''
        Возвращает вес дуги между v и i.

        Параметры:
        v (int) : индекс вершины
        i (int) : индекс вершины, которую следует вернуть

        Возвращает:
        int : вершина с индексом i
        '''
        return self.graph[v][i]

    def DEL_V(self, v:int)->None:
        '''
        Удаляет вершину из графа.

        Параметры:
        v (int) : индекс удаляемой вершины
        '''
        if v < self.V:
            self.graph.pop(v)
            for row in self.graph:
                row.pop(v)
            self.V -= 1

    def DEL_E(self, v:int, w:int)->None:
        '''
        Удаляет дугу из графа.

        Параметры:
        v (int) : начальная вершина
        w (int) : конечная вершина
        '''
        if v < self.V and w < self.V:
            self.graph[v][w] = 0

    def printAllPathsUtil(self, u:int, d:int, visited:List[bool], path:List[int])->None:
        '''
        Рекурсивно находит все возможные пути между вершинами u и d.

        Параметры:
        u (int) : начальная вершина
        d (int) : конечная вершина
        visited (List[bool]) : список посещенных вершин
        path (List[int]) : путь до текущей вершины
        '''
        visited[u]= True
        path.append(u)
        if u==d:
            yield path[:]
        else:
            for i in range(len(self.graph[u])):
                if visited[i] == False and self.graph[u][i] != 0:
                    for p in self.printAllPathsUtil(i, d, visited, path):
                        yield p
        path.pop()
        visited[u]= False

    def printAllPaths(self, s:int, d:int)->None:
        '''
        Выводит все пути между вершинами s и d.
        
        Параметры:
        s (int) : начальная вершина
        d (int) : конечная вершина
        '''
        visited =[False]*(self.V)
        path = []
        pa = []
        for p in self.printAllPathsUtil(s, d, visited, path):
            pa.append(p)
        return pa
    
    def visual(self)->None:
        '''
        Визуализирует граф.

        Создает визуализацию графа и показывает его на экране.
        '''
        G = nx.DiGraph(directed=True)
        
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != 0:
                    G.add_edge(i, j, weight=self.graph[i][j])     

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

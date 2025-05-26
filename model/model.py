import copy
import random
import warnings

from database.DAO import DAO
import networkx as nx
import itertools


class Model:
    def __init__(self):
        self._allTeams = []
        self._idMapTeams = {}
        self._grafo = nx.Graph()
        self._bestPath = []
        self._bestScore = 0

    def getBestPathV2(self, start):
        self._bestPath = []
        self._bestScore = 0

        parziale = [start]

        vicini = self._grafo.neighbors(start)

        viciniTuples = [(v, self._grafo[start][v]["weight"]) for v in vicini]
        viciniTuples.sort(key =lambda x: x[1], reverse=True)

        # for v in vicini:
        parziale.append(viciniTuples[0][0])
        self._ricorsioneV2(parziale)
        parziale.pop()

        return self.getWeightsOfPath(self._bestPath), self._bestScore

    def _ricorsioneV2(self, parziale):

        # 1) verifico che parziale sia una soluzione, e verifico se migliore della best
        if self.score(parziale) > self._bestScore:
            self._bestScore = self.score(parziale)
            self._bestPath = copy.deepcopy(parziale)

        # 2) verifico se posso aggiungere un nuovo nodo
        # 3) aggiungo nodo e faccio ricorsione

        vicini = self._grafo.neighbors(parziale[-1])
        viciniTuples = [(v, self._grafo[parziale[-1]][v]["weight"]) for v in vicini]
        viciniTuples.sort(key=lambda x: x[1], reverse=True)

        for t in viciniTuples:
            if (t[0] not in parziale and
                    self._grafo[parziale[-2]][parziale[-1]]["weight"] >
                    t[1]):
                parziale.append(t[0])
                self._ricorsioneV2(parziale)
                parziale.pop()
                return

    def getWeightsOfPath(self, path):
        pathTuple = [(path[0], 0)]
        for i in range(1, len(path)):
            pathTuple.append((path[i], self._grafo[path[i-1]][path[i]]["weight"]))
        return pathTuple



    def getBestPath(self, start):
        self._bestPath = []
        self._bestScore = 0

        parziale = [start]

        vicini = self._grafo.neighbors(start)
        for v in vicini:
            parziale.append(v)
            self._ricorsione(parziale)
            parziale.pop()

        return self._bestPath, self._bestScore

    def _ricorsione(self, parziale):
        print(len(parziale))
        # 1) verifico che parziale sia una soluzione, e verifico se migliore della best
        if self.score(parziale) > self._bestScore:
            self._bestScore = self.score(parziale)
            self._bestPath = copy.deepcopy(parziale)

        # 2) verifico se posso aggiungere un nuovo nodo
        # 3) aggiungo nodo e faccio ricorsione

        for v in self._grafo.neighbors(parziale[-1]):
            if (v not in parziale and
                    self._grafo[parziale[-2]][parziale[-1]]["weight"] >
                    self._grafo[parziale[-1]][v]["weight"]):
                parziale.append(v)
                self._ricorsione(parziale)
                parziale.pop()

    def score(self, listOfNodes):
        if len(listOfNodes) < 2:
            warnings.warn("Errore in score, attesa lista lunga almeno 2.")

        totPeso = 0
        for i in range(len(listOfNodes) - 1):
            totPeso += self._grafo[listOfNodes[i]][listOfNodes[i + 1]]["weight"]

        return totPeso

    def buildGraph(self, year):
        self._grafo.clear()

        if len(self._allTeams) == 0:
            print("Lista squadre vuota")
            return
        self._grafo.add_nodes_from(self._allTeams)

        # for u in self._allTeams:
        #     for v in self._allTeams:
        #         if u!=v:
        #             self._grafo.add_edge(u, v)

        myedges = list(itertools.combinations(self._allTeams, 2))

        self._grafo.add_edges_from(myedges)

        salariesOfTeams = DAO.getSalyOfTeams(year, self._idMapTeams)

        for e in self._grafo.edges:
            self._grafo[e[0]][e[1]]["weight"] = salariesOfTeams[e[0]] + salariesOfTeams[e[1]]

        # for n1 in self._grafo.nodes:
        #    for n2 in self._grafo.nodes:
        #        if n1 != n2:
        #            self._grafo.add_edge(n1, n2)

    def getNeighborsSorted(self, source):
        vicini = nx.neighbors(self._grafo, source)  # [v0 v1 v2 ...]
        # vicini = self._grafo.neighbors(source)

        viciniTuple = []

        for v in vicini:
            viciniTuple.append((v, self._grafo[source][v]["weight"]))  # [(v0, p0) (v1, p1) ()]

        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple

    def printGraphdetails(self):
        print(f"Grafo creato con {len(self._grafo.nodes())} nodi e {len(self._grafo.edges())} edges.")

    def getGraphDetails(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def getYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._allTeams = DAO.getTeamsOfYear(year)
        for t in self._allTeams:
            self._idMapTeams[t.ID] = t

        return self._allTeams

    def getRandomNode(self):
        index = random.randint(0, self._grafo.number_of_nodes()-1)
        return list(self._grafo.nodes)[index]

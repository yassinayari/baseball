import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMapTeams = {}
        self._grafo = nx.Graph()
        self._allTeams = {}

    def getYears(self):
        return DAO.getAllYears()

    def getTeamsByYear(self, year):
        self._allTeams = DAO.getAllTeamsByYear(year)
        for t in self._allTeams:
            self._idMapTeams[t.ID] = t

        return self._allTeams


    def buildGraph(self, year):
        self._allTeams = DAO.getAllTeamsByYear(year)
        self._grafo.clear()
        self._grafo.add_nodes_from(self._allTeams)

        for t in self._allTeams:
            for r in self._allTeams:
                if t!=r:
                    self._grafo.add_edge(t, r)

        salariesOfTeams = DAO.getSalyOfTeams(year, self._idMapTeams)

        for e in self._grafo.edges:
            self._grafo[e[0]][e[1]]["weight"] = salariesOfTeams[e[0]] + salariesOfTeams[e[1]]

    def getGraphDetails(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def getNeighborsSorted(self, source):
        vicini = nx.neighbors(self._grafo, source)  # [v0 v1 v2 ...]
        # vicini = self._grafo.neighbors(source)

        viciniTuple = []

        for v in vicini:
            viciniTuple.append((v, self._grafo[source][v]["weight"]))  # [(v0, p0) (v1, p1) ()]

        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple



from database.DAO import DAO
import networkx as nx
import itertools
class Model:
    def __init__(self):
        self._allTeams = []
        self._idMapTeams = {}
        self._grafo = nx.Graph()

    def buildGraph(self, year):
        self._grafo.clear()

        if len(self._allTeams) == 0:
            print("Lista squadre vuota")
            return
        self._grafo.add_nodes_from(self._allTeams)

        myedges = list(itertools.combinations(self._allTeams, 2))

        self._grafo.add_edges_from(myedges)

        salariesOfTeams = DAO.getSalyOfTeams(year, self._idMapTeams)

        for e in self._grafo.edges:
            self._grafo[e[0]][e[1]]["weight"] = salariesOfTeams[e[0]] + salariesOfTeams[e[1]]

        #for n1 in self._grafo.nodes:
        #    for n2 in self._grafo.nodes:
        #        if n1 != n2:
        #            self._grafo.add_edge(n1, n2)

    def printGraphdetails(self):
        print(f"Grafo creato con {len(self._grafo.nodes())} nodi e {len(self._grafo.edges())} edges.")

    def getYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._allTeams = DAO.getTeamsOfYear(year)
        for t in self._allTeams:
            self._idMapTeams[t.ID] = t

        return self._allTeams
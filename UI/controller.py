import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        self._model.buildGraph(int(self._view._ddAnno.value))
        n, a = self._model.getGraphDetails()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo è costituito di {n} nodi e {a} archi."))
        self._view.update_page()


    def handleDettagli(self, e):
        viciniSorted = self._model.getNeighborsSorted(self._selectedTeam)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Il vicinato conta {len(viciniSorted)} squadre."))
        for v in viciniSorted:
            self._view._txt_result.controls.append(
                ft.Text(f"{v[0]} -- peso: {v[1]}"))
        self._view.update_page()

    def handlePercorso(self, e):
        pass

    def handleDDYearSelection(self, e):
        year = self._view._ddAnno.value
        teams = self._model.getTeamsByYear(year)

        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Nell'anno {year} hanno militato {len(teams)} squadre."))
        for team in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{team.teamCode}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data=team,text=team.teamCode,on_click=self.readDDTeams))
        self._view.update_page()

    def fillDD(self):
        years = self._model.getYears()
        for year in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(year))

    def readDDTeams(self, e):
        if e.control.data is None:
            self._selectedTeam = None
        else:
            self._selectedTeam = e.control.data



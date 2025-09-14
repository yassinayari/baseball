from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.year as year
                            from teams t
                            where t.year >= 1980"""

        cursor.execute(query)

        results = []

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllTeamsByYear(year):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.*
                    from teams t
                    where t.year = %s"""

        cursor.execute(query, (year, ))

        results = []

        for row in cursor:
            results.append(Team(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getSalyOfTeams(year, idMap):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.teamCode, t.ID, sum(s.salary) as totSalary
                       from salaries s, teams t
                       where t.`year` = %s
                       and s.`year` = t.`year`
                       and t.ID = s.teamID 
                       group by t.teamCode"""

        cursor.execute(query, (year,))

        results = {}
        for row in cursor:
            # results.append(idMap[row["ID"]], row["totSalary"])
            results[idMap[row["ID"]]] = row["totSalary"]

        cursor.close()
        conn.close()
        return results
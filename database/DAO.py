from database.DB_connect import DBConnect

from model.team import Team
class DAO():
    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "select distinct(year) from teams t where `year` >= 1980 order by `year` desc "

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getTeamsOfYear(year):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from teams t where t.`year` = %s"

        cursor.execute(query, (year,))

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
                 from salaries s, teams t, appearances a) 
                where s.`year` = t.`year` and t.`year` = a.`year` 
                and a.`year` = 2015
                and t.ID = a.teamID 
                and s.playerID = a.playerID 
                group by t.teamCode"""

        cursor.execute(query, (year,))

        results = {}
        for row in cursor:
            #results.append(idMap[row["ID"]], row["totSalary"])
            results[idMap[row["ID"]]] = row["totSalary"]

        cursor.close()
        conn.close()
        return results
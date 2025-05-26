from model.model import Model


mymodel = Model()
mymodel.getTeamsOfYear(2015)
mymodel.buildGraph(2015)
mymodel.printGraphdetails()

start = mymodel.getRandomNode()
path, score = mymodel.getBestPathV2(start)
print(len(path), score)
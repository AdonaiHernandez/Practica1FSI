# Search methods
from tabulate import tabulate
import search
import time

ab = search.GPSProblem('A', 'B', search.romania)

#Calculo de tiempo de busqueda en amplitud 1000 iteraciones

bfsTime = time.time_ns()

for i in range(1000):
    search.breadth_first_graph_search(ab)
    
bfsTime = round((time.time_ns() - bfsTime)/1e6, 2)

#Calculo de tiempo de busqueda en profundidad 1000 iteraciones

dfsTime = time.time_ns()

for i in range(1000):
    search.depth_first_graph_search(ab)
    
dfsTime = round((time.time_ns() - dfsTime)/1e6, 2)

#Calculo de tiempo de busqueda con ramificacion y acotacion 1000 iteraciones

bAndBTime = time.time_ns()

for i in range(1000):
    search.branch_and_bound_search(ab)
    
bAndBTime = round((time.time_ns() - bAndBTime)/1e6, 2)

#Calculo de tiempo de busqueda con ramificacion y acotacion con substimacion 1000 iteraciones

substimationTime = time.time_ns()

for i in range(1000):
    search.branch_and_bound_substimation_search(ab)

substimationTime = round((time.time_ns() - substimationTime) / 1e6, 2)

#Resultados
    
bfsSearch = search.breadth_first_graph_search(ab)

dfsSearch = search.depth_first_graph_search(ab)

baandbound = search.branch_and_bound_search(ab)

substimation = search.branch_and_bound_substimation_search(ab)

table = [
    ['Origen', 'Destino', 'Amplitud', 'Profundidad', 'Ramificación y acotación', 'Ramificación y acotación con subestimación'],
    ['Arad', 'Bucarest', 'Generados: {0} \nVisitados: {1}\nCosto total: {2}\nTiempo(ms): {3}'.format(bfsSearch[2], bfsSearch[1], bfsSearch[0].path_cost, bfsTime),
     'Generados: {0} \nVisitados: {1}\nCosto total: {2}\nTiempo(ms): {3}'.format(dfsSearch[2], dfsSearch[1], dfsSearch[0].path_cost, dfsTime),
     'Generados: {0} \nVisitados: {1}\nCosto total: {2}\nTiempo(ms): {3}'.format(baandbound[2], baandbound[1], baandbound[0].path_cost, bAndBTime),
     'Generados: {0} \nVisitados: {1}\nCosto total: {2}\nTiempo(ms): {3}'.format(substimation[2], substimation[1], substimation[0].path_cost, substimationTime)]]

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
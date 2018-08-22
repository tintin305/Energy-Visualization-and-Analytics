import osmnx as ox
import matplotlib.pyplot as plt

place_name = "Kamppi, Helsinki, Finland"
graph = ox.graph_from_place(place_name)
type(graph)
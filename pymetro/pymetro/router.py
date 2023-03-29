from heapdict import heapdict

from .types import Route, Station
from .data import LINKS

from collections import defaultdict


class Router:
    def __init__(self, id = []):
        links_2 = LINKS.copy()
        diff = []
        result = []
        negative_result = []
        for link in links_2:
            for _ in id:
                if _ in link:
                    negative_result.append(link)
                result.append(link)
            diff = list(set(result) - set(negative_result))
        self.graph = defaultdict(heapdict)
        for i in diff:
            self.graph[Station(i[0])][Station(i[1])] = i[2]
            self.graph[Station(i[1])][Station(i[0])] = i[2]

    def make_route(self, source: Station, target: Station) -> Route:
        queue = heapdict()
        for i in self.graph:
            queue[i] = float('inf')
        parent = {}
        for i in self.graph:
            parent[i] = float('inf')
        queue[source], parent[source] = 0, 0
        visited = {source: [source]}
        while len(queue):
            # print(len(queue)
            nearest, nearest_dist = queue.popitem()
            for connection in self.graph[nearest]:
                if connection in queue:
                    updated = self.graph[nearest][connection] + nearest_dist
                    if parent[connection] > updated:
                        if connection in queue:
                            queue[connection] = updated
                        parent[connection] = updated
                        visited[connection] = visited[nearest] + [connection]
                        # print(visited[connection])
        # print(visited)
        self.time = parent[target]
        self.path = visited[target]
        return self

    # def delete_station(self, id=[]):
    #     links_2 = LINKS.copy()
    #     diff = []
    #     result = []
    #     negative_result = []
    #     for link in links_2:
    #         for _ in id:
    #             if _ in link:
    #                 negative_result.append(link)
    #             result.append(link)
    #         diff = list(set(result) - set(negative_result))
    #     return diff

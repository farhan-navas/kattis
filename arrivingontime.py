from heapq import heappop, heappush
import sys

def get_latest_departure(curr_time: int, init_dep_time: int, dep_interval: int, travel_time: int):

    # find the closest departure timing
    leave_from_stop = curr_time - travel_time

    # if leave_from_stop is earlier than the first train departure, return None
    if leave_from_stop < init_dep_time:
        return -1
    else:
        multiplier = (leave_from_stop - init_dep_time) // dep_interval
        latest_departure = init_dep_time + multiplier * dep_interval

    return latest_departure

# departure stop [0]
# arrival stop [1]
# initial departure time [2]
# departure interval [3]
# travel time [4]

def djikstras(n: int, m: int, s: int, lines: list[list[int]]) -> int:
    # s-> max arrival time, n-> num of cities, m -> num of tram lines, lines -> every possible tram route
    pq = [(-s, n - 1)]
    route_map = [[] for i in range(n)]
    visited = [False for i in range(n)]

    for line in lines:
        route_map[line[1]].append(line)

    while pq:
        priority, curr_stop = heappop(pq)
        priority = -priority
        if curr_stop == 0:
            return priority if priority >= 0 else "impossible"
        if visited[curr_stop]:
            continue
        for line in route_map[curr_stop]:
            prev_time = get_latest_departure(priority, line[2], line[3], line[4])
            if prev_time == -1:
                continue
            visited[curr_stop] = True
            heappush(pq, (-prev_time, line[0]))
    
    return "impossible"
    
def run_djikstras():
    first_line = sys.stdin.readline().strip()
    n, m, s = map(int, first_line.split())

    routes = []
    for i in range(m):
        next_line = sys.stdin.readline().strip()
        u, v, t0, p, d = map(int, next_line.split())
        routes.append([u, v, t0, p, d])

    res = djikstras(n, m, s, routes)
    print(res)

run_djikstras()
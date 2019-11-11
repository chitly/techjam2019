n, m = [int(e) for e in input().split()]
graph = list()
person = list()
clock = list()
for i in range(0, n):
    person.append(int(input()))
for i in range(0, m):
    clock.append([int(e) for e in input().split()])

for i in range(0, n):
    graph.append(list())
    for j in range(0, m):
        if (abs(int(person[i]) - clock[j][0]) <= clock[j][1]):
            graph[i].append(1)
        else:
            graph[i].append(0)

# ### print check graph
# for i in range(0, n):
#   for j in range(0, m):
#     print(str(graph[i][j]) + ' ', end = '')
#   print()


# Python program to find
# maximal Bipartite matching.

class GFG:
    def __init__(self, graph):

            # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

    # A DFS based recursive function
    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, matchR, seen):

        # Try every job one by one
        for v in range(self.jobs):

            # If applicant u is interested
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:

                # Mark v as visited
                seen[v] = True

                '''If job 'v' is not assigned to 
                  an applicant OR previously assigned  
                  applicant for job v (which is matchR[v])  
                  has an alternate job available.  
                  Since v is marked as visited in the  
                  above line, matchR[v]  in the following 
                  recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the  
            applicants assigned to jobs.  
            The value of matchR[i] is the  
            applicant number assigned to job i,  
            the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs

        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):

            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs

            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return result


g = GFG(graph)
print (g.maxBPM())
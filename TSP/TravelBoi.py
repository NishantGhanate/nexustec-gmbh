from py2opt.routefinder import RouteFinder

class TravelBoi():

    def __init__(self):
        self.city_names = []
        self.distances = []
        self.index = 0
    
    def insert_node(self):
        """
        TODO : 
        1. Add input data type validation on node edges
        2. Extend the graph 
        3. Validate node edges
        """
        self.clear()
        node_names = list(map(str,input('\nEnter node names : ').strip().split() ) )
        self.city_names.extend(node_names)
        node_len = len(self.city_names)

        for name in node_names:
            validated = False
            
            while not validated:
                inp = input('\nEnter {} values for node {} : '\
                    .format(node_len,name)).strip().split()

                node_edges = list(map(int,inp) )
                validated, message = self.validate_node_edges(node_edges)
                if validated:
                    self.distances.append(node_edges)
                    break
                else:
                    print("\nInvalid node edge")
                    print(message)
            self.index += 1
        
        best_distance, best_route = self.calculate_path(self.distances,self.city_names)
        print("\nBest distance = {}".format(best_distance))
        print("Best Route = {}".format(best_route))

    def validate_node_edges(self,node_edges):
        """
        1. self.index = 0 always 
        2. rest all vals > 0
        3. lables size == sub arr values 
        """
        message = ""
        
        # print(node_edges[self.index],node_edges[self.index]!=0)
        if node_edges[self.index] != 0 :
            message = f"There should be 0 at index {self.index}"
            return False, message 
        
        for i , val in enumerate(node_edges):
            if i != self.index and val < 1:
                message = f"This {val} should  greater than 1 at index {i}"
                return False, message

        if len(node_edges) != len(self.city_names):
            message = "Incorrect size edges "
            return False, message
        
        # This can be optimized .. 
        if self.index :
            loop = self.index 
            for i in range(loop):
                if node_edges[i] == 0:
                    break
                if not node_edges[i] == self.distances[i][self.index]:
                    message = f"Incorrect value {node_edges[i]} at index {i}"
                    return False, message

        return True, message
    
    def validate_graph(self):
        """
        1. all corresponding nodes values should be same 
            i.e A -> B and B -> A should be same value
        """

        col = row = len(self.distances) 
        for i in range(col):
            for j in range(row):
                # print(self.distances[i][j] == self.distances[j][i])
                if not self.distances[i][j] == self.distances[j][i]:
                    return False
        return True
        
    def calculate_path(self,distances,city_names):
        route_finder = RouteFinder(distances, city_names, iterations=len(city_names))
        best_distance, best_route = route_finder.solve()
        return best_distance, best_route
        
    def delete_node(self):
        city_len = len(self.city_names)
        if city_len >= 3 :
            
            print("\nSelect a Node label : {} ".format(self.city_names))
            delete_node = input("Enter a label name to delete : ")

            dist_len = len(self.distances)
            del_index = 0
            for i in range(city_len):
                if delete_node == self.city_names[i]:
                    del_index = i
                    del self.city_names[i]
                    break

            if city_len == len(self.city_names):
                print("\nDid not found matching label (Note : labels are case-sensitive)")
                return 

            for j in range(dist_len):
                del self.distances[j][del_index]
            del self.distances[i] 

            print("\nDeleted Node = {} ".format(delete_node))
            print("\nUpdated Graph Lables = {} ".format(self.city_names))
            print("Updated Graph edges = {} ".format(self.distances))

            best_distance, best_route = self.calculate_path(self.distances,self.city_names)
            print("\nBest distance = {}".format(best_distance))
            print("Best Route = {}".format(best_route))
        else:
            print("\n Insufficient nodes, There should be 2 or more nodes" )

    def help_menu(self):
        print("\n Welcome to Help menu")
        print("\nEnter node names (by giving a space) : A B C D ")
        print("\nEnter node values for A (by giving a space) : 0 29 15 35")
        print("Enter node values for B  : 29 0 57 42")
        print("Enter node values for C  : 15 57 0 61")
        print("Enter node values for D  : 35 42 61 0")

        print("\nFor each position of label the value  should be 0 ")
        print("For A [0, 29, 15, 35]\n B [29, 0, 57, 42] so on..." )

    def clear(self):
        self.city_names = []
        self.distances = []
        self.index = 0

    def console(self):
        deco = "#"*10
        print("\n{deco} Welcome to TSP  {deco}\n".format(deco=deco))
        print("press 1 : insert node ")
        print("press 2 : delete node ")
        print("press 3 : clear previous data ")
        print("press 4 : help menu ")
        print("press 5 : exit program \n")

        selection = int(input("Enter your selection : "))
        if selection == 1:
            self.insert_node()

        elif selection == 2:
            self.delete_node()

        elif selection == 3:
            self.clear()

        elif selection == 4:
            self.help_menu()

        elif selection == 5:
            exit()
        else :
            print("\nInvalid selection please try again")


if __name__ == "__main__":
    travel_boi = TravelBoi()

    while True:
        travel_boi.console()
    
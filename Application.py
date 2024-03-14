

from Node import  Node
from Btree import Btree
import sys



class Application :

    def __init__(self) -> None : 
        self.root = Node()
        self.arbreBtree = Btree(self.root,2)
        self.init()

    def init(self):
        self.arbreBtree.insert_liste([6,10,22,30,4,8,12,18,26,34,2,5,7,9,11,13,16])
        #il faut faire la fonction insert_liste

    def explore_test(self):
        print("***** tester la fonction explore *****")
        print(self.arbreBtree.explore())

    def recherche_test(self):
        print("***** tester la fonction recherche *****")
        print("Pour la valeur 0 " + str(self.arbreBtree.rechechre(0)))
        print("Pour la valeur 14 " + str(self.arbreBtree.rechechre(14)))
        print("Pour la valeur 3 " + str(self.arbreBtree.rechechre(3)))
        print("Pour la valeur 1 " + str(self.arbreBtree.rechechre(1)))

    def hauteur_test(self):
        print("***** tester la fonction hauteur *****")
        print(self.arbreBtree.hauteur())

    def isBtree_test(self):
        print("***** tester la fonction hauteur *****")
        print(self.arbreBtree.isBtree())

    def insertion_test(self):
        arbre = Btree(Node(),20)
        for i in range(1000) :
            arbre.insertion(i)
        result = arbre.explore()
        assert(len(result)==1000)
        assert(sorted(result)==result)
        assert(arbre.isBtree())

    def graphiz_test(self):
        print(self.arbreBtree.ptint_graphvoz())
        

    
def main() : 
    classeTest = Application()
    
    classeTest.explore_test()
    classeTest.hauteur_test()
    classeTest.isBtree_test()
    #classeTest.graphiz_test()
    """
    classeTest.arbreBtree.insertion(55)
    
    #classeTest.explore_test()
   
    classeTest.arbreBtree.insertion(-55)
    
    #classeTest.explore_test()
    
    
    """
    """
    arbre = Btree(Node(),4)
    for i in range(10000) :
            arbre.insertion(i)
   # classeTest.insertion_test()
    
    print(arbre.ptint_graphvoz())
    """
            
if __name__=="__main__" : 
    main()
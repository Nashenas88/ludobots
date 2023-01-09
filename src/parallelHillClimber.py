from solution import SOLUTION
import constants as c
import copy
import glob
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.children = {}
        self.nextAvailableId = 0
        # Clean up any old data left behind
        for box in glob.glob('assets/box*.npy'):
            os.remove(box)
        for body in glob.glob('assets/body*.npy'):
            os.remove(body)
        for brain in glob.glob('assets/brain*.npy'):
            os.remove(brain)
        for brain in glob.glob('data/fitness*.npy'):
            os.remove(brain)
        for i in range(c.POPULATION_SIZE):
            self.parents[i] = SOLUTION(self.Get_Id())

    def Get_Id(self):
        id = self.nextAvailableId
        self.nextAvailableId += 1
        return id

    def Evolve(self):
        self.Evaluate(self.parents.values())
        for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            print(
                f"================== Evolving iter generation {currentGeneration} ===========================")
            self.Evolve_For_One_Generation()
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children.values())
        self.Print()
        self.Select()

    def Spawn(self):
        self.children.clear()
        for parent in self.parents.values():
            child = copy.deepcopy(parent)
            self.children[parent.id] = child

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Evaluate(self, solutions):
        for solution in solutions:
            solution.Start_Simulation()
        for solution in solutions:
            solution.Wait_For_Simulation()

    def Print(self):
        for parent in self.parents.values():
            print(
                f'{parent.id}: {parent.fitness}, {self.children[parent.id].fitness}')

    def Select(self):
        for parent in self.parents.values():
            child = self.children[parent.id]
            if child.fitness < parent.fitness:
                self.parents[parent.id] = child

    def Show_Best(self):
        parents = list(self.parents.values())
        best = parents[0]
        for parent in parents[1:]:
            if parent.fitness < best.fitness:
                best = parent
        best.Show()

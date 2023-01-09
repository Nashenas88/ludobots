from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]
id = sys.argv[2]
match directOrGui:
    case 'GUI':
        pass
    case 'DIRECT':
        pass
    case other:
        print(f'Unrecognized argument `{directOrGui}`. Expected GUI or DIRECT')
        exit(1)

simulation = SIMULATION(directOrGui, id)
simulation.Run()
simulation.Get_Fitness()

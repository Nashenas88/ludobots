from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]
match directOrGui:
    case 'GUI':
        pass
    case 'DIRECT':
        pass
    case other:
        print(f'Unrecognized argument `{directOrGui}`. Expected GUI or DIRECT')
        exit(1)

simulation = SIMULATION(directOrGui)
simulation.Run()
simulation.Get_Fitness()

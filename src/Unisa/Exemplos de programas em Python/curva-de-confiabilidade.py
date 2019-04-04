# -*- coding: cp1252 -*-
import numpy as np
import matplotlib.pyplot as plt

def MatrixTeste(lambdaL, deltaT):
    return np.array([[1-(3*lambdaL*deltaT), 0, 0],
              [3*lambdaL*deltaT, 1-((2*lambdaL*deltaT)), 0],
              [0, 2*lambdaL*deltaT, 1]
              ], np.double)
    pass

def MatrixTeste2(lambdaL, deltaT, miC):
    return np.array([[1-(3*lambdaL*deltaT), 0, miC*deltaT],
              [3*lambdaL*deltaT, 1-((2*lambdaL*deltaT)), 0],
              [0, 2*lambdaL*deltaT, 1-(miC*deltaT)]
              ], np.double)
    pass

def initialpTeste():
    return np.array([[1],
                     [0],
                     [0]
                     ], np.double)
    pass

def arrayOK_Teste():
    return np.array([[1],
                     [1],
                     [0]
                     ], np.double)

################################################

def matrixA_Conf(lambdaL, deltaT, miC, miP):
    return np.array([[1-(3*lambdaL*deltaT), miC*deltaT, miP*deltaT, 0],
              [lambdaL*deltaT, (1-(2*lambdaL*deltaT))-(miC*deltaT), 0, 0],
              [2*lambdaL*deltaT, 0, (1-(lambdaL*deltaT))-(miP*deltaT), 0],
              [0, 2*lambdaL*deltaT, lambdaL*deltaT, 1]
              ], np.double)
    pass


def matrixA_Av(lambdaL, deltaT, miC, miP):
     return np.array([[1-(3*lambdaL*deltaT), miC*deltaT, miP*deltaT, miC*deltaT],
              [lambdaL*deltaT, (1-(2*lambdaL*deltaT))-(miC*deltaT), 0, 0],
              [2*lambdaL*deltaT, 0, (1-(lambdaL*deltaT))-(miP*deltaT), 0],
              [0, 2*lambdaL*deltaT, lambdaL*deltaT, 1-(miC*deltaT)]
               ], np.double)
     pass


def initialp():
    return np.array([[1],
                     [0],
                     [0],
                     [0]
                     ], np.double)
    pass


def arrayOK():
    return np.array([[1],
                     [1],
                     [1],
                     [0]
                     ], np.double)
    pass

def arrayFail():
    return np.array([[0],
                     [0],
                     [0],
                     [1]
                     ], np.double)
    pass


if __name__ == "__main__":
    ###########################
    # Parâmetros
    ###########################
    # Número de interações
    num_Interacoes = 10000
    # MTTF
    mttf = 5000
    #MTTRc
    mttrc = 0.5
    #MTTRp
    mttrp = 5*30*24
    ###########################
    # Código
    ###########################
    print("Starting...")
    lambdaL = 1/mttf
    miC = 1/mttrc
    miP = 1/mttrp
    deltaT = 1/60 # 1 minuto
    print("Lambda: "+ str(lambdaL))
    print("Delta: " + str(deltaT))
    print("MiC: " + str(miC))
    print("MiP: " + str(miP))
    #print(matrixA_Conf(lambdaL,deltaT,miC,miP))
    #print(matrixA_Av(lambdaL, deltaT, miC, miP))
    ok = arrayOK()
    fail = arrayFail()
    pc = initialp()
    Ac = matrixA_Conf(lambdaL,deltaT,miC,miP)
    pa = initialp()
    Av = matrixA_Av(lambdaL, deltaT, miC, miP)
    y1 = np.array([])
    y2 = np.array([])
    #for i in range(0,num_Interacoes):
    #    pc = np.matmul(Ac, pc)
        #print(np.sum(pc * ok))
        #
   #     pa = np.matmul(Av, pa)
        #print(np.sum(pa * ok))
    #print(np.sum(pc))
    #print(np.sum(pa))
    #Ac = np.linalg.matrix_power(Ac, num_Interacoes)
    #pc = np.matmul(Ac, pc)
    #
    #Av = np.linalg.matrix_power(Av, num_Interacoes)
    #pa = np.matmul(Av, pa)
    ###########
    y0 = np.array([])
    y00 = np.array([])
    TesteM = MatrixTeste(lambdaL, deltaT)
    TesteM2= MatrixTeste2(lambdaL, deltaT, miC)
    pt = initialpTeste()
    ok_t = arrayOK_Teste()
    for i in range(0, num_Interacoes):
        Temp = np.linalg.matrix_power(TesteM, i)
        pr = np.matmul(Temp, pt)
        teste = np.sum(pr * ok_t)
        y0 = np.append(y0, teste)

    for i in range(0, num_Interacoes):
        Temp = np.linalg.matrix_power(TesteM2, i)
        pr = np.matmul(Temp, pt)
        teste2 = np.sum(pr * ok_t)
        y00 = np.append(y00, teste2)

    #############################

    for i in range(0, num_Interacoes):
        Temp = np.linalg.matrix_power(Ac, i)
        pr = np.matmul(Temp, pc)
        conf = np.sum(pr * ok)
        y1 = np.append(y1, conf)

    for i in range(0, num_Interacoes):
        Temp = np.linalg.matrix_power(Av, i)
        pr = np.matmul(Temp, pa)
        ava = np.sum(pr * ok)
        y2 = np.append(y2, ava)

    #print(np.sum(pc))
    #print(pc)
    #print(pa)
    #print(np.sum(pc*ok))
    #print(1- np.sum(pc * fail))
    #
    #print(np.sum(pa*ok))
    #print(1- np.sum(pa * fail))

    ## Plot
    x = np.arange(0, num_Interacoes, 1)
    #plt.plot(x, y0, 'o')
    #plt.plot(x, y00, '^')
    plt.plot(x, y1, 'g')
    plt.plot(x, y2, 'r')
    plt.show()
    pass

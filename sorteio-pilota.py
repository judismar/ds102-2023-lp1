from random import randint

turma = ['Artur', 'Ana', 'Asafe', 'Zai', 'Mika', 'Hy', "João", "Karol", 'Leslie', 'Luís', 'Luiz', 'Moisés', 'Pablo', 'Pedro D.', 'PH', 'Paixão', 'Ramon', 'Tomás', 'Victor de Medeiros','Victor Lucas', 'Victória', 'Vitória', 'Wallace', 'Beatriz', 'Erick']
while len(turma) > 0: #length
    i =randint(0,len(turma)-1)
    estudante = turma[i]
    turma.pop(i)
    print(estudante)
    input() #pausa

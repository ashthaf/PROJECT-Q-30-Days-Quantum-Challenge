from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()

qc = QuantumCircuit(1,1)
qc.h(0)
qc.measure(0,0)

job = simulator.run(qc)

result = job.result()

counts = result.get_counts()

random_bit = list(counts.keys())[0]

print("Random Bit: ",random_bit)



from ast import If
from qiskit import QuantumCircuit
import math

# pretend inputs (just for understanding, not the homework function)
circuit = QuantumCircuit(3, 2)   # 3 qubits, 2 classical bits
outside_qubit = 0                  # the qubit we will teleport from
qubit_pair = (1, 2)                # bell pair qubits
bell_pair_start = "00"             # starting state of bell pair before entangling

print("Circuit:", circuit)
print("Outside qubit index:", outside_qubit)
print("Bell pair qubits:", qubit_pair)
print("Bell pair start string:", bell_pair_start)

# Unpack the Bell pair qubits
q1, q2 = qubit_pair

# Store the string bits (like "0" or "1")
b0 = bell_pair_start[0]
b1 = bell_pair_start[1]

# Just to keep names clear 
outside = outside_qubit
bell_a = q1
bell_b = q2

print("--------------------")
print("outside:", outside)
print("bell_a pos in circuit:", bell_a)
print("bell_b pos in circuit:", bell_b)
print("start pair b0:", b0)
print("start pair b1:", b1)
print("--------------------")

# i want to make it explicit that bell qubits start in |00>
circuit.reset([bell_a, bell_b])

# Prepare the computational basis for the Bell qubits 
# simply this is replicating the bits in bell_pair_start
if b0 == "1":
    circuit.x(bell_a) #applying X gate (not) to bell_a if b0 is 1

if b1 == "1":
    circuit.x(bell_b) #applying X gate (not) to bell_b if b1 is 1

# Create Bell pair (entanglement)
circuit.h(bell_a)              # put bell_a into superposition
circuit.cx(bell_a, bell_b)     # entangle bell_a with bell_b

amp0 = math.sqrt(0.4) #40% 0
amp1 = math.sqrt(0.6) #60% 1

# Step 4: Prepare the outside qubit we are going to teleport
circuit.initialize([amp0, amp1], outside)

# Display the circuit BEFORE teleportation steps
print(circuit)


# This does NOT create new entanglement. It uses the existing Bell pair
# to "inject" the unknown quantum information into the teleportation channel.

# 1) CNOT with outside as control and Bell A as target
# If outside = |1>, flip Bell A.
# This couples the unknown amplitudes (α and β) to Bell A.
circuit.cx(outside, bell_a)

# 2) Apply Hadamard to the outside qubit
# This creates interference on the outside qubit so that
# measurement will convert the quantum amplitudes (α, β)
# into classical bits that the receiver can use.
circuit.h(outside)

print(circuit)

circuit.measure(outside, 0)
circuit.measure(bell_a, 1)
 
# STEP 7: teleportation corrections
# If measurement of outside qubit (classical bit 0) is 1, apply X to bell_b
# If circuit.clbits[0] == 1: apply X to bell_b
with circuit.if_test((circuit.clbits[0], 1)):
    circuit.x(bell_b)

# If measurement of bell_a (classical bit 1) is 1, apply Z to bell_b
with circuit.if_test((circuit.clbits[1], 1)):
    circuit.z(bell_b)
 
print(circuit)   

 
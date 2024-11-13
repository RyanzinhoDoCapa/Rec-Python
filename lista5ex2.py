clientes_A = {"Carlos", "Ana", "Lucas", "Maria", "Fernanda"}
clientes_B = {"Lucas", "Ana", "João", "Rita", "Paulo", "Maria"}

# A. Identificar os clientes que estão em ambos os conjuntos
clientes_em_ambos = clientes_A & clientes_B  

# B. Identificar os clientes que estão apenas em clientes_A
clientes_apenas_A = clientes_A - clientes_B  

# C. Identificar os clientes que estão em apenas um dos conjuntos (diferença simétrica)
clientes_apenas_um = clientes_A ^ clientes_B  

# D. Calcular a porcentagem de clientes únicos
# Clientes únicos são aqueles que não estão na interseção
clientes_unicos = len(clientes_A | clientes_B) - len(clientes_em_ambos)
total_clientes = len(clientes_A | clientes_B)
porcentagem_unicos = (clientes_unicos / total_clientes) * 100 if total_clientes > 0 else 0


print(f"Clientes em ambos os conjuntos: {clientes_em_ambos}")
print(f"Clientes apenas em clientes_A: {clientes_apenas_A}")
print(f"Clientes em apenas um dos conjuntos: {clientes_apenas_um}")
print(f"Porcentagem de clientes únicos: {porcentagem_unicos:.2f}%")



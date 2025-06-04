import itertools
import networkx as nx
import matplotlib.pyplot as plt

# Input jumlah titik
jumlah_titik = int(input("Masukkan jumlah titik: "))
titik = [input(f"Nama titik ke-{i+1}: ") for i in range(jumlah_titik)]

# Buat semua pasangan kombinasi titik
pasangan = list(itertools.combinations(titik, 2))

# Input jarak untuk setiap pasangan titik
jarak = {pas: float(input(f"Masukkan jarak dari {pas[0]} ke {pas[1]}: ")) for pas in pasangan}

# Buat graf dan tambahkan sisi-sisi
G = nx.Graph()
G.add_edges_from(jarak.keys())

# posisi titik dan gambar graf
posisi = nx.spring_layout(G)
nx.draw(G, posisi, with_labels=True, node_color='skyblue', edge_color='gray',
        node_size=2000, font_size=12)
nx.draw_networkx_edge_labels(G, posisi, edge_labels=jarak)

plt.title("Visualisasi Kombinasi Titik dan Jarak")
plt.show()
import folium
import requests

# Koordinat (lon, lat) → (x, y)
jakarta = (106.8456, -6.2088)
bandung = (107.6191, -6.9175)

# Hitung jarak dengan OSRM
osrm_url = f"http://router.project-osrm.org/route/v1/driving/{jakarta[0]},{jakarta[1]};{bandung[0]},{bandung[1]}?overview=false"
response = requests.get(osrm_url)
data = response.json()

jarak_m = data['routes'][0]['distance']
durasi_s = data['routes'][0]['duration']

# Bikin peta pakai folium
# Fokus tengahnya di antara Jakarta dan Bandung
peta = folium.Map(location=[-6.6, 107.0], zoom_start=8)

# Tambah marker
folium.Marker(location=[jakarta[1], jakarta[0]], popup='Jakarta').add_to(peta)
folium.Marker(location=[bandung[1], bandung[0]], popup='Bandung').add_to(peta)

# Gambar garis antar titik
folium.PolyLine(
    locations=[
        [jakarta[1], jakarta[0]],
        [bandung[1], bandung[0]]
    ],
    color='blue',
    weight=3,
    popup=f"Jarak: {jarak_m/1000:.2f} km\nDurasi: {durasi_s/60:.2f} menit"
).add_to(peta)

# menambahkan informasi jarak dan durasi ke peta
print(f"jarak dari jakarta ke bandung: {jarak_m/1000:.2f}km")
print(f"durasi perjalanan: {durasi_s/60:.2f} menit")
# Simpan ke file HTML
peta.save("visualisasi_jarak.html")
print("Peta berhasil dibuat: visualisasi_jarak.html")

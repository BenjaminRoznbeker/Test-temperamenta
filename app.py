from flask import Flask, render_template, request

# Definiraj liste
kolerik_lista = [1, 3, 5, 8, 11, 14, 15, 25, 30, 36, 37, 38, 42, 43, 44, 50, 53, 54, 56, 60, 66, 67, 73, 81, 83, 84, 86, 90, 92, 96, 105, 108, 112, 115, 116, 117, 118, 121, 123, 124, 125, 127, 130, 132, 133, 134, 135, 138, 140, 143, 144, 154, 155, 156, 157, 158, 167, 168, 172, 176, 177, 183, 191, 192, 194, 196, 200, 207, 209, 213, 218, 219, 222, 224, 227]
sangvinik_lista = [1, 3, 5, 9, 10, 11, 14, 17, 18, 23, 26, 29, 30, 32, 36, 37, 38, 41, 43, 46, 47, 48, 49, 50, 56, 59, 68, 69, 71, 76, 77, 79, 80, 82, 87, 89, 91, 92, 93, 94, 95, 104, 107, 110, 112, 113, 114, 116, 117, 118, 120, 121, 129, 131, 136, 138, 139, 142, 144, 145, 146, 148, 149, 152, 157, 159, 160, 161, 175, 178, 179, 180, 203, 206, 212, 214, 220, 223, 226, 228, 230, 231]
melankolik_lista = [2, 7, 8, 12, 13, 16, 19, 20, 21, 22, 24, 27, 28, 31, 33, 34, 39, 40, 42, 48, 51, 52, 54, 57, 62, 63, 70, 72, 73, 74, 75, 78, 79, 80, 81, 88, 98, 99, 101, 106, 109, 111, 122, 131, 133, 141, 150, 151, 153, 159, 163, 165, 166, 170, 173, 176, 181, 182, 184, 186, 187, 190, 193, 197, 202, 204, 208, 210, 215, 216, 221, 222, 227]
flegmatik_lista = [2, 4, 6, 9, 10, 21, 26, 28, 30, 31, 35, 39, 45, 52, 55, 58, 61, 63, 64, 65, 68, 70, 72, 75, 78, 85, 88, 97, 98, 100, 102, 103, 106, 107, 110, 111, 113, 119, 122, 126, 128, 129, 131, 137, 139, 147, 153, 160, 162, 166, 169, 171, 173, 174, 175, 185, 186, 188, 189, 195, 198, 199, 201, 204, 205, 206, 210, 211, 215, 217, 219, 221, 225, 226, 228, 232]

# Definiraj funkciju za pronalaženje zajedničkih brojeva
def zajednicki_brojevi(unos_lista):
    zajednicki_kolerik = set(unos_lista) & set(kolerik_lista)
    zajednicki_sangvinik = set(unos_lista) & set(sangvinik_lista)
    zajednicki_melankolik = set(unos_lista) & set(melankolik_lista)
    zajednicki_flegmatik = set(unos_lista) & set(flegmatik_lista)

    return len(zajednicki_kolerik), len(zajednicki_sangvinik), len(zajednicki_melankolik), len(zajednicki_flegmatik)

# Inicijaliziraj Flask aplikaciju
app = Flask(__name__)

# Definiraj rute
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rezultati', methods=['POST'])
def rezultati():
    unos_string = request.form['unos']
    unos_lista = [int(x) for x in unos_string.replace(",", " ").split()]

    rezultati = zajednicki_brojevi(unos_lista)
    najvise_zajednickih = max(range(4), key=lambda i: rezultati[i])

    return render_template('rezultati.html', rezultati=rezultati, najvise_zajednickih=najvise_zajednickih)

# Pokreni aplikaciju
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

kelimeler ={
    "piton":"zehirsiz bir ilan turu",
    "laboratuvar":"deney yapilan yer",
    "sefa":"kayif"
}

while True:
    kelime=input("bir kelime girin")
    if kelime in list(kelimeler.keys()):
        print(kelimeler[kelime])
    else:
        anlami=input("anlamini girin")
        kelimeler[kelime]=anlami
        print(kelime,"sozluge eklendi")
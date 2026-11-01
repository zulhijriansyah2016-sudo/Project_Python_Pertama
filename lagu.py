import time
import sys
lirik = [
    ("Kusangkakan panas berpanjangan"),

    "Rupanya gerimis,"
    "rupanya gerimis mengundang",
    "Dalam tak sedar ku kebasahan",
    "Pernah juga kau pinta perpisahan",
    "Aku sangkakan itu hanyalah gurauan",

    "Nyata kau serius dalam senyuman",

    "Bukan sekejap denganmu",

    "Bukan mainan hasratku",
    "Engkau pun tahu niatku",
    "Tulus dan suci",
    "Senang benar kau ucapkan"
    "Kau anggap itu suratan",
    "Sikit pun riak wajahmu",
    "Tiada terkilan",
    "Hanya aku separuh nyawa",
    "Menahan sebak di dada",
    "Sedangkan kau bersahaja",
    "Berlalu tanpa kata",
    "Terasa diri amat terhina kau lakukan",
    "Terasa diri amat terhina kau lakukan"
]

for baris in lirik:
    for huruf in baris:
        print(huruf,end="",flush=True)
        time.sleep(0.15)
    print()
    time.sleep(1.5)

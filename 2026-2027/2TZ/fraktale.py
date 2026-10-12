#!/usr/bin/env python3
"""
Galeria ładnych fraktali w Pythonie.

Wymagania:  pip install numpy matplotlib

Uruchomienie:
    python fraktale.py            # pokazuje wszystkie fraktale w jednym oknie
    python fraktale.py mandelbrot # pojedynczy fraktal (patrz FRAKTALE niżej)
    python fraktale.py --zapisz   # zapisuje obrazy PNG do folderu ./fraktale_png
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# 1. Zbiór Mandelbrota
# ---------------------------------------------------------------------------
def mandelbrot(szer=1200, wys=800, max_iter=300,
               xmin=-2.2, xmax=0.9, ymin=-1.2, ymax=1.2):
    x = np.linspace(xmin, xmax, szer)
    y = np.linspace(ymin, ymax, wys)
    c = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    z = np.zeros_like(c)
    wynik = np.zeros(c.shape, dtype=float)
    maska = np.ones(c.shape, dtype=bool)

    for i in range(max_iter):
        z[maska] = z[maska] ** 2 + c[maska]
        uciekl = maska & (np.abs(z) > 2)
        # gładkie kolorowanie (smooth coloring) - brak "schodków"
        wynik[uciekl] = i + 1 - np.log2(np.log(np.abs(z[uciekl])))
        maska &= ~uciekl
    wynik[maska] = 0  # punkty należące do zbioru
    return wynik


def rysuj_mandelbrot(ax):
    obraz = mandelbrot()
    # wnętrze zbioru (wartość 0) -> czarne, reszta w skali pierwiastkowej
    maska = np.ma.masked_where(obraz == 0, np.sqrt(obraz))
    cmap = plt.get_cmap("turbo").copy()
    cmap.set_bad("black")
    ax.imshow(maska, cmap=cmap, extent=(-2.2, 0.9, -1.2, 1.2),
              origin="lower")
    ax.set_title("Zbiór Mandelbrota")


# ---------------------------------------------------------------------------
# 2. Zbiór Julii
# ---------------------------------------------------------------------------
def julia(c=-0.8 + 0.156j, szer=1000, wys=1000, max_iter=300, zakres=1.6):
    x = np.linspace(-zakres, zakres, szer)
    y = np.linspace(-zakres, zakres, wys)
    z = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    wynik = np.zeros(z.shape, dtype=float)
    maska = np.ones(z.shape, dtype=bool)

    for i in range(max_iter):
        z[maska] = z[maska] ** 2 + c
        uciekl = maska & (np.abs(z) > 2)
        wynik[uciekl] = i + 1 - np.log2(np.log(np.abs(z[uciekl])))
        maska &= ~uciekl
    return wynik


def rysuj_julia(ax):
    obraz = julia()
    ax.imshow(obraz, cmap="magma", extent=(-1.6, 1.6, -1.6, 1.6),
              origin="lower")
    ax.set_title("Zbiór Julii  (c = -0.8 + 0.156i)")


# ---------------------------------------------------------------------------
# 3. Trójkąt Sierpińskiego (gra w chaos)
# ---------------------------------------------------------------------------
def rysuj_sierpinski(ax, n=200_000):
    wierzcholki = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
    rng = np.random.default_rng(42)
    wybor = rng.integers(0, 3, size=n)

    punkty = np.zeros((n, 2))
    p = np.array([0.3, 0.3])
    for i in range(n):
        p = (p + wierzcholki[wybor[i]]) / 2
        punkty[i] = p

    ax.scatter(punkty[:, 0], punkty[:, 1], c=wybor, s=0.05, cmap="cool")
    ax.set_aspect("equal")
    ax.set_title("Trójkąt Sierpińskiego")


# ---------------------------------------------------------------------------
# 4. Paproć Barnsleya (IFS)
# ---------------------------------------------------------------------------
def rysuj_paproc(ax, n=150_000):
    rng = np.random.default_rng(1)
    los = rng.random(n)
    x, y = 0.0, 0.0
    xs = np.empty(n)
    ys = np.empty(n)

    for i in range(n):
        r = los[i]
        if r < 0.01:
            x, y = 0.0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        xs[i], ys[i] = x, y

    ax.scatter(xs, ys, c=ys, s=0.1, cmap="YlGn", vmin=-4)  # vmin: dół nie znika na białym tle
    ax.set_aspect("equal")
    ax.set_title("Paproć Barnsleya")


# ---------------------------------------------------------------------------
# 5. Płatek śniegu Kocha
# ---------------------------------------------------------------------------
def krzywa_kocha(p1, p2, poziom):
    """Zwraca listę punktów krzywej Kocha między p1 i p2."""
    if poziom == 0:
        return [p1, p2]
    p1, p2 = np.array(p1), np.array(p2)
    d = (p2 - p1) / 3
    a = p1 + d
    b = p1 + 2 * d
    # wierzchołek "czubka" - obrót wektora d o -60 stopni
    kat = -np.pi / 3
    rot = np.array([[np.cos(kat), -np.sin(kat)],
                    [np.sin(kat),  np.cos(kat)]])
    szczyt = a + rot @ d

    wynik = []
    for s, e in [(p1, a), (a, szczyt), (szczyt, b), (b, p2)]:
        czesc = krzywa_kocha(s, e, poziom - 1)
        wynik.extend(czesc[:-1])
    wynik.append(p2)
    return wynik


def rysuj_platek_kocha(ax, poziom=5):
    A = (0.0, 0.0)
    B = (1.0, 0.0)
    C = (0.5, np.sqrt(3) / 2)
    punkty = []
    for s, e in [(A, B), (B, C), (C, A)]:  # obieg przeciwny do ruchu wskazówek: czubki na zewnątrz
        punkty.extend(krzywa_kocha(s, e, poziom)[:-1])
    punkty.append(punkty[0])
    punkty = np.array(punkty)

    ax.fill(punkty[:, 0], punkty[:, 1], color="#bfe3ff", alpha=0.8)
    ax.plot(punkty[:, 0], punkty[:, 1], color="#0b4f8a", lw=0.6)
    ax.set_aspect("equal")
    ax.set_title("Płatek śniegu Kocha")


# ---------------------------------------------------------------------------
# 6. Płonący statek (Burning Ship)
# ---------------------------------------------------------------------------
def rysuj_burning_ship(ax, szer=1200, wys=800, max_iter=300):
    # przybliżenie na "statek" (maszty i kadłub), gdzie widać najwięcej detali
    xmin, xmax, ymin, ymax = -1.80, -1.60, -0.14, 0.02
    x = np.linspace(xmin, xmax, szer)
    y = np.linspace(ymin, ymax, wys)
    c = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    z = np.zeros_like(c)
    wynik = np.zeros(c.shape)
    maska = np.ones(c.shape, dtype=bool)

    for i in range(max_iter):
        zz = z[maska]
        zz = (np.abs(zz.real) + 1j * np.abs(zz.imag)) ** 2 + c[maska]
        z[maska] = zz
        uciekl = maska & (np.abs(z) > 2)
        wynik[uciekl] = i + 1 - np.log2(np.log(np.abs(z[uciekl])))
        maska &= ~uciekl

    # skala pierwiastkowa wyciąga detale; punkty wewnątrz zbioru zostają czarne
    ax.imshow(np.sqrt(wynik), cmap="inferno", extent=(xmin, xmax, ymin, ymax),
              origin="upper", aspect="auto")
    ax.set_title("Płonący statek")


# ---------------------------------------------------------------------------
# Główna część programu
# ---------------------------------------------------------------------------
FRAKTALE = {
    "mandelbrot": rysuj_mandelbrot,
    "julia": rysuj_julia,
    "sierpinski": rysuj_sierpinski,
    "paproc": rysuj_paproc,
    "kocha": rysuj_platek_kocha,
    "statek": rysuj_burning_ship,
}


def pokaz_pojedynczy(nazwa, zapisz=False):
    fig, ax = plt.subplots(figsize=(8, 8))
    FRAKTALE[nazwa](ax)
    ax.axis("off")
    ax.set_title(ax.get_title(), color="black")
    plt.tight_layout()
    if zapisz:
        os.makedirs("fraktale_png", exist_ok=True)
        sciezka = os.path.join("fraktale_png", f"{nazwa}.png")
        fig.savefig(sciezka, dpi=200, bbox_inches="tight")
        print("Zapisano:", sciezka)
        plt.close(fig)
    else:
        plt.show()


def main():
    argumenty = [a for a in sys.argv[1:] if not a.startswith("--")]
    zapisz = "--zapisz" in sys.argv

    if argumenty:
        for nazwa in argumenty:
            if nazwa not in FRAKTALE:
                print(f"Nieznany fraktal: {nazwa}. Dostępne: {', '.join(FRAKTALE)}")
                sys.exit(1)
            pokaz_pojedynczy(nazwa, zapisz)
        return

    if zapisz:
        for nazwa in FRAKTALE:
            pokaz_pojedynczy(nazwa, zapisz=True)
        return

    # wszystkie fraktale w jednym oknie (2 x 3)
    fig, osie = plt.subplots(2, 3, figsize=(18, 11))
    for ax, (nazwa, fun) in zip(osie.ravel(), FRAKTALE.items()):
        fun(ax)
        ax.axis("off")
    fig.suptitle("Galeria fraktali", fontsize=18)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

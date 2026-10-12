#!/usr/bin/env python3
"""
Fraktale KROK PO KROKU - pokazuje, jak fraktal powstaje iteracja po iteracji.

Wymagania:  pip install numpy matplotlib

Uruchomienie:
    python fraktale_krok_po_kroku.py              # menu wyboru fraktala
    python fraktale_krok_po_kroku.py kocha        # od razu wybrany fraktal
    python fraktale_krok_po_kroku.py kocha --zapisz    # kolejne kroki jako PNG
    python fraktale_krok_po_kroku.py kocha --plansza   # wszystkie kroki na jednym obrazie

Sterowanie w oknie:
    strzałka w prawo / spacja / w górę  -> następny krok
    strzałka w lewo / w dół              -> poprzedni krok
    Home / End                           -> pierwszy / ostatni krok
    albo suwak "Krok" na dole
"""

import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.collections import PolyCollection, LineCollection
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


# ---------------------------------------------------------------------------
# 1. Płatek śniegu Kocha
# ---------------------------------------------------------------------------
def koch_punkty(poziom):
    A = np.array([0.0, 0.0])
    B = np.array([1.0, 0.0])
    C = np.array([0.5, np.sqrt(3) / 2])
    pts = [A, B, C, A]                      # trójkąt, obieg przeciwny do wskazówek
    kat = -np.pi / 3                        # czubek rośnie na zewnątrz
    rot = np.array([[np.cos(kat), -np.sin(kat)],
                    [np.sin(kat),  np.cos(kat)]])
    for _ in range(poziom):
        nowe = []
        for p, q in zip(pts[:-1], pts[1:]):
            d = (q - p) / 3
            a = p + d
            b = p + 2 * d
            szczyt = a + rot @ d
            nowe += [p, a, szczyt, b]
        nowe.append(pts[-1])
        pts = nowe
    return np.array(pts)


def rysuj_kocha(ax, k):
    p = koch_punkty(k)
    ax.fill(p[:, 0], p[:, 1], color="#bfe3ff")
    ax.plot(p[:, 0], p[:, 1], color="#0b4f8a", lw=1.2 if k < 5 else 0.5)
    ax.set_xlim(-0.15, 1.15)
    ax.set_ylim(-0.4, 1.05)
    ax.set_aspect("equal")
    if k == 0:
        return "Zaczynamy od trójkąta równobocznego (3 boki)."
    return (f"Każdy bok dzielimy na 3 części, a na środkowej dobudowujemy "
            f"mały trójkąt.  Boków: {3 * 4 ** k}")


# ---------------------------------------------------------------------------
# 2. Trójkąt Sierpińskiego
# ---------------------------------------------------------------------------
def sierpinski_trojkaty(poziom):
    tr = [np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])]
    for _ in range(poziom):
        nowe = []
        for a, b, c in tr:
            ab, bc, ca = (a + b) / 2, (b + c) / 2, (c + a) / 2
            nowe += [np.array([a, ab, ca]),
                     np.array([ab, b, bc]),
                     np.array([ca, bc, c])]
        tr = nowe
    return tr


def rysuj_sierpinski(ax, k):
    tr = sierpinski_trojkaty(k)
    ax.add_collection(PolyCollection(tr, facecolors="#2a6fdb",
                                     edgecolors="#2a6fdb", linewidths=0.3))
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 0.92)
    ax.set_aspect("equal")
    if k == 0:
        return "Zaczynamy od pełnego trójkąta."
    return (f"W każdym trójkącie łączymy środki boków i wycinamy środkowy.  "
            f"Trójkątów: {3 ** k}")


# ---------------------------------------------------------------------------
# 3. Dywan Sierpińskiego
# ---------------------------------------------------------------------------
def dywan(poziom):
    c = np.ones((1, 1), dtype=int)
    for _ in range(poziom):
        z = np.zeros_like(c)
        c = np.block([[c, c, c], [c, z, c], [c, c, c]])
    return c


def rysuj_dywan(ax, k):
    ax.imshow(dywan(k), cmap=ListedColormap(["white", "#7a1fa2"]),
              interpolation="nearest", vmin=0, vmax=1)
    if k == 0:
        return "Zaczynamy od pełnego kwadratu."
    return (f"Każdy kwadrat dzielimy na 9 równych części i usuwamy środkową.  "
            f"Kwadratów: {8 ** k}")


# ---------------------------------------------------------------------------
# 4. Smok Heighwaya (krzywa smoka)
# ---------------------------------------------------------------------------
def smok_punkty(poziom):
    zwroty = []
    for _ in range(poziom):
        # dokładamy zwrot w lewo i lustrzaną kopię poprzednich zwrotów
        zwroty = zwroty + [1] + [-t for t in reversed(zwroty)]
    katy = np.concatenate(([0], np.cumsum(zwroty))) if zwroty else np.array([0])
    kierunki = np.exp(1j * np.pi / 2 * katy)
    return np.concatenate(([0], np.cumsum(kierunki)))


def rysuj_smoka(ax, k):
    p = smok_punkty(k)
    a = np.column_stack([p[:-1].real, p[:-1].imag])
    b = np.column_stack([p[1:].real, p[1:].imag])
    segs = np.stack([a, b], axis=1)
    lc = LineCollection(segs, cmap="plasma", linewidths=1.5 if k < 10 else 0.8)
    lc.set_array(np.linspace(0, 1, len(segs)))
    ax.add_collection(lc)
    srodek = np.array([(p.real.min() + p.real.max()) / 2,
                       (p.imag.min() + p.imag.max()) / 2])   # środek obwiedni
    pol = max(np.ptp(p.real), np.ptp(p.imag), 1.0) / 2 * 1.1
    ax.set_xlim(srodek[0] - pol, srodek[0] + pol)
    ax.set_ylim(srodek[1] - pol, srodek[1] + pol)
    ax.set_aspect("equal")
    if k == 0:
        return "Zaczynamy od jednego odcinka."
    return (f"Dokładamy kopię krzywej obróconą o 90° na jej końcu.  "
            f"Odcinków: {2 ** k}")


# ---------------------------------------------------------------------------
# 5. Drzewo fraktalne
# ---------------------------------------------------------------------------
def drzewo_odcinki(poziom, kat=np.radians(25), skala=0.72):
    odc = []

    def rec(x, y, dl, alfa, g):
        x2 = x + dl * np.cos(alfa)
        y2 = y + dl * np.sin(alfa)
        odc.append(((x, y), (x2, y2), g))
        if g < poziom:
            rec(x2, y2, dl * skala, alfa + kat, g + 1)
            rec(x2, y2, dl * skala, alfa - kat, g + 1)

    rec(0.0, 0.0, 1.0, np.pi / 2, 0)
    return odc


def rysuj_drzewo(ax, k):
    odc = drzewo_odcinki(k)
    cmap = LinearSegmentedColormap.from_list(
        "drzewo", ["#5b3a1a", "#2e8b3d", "#9be15d"])
    segs = [(p, q) for p, q, _ in odc]
    kolory = [cmap(g / max(k, 1)) for _, _, g in odc]
    grub = [0.8 + 5 * 0.78 ** g for _, _, g in odc]
    ax.add_collection(LineCollection(segs, colors=kolory, linewidths=grub,
                                     capstyle="round"))
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-0.1, 3.8)
    ax.set_aspect("equal")
    if k == 0:
        return "Zaczynamy od samego pnia."
    return (f"Na końcu każdej gałęzi wyrastają dwie krótsze (długość × 0,72, "
            f"kąt ±25°).  Gałęzi: {2 ** (k + 1) - 1}")


# ---------------------------------------------------------------------------
# 6. Zbiór Mandelbrota - kolejne iteracje z -> z^2 + c
# ---------------------------------------------------------------------------
ITERACJE_MANDELBROTA = [1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 50, 100, 200]


def mandelbrot_licznik(n, szer=700, wys=500):
    x = np.linspace(-2.2, 0.9, szer)
    y = np.linspace(-1.2, 1.2, wys)
    c = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    z = np.zeros_like(c)
    licz = np.zeros(c.shape, dtype=int)
    for _ in range(n):
        zywe = np.abs(z) <= 2
        z[zywe] = z[zywe] ** 2 + c[zywe]
        licz += np.abs(z) <= 2
    return licz


def rysuj_mandelbrota(ax, k):
    n = ITERACJE_MANDELBROTA[k]
    licz = mandelbrot_licznik(n)
    obraz = np.ma.masked_where(licz == n, licz)   # czarne = jeszcze nie uciekły
    cmap = plt.get_cmap("turbo").copy()
    cmap.set_bad("black")
    ax.imshow(obraz, cmap=cmap, extent=(-2.2, 0.9, -1.2, 1.2),
              origin="lower", vmin=0, vmax=max(n, 2))
    return (f"Po {n} iteracjach z → z² + c.  Czarne punkty jeszcze nie uciekły "
            f"(|z| ≤ 2), kolor = po ilu krokach uciekły.")


# ---------------------------------------------------------------------------
# Rejestr fraktali
# ---------------------------------------------------------------------------
FRAKTALE = {
    "kocha": dict(nazwa="Płatek śniegu Kocha", kroki=7, rysuj=rysuj_kocha),
    "sierpinski": dict(nazwa="Trójkąt Sierpińskiego", kroki=8,
                       rysuj=rysuj_sierpinski),
    "dywan": dict(nazwa="Dywan Sierpińskiego", kroki=6, rysuj=rysuj_dywan),
    "smok": dict(nazwa="Krzywa smoka", kroki=15, rysuj=rysuj_smoka),
    "drzewo": dict(nazwa="Drzewo fraktalne", kroki=11, rysuj=rysuj_drzewo),
    "mandelbrot": dict(nazwa="Zbiór Mandelbrota (iteracje)",
                       kroki=len(ITERACJE_MANDELBROTA),
                       rysuj=rysuj_mandelbrota),
}


# ---------------------------------------------------------------------------
# Tryby pracy
# ---------------------------------------------------------------------------
def pokaz_interaktywnie(klucz):
    f = FRAKTALE[klucz]
    n = f["kroki"]
    fig = plt.figure(figsize=(9, 9.5))
    ax = fig.add_axes([0.05, 0.12, 0.9, 0.78])
    ax_sl = fig.add_axes([0.2, 0.04, 0.6, 0.03])
    slider = Slider(ax_sl, "Krok", 1, n, valinit=1, valstep=1)

    def odswiez(_=None):
        k = int(slider.val) - 1
        ax.clear()
        opis = f["rysuj"](ax, k)
        ax.set_title(f"{f['nazwa']} - krok {k + 1}/{n}\n{opis}", fontsize=11)
        ax.axis("off")
        fig.canvas.draw_idle()

    def klawisz(ev):
        k = int(slider.val)
        if ev.key in ("right", " ", "up"):
            slider.set_val(min(k + 1, n))
        elif ev.key in ("left", "down"):
            slider.set_val(max(k - 1, 1))
        elif ev.key == "home":
            slider.set_val(1)
        elif ev.key == "end":
            slider.set_val(n)

    slider.on_changed(odswiez)
    fig.canvas.mpl_connect("key_press_event", klawisz)
    odswiez()
    plt.show()


def zapisz_kroki(klucz):
    f = FRAKTALE[klucz]
    n = f["kroki"]
    folder = os.path.join("krok_png", klucz)
    os.makedirs(folder, exist_ok=True)
    for k in range(n):
        fig, ax = plt.subplots(figsize=(8, 8.5))
        opis = f["rysuj"](ax, k)
        ax.set_title(f"{f['nazwa']} - krok {k + 1}/{n}\n{opis}", fontsize=10)
        ax.axis("off")
        sciezka = os.path.join(folder, f"krok_{k + 1:02d}.png")
        fig.savefig(sciezka, dpi=120, bbox_inches="tight")
        plt.close(fig)
        print("Zapisano:", sciezka)


def zapisz_plansze(klucz):
    f = FRAKTALE[klucz]
    n = f["kroki"]
    kol = min(n, 4)
    wier = math.ceil(n / kol)
    fig, osie = plt.subplots(wier, kol, figsize=(4 * kol, 4.2 * wier),
                             squeeze=False)
    osie = osie.ravel()
    for ax in osie:
        ax.axis("off")
    for k in range(n):
        f["rysuj"](osie[k], k)
        osie[k].set_title(f"krok {k + 1}", fontsize=10)
        osie[k].axis("off")
    fig.suptitle(f["nazwa"] + " - kolejne kroki", fontsize=16)
    fig.tight_layout()
    sciezka = f"plansza_{klucz}.png"
    fig.savefig(sciezka, dpi=110, bbox_inches="tight")
    plt.close(fig)
    print("Zapisano:", sciezka)


def wybierz_z_menu():
    klucze = list(FRAKTALE)
    print("Wybierz fraktal:")
    for i, kl in enumerate(klucze, 1):
        print(f"  {i}. {FRAKTALE[kl]['nazwa']}  ({kl})")
    try:
        wybor = input("Numer: ").strip()
        return klucze[int(wybor) - 1]
    except (ValueError, IndexError, EOFError):
        print("Nieprawidłowy wybór.")
        sys.exit(1)


def main():
    nazwy = [a for a in sys.argv[1:] if not a.startswith("--")]
    for nazwa in nazwy:
        if nazwa not in FRAKTALE:
            print(f"Nieznany fraktal: {nazwa}. Dostępne: {', '.join(FRAKTALE)}")
            sys.exit(1)
    if not nazwy:
        nazwy = [wybierz_z_menu()] if not (
            "--zapisz" in sys.argv or "--plansza" in sys.argv) else list(FRAKTALE)

    for nazwa in nazwy:
        if "--zapisz" in sys.argv:
            zapisz_kroki(nazwa)
        if "--plansza" in sys.argv:
            zapisz_plansze(nazwa)
        if "--zapisz" not in sys.argv and "--plansza" not in sys.argv:
            pokaz_interaktywnie(nazwa)


if __name__ == "__main__":
    main()

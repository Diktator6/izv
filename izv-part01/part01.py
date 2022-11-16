#!/usr/bin/env python3
"""
IZV cast1 projektu
Autor: 

Detailni zadani projektu je v samostatnem projektu e-learningu.
Nezapomente na to, ze python soubory maji dane formatovani.

Muzete pouzit libovolnou vestavenou knihovnu a knihovny predstavene na prednasce
"""


from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt
from typing import List


def integrate(x: np.array, y: np.array) -> float:
    # Ziskani x hodnot rovnice pro sumu
    ix = x[1::] - x[:-1:]

    # Ziskani y hodnot rovnice pro sumu s vyuzitim broadcastingu pro / 2
    iy = (y[1::] + y[:-1:]) / 2

    # Vraceni sumy nasobku mezivysledku
    return np.sum(ix * iy)


def generate_graph(a: List[float], show_figure: bool = False, save_path: str | None=None):
    b =  np.linspace(-3, 3, 50).reshape(-1, 1)

    a += b

    plt.plot(b, a[:,0] * b ** 2, c="tab:blue")
    plt.plot(b, a[:,1] * b ** 2, c="tab:orange")
    plt.plot(b, a[:,2] * b ** 2, c="tab:green")
    plt.xlabel("x")
    plt.ylabel("fa(x)")
    
    if show_figure:
        plt.show()
    
    if save_path:
        plt.savefig(save_path)

def generate_sinus(show_figure: bool=False, save_path: str | None=None):
    pass


def download_data(url="https://ehw.fit.vutbr.cz/izv/temp.html"):
    # Ziskani html dokumentu
    htmlObj = requests.get(url)

    # Ziskani BS objektu
    soup = BeautifulSoup(htmlObj.text, 'html.parser')

    # Vytvoreni vysledneho seznamu
    res_list = list()

    odd_months = (1,3,5,7,8,10,12)
    even_months = (4,6,9,11)

    # Cyklus prochazejici radky tabulky
    for row in soup.find_all("tr"):
        # Zjisteni roku
        ptr = row.td
        year = int(ptr.text)
        # Zjisteni mesice
        ptr = ptr.next_sibling.next_sibling
        month = int(ptr.text)

        # Zjisteni dnu v mesici
        if month in odd_months:
            days = 31
        elif month in even_months:
            days = 30
        elif month == 2 and year % 4 == 0:
            days = 29
        else:
            days = 28
        
        # Vytvoreni prazdneho np pole
        temp = np.empty([days])
        
        # Nahrani hodnot teplot do np pole
        for i in range(days):
            ptr = ptr.next_sibling.next_sibling
            temp[i] = float(ptr.text.replace(",", "."))
        
        res_list.append({"year": year, "month": month, "temp": temp}) 
    
    # Vraceni vysledneho pole
    return res_list


def get_avg_temp(data, year=None, month=None) -> float:
    # pomocne
    result = 0.0
    rows = 0

    # 4 varianty 
    if year == None and month == None:
        for row in data:
            result += np.sum(row["temp"])
            rows += row["temp"].size
    elif year != None and month != None:
        for row in data:
            if year == row["year"] and month == row["month"]:
                result += np.sum(row["temp"])
                rows += row["temp"].size
    elif year != None and month == None:
        for row in data:
            if year == row["year"]:
                result += np.sum(row["temp"])
                rows += row["temp"].size
    else:
        for row in data:
            if month == row["month"]:
                result += np.sum(row["temp"])
                rows += row["temp"].size

    # kontrola deleni nulou a vraceni vysledku
    if rows != 0:
        return result.round(1) / rows
    else:
        float("NaN")

generate_graph([1., 2., -2.], show_figure=True, save_path="tmp_fn.png")
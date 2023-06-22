#/bin/python
# -*- coding: utf-8 -*-
import os
import random
import sys


global debug 
debug = False

def main():
    global debug
    argumentit = argumentti_check()

    ruokalista = check_lista()
    if len(ruokalista) > 0:
        pass
    else:
        if debug:
            print("Ruokalistaa ei ollut, nyt on")
    
    lisaa_generoi = input("Generoi lista (g) / laita esineitä (l) / + Arki (a) / Viikonloppu (v), esim (ga) => generoi viikolopulle")
    if (lisaa_generoi[0] == "g" or lisaa_generoi[0] == "l") and (lisaa_generoi[2] == "a" or lisaa_generoi[2] == "v"):
        rivinvaihto_indeksi = 0
        for esine in ruokalista:
            if esine == "\n":
                break
            else:
                rivinvaihto_indeksi += 1
        arki_ruokien_pituus = rivinvaihto_indeksi - 1
        vklp_ruokien_pituus = len(ruokalista) - arki_ruokien_pituus - 1
        arki_ruoat = ruokalista[1:rivinvaihto_indeksi]

        if lisaa_generoi[0] == "g" and lisaa_generoi[1] == "a":
            print("Arjen ruuat voisi olla: ")
            ei_samoja[arki_ruokien_pituus]
            
            for esine in ruokalista:
                 ei_samoja.append(esine)



        if else lisaa_generoi[0] == "g" and lisaa_generoi[1] == "v":
            viikonloppu_indeksi = 
            ei_samoja[len(ruokalista)]
        if else lisaa_generoi[0] == "l" and lisaa_generoi[1] == "a":
            arki = True
        if else lisaa_generoi[0] == "l" and lisaa_generoi[1]:
            viikonloppu = true
        

        rivinvaihto = ""

        viikoloppu_indeksi = 0
        for esine in ruokalista_in:
            if lisaa_generoi[2] 
            

def check_lista():
    workdir = os.getcwd()
    try:
        lista = open(workdir + "/ruokalista.txt", "r")
        return lista_in
 
    except:
        lista = open(workdir + "/ruokalista.txt", "w")
        lista.write("ARKI\n")
        lists.write("\n")
        lista.write("VIIKONLOPPU\n")
        lista.close()
        return -1, lista_in

def argumentti_check():
    global debug
    argumentit = sys.argv[]
    for argumentti in argumentit:
        if argumentti == ["debug"]:
            debug = True
            print("Debug mode on")
            for i in argumentit[:]:
                if i.find("debug".lower()) != -1:
                    argumentit.remove[i]
                    

        if argumentti == ["help"] or len(argumentti) < 2:
            tulosta_opas()
            exit(1)


main()

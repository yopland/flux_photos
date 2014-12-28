#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, sys, os.path

dossierJpeg = "jpeg"
dossierRaw = "nef"
dossierDev = "dev"

extentionRaw = ".nef"
extentionJpeg = ".jpg"



#
# Affiche un texte d'aide
#
def afficherAide():
    print("Précisez une action en paramètre")
    print("dossier  : création des dossier 'jpeg', 'nef' et 'dev'. Les photos sont déplacés dans l'un des dossiers en fonction de l'extention. Le dossier 'dev' destiné à recevoir les développments reste initalement vide")
    print("dev : développer les photos")



#
# Création des dossiers
#
def creationDossier():
  if (not os.path.isdir(dossierJpeg)):
    os.mkdir(dossierJpeg)
  if (not os.path.isdir(dossierRaw)):
    os.mkdir(dossierRaw)
  if (not os.path.isdir(dossierDev)):
    os.mkdir(dossierDev)
    
  for fichier in os.listdir('.'):
    nomFichier, extFichier = os.path.splitext(fichier)
    if extFichier == extentionRaw:
      nom=dossierRaw + "/" + fichier
      print (nom)
      os.renames(fichier, nom )
    if extFichier == extentionJpeg:
      nom=dossierJpeg + "/" + fichier
      print (nom)
      os.renames(fichier, nom )

def devDossier():
  for fichier in os.listdir('./nef'):
    nomFichier, extFichier = os.path.splitext(fichier)
    print ("développement de '" + nomFichier + "'")
    cmd = "darktable-cli " + "nef/" + nomFichier + ".nef" + " dev/" + nomFichier + ".jpg"
    os.system(cmd)   




#
# Programme principal
#
if __name__ == "__main__":
  if len(sys.argv) < 2:
    afficherAide()
    sys.exit(1)
  
  action = sys.argv[1]
  if action == "dossier":
    print("Création des différents dossiers")
    creationDossier()
  elif action == "renommer":
    print("Modifie le nom du dossier en fonction du fichier .nfo présent dans le dossier")
    renommerDossier()
  elif action == "dev":
    print("Développe les photos présentes dans le dossier nef vers le dossier dev")
    devDossier()
  else:
    afficherAide()

# mandelbrot

## Table of content
- [mandelbrot](#mandelbrot)
  - [Table of content](#table-of-content)
  - [Context](#context)
    - [Introduction](#introduction)
    - [Tasks](#tasks)
  - [Getting started](#getting-started)
    - [Install](#install)
    - [Use](#use)
    - [Differents fractals](#differents-fractals)
      - [Triangle de Sierpiński](#triangle-de-sierpiński)
      - [Ensemble de Mandelbrot](#ensemble-de-mandelbrot)
      - [Ensemble de Julia](#ensemble-de-julia)
      - [Flocon de neige de Koch](#flocon-de-neige-de-koch)
      - [Burning ship](#burning-ship)
    - [Team](#team)

## Context
### Introduction
### Tasks

## Getting started
### Install
- Open git bash
```bash
# Clone repository
git clone https://github.com/christian-aucane/mandelbrot.git

# Move in the repository folder
cd manbelbrot

# Create virtual environment and install dependancies
source scripts/install.sh
```

### Use
- Open git bash
```bash
# Activate virtual environment and run application
source scripts/run.sh
```

### Differents fractals 

Une figure fractale est un objet mathématique qui présente une structure similaire à toutes les échelles.

C'est un objet géométrique « infiniment morcelé » dont des détails sont observables à une échelle arbitrairement choisie. En zoomant sur une partie de la figure, il est possible de retrouver toute la figure ; on dit alors qu’elle est « autosimilaire ».

#### Triangle de Sierpiński

Le triangle de Sierpiński est une fractale, du nom de Wacław Sierpiński qui l'a décrit en 1915.
Il peut s'obtenir à partir d'un triangle « plein », par une infinité de répétitions consistant à diviser par deux la taille du triangle puis à les accoler en trois exemplaires par leurs sommets pour former un nouveau triangle. À chaque répétition le triangle est donc de même taille, mais « de moins en moins plein ».

#### Ensemble de Mandelbrot

L'ensemble de Mandelbrot, une fractale construite par une relation de récurrence, liant des nombres complexes entres-eux.

#### Ensemble de Julia

L'ensemble de Julia est essentiellement caractérisé par le fait qu'une petite perturbation au départ se répercute en un changement radical de cette suite (chaos).

#### Flocon de neige de Koch

La courbe de Koch est la limite des courbes obtenues lorsqu’on répète indéfiniment les étapes précédentes. Le flocon de Koch s’obtient de la même façon, sauf que l’on ne part pas d’un segment, mais d’un triangle équilatéral. Le nom provient du fait qu’après quelques itérations, on obtient une figure ressemblant à un flocon de neige.

#### Burning ship

Fractale burning ship La fractale burning ship (« navire en feu », en anglais), décrite pour la première fois par Michael Michelitsch et Otto E. Rössler en 1992, est générée dans le plan complexe par la fonction itérée suivante : La fractale est définie par l'ensemble des points ne divergeant pas à l'infini.

### Team
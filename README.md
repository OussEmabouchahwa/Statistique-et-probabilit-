# 📊 TP Mathématiques : Probabilités & Optimisation Linéaire

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![PuLP library](https://img.shields.io/badge/solvers-PuLP-orange.svg?style=flat-square)](https://coin-or.github.io/pulp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Ce dépôt rassemble les travaux pratiques (TP) de mathématiques appliquées, structurés autour de deux grands axes :
1. **Simulations Probabilistes & Combinatoire** (Méthode de Monte-Carlo, tirages combinatoires, jeux stochastiques).
2. **Optimisation Sous Contraintes & Programmation Linéaire** (Résolution de problèmes industriels à l'aide de la bibliothèque `PuLP`).

---

## 📂 Structure du Projet

```text
├── 📁 tp3/                           # Partie Optimisation Linéaire (Programmation Linéaire)
│   ├── ex1.py                        # Optimisation de production de véhicules (Grande vs Petite)
│   ├── Ex4.py                        # Optimisation de production d'une multinationale de bonbons
│   └── ex5.py                        # Allocation de ressources & planification d'ameublement
├── 📁 part2/                         # Captures d'écrans & illustrations de la Partie 2
├── 📁 part3/                         # Captures d'écrans & illustrations de la Partie 3
├── 📄 ex1.py                         # Modélisation simple d'une classe (Filles / Garçons)
├── 📄 ex2.py                         # Jeu de score aléatoire
├── 📄 ex3.py                         # Simulation du jeu stochastique "La Tortue et le Lapin"
├── 📄 ex4.py                         # Simulation de Monte-Carlo (1000 tirages de genre)
├── 📄 ex6.py                         # Loi de probabilité sur le lancer de deux dés simultanés
├── 📄 ex7.py                         # Analyse combinatoire exacte de tirages dans une urne
├── 📄 ProjetMath Oussema bouchahwa.docx # Rapport académique complet du projet
└── 📄 README.md                      # Présentation et documentation du projet (ici présent)
```

---

## 🎲 Partie 1 : Simulations & Calculs de Probabilités

Cette première partie utilise Python pour modéliser des situations réelles de probabilités, comparer les fréquences empiriques aux probabilités théoriques et manipuler l'analyse combinatoire.

### 👥 1. Modélisation de Classes & Loi des Grands Nombres (`ex1.py` & `ex4.py`)
* **Scénario :** Une classe de 23 élèves composée de 10 filles (marquées `f1` à `f10`) et 13 garçons (`g1` à `g13`).
* **Méthodologie :**
  - Sélection aléatoire via `random.choice`.
  - Évaluation de la probabilité empirique simple.
  - **Loi des grands nombres (`ex4.py`) :** Simulation répétée sur **1000 tirages** pour calculer la fréquence limite d'apparition des filles et valider la convergence vers la probabilité théorique ($P(F) \approx 0.4348$).

---

### 🏆 2. Course Aléatoire : La Tortue et le Lapin (`ex3.py`)
* **Principe :** Simulation du célèbre jeu probabiliste de la course.
  - À chaque tour, on lance un dé à 6 faces.
  - Si le **Lapin** obtient un $6$, il gagne instantanément la course.
  - Si le dé donne un chiffre de $1$ à $5$, la **Tortue** avance d'une case. La Tortue doit avancer de 6 cases pour gagner.
* **Intérêt mathématique :** Étude d'un processus stochastique à arrêt précoce. La probabilité que le lapin gagne est de $1 - (5/6)^6 \approx 66.5\%$, tandis que celle de la tortue est de $(5/6)^6 \approx 33.5\%$.

---

### 🎲 3. Lancers de Dés et Événements Composés (`ex6.py`)
* **Scénario :** Lancement simultané de deux dés équilibrés à 6 faces sur 100 itérations.
* **Mesures effectuées :**
  - Probabilité d'obtenir un **double** (ex: $(2,2)$, $(5,5)$).
  - Probabilité d'obtenir deux **chiffres pairs**.
  - Probabilité de l'union des événements (Double **ou** Pair).

---

### 🔮 4. Analyse Combinatoire Rigoureuse avec Urnes (`ex7.py`)
* **Scénario :** Une urne contient **4 boules blanches** et **5 boules noires**. On effectue un tirage simultané de **3 boules** sans remise.
* **Méthodologie :** Utilisation du module `itertools.combinations` pour générer l'univers complet des possibles ($\Omega$, cardinal de $\binom{9}{3} = 84$ tirages distincts).
* **Calculs exacts programmés :**
  - $P(\text{3 boules blanches}) = \frac{\binom{4}{3}}{\binom{9}{3}} = \frac{4}{84} \approx 4.76\%$
  - $P(\text{3 boules de couleurs différentes/non monochromes}) = \frac{70}{84} \approx 83.3\%$
  - $P(\text{Au moins 2 boules blanches}) = \frac{\binom{4}{2}\binom{5}{1} + \binom{4}{3}\binom{5}{0}}{84} = \frac{34}{84} \approx 40.48\%$
  - Probabilité que l'index de toutes les boules tirées soit pair.

---

## 📈 Partie 2 : Programmation & Optimisation Linéaire (`📁 tp3`)

L'optimisation sous contraintes est implémentée avec la bibliothèque **PuLP**, permettant de modéliser des équations mathématiques de maximisation de profit sous contraintes de ressources matérielles et temporelles.

### 🚗 Exercice 1 : Production Automobile Optimale
* **Objectif :** Maximiser le profit d'une usine produisant deux types de véhicules.
  - **Variables :** $X$ (Grandes voitures), $Y$ (Petites voitures).
  - **Fonction Objectif (Profit) :** $\max (16000X + 10000Y)$
  - **Contraintes de ressources :**
    - Caoutchouc : $X + Y \le 400$
    - Acier : $2X + Y \le 600$
    - Non-négativité : $X \ge 0, Y \ge 0$

---

### 🍬 Exercice 4 : Rentabilité d'une Confiserie
* **Objectif :** Maximiser le profit de fabrication de trois gammes de bonbons ($A, B, C$).
  - **Fonction Objectif :** $\max (24X + 40Y + 9Z)$
  - **Contraintes de fabrication :**
    - Temps machine : $500X + 200Y + 1000Z \le 500$
    - Temps main-d'œuvre : $\frac{1}{25}X + \frac{1}{10}Y + \frac{1}{50}Z \le 45$

---

### 🗄️ Exercice 5 : Gestion d'Atelier d'Ameublement
* **Objectif :** Résolution d'un problème d'ordonnancement et d'affectation pour la production de cabinets ($X$), bureaux ($Y$) et étagères ($Z$) sous double contrainte d'équipes de maintenance/nettoyage.

---

## 🚀 Installation & Utilisation

### 🔧 Prérequis

Assurez-vous d'avoir Python 3.8+ d'installé. Installez le solveur d'optimisation linéaire `PuLP` via pip :

```bash
pip install pulp
```

### 💻 Exécution des Scripts

Pour lancer une simulation de probabilité :
```bash
python ex7.py
```

Pour exécuter un modèle d'optimisation linéaire :
```bash
python tp3/ex1.py
```

---

## 📊 Résultats & Visualisations

Les répertoires `📁 part2` et `📁 part3` contiennent des captures graphiques exhaustives des arbres de probabilités, des régions réalisables d'optimisation (méthode graphique) et des logs d'exécution des différents algorithmes.

> [!NOTE]
> Pour une analyse plus formelle avec les démonstrations théoriques complètes rédigées, veuillez consulter le fichier Word : [ProjetMath Oussema bouchahwa.docx](file:///c:/Users/ousse/OneDrive/Desktop/COURS/tp%20math/ProjetMath%20Oussema%20bouchahwa.docx).

---

## 👥 Auteur
* **Oussema Bouchahwa** - *Étudiant en Informatique & Mathématiques*
### Question 1
**Quel est le facteur de branchement du jeu représenté sur l’arbre ci-dessus ? Toutes les branches d’un arbre de jeu doivent-elles être de la même hauteur ?**

- **Facteur de branchement** : 2.
- **Hauteur des branches** : Non, toutes les branches d'un arbre de jeu ne doivent pas nécessairement être de la même hauteur. Cela dépend de la structure du jeu et des règles qui déterminent les mouvements possibles à chaque étape.

### Question 2
**Sans tenir compte de la feuille ayant une valeur de “ ? ?”, quelle est le meilleur plateau pour Ami ? Quel est le meilleur plateau pour Ennemi ? Expliquez le fait que deux nœuds de l’arbre aient un seul fils. Est-ce plutôt une bonne chose ou une mauvaise chose pour ami ?**

- **Meilleur plateau pour Ami** :  8
- **Meilleur plateau pour Ennemi** : -4, mais y'en a deux.
- **Nœuds avec un seul fils** : Si un nœud a un seul fils, cela signifie qu'il n'y a qu'un seul mouvement possible à partir de ce nœud. Cela peut être une bonne chose si ce mouvement est avantageux pour Ami, mais cela peut aussi être une mauvaise chose si ce mouvement est défavorable.
- **Impact pour Ami** : Cela dépend des valeurs des feuilles. Si le seul fils conduit à une feuille avec une valeur élevée, c'est bon pour Ami. Sinon, c'est mauvais.

### Question 3
**Donnez la plus grande valeur possible pour la feuille ayant la valeur heuristique notée “ ?” et permettant à α-β d’élaguer la feuille 8. Vous utiliserez cette valeur pour la suite du sujet ;**

- **Valeur heuristique “ ?”** : 3

### Question 4
**Déroulez alpha-béta classique sur ce même arbre de jeu : Attention, vous ferez bien figurer sur votre solution les coupes effectuées et l’évolution éventuelle des valeurs α et β au cours de la recherche ;**

- **Algorithme α-β** : L'algorithme α-β est une amélioration de l'algorithme minimax qui permet de réduire le nombre de nœuds à explorer en élaguant les branches qui ne conduiront pas à une meilleure solution.
- **Déroulement** : Vous devez suivre l'algorithme α-β en commençant par la racine de l'arbre et en explorant les nœuds en profondeur. À chaque nœud, vous devez mettre à jour les valeurs α (meilleure valeur trouvée pour Ami) et β (meilleure valeur trouvée pour Ennemi). Lorsque α ≥ β, vous pouvez élaguer la branche actuelle.
- **Coupes et évolution des valeurs** : Vous devez noter chaque fois que vous effectuez une coupe et comment les valeurs α et β évoluent au cours de la recherche.

J'espère que cela clarifie les questions posées. Si vous avez besoin de plus de détails ou d'explications supplémentaires, n'hésitez pas à demander !
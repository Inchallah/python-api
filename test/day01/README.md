Pré-requisite

Créer kubernetes sur gcp

Envoyer les yaml à mon repo albertq va lire avec ses beaux yeux

Faire un dossier par achievement

Object :

[]

Déployer un pod avec le nom "test-pod-01"

    configurer son port
    image docker à mettre dans le pod
    configurer les probs

    ne pas configuer le service account
                     le resource

déployer sur le namespace "default"

```bash
kubectl get pod -n default -> affiche test-pod-01
```

[]

Créer un namespace "test-ns-01"

Déployer pod précédent dans le namespace

```bash
kubectl get pod/test-pod-01 -o yaml -n test-ns-01
```

[]

Créer un deployment de mon application "python-docker"

    Ne pas configuer service account

    Ne pas configuer les resources

Mettre le Deployment nommé "test-dep-01" dans le namespace "test-ns-02"

    contient les memes specificités que le pod achievement 1

    Ne pas configuer les security / service account / resource

4 replica de mon application "python-docker"

Resultat :

```bash
kubectl get deployment/test-dep-01 -o yaml -n test-ns-02

kubectl get pod -n test-ns-02
```
> Vérifier qu'il y a bien 4 pods


[]

Créer un service de type "Internal IP" nommé "test-dep-01"

    pointe vers le Déployment "test-dep-01" "test-ns-02"

Resultat :


Term 1
```bash
kubectl port-forward service/test-dep-01 5000:5000 -n test-ns-02
```

Term 2
```bash
curl 127.0.0.1:5000/prout/albertq
```
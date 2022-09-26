Pré-requisite

Créer kubernetes sur gcp

node-pool info :
    - nom test-pool-01
    - machine e2 small
    - 2 nodes
    - vm spot

Envoyer les yaml à mon repo albertq va lire avec ses beaux yeux

Faire un dossier par achievement

[*] Déployer un pod avec le nom "test-pod-01"

>configurer son port

>image docker à mettre dans le pod

>configurer les probes


```bash
kubectl apply -f task/day01/task01/createPod.yaml

kucetl get pod test-pod-01 -o yaml > task/day01/task01/podStatus.yaml
```


[*] Créer un namespace "test-ns-01"

Déployer pod précédent dans le namespace

```bash
kubectl apply -f task/day01/task02/createNamespace.yaml
kubectl apply -f task/day01/task02/createPod.yaml

kubectl get namespaces test-ns-01 -o yaml > task/day01/task02/namespaceStatus.yaml
kubectl -n test-ns-01 get pods test-pod-01 -o yaml > task/day01/task02/podStatus.yaml
```

[*] Créer un deployment de mon application "python-docker"

Ne pas configuer service account

Ne pas configuer les resources

Mettre le Deployment nommé "test-dep-01" dans le namespace "test-ns-02"

contient les memes specificités que le pod achievement 1

Resultat :

```bash
kubectl apply -f task/day01/task03/createNamespace.yaml
kubectl apply -f task/day01/task03/createDeployment.yaml

kubectl get namespaces test-ns-02 -o yaml > task/day01/namespaceStatus.yaml
kubectl -n test-ns-02 get deployment test-dep-01 -o yaml > task/day01/namespaceStatus.yaml
```

[*] Créer un service de type "Cluster IP" nommé "test-service"

pointe vers le Déployment "test-dep-02" "test-ns-02"

Resultat :

Term 1
```bash
kubectl apply -f task/day01/task04/createService.yaml
kubectl apply -f task/day01/task04/createDeployment.yaml

kubectl -n test-ns-02 get services test-service -o yaml > task/day01/task04/serviceStatus.yaml

kubectl -n test-ns-02 get deployments.app test-dep-02 -o yaml > task/day01/task04/serviceStatus.yaml


kubectl -n test-ns-02 port-forward services/test-service 5000:5000
```

Term 2
```bash
curl 127.0.0.1:5000/prout/albertq
```

[] Une route python doit renvoyer un envar local, un envar configmap et un envar secret



Probes :

Probe startup -> Node lancé ?

Probe readiness -> Node lancé, app ready ?

Probe lifecycle -> Node lancé, app ready, working ?

# riso_d1
RISO domaci 1 docker-kubernetes
## Proces izrade
1. Prvo je testiran flask server uz pomoc Insominia programa, a nakon toga je napravljena prosta client skripta koja salje 3 POST request-a.
2. Nakon testiranja napravljeni su Dockerfile-ovi za client i server i onda istestirani


![Docker_test](https://github.com/markoMaksimovic1419S/riso_d1/blob/main/slike/docker_testiranje.png?raw=true)

*** Ovo testiranje je odradjeno na localhost-u, ali sam kasnije to promenio zbog problema sa k8s-om ***

3. Docker image sam upload na docker hub (mmaksimovic1419s/dcr_server i mmaksimovic1419s/dcr_client)
4. Nakon toga kreirani su deploy i service yaml fajlovi, postavljeni kao loadbalancer sa portovima 8081 i koriscene su image sa hub-a

![Docker_test](https://github.com/markoMaksimovic1419S/riso_d1/blob/main/slike/kubernetes_testiranje.png?raw=true)

6. Prilikom testiranja sam enable metalib za ip range 192.168.1.5 - 192.168.1.5 (moj laptop) kako bih imao external ip i istestirao

![Docker_test](https://github.com/markoMaksimovic1419S/riso_d1/blob/main/slike/kubernetes_insomnia.png?raw=true)

*** Takodje sam i u client skripti to zamenio, pa obratiti paznju prilikom testiranja na drugoj masini ***

        

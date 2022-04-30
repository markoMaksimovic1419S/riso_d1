# riso_d1
RISO domaci 1 docker-kubernetes
## Proces izrade
1. Prvo je testiran flask server uz pomoc Insominia programa, a nakon toga je napravljena prosta client skripta koja salje 3 POST request-a.
2. Nakon testiranja napravljeni su Dockerfile-ovi za client i server i onda istestirani

    *** Ovo testiranje je odradjeno na window-u, ali sam kasnije presao na linux zbog problema sa k8s-om, na windows-u sam koristio localhost ***

3. Docker image sam upload na docker hub (mmaksimovic1419s/dcr_server i mmaksimovic1419s/dcr_client)
4. Nakon toga kreirani su deploy i service yaml fajlovi, postavljeni kao loadbalancer sa portovima 8081 i koriscene su image sa hub-a
5. Prilikom testiranja sam enable metalib za ip range 192.168.1.5 - 192.168.1.5 (moj laptop) kako bih imao external ip i istestirao
    *** Takodje sam i u client skripti to zamenio, pa obratiti paznju prilikom testiranja na drugoj masini ***
        

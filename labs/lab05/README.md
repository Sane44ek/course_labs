<div align="center">
<h1><a id="intro">Лабораторная работа №5</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Чередова.А.С.-8b9aff" alt="Contributor Badge"></a></div>

***

Данная лабораторная работа посвещена изучению Docker и как с ним работать. Эта лабораторная работа послужит подпоркой для старта в выявлении и определении уязвимостей на уровне сканирования контейнеров при сборке приложений. 

***

## Задание

- [ ] 1. Поставьте `Docker` и `buildkit`

```bash
$ brew install buildkit
$ brew install docker
```

- [ ] 2. Перейдите в `source` и выведите на терминале, далее проанализируйте следующие команды консоли

```bash
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$  docker buildx build -t hellow-appsec-world .
[+] Building 29.7s (13/13) FINISHED                                    docker:default
 => [internal] load build definition from Dockerfile                             0.1s
 => => transferring dockerfile: 443B                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.11-slim              7.0s 
 => [internal] load .dockerignore                                                0.0s
 => => transferring context: 2B                                                  0.0s 
 => [internal] load build context                                                0.1s 
 => => transferring context: 494B          
 
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker run hellow-appsec-world
hello appsec world

acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker run --rm -it hellow-appsec-world
hello appsec world

$ docker save -o hello.tar hello-appsec-world
$ docker load -i hello.tar
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker load -i image.tar
f1b30ab99183: Loading layer  30.14MB/30.14MB
c24001014542: Loading layer  1.274MB/1.274MB
7a4b2171e46d: Loading layer  14.31MB/14.31MB
591779db3273: Loading layer     250B/250B
efd49302dd30: Loading layer      95B/95B
8fe7432c3de3: Loading layer      96B/96B
e687a26fd0a6: Loading layer     141B/141B
71299f61dc2b: Loading layer  4.065MB/4.065MB
5b8b2e16a223: Loading layer     344B/344B
Loaded image: hello-appsec-world:latest

```
- [ ] 3. Откройте `Dockerfile` и сделайте его анализ. Сделайте `commit`
```dockerfile
# Этап 1: сборка зависимостей
FROM python:3.11-slim AS builder
WORKDIR /hello
# Копируем файл с зависимостями
COPY requirements.txt . 
# Устанавливаем зависимости в отдельную директорию wheelhouse для кеширования
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

# Этап 2: запускаемый образ
FROM python:3.11-slim
WORKDIR /hello
# Копируем файл с зависимостями
COPY --from=builder /wheels /wheels # Копируем собранные wheel-пакеты
COPY requirements.txt . 
# Устанавливаем зависимости из wheel-пакетов
RUN pip install --no-index --find-links=/wheels -r requirements.txt
# Копируем исходный код приложения
COPY hello.py .

# Переменные окружения для улучшенной работы Python
ENV PYTHONUNBUFFERED=1
# Запускаем приложение
CMD ["python", "hello.py"] 

acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ git add Dockerfile
warning: in the working copy of 'labs/lab05/source/Dockerfile', CRLF will be replaced by LF the next time Git touches it
                                                                                      
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ git commit -m "lab5: analyse original Dockerfile"
[develop 7db8bfa] lab5: analyse original Dockerfile
 1 file changed, 14 insertions(+), 5 deletions(-)
```

- [ ] 4. Замените в `Dockerfile`значение скрипта на `python` тем, который вы сделали ранее в прошлых лабораторных работах. Вложите свой файл `python` в директорию. Сделайте анализ своего измененного `Dockerfile` и внесите изменения. Сделайте `commit`. 

```py
import base64
import typer


def main(
    name: str = typer.Argument(...),
    lastname: str = typer.Option("", "--lastname", "-l"),
) -> None:
    greeting = base64.b64decode(b"SGVsbG8gYXBwc2Vjd29ybGQ=").decode()
    tail = f"@{name}" + (f" {lastname}" if lastname else "")
    typer.echo(f"{greeting} from {tail}")


if __name__ == "__main__":
    typer.run(main)
# test comment
```
```
git add hello.py                                 
                                                                                      
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ git commit -m "lab5: use custom hello.py & multi-stage build"
[develop 06eaa22] lab5: use custom hello.py & multi-stage build
 1 file changed, 11 insertions(+), 12 deletions(-)

```

- [ ] 5. Выведите на терминале и проанализируйте следующие команды консоли. Сравните хеш сумму вашего архива с `image.tar` из репозитория, выведите на терминал.

```bash
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker buildx build -t hellow-appsec-world .
[+] Building 21.2s (13/13) FINISHED                                    docker:default
 => [internal] load build definition from Dockerfile                             0.0s
 => => transferring dockerfile: 599B                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.11-slim              0.6s 
 => [internal] load .dockerignore                                                0.0s
 => => transferring context: 2B                                                  0.0s 
 => [internal] load build context                                                0.0s 
 => => transferring context: 89B                                                 0.0s 
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2c  0.0s 
 => CACHED [builder 2/4] WORKDIR /hello                                          0.0s 
 => [builder 3/4] COPY requirements.txt .                                        0.1s 
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/whee  11.9s 
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                            0.1s 
 => [stage-1 4/6] COPY requirements.txt .                                        0.2s 
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requiremen  6.8s 
 => [stage-1 6/6] COPY hello.py .                                                0.2s 
 => exporting to image                                                           0.6s 
 => => exporting layers                                                          0.5s 
 => => writing image sha256:afb8b0b473de9b1f67b6a85142dc96e9a074d880894da14da61  0.0s 
 => => naming to docker.io/library/hellow-appsec-world                           0.0s 
                                                                                      
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker run hello-appsec-world
Hello appsecworld from @None
                                    
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker save -o hello_your_project.tar hellow-appsec-world

acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ sha256sum hello_your_project.tar
2b68afa6441e89acd92bc623e9b98c90c943f199ae96efeabb130612c0ef4625  hellow_your_project.tar

acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker load -i hello_your_project.tar 
Loaded image: hellow-appsec-world:latest
                                     
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker run hellow-appsec-world       
Hello appsecworld from @None

$ docker load -i image.tar
$ docker run hello-appsec-world
$ sha256sum image.tar         


```

- [ ] 6. Доработайте свой `python` скрипт подключаемыми библиотеками, далее их необходимо разместить в `requirements.txt`. Размещение библиотек в следующем формате:

```
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ cat > requirements.txt <<'EOF'
flask==2.2.3
requests==2.28.1
typer==0.12.5
EOF
```

```py
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name   = request.args.get("name",   default="user", type=str)
    lastname = request.args.get("lastname", default="",   type=str)
    greeting = base64.b64decode(b"SGVsbG8gYXBwc2Vjd29ybGQ=").decode()
    tail     = f"@{name}" + (f" {lastname}" if lastname else "")
    return f"{greeting} from {tail}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF
```

- [ ] 7. Сделайте `commit`. Повторите сборку приложения по вашему `Dockerfile` для доработанного скрипта `python`. Сохраните `image` в виде .`tar` архива. Сделайте `commit`.

```
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ git add requirements.txt hello.py
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ git commit -m "lab5: add requirements.txt & Flask-wrapper for typer script"
[lab01 56fb37f] lab5: add requirements.txt & Flask-wrapper for typer script
 2 files changed, 21 insertions(+), 16 deletions(-)
 rewrite labs/lab05/source/hello.py (66%)
 
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ docker buildx build -t hellow-appsec-world .
[+] Building 2.2s (3/3) FINISHED                                           docker:default
 => [internal] load build definition from Dockerfile                                 0.0s
 => => transferring dockerfile: 429B                                                 0.0s
 => CANCELED [internal] load metadata for docker.io/library/python:3.11-slim         2.1s
 => ERROR [internal] load metadata for docker.io/library/python:2.11-slim            2.1s
------
 > [internal] load metadata for docker.io/library/python:2.11-slim:
------
Dockerfile:1
--------------------
   1 | >>> FROM python:2.11-slim AS builder
   2 |     WORKDIR /hello
   3 |     COPY requirements.txt .
--------------------                                                                          
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ docker run -p 8000:5000 hellow-appsec-world
hello appsec world
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ docker save -o hello_with_deps.tar hellow-appsec-world
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ git add hello_with_deps.tar
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ git commit -m "add tar image"
[lab01 6e86f01] add tar image
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 labs/lab05/source/hello_with_deps.tar
 
```

- [ ] 8. Выведите на терминале и проанализируйте следующие команды консоли

```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ docker login -u sane44ek

i Info → A Personal Access Token (PAT) can be used instead.
         To create a PAT, visit https://app.docker.com/settings


Password:
Login Succeeded
                                                                                      
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker tag hellow-appsec-world acher/hellow-appsec-world
                                                                                      
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker push acher/hellow-appsec-world

Using default tag: latest
The push refers to repository [docker.io/acher/hellow-appsec-world]
a4816f2a838f: Pushed 
f1ea60eea430: Pushed 
4ed96d1d8ac5: Pushed 
bf2d6dfacd93: Pushed 
49ae95fb9faa: Pushed 
fa384bf02ac1: Mounted from library/python 
600af8de593b: Mounted from library/python 
424dc4972605: Mounted from library/python 
77a2b55fbe8b: Mounted from library/python 
latest: digest: sha256:5db56befdb1f992e2a4e2b3bbfbf5d747dfc597186fcdbc95d97f623f70166ba size: 2202
                                                                                      
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$  docker inspect acher/hellow-appsec-world
[
    {
        "Id": "sha256:f95b4a2df4c9882d1d9fcd98df8f080ea9c760a9e8610f5cd8b52c3e23e8e571",
        "RepoTags": [
            "acher/hellow-appsec-world:latest",
            "hellow-appsec-world:latest"
        ],
        "RepoDigests": [
            "acher/hellow-appsec-world@sha256:f95b4a2df4c9882d1d9fcd98df8f080ea9c760a9e8610f5cd8b52c3e23e8e571",
            "hellow-appsec-world@sha256:f95b4a2df4c9882d1d9fcd98df8f080ea9c760a9e8610f5cd8b52c3e23e8e571"
        ],
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-01-15T07:22:10.469544489Z",
        "Config": {
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1"
            ],
            "Cmd": [
                "python",
                "hello.py"
            ],
            "WorkingDir": "/hello",
            "ArgsEscaped": true
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 49503370,
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:e50a58335e1366e2581fe61794c1651afe2fe04e881e795aa166f24f4fc78d92",
                "sha256:523062ea36b5189e9ea6d7d86850296d1d7b5b4418109217e7ac12e13273fbba",
                "sha256:5d89b1d5fc98cb4fa0c3a8ac89cf83932b8b287e318b7761badd4b9ce58b3ecb",
                "sha256:49d74831a2871d1733e397932626f721303aef93edc180602b0877d68c6cbf5a",
                "sha256:fae0bd33586146466e02031f406dd45e1e3ae91ce52ed20d2b844ec3a2558480",
                "sha256:70a927f0ea432461d7909b3b6dde7deed55d10d0a7183c21b661829dd1eb4787",
                "sha256:c058fa6c0ffd902b5554f0635cb0a48c75232750f430de8c78c0794286cec7ae",
                "sha256:5b97e063f423cebc6327d2b9462ff12e292d2da86efd51ed00c46fcfb128a128",
                "sha256:13f6454cbef200d64d55e5c0e8a121fa3f46bbbe605c5effde6e704776233916"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-01-15T07:37:58.584307042Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.oci.image.index.v1+json",
            "digest": "sha256:f95b4a2df4c9882d1d9fcd98df8f080ea9c760a9e8610f5cd8b52c3e23e8e571",
            "size": 856,
            "annotations": {
                "io.containerd.image.name": "docker.io/library/hellow-appsec-world:latest",
                "org.opencontainers.image.ref.name": "latest"
            }
        }
    }
]
```

```bash
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker container create --name first hellow-appsec-world
d8bfa18386bb4fe1bb05699230c3ce59d613fa87764e87bf8065c5647f5b37a3

acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker image pull geminishkvdev/hello-appsec-world
Using default tag: latest
latest: Pulling from geminishkvdev/hello-appsec-world
no matching manifest for linux/amd64 in the manifest list entries
                                                                                      
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker inspect geminishkvdev/hello-appsec-world
[]
Error: No such object: geminishkvdev/hello-appsec-world

$ acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ docker container create --name second hello-appsec-world
WARNING: The requested image's platform (linux/arm64) does not match the detected host platform (linux/amd64/v3) and no specific platform was requested
a24cc6e9098bfeba5844fe8d92b324975cb3843ebd68cee1327687672f359f0e

``` 

- [ ] 9. Выведите на терминале и проанализируйте в консоли процессы, которые запущены, владельцев по пользователям

```bash 
                                                                              
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$ docker container run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
20043066d3d5: Pull complete
06808451f0d6: Download complete
Digest: sha256:c35e29c9450151419d9448b0fd75374fec4fff364a27f176fb458d472dfc9e54
Status: Downloaded newer image for ubuntu:latest
root@87415ac08cde:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.7  0.0   4588  3872 pts/0    Ss   07:45   0:00 /bin/bash
root           9  0.0  0.0   7888  4048 pts/0    R+   07:46   0:00 ps aux
root@87415ac08cde:/#

``` 
 
- [ ] 10. Выведите оба контейнера first и second на терминал
```
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05/source$  docker ps -a | grep -E "first|second"
87415ac08cde   ubuntu                "/bin/bash"         38 seconds ago   Exited (0) 1 second ago               vibrant_dijkstra
d8bfa18386bb   hellow-appsec-world   "python hello.py"   2 minutes ago    Created                               first
```
- [ ] 11. Перейдите в основной корень `lab05` и выведите на терминале, и проанализируйте

```bash 
[+] up 5/5
 ✔ Image lab05-server       Built                                                                   16.1s
 ✔ Image lab05-client       Built                                                                   16.1s
 ✔ Network lab05_app_net    Created                                                                  0.0s
 ✔ Container lab05-server-1 Created                                                                  0.1s
 ✔ Container lab05-client-1 Created                                                                  0.1s
Attaching to client-1, server-1
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:8000
server-1  |  * Running on http://172.18.0.2:8000
server-1  | Press CTRL+C to quit
server-1  | 172.18.0.3 - - [15/Jan/2026 07:48:05] "GET / HTTP/1.1" 200 -
client-1  |
client-1  |     <html>
client-1  |     <head><title>Colorful Output</title></head>
client-1  |     <body style="font-family: monospace; font-size: 24px;">
server-1  | 172.18.0.1 - - [15/Jan/2026 07:49:54] "GET / HTTP/1.1" 200 -
server-1  | 172.18.0.1 - - [15/Jan/2026 07:49:54] "GET /favicon.ico HTTP/1.1" 404 -


``` 
<img width="1829" height="527" alt="image" src="https://gist.github.com/user-attachments/assets/10f8df7f-727e-4743-85fd-933d1646512b" />

- [ ] 12. Откройте соседнее окно терминала и и выведите на терминале

```bash 
open -a "Google Chrome" http://localhost:8000

acher@LAPTOP-G8JP4BBC:~/ $ curl -I http://localhost:8000
HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.14
Date: Mon, 15 Dec 2025 16:02:05 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 761
Connection: close
/// server-1  | 172.18.0.1 - - [15/Jan/2026 07:51:08] "HEAD / HTTP/1.1" 200 -
```

- [ ] 13. Остановите работу `docker-compose`.

```bash 
$ docker ps -a                         

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05$ docker ps -q
1b90a4dfae80
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab05$ docker images
                                                                                      i Info →   U  In Use
IMAGE                              ID             DISK USAGE   CONTENT SIZE   EXTRA
acher/hellow-appsec-world:latest   f95b4a2df4c9        203MB         49.5MB    U
hello-world:latest                 05813aedc15f       25.9kB         9.52kB    U
hellow-appsec-world:latest         f95b4a2df4c9        203MB         49.5MB    U
lab05-client:latest                07a27038e40e        208MB         50.9MB    U
lab05-server:latest                311fc2889b98        211MB         51.7MB    U
ubuntu:latest                      c35e29c94501        119MB         31.7MB    U

acher@LAPTOP-G8JP4BBC:~/labs/lab05 $ docker ps -q | xargs docker stop
1b90a4dfae80

acher@LAPTOP-G8JP4BBC:~/labs/lab05 $ docker compose down             
WARN[0000] /home/acher/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] down 3/3
 ✔ Container lab05-client-1 Removed                                                                  0.1s
 ✔ Container lab05-server-1 Removed                                                                  0.1s
 ✔ Network lab05_app_net    Removed                                                                  0.2s  
 
```
- [ ] 14. Доработайте `docker-compose` и скрипт, который вы подготовили ранее, что бы вы смогли воспроизвести шаги п.11 по п.13 с демонстрацией. Сделайте `commit`.

```
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ cat Dockerfile             
FROM python:3.11-slim
WORKDIR /hello
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY hello.py .
ENV PYTHONUNBUFFERED=1
CMD ["python", "hello.py"]
                                                                                      
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ cat docker-compose.yml 
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
    environment:
      - FLASK_RUN_HOST=0.0.0.0
                                                                                      
acher@LAPTOP-G8JP4BBC:~/labs/lab05/source$ cat requirements.txt  
flask==2.2.3
werkzeug==2.3.6
requests==2.28.1
typer==0.12.5

```

- [ ] 15. Залейте изменения в свой удаленный репозиторий, проверьте историю `commit`.
```
acher@LAPTOP-G8JP4BBC:~/labs/lab05 $ git log --oneline -5
a73dbbc (HEAD -> lab_05, origin/lab_05) lab5: docker-compose for Flask app (clean, no tar)

```
- [ ] 16. Подготовьте отчет `gist`.

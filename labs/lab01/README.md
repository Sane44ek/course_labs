<div align="center">
<h1><a id="intro">Лабораторная работа 1: Системы обмена данными (Git SCM)</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Чередова_A._С.-8b9aff" alt="Contributor Badge"></a> <img src="https://img.shields.io/badge/Contributor-Шмаков_И._С.-8b9aff" alt="Contributor Badge"></a></div>


## Выполнил: Sane44ek
## Дата: 2025-11-23

## ✅ Выполненные задачи:

### 1. Настройка окружения
- Настроены глобальные переменные Git
- Сгенерированы SSH ключи
- Сгенерированы GPG ключи для подписи коммитов
- Настроена автоматическая подпись коммитов

### 2. Работа с репозиторием
- Создан локальный репозиторий
- Создан удаленный репозиторий на GitHub: https://github.com/Sane44ek/my-labs
- Настроена структура проекта с labs

### 3. Разработка приложения
- Создан файл `typersteel.py` с CLI интерфейсом
- Реализованы формальные/неформальные приветствия
- Добавлена обработка параметров командной строки

### 4. Работа с ветками и PR
- Созданы ветки: patch1, patch2, patch3
- Выполнены Pull Requests и merge
- Решены конфликты слияния

## Структура проекта:
```bash
my-labs/
├── lab01/
│ ├── README.md
│ └── typersteel.py
├── lab02/
│ ├── exmpl_hello.py
│ ├── pygamesteel.py
│ └── README.md
├── LICENSE.md
├── NOTICE.md
├── README.md
└── SECURITY.md
```

## Задание

- [х] 1. Зарегистрироваться на почтовом сервисе **Gmail**. В случае наличия аккаунта - не требуется
- [х] 2. Зарегистрироваться на сервисе совместной разработки **GitHub**. В случае наличия аккаунта требуется произвести дополнительные настройки и обновить данные персонификации
- [х] 3. Отправить зарегистрированный адрес почтового ящика личным сообщением
- [х] 4. Отправить зарегистрированный логин личным сообщением
- [х] 5. Ознакомиться со ссылками учебного материала и формализованными требованиями из основного описания
- [х] 6. Сгенерировать **SSH** ключ и добавить его в список ключей для сервиса **GitHub**
- [х] 7. Сгенерировать **Personal Token** с правами **gist** и сохранить его в файл
- [х] 8. Сгенерировать GnuPG для подтверждения подписания коммитов и возможно использование Х.509 (включить в отчет описание, что такое `smimesign`)
- [х] 9. Подготовить глобальные переменные окружения для **GitHub**
- [х] 10. Ознакомиться с материалами `gh` сервиса и использовать их для авторизации, `commit`, `pull request` и тд.
- [х] 11. Выполнить инструкцию учебного материала
- [х] 12. Оформить `README.md` по аналогии и использовать `shield`, etc.
- [х] 13. Составить `gist` отчет и отправить ссылку личным сообщением



-  Подготовим переменные окружения через конфигурацию git config на одном из трёх уровней:
    - Локальный (--local) - только для текущего репозитория, файл .git/config
    - Глобальный (--global) - для пользователя, файл ~/.gitconfig
    - Системный (--system) - для всех пользователей /etc/gitconfig

```bash
$ git config --global user.name "Ваше Имя" # Установить имя пользователя (глобально)
$ git config --global user.email "email@example.com" # Установить email пользователя (глобально)
$ git config --global core.editor "vim" # Установить текстовый редактор по умолчанию или nano
$ git config unset --global user.email # Удалить глобальную настройку email. Допустима замена "unset" на "--unset"
$ git config edit --global # Редактирование конфига на указанном уровне в редакторе "core.editor". Допустима замена "edit" на "-e"
$ git config list # Показать все текущие настройки. Допустима замена "list" на "--list"
$ git config user.name # Показать имя пользователя. Без атрибутов — локальная настройка
$ git config --global alias.co checkout # Создать псевдоним (например, "git co" вместо "git checkout")
$ git config --global help.autocorrect prompt # Предложения автозамены при ошибке набора команды.
$ git config --global core.autocrlf true # Настроить конвертацию концов строк (для Windows: "true", для Linux/macOS: "input")
$ git config --global credential.helper cache # Кэшировать учётные данные. По умолчанию 15 минут. Укажи "cache --timeout=3600" для часа. Не работает для пассфраз ключей.
$ git config --global commit.gpgsign true # Настроить автоматическое подписание коммитов
```

- Поставим на машину необходимые компоненты для `gitscm`, `GitHub CLI`
- Поставим дополнительные пакеты для своего удобства, рекомендуется поставить `zsh` 

```bash
$ echo $SHELL
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" # Homebrew
$ brew install zsh

$ acher@LAPTOP-G8JP4BBC:~/my-labs$ brew install zsh
==> Fetching downloads for: zsh
^CBottle Manifest zsh (5.9)
$ zsh --version
$ acher@LAPTOP-G8JP4BBC:~$ zsh --version
zsh 5.8.1 (x86_64-ubuntu-linux-gnu)

```
- Поставьте `GnuPG` и используйте для подписания коммитов флагом `-S`

```bash
$ gpg --full-generate-key # Создание ключа с выбором его типа

$ acher@LAPTOP-G8JP4BBC:~/my-labs$ gpg --full-generate-key
gpg (GnuPG) 2.2.27; Copyright (C) 2021 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
  (14) Existing key from card
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072) 4096
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0)
Real name: Sane44ek
Email address: acheredova621816@gmail.com
Comment:
You selected this USER-ID:
    "Sane44ek <acheredova621816@gmail.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit?



         ┌──────────────────────────────────────────────────────┐
         │ Please enter the passphrase to                       │
         │ protect your new key                                 │
         │                                                      │
         │ Passphrase: ________________________________________ │
         │                                                      │
         │       <OK>                              <Cancel>     │
         └──────────────────────────────────────────────────────┘



$ gpg --list-secret-keys --keyid-format=long # Вывод всех ключей в длинной форме
$ gpg --armor --export xxxxxx  # Экспорт публичного ключа в ASCII формате (замените xxxxxx на ваш ключ KEYID - gpg --list-secret-keys --keyid-format=long sec   rsa3072/xxxxx)
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGk6rg4...

-----END PGP PUBLIC KEY BLOCK-----

$ git config --global --unset gpg.format
$ git config --global user.signingkey # Внесение вложенного ключа (обоих)
$ git config --global commit.gpgsign true # Подпись всех фиксаций
$ git config --global tag.gpgSign true # Подпись всех тегов
```

- Подготовьте и опишите материалы в отчете:
1. Создайте локальный репозиторий на машине
```bash
mkdir lab01
cd lab01/
```
2. Проинициализируйте репозиторий
	
```bash
git init
```
3. Авторизуйтесь и используйте `GitHub CLI` для создания удаленного репозитория
	
```bash  
gh auth login
gh repo create lab01 --public
```

4. Создайте пустой README.md
	
```bash
touch README.md
``` 
5. Используйте указание URL своего созданного репозитория для присвоения ветки `master` статуса `origin`
	
```bash
git remote set-url origin git@github.com:Sane44ek/lab01.git
``` 

6. В локальном репозитории и сделайте `commit`
    
```bash
git add README.md
git commit -S -m "test"
```

7. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий
 
```bash
git push -u origin master
```

8. Создайте файл `hello.py` в локальном репозитории. Реализуйте **Hello appsec world** на языке python используя несколько интерпретаторов с "грязным" кодом
    
```bash
import sys
import os

def main():
	v = sys.version_info[0]
	if v==2:
		exec('print "Hello appsec world"')
	elif v==3:
		print("Hello appsec world")
	else:
		print("Unknown python version")

if __name__ == "__main__":
	main()
```

9. Сделайте `commit` с флагом `-S`
	
```bash
git add hello.py
git commit -S -m "hello.py"
```    

10. Измените исходный код, что бы скрипт запрашивал имя пользователя и выводил `Hello appsec world from @name`
	
```bash
def main():
	v = sys.version_info[0]
	if v==2:
		name = raw_input("Enter your name: ").strip()
		exec('print "Hello appsec world from" + name')
	elif v==3:
		name = input("Enter your name: ")
		print("Hello appsec world from" + name)
	else:
		print("Unknown python version")
```    

11. Сделайте `commit` с флагом `-S` и сделайте публикацию в удаленный репозиторий. Проверьте вывод истории изменений
	
```bash    
git add hello.py
git commit -S -m "Add hello.py with basic functionality"
git push origin master
git log --graph --decorate --all
```    
12. В локальном репозитории создайте ветку `patch1` и внесите изменения исправлению кода и модернизации до следующего вида, что бы код был рабочим. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий:

```bash
"""
Lab 01: CLI Application - PATCH3 VERSION - EDITED IN MAIN BRANCH
This version was edited directly in GitHub main branch
"""

def main(
    name: str,
    lastname: str = "",
    formal: bool = False
) -> None:
    """
    SAYS HELLO TO USER, OPTIONALLY USING LASTNAME AND FORMAL STYLE

    ARGS:
        NAME (STR): USER NAME (REQUIRED)
        LASTNAME (STR): USER LASTNAME (OPTIONAL)
        FORMAL (BOOL): FORMAL GREETING FLAG (OPTIONAL)

    RETURNS:
        NONE: PRINTS GREETING TO CONSOLE
    """
    # CHECK GREETING MODE
    if formal:
        # FORMAL GREETING WITH LASTNAME
        greeting = f"Добрый день, {name} {lastname}!"
    else:
        # INFORMAL GREETING WITH NAME ONLY
        greeting = f"Привет, {name}!"

    # PRINT THE GREETING
    print(greeting)


if __name__ == "__main__":
    import argparse

    # COMMAND LINE ARGUMENTS PARSING
    parser = argparse.ArgumentParser(
        description="Говорит 'Привет' пользователю"
    )

    parser.add_argument(
        "name",
        help="Имя пользователя"
    )

    parser.add_argument(
        "--lastname",
        default="",
        help="Фамилия пользователя."
    )

    parser.add_argument(
        "--formal",
        "-f",
        action="store_true",
        help="Использовать формальное приветствие."
    )

    # GET ARGUMENTS AND CALL MAIN FUNCTION
    arguments = parser.parse_args()
    main(arguments.name, arguments.lastname, arguments.formal)

 ```

 - Доработайте материалы и также опишите их в отчете: 
    1. Проверьте, что ветка `patch1` в удалённом репозитории
    2. Создайте `pull-request` в виде `patch1 -> master`
    3. В ветке `patch1` добавьте в исходный код комментарии и убедитесь, что есть указанные изменения в `pull-request`
    4. В удалённый репозитории выполните слияние `pull-request` для `patch1 -> master` и удалите ветку `patch1`
    5. Стяните последние актуальные изменения и просмотрите историю изменений для `master`
    6. Удалите локальную ветку `patch1`
    7. Создайте новую локальную ветку `patch2`.
    8. Измените *code style* по своему усмотрению
    9. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий и создайте pull-request `patch2 -> master`
    10. В ветке **master** удаленного репозитория явно измените комментарий
    11. Увидите, что в `pull-request` появились расхождения
    <img width="2014" height="1224" alt="image" src="https://gist.github.com/user-attachments/assets/a779d6f3-2ed8-48c7-a412-07e26880b63b" />

    13. Локально сделайте **rebase** и исправьте расхождения (это называется **конфликт**)
    <img width="2023" height="995" alt="image" src="https://gist.github.com/user-attachments/assets/dc67728a-af93-4f3d-8f68-9c7d8986c5bd" />

    14. Сделайте `commit` и опубликуйте изменения в ветке `patch2`
    15. Убедитесь, что пропали конфликтны. 
    <img width="1317" height="435" alt="image" src="https://gist.github.com/user-attachments/assets/bc99ba7c-8152-4f2c-ac4e-82697c27081b" />

    17. Сделайте `merge` для `pull-request` `patch2 -> master`.
    18. Подготовьте отчет `gist`.
    19. Продемонстрируйте в материалах отчета историю коммитов на локальном и удаленном репозитории.
    <img width="1611" height="774" alt="image" src="https://gist.github.com/user-attachments/assets/1b8cb24a-817d-4050-a939-bf1ae1b0c19e" />


```bash
acher@LAPTOP-G8JP4BBC:~/labs$ git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
* f659cb6 - (HEAD -> patch3, origin/patch3) chore: update title for patch3 (19 hours ago) <Sane44ek>
* bbaadbd - (main) docs: update comment in main branch directly (19 hours ago) <Sane44ek>
*   70cacc9 - Merge pull request #2 from Sane44ek/patch2 (19 hours ago) <Sane44ek>
|\
| * dba125a - (origin/patch2, patch2) style: update code style - uppercase comments, better formatting (19 hours ago) <Sane44ek>
|/
*   b10f3e7 - Merge pull request #1 from Sane44ek/patch1 (19 hours ago) <Sane44ek>
|\
| * f97bd9f - (origin/patch1, patch1) docs: add comprehensive code comments and documentation (19 hours ago) <Sane44ek>
| * 95cf57c - refactor: implement CLI with typer-compatible interface using argparse as fallback (20 hours ago) <Sane44ek>
| * fb30594 - refactor: implement Typer CLI with options (20 hours ago) <Sane44ek>
|/
* 6c6dca0 - docs: Add beautiful documentation with badges and structure (20 hours ago) <Sane44ek>
* 233b71c - Restructure repository: move to root with complete labs structure (28 hours ago) <Sane44ek>
* d967f4f - Clean up repository: remove sensitive files, rename hello.py, update README (28 hours ago) <Sane44ek>
* fcd03b1 - Initial commit: Add README.md, hello.py and .gitignore (28 hours ago) <Sane44ek>
* 5c2995c - Add hello.py with basic functionality (2 days ago) <Sane44ek>
* 9f017d2 - Initial commit: Add README.md (2 days ago) <Sane44ek>
```

***

## Мой дополнительный вопрос
Как сделать автообновления репозитория через github CLI без push?
- Способ 1: Синхронизация форка через gh repo sync

```bash
cd ~/course_labs
git remote add upstream https://github.com/Sane44ek/ORIGINAL_REPO.git
gh repo sync your_username/your_repo --branch develop
```
- Способ 2: Ручное обновление через консоль Git
```bash
git fetch upstream
git checkout develop
git merge upstream/develop
git push origin develop
```
- Способ 3: Полная автоматизация через GitHub Actions

```bash
"Actions" → "New workflow".

name: Sync Fork
on:
  schedule:
    - cron: '0 */6 * * *'  # Автосинхронизация каждые 6 часов
  workflow_dispatch:        # Позволяет запускать вручную
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Sync Fork
        uses: aormsby/Fork-Sync-With-Upstream-action@v3.4
        with:
          upstream_repository: BMSTU-IU8-ORG/BMSTU-REPO
          upstream_branch: develop
          target_branch: develop
          git_pull_args: --rebase
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
``` 

## Links

- [Google Sheets](https://www.google.ru/intl/ru/sheets/about/)
- [Google Docs](https://www.google.ru/intl/ru/docs/about/)
- [GitHub](https://github.com)
- [GitHub SSH Key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Markdown](https://stackedit.io)
- [Gist](https://gist.github.com)
- [GitHub Personal Token](https://github.com/settings/tokens/new)
- [GitHub CLI](https://cli.github.com)


## Безопасность:
- Все коммиты подписаны GPG ключами
- Настроены SSH ключи для безопасного подключения
- Чувствительные файлы исключены через .gitignore

## Результат:
- Освоены основы Git и GitHub
- Навыки работы с ветками и Pull Requests
- Решение конфликтов слияния через rebase
- Подпись коммитов GPG для верификации
- Создание структурированного репозитория

## Ссылки:
- Репозиторий: https://github.com/Sane44ek/my-labs

<div align="center">
<h1><a id="intro">Лабораторная работа №2</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Чередова_А.С.-8b9aff" alt="Contributor Badge"></a></div>

***

Данная лабораторная работа посвещена изучению *nix машин и как они работают, позволяет приобрести навыки для работы с терминалом/ консолью и приобрести знания по работе ОС. В лабоработрной работе описываются материалы по командам, скриптам и подключаемым приложениям.

***
## Задание

- [x] 1. Выведите на терминале и проанализируйте следующие команды консоли
```bash
$ who | wc -l # who показывает активные интерактивные сессии, wc -l считает строки → сколько пользователей "в системе" сейчас
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% who | wc -l
0
$ id # показывает uid/gid текущего пользователя и его группы
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% id
uid=1000(acher) gid=1000(acher) groups=1000(acher),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev)
$ whoami # выводит имя текущего пользователя
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% whoami 
acher

$ hostnamectl # подробная инфа о хосте: имя, ОС, ядро, архитектура, тип машины
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% hostnamectl 
 Static hostname: ubuntu
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 22f866e906284626a47f5ed8edf04972
         Boot ID: b09ek61ccdab456eb02eb92040ebc1ca
  Virtualization: vmware
Operating System: Ubuntu 24.04.2 LTS          
          Kernel: Linux 6.12.13-amd64
    Architecture: x86-64
 Hardware Vendor: Vmware, Inc
  Hardware Model: Vmware
Firmware Version: 6.00
   Firmware Date: Mon 2025-03-01
    Firmware Age: 8month 4w 2d

```
- [x] 2. Выведите утилитой `tree` список вложенности дерева диреторий для каталога своего пользователя. Далее используйте `ls -a` и укажите отличие от `ls -l`.

```bash
root@LAPTOP-G8JP4BBC:/home/acher/course_labs/labs/lab02# tree
.
├── README.md
├── exmpl_hello.py
└── pygamesteel.py

0 directories, 3 files


acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% ls -a
.  ..  README.md  exmpl_hello.py  pygamesteel.py
                                                                                                     
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% ls -l
total 28
-rw-r--r-- 1 acher acher 17951 Dec 15 15:03 README.md
-rw-r--r-- 1 acher acher   403 Dec 15 15:03 exmpl_hello.py
-rw-r--r-- 1 acher acher   790 Dec 15 15:03 pygamesteel.py

#ls -a — показать все файлы/папки, включая скрытые (начинающиеся с точки).
#ls -l — показать подробный список (права, владелец, размер, дата, имя), но скрытые файлы не выводит.
```
- [x] 3. Используйте утилиту `file` и `df` для определения какая файловая система на разделе `/dev/sda1`.
```bash
root@LAPTOP-G8JP4BBC:/home/acher/course_labs/labs/lab02# file -s /dev/sda
/dev/sda: Linux rev 1.0 ext2 filesystem data, UUID=00000000-0000-0000-0000-000000000000 (extents) (large files) (huge files)                                                                                                     
root@LAPTOP-G8JP4BBC:/home/acher/course_labs/labs/lab02# df -h /dev/sda
Filesystem      Size  Used Avail Use% Mounted on
none            7.7G     0  7.7G   0% /dev

```
- [x] 4. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ which vi # показывает путь к vi
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% which vi
/usr/bin/vi

$ locate hello.py # ищет hello.py в locate
root@LAPTOP-G8JP4BBC:/home/acher/course_labs/labs/lab02# locate hello.py
/home/acher/course_labs/labs/lab02/exmpl_hello.py
/home/acher/course_labs/labs/lab05/source/hello.py
/home/acher/labs/lab02/exmpl_hello.py

$ sudo updatedb # обновляет базу locate
$ locate hello # ищет все файлы/пути где встречается hello
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% locate hello   
/home/acher/course_labs/labs/lab02/exmpl_hello.py
/home/acher/course_labs/labs/lab05/source/hello.py
/home/acher/labs/lab02/exmpl_hello.py
/home/linuxbrew/.linuxbrew/Homebrew/Library/Homebrew/test/support/fixtures/elf/hello
/home/linuxbrew/.linuxbrew/Homebrew/Library/Homebrew/test/support/fixtures/elf/hello_with_rpath
/home/linuxbrew/.linuxbrew/Homebrew/Library/Homebrew/test/support/fixtures/elf/libhello.so.0
/mnt/c/Program Files/Go/src/cmd/cgo/internal/testfortran/testdata/helloworld
/mnt/c/Program Files/Go/src/cmd/cgo/internal/testfortran/testdata/helloworld/helloworld.f90
/mnt/c/Program Files/Go/src/cmd/cgo/internal/teststdio/testdata/hello.go
/mnt/c/Program Files/Go/src/cmd/cgo/internal/teststdio/testdata/hello.out
/mnt/c/Program Files/Go/src/cmd/go/testdata/script/run_hello.txt
/mnt/c/Program Files/Go/src/cmd/go/testdata/script/run_hello_pkg.txt
/mnt/c/Program Files/Go/src/cmd/go/testdata/vcstest/bzr/hello.txt
/mnt/c/Program Files/Go/src/cmd/go/testdata/vcstest/fossil/hello.txt
/mnt/c/Program Files/Go/src/cmd/go/testdata/vcstest/git/hello.txt
/mnt/c/Program Files/Go/src/cmd/go/testdata/vcstest/go/custom-hg-hello.txt
/mnt/c/Program Files/Go/src/cmd/go/testdata/vcstest/hg/custom-hg-hello.txt

$ touch screen
$ find ~ -name screen  # поиск по файловой системе в ~
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% find ~ -name screen
/home/kali/course_labs/labs/lab02/screen

$ locate screen  # ищет screen в locate

$ sudo updatedb # обновляем базу ещё раз после создания файла
$ locate screen # ищет screen в locate
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% locate screen
/etc/screenrc
/etc/alternatives/desktop-lockscreen.xml
/etc/init.d/screen-cleanup
/etc/pam.d/xfce4-screensaver
/etc/rcS.d/S01screen-cleanup
/etc/tmpfiles.d/screen-cleanup.conf
/etc/xdg/kscreenlockerrc
/etc/xdg/autostart/xfce4-screensaver.desktop
/etc/xdg/menus/xfce4-screensavers.menu
```

- [x]  5. Используйте конструкцию и вставьте ее в созданный файл ранее. Подключите `pygame` - используем исключительно для стилизации окна.

```py
import pygame
pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)
pygame.display.set_mode(window_size) # Создаем окно

# Задаем цвет фона
bg_color = (255, 255, 255)
pygame.draw.rect(screen, bg_color, [0, 0, screen_width, screen_height], 1)

# Выводим текст на экран
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = (400, 300)
screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
pygame.display.flip() # Обновляем экран
```

- [x] 6. Сделайте `commit` и `push` в свой репозиторий с изменениями в `master branch`. На следующих лабораторных работах мы вернемся к этому файлу.

```bash
root@LAPTOP-G8JP4BBC:/home/acher/course_labs/labs/lab02# git branch
  develop
* lab01
root@LAPTOP-G8JP4BBC:/home/acher/course_labs/labs/lab02# git status
On branch lab01
Your branch is up to date with 'origin/lab01'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        screen.py

nothing added to commit but untracked files present (use "git add" to track)
root@LAPTOP-G8JP4BBC:/home/acher/course_labs/labs/lab02# git log --oneline -3
ce54e7f (HEAD -> lab01) Добавлен файл screen.py с конструкцией pygame для lab02
ba2288a (tag: v1.3.0, upstream/develop, origin/lab01, origin/develop, origin/HEAD, develop) release v1.3.0
167788a release v1.3.0
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   screen.py
```


- [x] 7. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ groups # показывает группы текущего пользователя
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% groups
acher adm dialout cdrom floppy sudo audio dip video plugdev netdev

$ useradd smallman # создаёт пользователя acher
$ userdel smallman -rf # удаляет пользователя
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% sudo userdel smallman -rf
userdel: acher mail spool (/var/mail/acher) not found
userdel: acher home directory (/home/acher) not found

$ useradd smallman
$ passwd smallman # задает пароль пользователю
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% passwd smallman
New password: 
Retype new password: 
passwd: password updated successfully

$ usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33' # записываем GECOS-комментарий
$ passwd smallman
$ id smallman # выводит uid/gid и группы acher
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% sudo id smallman    
uid=1001(smallman) gid=1001(smallman) groups=1001(smallman)

$ groupadd -g 1500 readgroup # создает группу readgroup с gid=1500
$ usermod -aG readgroup smallman  # добавляет acher в readgroup
$ chmod 666 screen.py # ставит права rw-rw-rw- (читать/писать всем)
```
- [x] 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному пользователю и выведите права этого польователя для измененного файла только используя `readgroup`.
```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% ls -l screen.py 
-rw-rw-rw- 1 root root 781 Dec 15 17:32 screen.py

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% chgrp readgroup screen.py # меняем группу файла на readgroup

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% sudo chmod 640 screen.py # права: владелец rw, группа r

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% ls -l screen.py 
-rw-r----- 1 root readgroup 781 Dec 15 17:32 screen.py
```
- [x] 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ touch nmapres.txt
$ setfacl -m u:smallman:rw nmapres.txt
$ setfacl -m g:readgroup:r nmapres.txt
$ getfacl nmapres.txt
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% getfacl nmapres.txt
# file: nmapres.txt
# owner: root
# group: root
user::rw-
user:smallman:rw-
group::r--
group:readgroup:r--
mask::rw-
other::r--


```

- [x] 10. Сохраните файл внутри локального репозитория, так как следующая работа будет подразумевать запись в нее данных о nmap.
```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% git add nmapres.txt                       
                                                                                                     
root@LAPTOP-G8JP4BBC:/home/acher/course_labs/labs/lab02# git commit -m "for_lab02"
[lab01 0c28e11] for_lab02
 Committer: root <root@LAPTOP-G8JP4BBC.localdomain>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 labs/lab02/nmapres.txt                                                          
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% git branch
  develop
  lab01
* lab02
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% git push origin lab02
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Delta compression using up to 22 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (10/10), 1.33 KiB | 195.00 KiB/s, done.
Total 10 (delta 5), reused 1 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (5/5), completed with 2 local objects.
remote:
remote: Create a pull request for 'lab02' on GitHub by visiting:
remote:      https://github.com/Sane44ek/course_labs/pull/new/lab02
remote:
To github.com:Sane44ek/course_labs.git
 * [new branch]      lab02 -> lab02

```
- [x] 11. Для закрепления выведите все списки групп пользователей на вашей ОС и права на верхнеуровневые каталоги.
```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02%  ls -ld /*
lrwxrwxrwx   1 root root       7 Jan  7  2025 /bin -> usr/bin
drwxr-xr-x   2 root root    4096 Apr 18  2022 /boot
drwxr-xr-x  15 root root    3900 Dec 15 14:39 /dev
drwxr-xr-x  85 root root    4096 Dec 15 17:52 /etc
drwxr-xr-x   4 root root    4096 Nov 24 18:43 /home
-rwxr-xr-x   1 root root 2781552 Oct 10 03:22 /init
lrwxrwxrwx   1 root root       7 Jan  7  2025 /lib -> usr/lib
lrwxrwxrwx   1 root root       9 Jan  7  2025 /lib32 -> usr/lib32
lrwxrwxrwx   1 root root       9 Jan  7  2025 /lib64 -> usr/lib64
lrwxrwxrwx   1 root root      10 Jan  7  2025 /libx32 -> usr/libx32
drwx------   2 root root   16384 Nov 22 20:11 /lost+found
drwxr-xr-x   2 root root    4096 Jan  7  2025 /media
drwxr-xr-x   6 root root    4096 Nov 22 20:11 /mnt
drwxr-xr-x   2 root root    4096 Jan  7  2025 /opt
dr-xr-xr-x 298 root root       0 Dec 15 14:38 /proc
drwx------   5 root root    4096 Dec 15 17:57 /root
drwxr-xr-x   8 root root     160 Dec 15 17:03 /run
lrwxrwxrwx   1 root root       8 Jan  7  2025 /sbin -> usr/sbin
drwxr-xr-x   2 root root    4096 Nov 22 20:11 /snap
drwxr-xr-x   2 root root    4096 Jan  7  2025 /srv
dr-xr-xr-x  13 root root       0 Dec 15 14:38 /sys
drwxrwxrwt   8 root root    4096 Dec 15 17:03 /tmp
drwxr-xr-x  14 root root    4096 Jan  7  2025 /usr
drwxr-xr-x  13 root root    4096 Jan  7  2025 /var

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,acher
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:

```
- [x] 12. Выведите все права для файлов и директорий локального репозитория которые имеют различные пользователи  (без использования длинных путей)
```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% ls -l     
total 32
-rw-r--r--  1 acher acher     17951 Dec 15 15:03 README.md
-rw-r--r--  1 acher acher       403 Dec 15 15:03 exmpl_hello.py
-rw-rw-r--+ 1 root  root          0 Dec 15 17:52 nmapres.txt
-rw-r--r--  1 acher acher       790 Dec 15 15:03 pygamesteel.py
-rw-r-----  1 root  readgroup   781 Dec 15 17:32 screen.py

```
- [x] 13. Выведите процессы которые у вас запущены в термине и вне его.
```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% ps -a
    PID TTY          TIME CMD
   1120 pts/0    00:00:00 ps
                                                                                                    
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% ps -x 
    PID TTY      STAT   TIME COMMAND
     11 pts/0    Ss     0:00 -zsh
     54 ?        Ss     0:00 /usr/bin/dbus-daemon --syslog --fork --print-pid 5 --print-address 7 --
     59 ?        Ss     0:00 /usr/bin/dbus-daemon --syslog --fork --print-pid 5 --print-address 7 --
     64 ?        Ss     0:00 /usr/bin/dbus-daemon --syslog --fork --print-pid 5 --print-address 7 --
   1121 pts/0    R+     0:00 ps -x

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% pstree
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab02% pstree
init(Ubuntu-22.─┬─SessionLeader───Relay(11)─┬─3*[dbus-daemon]
                │                           └─zsh───pstree
                ├─init───{init}
                └─{init(Ubuntu-22.}
```
- [x] 14. Оформить `README.md` по аналогии и использовать `shield`, etc.
- [x] 15. Составить `gist` отчет и отправить ссылку личным сообщением

WallEngine - Open-Source Wallpaper Engine
============================= 

![(1)](https://user-images.githubusercontent.com/52446061/61069325-77132780-a425-11e9-9cac-3aeb00b9cc34.gif)


Установка и запуск 
----------- 
➊ Извлечь **rar** и поместить папку в любом месте. 

➋ Запускать через **WallEngine.exe** в директории WallEngine (Ярлык по желанию). 

**Предусмотрен автозапуск.** При желании можно установить видеоплеер mpv в качестве основного, достаточно запустить **mpv-install.bat** и установить плеер по умолчанию в настройках системы. Удаление плеера производится bat-файлом **mpv-uninstall.bat.**


Windows 7 требования
----------- 
Перейдите в меню Пуск - > поиск "Настройка производительности и внешнего вида Windows",
проверить:

**▪ Анимированные элементы управления и элементы внутри окна**

**▪ Включение композиции рабочего стола**

**▪ Использование стилей для отображения окон и кнопок**

Если не включить эти настройки, weebp не сможет поместить анимированные обои за значки.


Советы 
-----------
**•Использовать обои в разрешении 1920x1080p, 
другие разрешения работают некорректно, так как не прописаны в коде.**

**•Видео в 60FPS сильно нагружают процессор.**


Список багов версии 1.8 
----------- 
⓵ Если запустить обои повторно, происходит наложение друг на друга. 

⓶ Иногда окно mpv накладывается некорректно, решается приостановкой и
повторным запуском обоев, или перезагрузкой explorer.exe через диспетчер задач. 

⓷ Не реализована пауза когда другая программа развернута на весь экран, 
mpv продолжает работать. 

⓸ Возможны мелкие недочёты. 


Авторство 
----------- 
![(2)](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/120px-Python-logo-notext.svg.png)
**•Код написан MasajiNobe на языке Python**
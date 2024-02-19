Скрипты для [https://github.com/psqq/dwm](https://github.com/psqq/dwm)

* `check_wm.py`
  * Выводит имя текущего оконного менеджера
  * Зависимости: `wmctrl`
* `kb_layout.py`
  * Получение и смена текущей языка клавиатуры
  * Зависимости: `setxkbmap`
* `status_bar_date.py`
  * Для вывода текущей даты в строке состояния
* `battery_charge.py`
  * Для вывода заряда батареи в строке состояния
* `volume.py`
  * Для вывода и изменения громкости
  * Зависимости: `pactl`
* `status_bar.py`
  * Скрипт для вывода строки состояния с помощью `xsetroot`
  * `status_bar.py render`
    * Выводит строку состояния в таком формате:
    * `| US | B 70% | V 90% | Сб 17 фев 12:20:12 |` или
    * `| US | V 90% | Сб 17 фев 12:20:12 |`
  * `status_bar.py loop [display]` (пример: `status_bar.py loop :1`)
    * Запускает `render` в бесконечном цикле с интервалом в 1 секунду
  * Зависимости: `xsetroot`
* `startdwm`
  * Скрипт для запуска `dwm`
  * Добавить в `.xinitrc`: `exec ~/dwm-scripts/startdwm`

# Строка состояния

Для работы строки состояния нужно каким-то образом запустить `python status_bar.py loop` или периодически запускать `python status_bar.py render`.

Например, запуск можно добавить в `.xinitrc` :

```sh
python /home/USER_NAME/dwm-scripts/status_bar.py loop &

```

Репозиторий для тестирования сайта https://www.saucedemo.com/ командой PyRates

Инструкция по запуску проекта автоматизации:
1. Открыть git bash в локальном репозитории, куда планируете клонировать репозиторий
2. Ввести в git bash команду:
  - если SSH настроен `git clone git@github.com:pavelplatonov/saucedemo.git`
  - если SSH не настроен `git clone https://github.com/pavelplatonov/saucedemo.git`
3. Открыть клонированную папку проекта, в поисковой строке ввести powershell, нажать Enter. Должен открыться PowerShell с путём до открытой папки в консоли
4. Установить poetry если он у вас не установлен `pip install poetry`
5. В PowerShell с путём к папке в консоли ввести команду `poetry shell` , данная команда запустит виртуальную среду poetry
6. Далее в PowerShell ввести команду `poetry install`, данная команда установит зависимости(библиотеки) из файла `.toml` для работы проекта.

1. Для начала надо клонировать репозиторий 
    git clone https://github.com/Alan-95-hub/FastAPI

2. После открываем данную папку в Visual Studio Code. После того, как открыли, надо открыть терминал и там установить fastapi и uvicorn
    pip install fastapi
    pip install uvicorn

3. После этого запускаем микросервис также в том же терминале
    uvicorn main:app --reload

4. После этого перейдем на localhost. Он будет выглядеть вот так:
    http://127.0.0.1:8000
  Надо к нему дописать '/docs'. Должно выглядеть так:
    http://127.0.0.1:8000/docs 

5. Открываем наш post запрос, нажимаем кнопку "Try it out!", затем вводим название нашего build в строку build. 

6. Далее, при верном вводе build будет выведен список отсортированных tasks, введеной вами ранее build, в противом случае будет выведена ошибка "Build not found" с ошибкой 404

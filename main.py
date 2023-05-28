from fastapi import FastAPI, HTTPException
from typing import List
import yaml

app = FastAPI()
#открываем файлы tasks.yaml и buildis.yaml 
with open("tasks.yaml", "r") as tasks_file:
    TASKS = yaml.safe_load(tasks_file)["tasks"]
    

with open("builds.yaml", "r") as builds_file:
    BUILDS = yaml.safe_load(builds_file)["builds"]
            
@app.post("/get_tasks")
async def get_tasks(build: str):
    #проверка на корректность ввода build
    builds_names = []
    for i in BUILDS:
        builds_names.append(i["name"])
    if build not in builds_names:
        raise HTTPException(status_code=404, detail="Build not found")
    
    #берем нужный нам build с tasks
    def get_list(build):
        for one_build in BUILDS:
            if one_build["name"]==build:
                return one_build
    build_with_tasks=get_list(build)

    #собираем все задачи в виде двумерного списка, где первый элемент будет названия, а второй количество элементов
    list_tasks=[]
    def get_tasks(name_of_task):
        for task in TASKS:
            if task["name"] == name_of_task:
                return task
    for name_of_task in build_with_tasks["tasks"]:
        task = get_tasks(name_of_task)
        list_tasks.append((task["name"], len(task["dependencies"])))

    #сортируем наш массив в порядке убывания количества элементов    
    sorted_tasks=sorted(list_tasks, key=lambda x: x[1], reverse=True)
    
    #выбираем только первые элементы(названия) из нашего отсортированного двумерного списка
    answer = [pair[0] for pair in sorted_tasks]
    return answer

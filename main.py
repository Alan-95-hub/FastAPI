from fastapi import FastAPI, HTTPException
from typing import List
import yaml

app = FastAPI()

with open("C:\\Users\\alanb\\OneDrive\\Рабочий стол\\Fast-API\\tasks.yaml", "r") as tasks_file:
    tasks = yaml.safe_load(tasks_file)["tasks"]
    

with open("C:\\Users\\alanb\\OneDrive\\Рабочий стол\\Fast-API\\builds.yaml", "r") as builds_file:
    builds = yaml.safe_load(builds_file)["builds"]
    


@app.post("/get_tasks")
async def get_tasks(build: str):
    builds_names = []
    for i in builds:
        builds_names.append(i["name"])

    if build not in builds_names:
        raise HTTPException(status_code=404, detail="Build not found")

    def get_list(build):
        for one_build in builds:
            if one_build["name"]==build:
                return one_build
            
    buildings=get_list(build)

    def get_tasks(task):
        for name_task in tasks:
            if name_task["name"] == task:
                return name_task
            
    build_tasks=[]

    for task in buildings["tasks"]:
        name_task1 = get_tasks(task)
        build_tasks.append((name_task1["name"], len(name_task1["dependencies"])))

    
    sorted_tasks=sorted(build_tasks, key=lambda x: x[1], reverse=True)
    
    answer = [pair[0] for pair in sorted_tasks]
    return answer

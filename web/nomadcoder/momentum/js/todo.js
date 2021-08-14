const todoForm = document.querySelector("#todo-form");
const todoInput = todoForm.querySelector("input");
const todoList = document.querySelector("#todo-list");
const LS_KEY_JOBDATALIST = "jobDataList";
let jobDataList = [];

function updateLocalStorage(key, data) {
    localStorage.setItem(key, JSON.stringify(data));
}

function onRemoveJobButtonClick(event) {
    const job = event.target.parentNode;
    job.remove();
    
    jobDataList = jobDataList.filter((jobData) => jobData.id !== Number(job.id));
    updateLocalStorage(LS_KEY_JOBDATALIST, jobDataList);
}

function createJob(jobData) {
    const job = document.createElement("li");
    job.id = jobData.id;

    const span = document.createElement("span");
    span.innerText = jobData.title;
    job.appendChild(span);

    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", onRemoveJobButtonClick);
    job.appendChild(button);

    jobDataList.push(jobData);
    return job;
}

function showJob(job) {
    todoList.appendChild(job);
}

function onTodoFormSubmit(event) {
    event.preventDefault();
    const jobTitle = todoInput.value;
    todoInput.value = "";

    const jobData = {title: jobTitle, id: Date.now()}
    const newJob = createJob(jobData);
    showJob(newJob);

    updateLocalStorage(LS_KEY_JOBDATALIST, jobDataList);
}

todoForm.addEventListener("submit", onTodoFormSubmit);

const localStorageJobDataList= localStorage.getItem(LS_KEY_JOBDATALIST);
if (localStorageJobDataList !== null) {
    const parsedJobdataList = JSON.parse(localStorageJobDataList);
    parsedJobdataList.forEach(jobData => {
        const newJob = createJob(jobData);
        showJob(newJob);
    });
}

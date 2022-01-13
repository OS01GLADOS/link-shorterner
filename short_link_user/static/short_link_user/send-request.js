window.addEventListener('submit', customSubmit);
let url = "";
let currentUser = "";

function setUrl(value) {
    url = value;
}

function setCurrentUser(value) {
    currentUser = value;
}

function customSubmit(event) {
    event.preventDefault();
    let linkForm = new FormData(document.getElementById('form'));
    linkForm.append('user', currentUser);
    let xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                let request_res = xhr.response;
                document.getElementById('res_url').innerHTML =
                    '<p>result: <a href = "' + request_res + '">' + request_res + '</a></p>'
            }
        }
    };
    xhr.onerror = function (e) {
        console.error(xhr.statusText);
    };
    xhr.send(linkForm);
}
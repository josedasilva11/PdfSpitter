function makeURL(route) {
    if (window.baseURL) return window.baseURL + route;
    return route;
}

export class Core {
    static makeRequest(route, body) {
        return new Promise((resolve, reject) => {
            fetch(makeURL(route), {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(body),
            }).then((r) => {
                r.json().then((data) => {
                    if (data.result != null && "error" in data.result) {
                        reject(data.result.error);
                        return;
                    }
                    resolve(data.result);
                });
            }).catch((e) => {
                reject(e);
            })
        });
    }
}

export class API {
    static new_form (form_data,) {

    return Core.makeRequest("/api/app/new_form", {
        form_data: form_data,
        });
}

static search_form (filter,) {

    return Core.makeRequest("/api/app/search_form", {
        filter: filter,
        });
}

static update_form (id,form_data,) {

    return Core.makeRequest("/api/app/update_form", {
        id: id,
        form_data: form_data,
        });
}
}
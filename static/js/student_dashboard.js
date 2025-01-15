const decodeHTML = (str) => {
    const parser = new DOMParser();
    const decodedString = parser.parseFromString(`<!doctype html><body>${str}`, 'text/html').body.textContent;
    return decodedString;
};

function appliedJobs() {
    const jobList = document.getElementById('job-list');
    try {
        const decodedData = decodeHTML(applied_jobs);
        const jsonData = JSON.parse(decodedData);
        jsonData.forEach(job => {
            const card = document.createElement('div');
            card.classList.add('card', 'job-card');
            card.innerHTML = `
                    <img src="static/${job.image_url}" alt="${job.company_name} Logo">
                    <a href="${window.location.origin}/job/applied/${job.pk}" class="text-decoration-none text-black">
                        <div class="card-body text-black">
                            <h5 class="card-title">${job.title}</h5>
                            <p class="card-text">
                                Company: ${job.company}<br>
                                Status: ${job.status}
                            </p>
                        </div>
                    </a>
            `;
            jobList.appendChild(card);
        });
    } catch (error) {
        console.error("Error parsing JSON:", error);
    }
}

const recommendedJobs = () => {
    const recommendedJobList = document.getElementById('recommended-job');
    try {
        const decodedData = decodeHTML(applied_jobs);
        const jsonData = JSON.parse(decodedData);
        jsonData.forEach(cardre => {
            const recommended = document.createElement("div");
            recommended.classList.add("card", "saved-card");
            recommended.innerHTML = `
                <img src="static/${cardre.image_url}" alt="${cardre.company_name} Logo">
                <a href="${window.location.origin}/single-job/${cardre.pk}" class="text-decoration-none text-black">
                    <div class="card-body text-black">
                        <h5 class="card-title">${cardre.title}</h5>
                        <p class="card-text">
                            Company: ${cardre.company}<br>
                        </p>
                    </div>
                </a>
                `;
            recommendedJobList.appendChild(recommended);
        })
    } catch (error) {
        console.error("Error parsing JSON:", error);
    }
}

const savedJobs = () => {
    const savedJobList = document.getElementById('saved-job');
    try {
        const decodedData = decodeHTML(applied_jobs);
        const jsonData = JSON.parse(decodedData);
        jsonData.forEach(saved => {
            const saved_card = document.createElement("div");
            saved_card.classList.add("card", "saved-card");
            saved_card.innerHTML = `
                <img src="static/${saved.image_url}" alt="${saved.company_name} Logo">
                <a href="${window.location.origin}/single-job/${saved.pk}" class="text-decoration-none text-black">
                <div class="card-body text-black">
                        <h5 class="card-title">${saved.title}</h5>
                        <p class="card-text">
                            Company: ${saved.company}<br>
                        </p>
                    </div>
                </a>
                `;
            savedJobList.appendChild(saved_card);
        })
    } catch (error) {
        console.error("Error parsing JSON:", error);
    }
}


document.addEventListener("DOMContentLoaded", recommendedJobs());
document.addEventListener("DOMContentLoaded", appliedJobs());
document.addEventListener("DOMContentLoaded", savedJobs());
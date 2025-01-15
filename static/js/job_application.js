function viewApplicantProfile(name, email, resumeLink) {
    document.getElementById('applicant-name').textContent = name;
    document.getElementById('applicant-email').textContent = email;
    document.getElementById('applicant-resume').textContent = resumeLink;
    document.getElementById('applicant-profile').style.display = 'block';
}

function closeProfile() {
    document.getElementById('applicant-profile').style.display = 'none';
}

function exportApplicantData() {
    alert("Exporting applicant data...");
}

document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();
    alert("Filters applied!");
});
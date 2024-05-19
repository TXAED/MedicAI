document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle");
    const formDiv = document.getElementById("form-div");
    const pdfDiv = document.getElementById("pdf-div");

    toggleButton.addEventListener("click", function () {
        if (formDiv.style.display === "none") {
            formDiv.style.display = "flex";
            pdfDiv.style.display = "none";
            toggleButton.innerText = "Upload a Medical Report instead!";
        } else {
            formDiv.style.display = "none";
            pdfDiv.style.display = "flex";
            toggleButton.innerText = "Fill a Medical Form instead!";
        }
    });


    const form = document.getElementById("textForm");
    const file = document.getElementById("pdfForm");
    const loadingDiv = document.getElementById("loading");
    const contentDiv = document.getElementById("form-div");
    const PDFDiv = document.getElementById("pdf-div");

    form.addEventListener("submit", function () {
        // Show loading symbol and text
        loadingDiv.style.display = "flex";
        contentDiv.style.opacity = "0.5"; // Optional: dim the form while loading
    });

    file.addEventListener("submit", function () {
        // Show loading symbol and text
        loadingDiv.style.display = "flex";
        PDFDiv.style.opacity = "0.5"; // Optional: dim the form while loading
    });

    // Hide loading symbol when the page finishes loading
    window.addEventListener("load", function () {
        loadingDiv.style.display = "none";
        contentDiv.style.opacity = "1";
        PDFDiv.style.opacity = "1";
    });
});

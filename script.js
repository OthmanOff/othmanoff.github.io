const params = new URLSearchParams(window.location.search);
let lang =
  params.get("lang") ||
  localStorage.getItem("lang") ||
  navigator.language.slice(0, 2) ||
  "fr";
lang = ["fr", "ar", "ja", "en"].includes(lang) ? lang : "fr";
localStorage.setItem("lang", lang);

fetch("data/content.json")
  .then((response) => response.json())
  .then((content) => {
    document.getElementById("name").innerText = content.name[lang];
    document.getElementById("cv").innerText = content.cv[lang];
    document.getElementById("home_description").innerText =
      content.home_description[lang];
    document.getElementById("contact_me").innerText = content.contact_me[lang];
    const expTitle = content.experience_title[lang];
    const expDetails = content.experience_details[lang];

    const expSection = document.getElementById("cv_experience");
    expSection.innerHTML = `<h2 class="text-2xl font-semibold mb-2">${expTitle}</h2>
      <ul class="list-disc ml-5">${expDetails
        .map((item) => `<li>${item}</li>`)
        .join("")}</ul>`;

    // Formation
    const eduTitle = content.education_title[lang];
    const eduDetails = content.education_details[lang];

    const eduSection = document.getElementById("cv_education");
    eduSection.innerHTML = `<h2 class="text-2xl font-semibold mb-2">${eduTitle}</h2>
      <ul class="list-disc ml-5">${eduDetails
        .map((item) => `<li>${item}</li>`)
        .join("")}</ul>`;

    const langTitle = content.languages_title[lang];
    const langList = content.languages_list[lang];

    const langSection = document.getElementById("cv_languages");
    langSection.innerHTML = `<h2 class="text-2xl font-semibold mb-2">${langTitle}</h2>
  <ul class="list-disc ml-5">${langList
    .map((item) => `<li>${item}</li>`)
    .join("")}</ul>`;
  });

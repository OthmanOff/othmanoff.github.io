const params = new URLSearchParams(window.location.search);
let lang =
  params.get("lang") ||
  localStorage.getItem("lang") ||
  navigator.language.slice(0, 2) ||
  "fr";
lang = ["fr", "ar", "ja"].includes(lang) ? lang : "fr";
localStorage.setItem("lang", lang);

fetch("data/content.json")
  .then((response) => response.json())
  .then((content) => {
    document.getElementById("name").innerText = content.name[lang];
    document.getElementById("cv").innerText = content.cv[lang];
    document.getElementById("home_description").innerText =
      content.home_description[lang];
    document.getElementById("contact_me").innerText = content.contact_me[lang];
  });

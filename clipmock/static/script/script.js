//setting active link for nav-bar
nav_links = document.querySelectorAll(".foractive");
for (var i = 0; i < nav_links.length; i++) {
  if (nav_links[i].href === window.location.href) {
    nav_links[i].classList.add("active");
  }
}

// remove flashed messages after 5 seconds
flashed_msg = document.querySelectorAll(".flashed");
setTimeout(close, 5000);
function close() {
  for (var i = 0; i < flashed_msg.length; i++) {
    flashed_msg[i].classList.add("d-none");
  }
}

// adding to collection without page refresh(AJAX)

function getData(form) {
  var formData = new FormData(form);

  // console.log(formData.get("filename"));

  filename = formData.get("filename");

  // console.log(filename);
  // console.log(filename.replaceAll("/", "@"));
  filename = filename.replaceAll("/", "@");

  var xhr = new XMLHttpRequest();

  xhr.open("POST", "/add/" + filename, true);

  xhr.onload = function () {
    if (this.status == 200) {
      console.log("probably sent");
    }
  };

  xhr.send();
}

all_forms = document.querySelectorAll(".addForm");
for (var i = 0; i < all_forms.length; i++) {
  all_forms[i].addEventListener("submit", function (e) {
    e.preventDefault();
    console.log(user_id);
    if (user_id) {
      const toastLiveExample = document.getElementById("liveToast");
      const toast = new bootstrap.Toast(toastLiveExample);
      document.getElementById("toast-message").innerHTML =
        "Design added to collections.";
      toast.show();
      getData(e.target);
    } else {
      const toastLiveExample = document.getElementById("liveToast");
      const toast = new bootstrap.Toast(toastLiveExample);
      document.getElementById("toast-message").innerHTML =
        "Login to add designs to collection";
      toast.show();
    }
  });
}

const toastTrigger = document.getElementById("liveToastBtn");
const toastLiveExample = document.getElementById("liveToast");
if (toastTrigger) {
  toastTrigger.addEventListener("click", () => {
    const toast = new bootstrap.Toast(toastLiveExample);

    toast.show();
  });
}

// image animation in index page
let images_objects = ["static/index/objects1.png", "static/index/objects2.png"];
let images_apparel = ["static/index/apparel1.png", "static/index/apparel2.png"];
let images_bcards = ["static/index/bcards1.png", "static/index/bcards2.png"];

let index = 0;
const objects_img = document.querySelector("#objects-img");
const apparel_img = document.querySelector("#apparel-img");
const bcards_img = document.querySelector("#bcards-img");

function change() {
  objects_img.src = images_objects[index];
  apparel_img.src = images_apparel[index];
  bcards_img.src = images_bcards[index];
  index == 1 ? (index = 0) : index++;
}

window.onload = function () {
  setInterval(change, 1000);
};

const create = document.querySelector("#create_btn");

create.addEventListener("click", function () {
  create.classList.add("d-none");
  document.querySelector("#loader_btn").classList.remove("d-none");
});

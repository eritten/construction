window.addEventListener("load", () => {
  // menu button functionality
  const menuBtn = document.querySelector(".menu-btn");
  const menuList = document.querySelector(".nav-list");

  menuBtn.addEventListener("click", toggleNav);

  function toggleNav() {
    menuList.classList.toggle("active");
    if (menuList.classList.contains("active")) {
      menuBtn.innerHTML = `<i class="fas fa-times"></i>`;
    } else {
      menuBtn.innerHTML = `<i class="fas fa-bars"></i>`;
    }
  }

  window.addEventListener("scroll", () => {
    menuList.classList.remove("active", screenY > 0);
    menuBtn.innerHTML = `<i class="fas fa-bars"></i>`;
  });
  // newsletter toast
  const newsToast = document.querySelector(".newsletter-toast-box");

  setTimeout(() => {
    newsToast.classList.add("vanish");
  }, 3000);

  //  newsletter
  const subInputs = document.querySelectorAll(".sub-input");
  const newsSubmitBtn = document.querySelector("#news-add");

  //   newsSubmitBtn.addEventListener("click", subscribeToNewsletter);

  // if name and email is empty, disable submit button

  // subscribe email validation
  const validateEmail = (email) => {
    // this patern checks for correct format of email
    return email.match(
      /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
  };
  const newsEmail = document.querySelector("#news-email");
  function validation() {
    const validateMsg = document.querySelector("#validate-msg");
    const emailValue = newsEmail.value.trim();
    validateMsg.textContent = "";
    validateMsg.style.textTransform = "upperCase";

    if (validateEmail(emailValue)) {
      validateMsg.textContent = "valid email";
      validateMsg.style.color = "green";
      newsSubmitBtn.classList.add("active")
      newsSubmitBtn.disabled = false
    } else {
      validateMsg.textContent = "invalid email";
      validateMsg.style.color = "red";
      newsSubmitBtn.classList.remove("active")
      newsSubmitBtn.disabled = true
    }
    if (emailValue == "") {
      validateMsg.textContent = "";
    }
    return false;
  }
  // should validate as user is typing
  newsEmail.addEventListener("keyup", validation);
});

const input1 = document.querySelector("#firstname");
counter1 = document.querySelector(".firstname-counter");
maxLength1 = input1.getAttribute("maxlength");

input1.onkeyup = () => {
  counter1.innerText = maxLength1 - input1.value.length;
};

const input2 = document.querySelector("#lastname");
counter2 = document.querySelector(".lastname-counter");
maxLength2 = input2.getAttribute("maxlength");

input2.onkeyup = () => {
  counter2.innerText = maxLength2 - input2.value.length;
};

const input3 = document.querySelector("#companyname");
counter3 = document.querySelector(".companyname-counter");
maxLength3 = input3.getAttribute("maxlength");

input3.onkeyup = () => {
  counter3.innerText = maxLength3 - input3.value.length;
};

const input4 = document.querySelector("#companydesc");
counter4 = document.querySelector(".companydesc-counter");
maxLength4 = input4.getAttribute("maxlength");

input4.onkeyup = () => {
  counter4.innerText = maxLength4 - input4.value.length;
};

const input5 = document.querySelector("#title");
counter5 = document.querySelector(".title-counter");
maxLength5 = input5.getAttribute("maxlength");

input5.onkeyup = () => {
  counter5.innerText = maxLength5 - input5.value.length;
};

const input6 = document.querySelector("#email");
counter6 = document.querySelector(".email-counter");
maxLength6 = input6.getAttribute("maxlength");

input6.onkeyup = () => {
  counter6.innerText = maxLength6 - input6.value.length;
};

const input7 = document.querySelector("#phone");
counter7 = document.querySelector(".phone-counter");
maxLength7 = input7.getAttribute("maxlength");

input7.onkeyup = () => {
  counter7.innerText = maxLength7 - input7.value.length;
};

const input8 = document.querySelector("#website");
counter8 = document.querySelector(".website-counter");
maxLength8 = input8.getAttribute("maxlength");

input8.onkeyup = () => {
  counter8.innerText = maxLength8 - input8.value.length;
};

const input9 = document.querySelector("#address");
counter9 = document.querySelector(".address-counter");
maxLength9 = input9.getAttribute("maxlength");

input9.onkeyup = () => {
  counter9.innerText = maxLength9 - input9.value.length;
};

const input10 = document.querySelector("#qrdata");
counter10 = document.querySelector(".qrdata-counter");
maxLength10 = input10.getAttribute("maxlength");

input10.onkeyup = () => {
  counter10.innerText = maxLength10 - input10.value.length;
};

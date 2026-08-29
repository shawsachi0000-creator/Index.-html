const scenes = [...document.querySelectorAll(".scene")];

function go(id) { 
  scenes.forEach(s => {
    s.classList.toggle("active", s.id === id);
  });

  pop();
}

function pop() {
  for (let i = 0; i < 9; i++) {

    const x = document.createElement("span");

    x.className = "floating";

    x.textContent =
      ["♡", "✦", "♥"][Math.floor(Math.random() * 3)];

    x.style.left =
      (45 + Math.random() * 10) + "vw";

    x.style.top =
      (55 + Math.random() * 12) + "vh";

    x.style.setProperty(
      "--dx",
      (Math.random() * 180 - 90) + "px"
    );

    document.body.appendChild(x);

    setTimeout(() => {
      x.remove();
    }, 1500);
  }
}


// First button
document.querySelector("#accept").onclick = () => {
  go("s2");
};


// "No" button escape
const reject = document.querySelector("#reject");

function escapeNo() {

  reject.style.position = "relative";

  reject.style.left =
    (Math.random() * 150 - 75) + "px";

  reject.style.top =
    (Math.random() * 80 - 40) + "px";
}

reject.addEventListener(
  "mouseenter",
  escapeNo
);

reject.addEventListener(
  "touchstart",
  e => {
    e.preventDefault();
    escapeNo();
  }
);


// Next buttons
document
  .querySelectorAll("[data-next]")
  .forEach(button => {

    button.onclick = () => {
      go(button.dataset.next);
    };

  });


// Second escaping button
const mineNo = document.querySelector("#mineNo");

function escapeMine() {

  mineNo.style.position = "relative";

  mineNo.style.left =
    (Math.random() * 140 - 70) + "px";

  mineNo.style.top =
    (Math.random() * 60 - 30) + "px";
}

mineNo.addEventListener(
  "mouseenter",
  escapeMine
);

mineNo.addEventListener(
  "touchstart",
  e => {
    e.preventDefault();
    escapeMine();
  }
);


// Final Yes
document.querySelector("#mineYes").onclick = () => {
  go("s6");
};


// Broken photo ko hide karna
document.querySelectorAll("img").forEach(img => {

  img.onerror = () => {
    img.style.opacity = "0";
  };

});

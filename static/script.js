// Get modal elements
const modal = document.getElementById("recipe-modal");
const modalTitle = document.getElementById("modal-title");
const modalIngredients = document.getElementById("modal-ingredients");
const modalSteps = document.getElementById("modal-steps");
const closeBtn = document.querySelector(".close-btn");

// Fetch recipes from backend
fetch("http://127.0.0.1:5000/recipes")
  .then(res => res.json())
  .then(data => {
      const container = document.getElementById("recipes-container");
      container.innerHTML = "";

      data.forEach(recipe => {
          const card = document.createElement("div");
          card.classList.add("recipe-card");

          card.innerHTML = `
              <img src="${recipe.image_url}" alt="${recipe.name}" />
              <h3>${recipe.name}</h3>
              <p>${recipe.description || ""}</p>
          `;

          // لما أضغط على الكارت يفتح المودال
          card.addEventListener("click", () => openModal(recipe));

          container.appendChild(card);
      });
  })
  .catch(err => console.error("Error fetching recipes:", err));

// Open Modal
function openModal(recipe) {
    modalTitle.innerText = recipe.name;

    // Ingredients
    modalIngredients.innerHTML = "";
    if (recipe.ingredients && recipe.ingredients.length > 0) {
        recipe.ingredients.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            modalIngredients.appendChild(li);
        });
    }

    // Steps
    modalSteps.innerHTML = "";
    if (recipe.steps && recipe.steps.length > 0) {
        recipe.steps.forEach(step => {
            const li = document.createElement("li");
            li.textContent = step;
            modalSteps.appendChild(li);
        });
    }

    modal.style.display = "flex"; // Show modal
}

// Close Modal
closeBtn.onclick = function () {
    modal.style.display = "none";
};

// Close if clicked outside modal
window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
};
// Change text content dynamically
document.getElementById("change-text-btn").addEventListener("click", () => {
    const intro = document.getElementById("intro-text");
    intro.textContent = "The text has been updated dynamically!";
  });
  
  // Modify CSS styles via JavaScript
  document.getElementById("toggle-style-btn").addEventListener("click", () => {
    const title = document.getElementById("main-title");
    title.classList.toggle("highlight");
  });
  
  // Add an element when a button is clicked
  document.getElementById("add-element-btn").addEventListener("click", () => {
    const newDiv = document.createElement("div");
    newDiv.textContent = "I'm a new div added to the DOM!";
    newDiv.className = "highlight";
    newDiv.id = "dynamic-div";
    document.getElementById("container").appendChild(newDiv);
  });
  
  // Remove the added element
  document.getElementById("remove-element-btn").addEventListener("click", () => {
    const div = document.getElementById("dynamic-div");
    if (div) {
      div.remove();
    }
  });
  
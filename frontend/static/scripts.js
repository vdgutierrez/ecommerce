document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault();
  
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");
  
    try {
      const response = await fetch("http://localhost:5000/auth/login", { // Cambia la URL según tu configuración
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
  
      if (response.ok) {
        const data = await response.json();
        alert("¡Inicio de sesión exitoso!");
        // Redirigir a la página principal o dashboard
        window.location.href = "/dashboard.html"; // Cambia según tu configuración
      } else {
        const error = await response.json();
        errorMessage.textContent = error.message || "Usuario o contraseña incorrectos.";
        errorMessage.style.display = "block";
      }
    } catch (error) {
      errorMessage.textContent = "Error al conectar con el servidor.";
      errorMessage.style.display = "block";
    }
  });
  
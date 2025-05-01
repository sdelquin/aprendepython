document.addEventListener("DOMContentLoaded", function () {
  document.body.addEventListener("click", function (event) {
    // Verifica si se hizo clic en un botón de copiar
    const copyButton = event.target.closest("button.md-clipboard");
    if (!copyButton) return;

    // Encuentra el bloque de código asociado
    const preBlock = copyButton.closest("pre");
    const codeBlock = preBlock ? preBlock.querySelector("code") : null;
    if (!codeBlock) return;

    // Obtiene el texto del bloque de código
    let codeText = codeBlock.innerText;

    // Filtra y elimina los prompts ">>>", "...", y "$" al inicio de las líneas
    codeText = codeText
      .split("\n")
      .filter(
        (line) =>
          line.startsWith(">>>") ||
          line.startsWith("...") ||
          line.startsWith("$")
      ) // Solo instrucciones
      .map((line) => line.replace(/^(>>>|\.\.\.|\$)\s?/, "")) // Elimina ">>>", "..." o "$"
      .join("\n");

    // Si el bloque no es de sesión interactiva o Bash, copia todo el contenido
    if (codeText.trim() === "") {
      // Limpia las líneas resaltadas (hl_lines)
      codeText = codeBlock.textContent || codeBlock.innerText; // Usamos textContent para evitar problemas de espaciado
    }

    // Copia el código limpio al portapapeles
    navigator.clipboard.writeText(codeText).then(() => {
      // Opcional: Mostrar feedback visual en el botón
      copyButton.classList.add("copied");
      setTimeout(() => copyButton.classList.remove("copied"), 1000);
    });

    // Evita que el evento siga propagándose y se copie el código original
    event.stopPropagation();
    event.preventDefault();
  });
});

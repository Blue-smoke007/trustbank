document.addEventListener('DOMContentLoaded', () => {
  const fetchDataButton = document.getElementById('fetchData');
  const outputDiv = document.getElementById('output');

  fetchDataButton.addEventListener('click', async () => {
      try {
          const response = await fetch('');
          if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
          }
          const data = await response.json();
          outputDiv.textContent = JSON.stringify(data, null, 2);
      } catch (error) {
          outputDiv.textContent = `Error: ${error.message}`;
      }
  });
});

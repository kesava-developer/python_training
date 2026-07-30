const packageGrid = document.getElementById('package-grid');
const packageSelect = document.getElementById('package');
const form = document.getElementById('enroll-form');
const message = document.getElementById('form-message');

async function loadPackages() {
  const response = await fetch('/api/cafe-types');
  const packages = await response.json();

  packageGrid.innerHTML = packages.map(pkg => `
    <article class="package-card">
      <span class="tag">${pkg.highlight}</span>
      <h3>${pkg.name}</h3>
      <p class="price">${pkg.price}</p>
      <ul>
        ${pkg.features.map(feature => `<li>${feature}</li>`).join('')}
      </ul>
    </article>
  `).join('');

  packageSelect.innerHTML = ['<option value="">Choose a package</option>', ...packages.map(pkg => `<option value="${pkg.name}">${pkg.name}</option>`)].join('');
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const payload = {
    name: document.getElementById('name').value,
    email: document.getElementById('email').value,
    package: document.getElementById('package').value
  };

  const response = await fetch('/api/enroll', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  message.textContent = result.message;
  if (result.ok) {
    form.reset();
  }
});

loadPackages();

const baseUrl = 'http://127.0.0.1:5000';  // Replace with your Flask app's base URL

document.getElementById('registrationForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const data = {
    name: document.getElementById('name').value,
    email: document.getElementById('email').value,
    date_of_birth: document.getElementById('dateOfBirth').value,
    phone_number: document.getElementById('phoneNumber').value,
    gender: document.getElementById('gender').value,
    address: document.getElementById('address').value,
  };

  try {
    const response = await fetch(`${baseUrl}/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    const result = await response.json();
    alert(result.message || result.error);
  } catch (error) {
    console.error('Error:', error);
  }
});

async function readRegistration() {
  const id = document.getElementById('viewId').value;
  try {
    const response = await fetch(`${baseUrl}/register/${id}`);
    const result = await response.json();
    if (result.error) {
      document.getElementById('registrationData').innerText = result.error;
    } else {
      document.getElementById('registrationData').innerText = JSON.stringify(result, null, 2);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

async function updateRegistration() {
  const id = document.getElementById('updateId').value;
  const data = {
    name: document.getElementById('name').value,
    email: document.getElementById('email').value,
    date_of_birth: document.getElementById('dateOfBirth').value,
    phone_number: document.getElementById('phoneNumber').value,
    gender: document.getElementById('gender').value,
    address: document.getElementById('address').value,
  };

  try {
    const response = await fetch(`${baseUrl}/register/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    const result = await response.json();
    alert(result.message || result.error);
  } catch (error) {
    console.error('Error:', error);
  }
}

async function deleteRegistration() {
  const id = document.getElementById('deleteId').value;
  try {
    const response = await fetch(`${baseUrl}/register/${id}`, { method: 'DELETE' });
    const result = await response.json();
    document.getElementById('deleteMessage').innerText = result.message || result.error;
  } catch (error) {
    console.error('Error:', error);
  }
}
